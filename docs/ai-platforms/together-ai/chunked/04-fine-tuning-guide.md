**Navigation:** [← Previous](./03-deploying-a-fine-tuned-model.md) | [Index](./index.md) | [Next →](./05-how-to-build-coding-agents.md)

---

# Fine-tuning Guide
Source: https://docs.together.ai/docs/fine-tuning-quickstart

Learn the basics and best practices of fine-tuning large language models.

## Introduction

Large Language Models (LLMs) offer powerful general capabilities, but often require **fine-tuning** to excel at specific tasks or understand domain-specific language. Fine-tuning adapts a trained model to a smaller, targeted dataset, enhancing its performance for your unique needs.

This guide provides a step-by-step walkthrough for fine-tuning models using the Together AI platform. We will cover everything from preparing your data to evaluating your fine-tuned model.

We will cover:

1. **Dataset Preparation:** Loading a standard dataset, transforming it into the required format for supervised fine-tuning on Together AI, and uploading your formatted dataset to Together AI Files.
2. **Fine-tuning Job Launch:** Configuring and initiating a fine-tuning job using the Together AI API.
3. **Job Monitoring:** Checking the status and progress of your fine-tuning job.
4. **Inference:** Using your newly fine-tuned model via the Together AI API for predictions.
5. **Evaluation:** Comparing the performance of the fine-tuned model against the base model on a test set.

By following this guide, you'll gain practical experience in creating specialized LLMs tailored to your specific requirements using Together AI.

<Info>
  ### Fine-tuning Guide Notebook

  Here is a runnable notebook version of this fine-tuning guide: [Fine-tuning Guide Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Finetuning/Finetuning_Guide.ipynb)
</Info>

## Table of Contents

1. [What is Fine-tuning?](#what-is-fine-tuning)
2. [Getting Started](#getting-started)
3. [Dataset Preparation](#dataset-preparation)
4. [Starting a Fine-tuning Job](#starting-a-fine-tuning-job)
5. [Monitoring Your Fine-tuning Job](#monitoring-your-fine-tuning-job)
6. [Using Your Fine-tuned Model](#using-your-fine-tuned-model)
7. [Evaluating Your Fine-tuned Model](#evaluating-your-fine-tuned-model)
8. [Advanced Topics](#advanced-topics)

## What is Fine-tuning?

Fine-tuning is the process of improving an existing LLM for a specific task or domain. You can enhance an LLM by providing labeled examples for a particular task which it can learn from. These examples can come from public datasets or private data specific to your organization.

Together AI facilitates every step of the fine-tuning process, from data preparation to model deployment. Together supports two types of fine-tuning:

1. **LoRA (Low-Rank Adaptation) fine-tuning**: Fine-tunes only a small subset of weights compared to full fine-tuning. This is faster, requires less computational resources, and is **recommended for most use cases**. Our fine-tuning API defaults to LoRA.

2. **Full fine-tuning**: Updates all weights in the model, which requires more computational resources but may provide better results for certain tasks.

## Getting Started

**Prerequisites**

1. **Register for an account**: Sign up at [Together AI](https://api.together.xyz/settings/api-keys) to get an API key.

2. **Set up your API key**:

   ```shell  theme={null}
   export TOGETHER_API_KEY=your_api_key_here
   ```

3. **Install the required libraries**:

   ```shell  theme={null}
   # Python
   pip install -U together datasets transformers tqdm
   ```

**Choosing Your Model**

The first step in fine-tuning is choosing which LLM to use as the starting point for your custom model:

* **Base models** are trained on a wide variety of texts, making their predictions broad
* **Instruct models** are trained on instruction-response pairs, making them better for specific tasks

For beginners, we recommend an instruction-tuned model:

* *meta-llama/Meta-Llama-3.1-8B-Instruct-Reference* is great for simpler tasks
* *meta-llama/Meta-Llama-3.1-70B-Instruct-Reference* is better for more complex datasets and domains

You can find all available models on the Together API [here](/docs/fine-tuning-models).

## Dataset Preparation

Fine-tuning requires data formatted in a specific way. We'll use a conversational dataset as an example - here the goal is to improve the model on multi-turn conversations.

**Data Formats**

Together AI supports several data formats:

1. **Conversational data**: A JSON object per line, where each object contains a list of conversation turns under the `"messages"` key. Each message must have a `"role"` (`system`, `user`, or `assistant`) and `"content"`. See details [here](/docs/fine-tuning-data-preparation#conversational-data).

   ```json  theme={null}
   {
     "messages": [
       { "role": "system", "content": "You are a helpful assistant." },
       { "role": "user", "content": "Hello!" },
       { "role": "assistant", "content": "Hi! How can I help you?" }
     ]
   }
   ```

2. **Instruction data**: For instruction-based tasks with prompt-completion pairs. See details [here](/docs/fine-tuning-data-preparation#instruction-data).

3. **Preference data**: For preference-based fine-tuning. See details [here](/docs/fine-tuning-data-preparation#preference-data).

4. **Generic text data**: For simple text completion tasks. See details [here](/docs/fine-tuning-data-preparation#generic-text-data).

**File Formats**

Together AI supports two file formats:

1. **JSONL**: Simpler and works for most cases.
2. **Parquet**: Stores pre-tokenized data, provides flexibility to specify custom attention mask and labels (loss masking).

By default, it's easier to use `JSONL`. However, `Parquet` can be useful if you need custom tokenization or specific loss masking.

**Example: Preparing the CoQA Dataset**

Here's an example of transforming the CoQA dataset into the required chat format:

```python Python theme={null}
from datasets import load_dataset

## Load the dataset
coqa_dataset = load_dataset("stanfordnlp/coqa")

## The system prompt, if present, must always be at the beginning
system_prompt = (
    "Read the story and extract answers for the questions.\nStory: {}"
)


def map_fields(row):
    # Create system prompt
    messages = [
        {"role": "system", "content": system_prompt.format(row["story"])}
    ]

    # Add user and assistant messages
    for q, a in zip(row["questions"], row["answers"]["input_text"]):
        messages.append({"role": "user", "content": q})
        messages.append({"role": "assistant", "content": a})

    return {"messages": messages}


## Transform the data using the mapping function
train_messages = coqa_dataset["train"].map(
    map_fields,
    remove_columns=coqa_dataset["train"].column_names,
)

## Save data to JSON file
train_messages.to_json("coqa_prepared_train.jsonl")
```

**Loss Masking**

In some cases, you may want to fine-tune a model to focus on predicting only a specific part of the prompt:

1. When using Conversational or Instruction Data Formats, you can specify `train_on_inputs` (bool or 'auto') - whether to mask the user messages in conversational data or prompts in instruction data.
2. For Conversational format, you can mask specific messages by assigning weights.
3. With pre-tokenized datasets (Parquet), you can provide custom `labels` to mask specific tokens by setting their label to `-100`.

**Checking and Uploading Your Data**

Once your data is prepared, verify it's correctly formatted and upload it to Together AI:

<CodeGroup>
  ```python Python theme={null}
  ## Using Python
  from together import Together
  import os
  import json

  TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
  WANDB_API_KEY = os.getenv(
      "WANDB_API_KEY"
  )  # Optional, for logging fine-tuning to wandb

  ## Check the file format

  from together.utils import check_file

  client = Together(api_key=TOGETHER_API_KEY)

  sft_report = check_file("coqa_prepared_train.jsonl")
  print(json.dumps(sft_report, indent=2))

  assert sft_report["is_check_passed"] == True

  ## Upload the data to Together

  train_file_resp = client.files.upload("coqa_prepared_train.jsonl", check=True)
  print(train_file_resp.id)  # Save this ID for starting your fine-tuning job
  ```

  ```shell Shell theme={null}
  ## Using CLI
  together files check "coqa_prepared_train.jsonl"
  together files upload "coqa_prepared_train.jsonl"
  ```
</CodeGroup>

The output from checking the file should look similar to:

```json JSON theme={null}
{
  "is_check_passed": true,
  "message": "Checks passed",
  "found": true,
  "file_size": 23777505,
  "utf8": true,
  "line_type": true,
  "text_field": true,
  "key_value": true,
  "has_min_samples": true,
  "num_samples": 7199,
  "load_json": true,
  "filetype": "jsonl"
}
```

## Starting a Fine-tuning Job

With our data uploaded, we can now launch the fine-tuning job using `client.fine_tuning.create()`.

**Key Parameters**

* `model`: The base model you want to fine-tune (e.g., `'meta-llama/Meta-Llama-3.1-8B-Instruct-Reference'`)
* `training_file`: The ID of your uploaded training JSONL file
* `validation_file`: Optional ID of validation file (highly recommended for monitoring)
* `suffix`: A custom string added to create your unique model name (e.g., `'test1_8b'`)
* `n_epochs`: Number of times the model sees the entire dataset
* `n_checkpoints`: Number of checkpoints to save during training (for resuming or selecting the best model)
* `learning_rate`: Controls how much model weights are updated
* `batch_size`: Number of examples processed per iteration (default: "max")
* `lora`: Set to `True` for LoRA fine-tuning
* `train_on_inputs`: Whether to mask user messages or prompts (can be bool or 'auto')
* `warmup_ratio`: Ratio of steps for warmup

<Icon icon="link" iconType="solid" /> For an exhaustive list of all the available
fine-tuning parameters refer to the [Together AI Fine-tuning API Reference](/reference/post-fine-tunes)
docs.

**LoRA Fine-tuning (Recommended)**

<CodeGroup>
  ```python Python theme={null}
  ## Using Python - This fine-tuning job should take ~10-15 minutes to complete
  ft_resp = client.fine_tuning.create(
      training_file=train_file_resp.id,
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
      train_on_inputs="auto",
      n_epochs=3,
      n_checkpoints=1,
      wandb_api_key=WANDB_API_KEY,  # Optional, for visualization
      lora=True,  # Default True
      warmup_ratio=0,
      learning_rate=1e-5,
      suffix="test1_8b",
  )

  print(ft_resp.id)  # Save this job ID for monitoring
  ```

  ```shell Shell theme={null}
  ## Using CLI
  together fine-tuning create \
    --training-file "file-id-from-upload" \
    --model "meta-llama/Meta-Llama-3.1-8B-Instruct-Reference" \
    --train-on-inputs auto \
    --lora \
    --n-epochs 3 \
    --n-checkpoints 1 \
    --warmup-ratio 0 \
    --learning-rate 1e-5 \
    --suffix "test1_8b" \
    --wandb-api-key $WANDB_API_KEY  # Optional
  ```
</CodeGroup>

**Full Fine-tuning**

For full fine-tuning, simply omit the `lora` parameter:

<CodeGroup>
  ```python Python theme={null}
  ## Using Python
  ft_resp = client.fine_tuning.create(
      training_file=train_file_resp.id,
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
      train_on_inputs="auto",
      n_epochs=3,
      n_checkpoints=1,
      warmup_ratio=0,
      lora=False,  # Must be specified as False, defaults to True
      learning_rate=1e-5,
      suffix="test1_8b_full_finetune",
  )
  ```

  ```shell Shell theme={null}
  ## Using CLI
  together fine-tuning create \
    --training-file "file-id-from-upload" \
    --model "meta-llama/Meta-Llama-3.1-8B-Instruct-Reference" \
    --train-on-inputs auto \
    --n-epochs 3 \
    --n-checkpoints 1 \
    --warmup-ratio 0 \
    --no-lora \
    --learning-rate 1e-5 \
    --suffix "test1_8b_full_finetune"
  ```
</CodeGroup>

The response will include your job ID, which you'll use to monitor progress:

```text Text theme={null}
ft-d1522ffb-8f3e #fine-tuning job id
```

## Monitoring a Fine-tuning Job

Fine-tuning can take time depending on the model size, dataset size, and hyperparameters. Your job will progress through several states: Pending, Queued, Running, Uploading, and Completed.

You can monitor and manage the job's progress using the following methods:

* **List all jobs**: `client.fine_tuning.list()`
* **Status of a job**: `client.fine_tuning.retrieve(id=ft_resp.id)`
* **List all events for a job**: `client.fine_tuning.list_events(id=ft_resp.id)` - Retrieves logs and events generated during the job
* **Cancel job**: `client.fine_tuning.cancel(id=ft_resp.id)`
* **Download fine-tuned model**: `client.fine_tuning.download(id=ft_resp.id)`

Once the job is complete (`status == 'completed'`), the response from `retrieve` will contain the name of your newly created fine-tuned model. It follows the pattern: `<your-account>/<base-model-name>:<suffix>:<job-id>`.

**Check Status via API**

<CodeGroup>
  ```python Python theme={null}
  ## Check status of the job
  resp = client.fine_tuning.retrieve(ft_resp.id)
  print(resp.status)

  ## This loop will print the logs of the job thus far
  for event in client.fine_tuning.list_events(id=ft_resp.id).data:
      print(event.message)
  ```

  ```shell Shell theme={null}
  ## Using CLI
  together fine-tuning retrieve "your-job-id"
  ```
</CodeGroup>

Example output:

```text Text theme={null}
Fine tune request created
Job started at Thu Apr  3 03:19:46 UTC 2025
Model data downloaded for togethercomputer/Meta-Llama-3.1-8B-Instruct-Reference__TOG__FT at Thu Apr  3 03:19:48 UTC 2025
Data downloaded for togethercomputer/Meta-Llama-3.1-8B-Instruct-Reference__TOG__FT at 2025-04-03T03:19:55.595750
WandB run initialized.
Training started for model togethercomputer/Meta-Llama-3.1-8B-Instruct-Reference__TOG__FT
Epoch completed, at step 24
Epoch completed, at step 48
Epoch completed, at step 72
Training completed for togethercomputer/Meta-Llama-3.1-8B-Instruct-Reference__TOG__FT at Thu Apr  3 03:27:55 UTC 2025
Uploading output model
Compressing output model
Model compression complete
Model upload complete
Job finished at Thu Apr  3 03:31:33 UTC 2025
```

**Dashboard Monitoring**

You can also monitor your job on the [Together AI jobs dashboard](https://api.together.xyz/jobs).

If you provided a Weights & Biases API key, you can view detailed training metrics on the W\&B platform, including loss curves and more.

<img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=2973b0ebdc3f38a4b7466c02fd0ddc40" alt="" data-og-width="3290" width="3290" data-og-height="1366" height="1366" data-path="images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=c511ef3fd1475fd005d3387fa3ef5194 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=8ae7668e3592726f6bb90272d45d16b4 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=9246196bf8f56237a60bc35020873347 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=11bf77aec25449cdd17fc5f9b5252fb7 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=b7833a099df09e37c228384c3e203685 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=5ad6e32772425ac3006d368830a3d999 2500w" />

## Deleting a fine-tuning job

You can also delete your fine-tuning job. This action can not be undone. This will destroy all files produced by your job including intermediate and final checkpoints.

<CodeGroup>
  ```python Python theme={null}
  ## Run delete
  resp = client.fine_tuning.delete(ft_resp.id)
  print(resp)
  ```

  ```shell Shell theme={null}
  ## Using CLI
  together fine-tuning delete "your-job-id"
  ```
</CodeGroup>

## Using a Fine-tuned Model

Once your fine-tuning job completes, your model will be available for use:

**Option 1: Serverless LoRA Inference**

If you used LoRA fine-tuning and the model supports serverless LoRA inference, you can immediately use your model without deployment. We can call it just like any other model on the Together AI platform, by providing the unique fine-tuned model `output_name` from our fine-tuning job.

<Icon icon="link" iconType="solid" /> See the list of all models that support [LoRA
Inference](/docs/lora-inference).

```python Python theme={null}
## The first time you run this it'll take longer to load the adapter weights for the first time
finetuned_model = ft_resp.output_name  # From your fine-tuning job response

user_prompt = "What is the capital of France?"

response = client.chat.completions.create(
    model=finetuned_model,
    messages=[
        {
            "role": "user",
            "content": user_prompt,
        }
    ],
    max_tokens=124,
)

print(response.choices[0].message.content)
```

You can also prompt the model in the Together AI playground by going to your [models dashboard](https://api.together.xyz/models) and clicking `"OPEN IN PLAYGROUND"`. Read more about Serverless LoRA Inference [here](https://docs.together.ai/docs/lora-inference)

<img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/39e0a986de7daa852130503531600f2cceef65ab1b8c55267e13c5eafee5ea6f-open_in_playground.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=a9a719d70fd612b05fc6eec5a0ea3247" alt="" data-og-width="2814" width="2814" data-og-height="932" height="932" data-path="images/39e0a986de7daa852130503531600f2cceef65ab1b8c55267e13c5eafee5ea6f-open_in_playground.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/39e0a986de7daa852130503531600f2cceef65ab1b8c55267e13c5eafee5ea6f-open_in_playground.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=5bc7260604b428600c48a2c0776a04a9 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/39e0a986de7daa852130503531600f2cceef65ab1b8c55267e13c5eafee5ea6f-open_in_playground.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=350efd822699951645e5716175603968 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/39e0a986de7daa852130503531600f2cceef65ab1b8c55267e13c5eafee5ea6f-open_in_playground.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=0d5a33d838354de3f8f5c1e74473e1d8 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/39e0a986de7daa852130503531600f2cceef65ab1b8c55267e13c5eafee5ea6f-open_in_playground.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=79f3c8611c70fb67dd344be32cccf8a5 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/39e0a986de7daa852130503531600f2cceef65ab1b8c55267e13c5eafee5ea6f-open_in_playground.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=e641991ae1ffe95ad3794dbe3f615c3a 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/39e0a986de7daa852130503531600f2cceef65ab1b8c55267e13c5eafee5ea6f-open_in_playground.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=02181a091af1ab544aa7dc88b3c477f8 2500w" />

**Option 2: Deploy a Dedicated Endpoint**

Another way to run your fine-tuned model is to deploy it on a custom dedicated endpoint:

1. Visit [your models dashboard](https://api.together.xyz/models)
2. Click `"+ CREATE DEDICATED ENDPOINT"` for your fine-tuned model
3. <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/97a0b8c1e144d5981840f417d85c7400c70bde53e8eca3289b0722ad642d7d33-create_DE.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=d3551d242d1ebd1fdf9df14c5a5dc132" alt="" data-og-width="2814" width="2814" data-og-height="1342" height="1342" data-path="images/97a0b8c1e144d5981840f417d85c7400c70bde53e8eca3289b0722ad642d7d33-create_DE.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/97a0b8c1e144d5981840f417d85c7400c70bde53e8eca3289b0722ad642d7d33-create_DE.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=adc835ab47098775f088fbfbec5c9b2a 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/97a0b8c1e144d5981840f417d85c7400c70bde53e8eca3289b0722ad642d7d33-create_DE.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=4c6c23dbd1e571c4209dccbc836ac7c6 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/97a0b8c1e144d5981840f417d85c7400c70bde53e8eca3289b0722ad642d7d33-create_DE.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=14072171333d10ebdc86bf2fb41e0c1e 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/97a0b8c1e144d5981840f417d85c7400c70bde53e8eca3289b0722ad642d7d33-create_DE.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=313c71850d15ff94864432be006640d2 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/97a0b8c1e144d5981840f417d85c7400c70bde53e8eca3289b0722ad642d7d33-create_DE.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=5ac0985b84e22754b8a8981e5bbf6edb 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/97a0b8c1e144d5981840f417d85c7400c70bde53e8eca3289b0722ad642d7d33-create_DE.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=212e815b464e1f8c2c7134de2a3b2681 2500w" />

   Select hardware configuration and scaling options, including min and max replicas which affects the maximum QPS the deployment can support and then click `"DEPLOY"`

You can also deploy programmatically:

```python Python theme={null}
response = client.endpoints.create(
    display_name="Fine-tuned Meta Llama 3.1 8B Instruct 04-09-25",
    model="zainhas/Meta-Llama-3.1-8B-Instruct-Reference-test1_8b-e5a0fb5d",
    hardware="4x_nvidia_h100_80gb_sxm",
    autoscaling={"min_replicas": 1, "max_replicas": 1},
)

print(response)
```

⚠️ If you run this code it will deploy a dedicated endpoint for you. For detailed documentation around how to deploy, delete and modify endpoints see the [Endpoints API Reference](/reference/createendpoint).

<img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/847e93749bb2e180a23c191e74f9e1040c7f9373701621614d99d08968ef54ac-deployed_DE.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=82c195dda7e8b0e0133ad07e0ee4eaf0" alt="" data-og-width="2832" width="2832" data-og-height="932" height="932" data-path="images/847e93749bb2e180a23c191e74f9e1040c7f9373701621614d99d08968ef54ac-deployed_DE.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/847e93749bb2e180a23c191e74f9e1040c7f9373701621614d99d08968ef54ac-deployed_DE.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=95aba9294ddb100f539c1e61efd90f93 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/847e93749bb2e180a23c191e74f9e1040c7f9373701621614d99d08968ef54ac-deployed_DE.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=343a48385e9e66b64e9f599c5eb85a1f 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/847e93749bb2e180a23c191e74f9e1040c7f9373701621614d99d08968ef54ac-deployed_DE.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=530b41d9f625410cb8afc9ea72186e63 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/847e93749bb2e180a23c191e74f9e1040c7f9373701621614d99d08968ef54ac-deployed_DE.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=a103ce58d60d78de5db666b02fd3c070 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/847e93749bb2e180a23c191e74f9e1040c7f9373701621614d99d08968ef54ac-deployed_DE.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=fa519ae89f25ea4fa5756d140885faca 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/847e93749bb2e180a23c191e74f9e1040c7f9373701621614d99d08968ef54ac-deployed_DE.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=048f087fefb75c4f94bd0bcc2dbd0568 2500w" />

Once deployed, you can query the endpoint:

```python Python theme={null}
response = client.chat.completions.create(
    model="zainhas/Meta-Llama-3.1-8B-Instruct-Reference-test1_8b-e5a0fb5d-ded38e09",
    messages=[{"role": "user", "content": "What is the capital of France?"}],
    max_tokens=128,
)

print(response.choices[0].message.content)
```

## Evaluating a Fine-tuned Model

To assess the impact of fine-tuning, we can compare the responses of our fine-tuned model with the original base model on the same prompts in our test set. This provides a way to measure improvements after fine-tuning.

**Using a Validation Set During Training**

You can provide a validation set when starting your fine-tuning job:

```python Python theme={null}
response = client.fine_tuning.create(
    training_file="your-training-file-id",
    validation_file="your-validation-file-id",
    n_evals=10,  # Number of times to evaluate on validation set
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
)
```

**Post-Training Evaluation Example**

Here's a comprehensive example of evaluating models after fine-tuning, using the CoQA dataset:

1. First, load a portion of the validation dataset:

```python Python theme={null}
coqa_dataset_validation = load_dataset(
    "stanfordnlp/coqa",
    split="validation[:50]",
)
```

2. Define a function to generate answers from both models:

```python Python theme={null}
from tqdm.auto import tqdm
from multiprocessing.pool import ThreadPool

base_model = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"  # Original model
finetuned_model = ft_resp.output_name  # Fine-tuned model


def get_model_answers(model_name):
    """
    Generate model answers for a given model name using a dataset of questions and answers.
    Args:
        model_name (str): The name of the model to use for generating answers.
    Returns:
        list: A list of lists, where each inner list contains the answers generated by the model.
    """
    model_answers = []
    system_prompt = (
        "Read the story and extract answers for the questions.\nStory: {}"
    )

    def get_answers(data):
        answers = []
        messages = [
            {
                "role": "system",
                "content": system_prompt.format(data["story"]),
            }
        ]
        for q, true_answer in zip(
            data["questions"],
            data["answers"]["input_text"],
        ):
            try:
                messages.append({"role": "user", "content": q})
                response = client.chat.completions.create(
                    messages=messages,
                    model=model_name,
                    max_tokens=64,
                )
                answer = response.choices[0].message.content
                answers.append(answer)
            except Exception:
                answers.append("Invalid Response")
        return answers

    # We'll use 8 threads to generate answers faster in parallel
    with ThreadPool(8) as pool:
        for answers in tqdm(
            pool.imap(get_answers, coqa_dataset_validation),
            total=len(coqa_dataset_validation),
        ):
            model_answers.append(answers)

    return model_answers
```

3. Generate answers from both models:

```python Python theme={null}
base_answers = get_model_answers(base_model)
finetuned_answers = get_model_answers(finetuned_model)
```

4. Define a function to calculate evaluation metrics:

```python Python theme={null}
import transformers.data.metrics.squad_metrics as squad_metrics


def get_metrics(pred_answers):
    """
    Calculate the Exact Match (EM) and F1 metrics for predicted answers.
    Args:
        pred_answers (list): A list of predicted answers.
    Returns:
        tuple: A tuple containing EM score and F1 score.
    """
    em_metrics = []
    f1_metrics = []

    for pred, data in tqdm(
        zip(pred_answers, coqa_dataset_validation),
        total=len(pred_answers),
    ):
        for pred_answer, true_answer in zip(
            pred, data["answers"]["input_text"]
        ):
            em_metrics.append(
                squad_metrics.compute_exact(true_answer, pred_answer)
            )
            f1_metrics.append(
                squad_metrics.compute_f1(true_answer, pred_answer)
            )

    return sum(em_metrics) / len(em_metrics), sum(f1_metrics) / len(f1_metrics)
```

5. Calculate and compare metrics:

```python Python theme={null}
## Calculate metrics for both models
em_base, f1_base = get_metrics(base_answers)
em_ft, f1_ft = get_metrics(finetuned_answers)

print(f"Base Model - EM: {em_base:.2f}, F1: {f1_base:.2f}")
print(f"Fine-tuned Model - EM: {em_ft:.2f}, F1: {f1_ft:.2f}")
```

You should get figures similar to the table below:

| Llama 3.1 8B | EM   | F1   |
| ------------ | ---- | ---- |
| Original     | 0.01 | 0.18 |
| Fine-tuned   | 0.32 | 0.41 |

We can see that the fine-tuned model performs significantly better on the test set, with a large improvement in both Exact Match and F1 scores.

## Advanced Topics

**Continuing a Fine-tuning Job**

You can continue training from a previous fine-tuning job:

<CodeGroup>
  ```python Python theme={null}
  response = client.fine_tuning.create(
      training_file="your-new-training-file-id",
      from_checkpoint="previous-finetune-job-id",
      wandb_api_key="your-wandb-api-key",
  )
  ```

  ```shell Shell theme={null}
  together fine-tuning create \
    --training-file "your-new-training-file-id" \
    --from-checkpoint "previous-finetune-job-id" \
    --wandb-api-key $WANDB_API_KEY
  ```
</CodeGroup>

You can specify a checkpoint by using:

* The output model name from the previous job
* Fine-tuning job ID
* A specific checkpoint step with the format `ft-...:{STEP_NUM}`

To check all available checkpoints for a job, use:

```shell Shell theme={null}
together fine-tuning list-checkpoints {FT_JOB_ID}
```

### Continued Fine-tuning jobs and LoRA Serverless Inference

Continued Fine-tuning supports various training method combinations: you can train an adapter module on top of a fully trained model or continue training an existing adapter from a previous job. Therefore, LoRA Serverless can be enabled or disabled after training is completed.
If you continue a LoRA fine-tuning job with the same LoRA hyperparameters (rank, alpha, selected modules), the trained model will be available for LoRA Serverless. However, if you change any of these parameters or continue with Full training, LoRA Serverless will be disabled. Additionally, if you continue a Full fine-tuning job, LoRA Serverless will remain disabled.
\*Note: The feature is disabled when parameters change because the Fine-tuning API merges the parent fine-tuning adapter to the base model when it detects different adapter hyperparameters, ensuring optimal training quality.

**Training and Validation Split**

To split your dataset into training and validation sets:

```shell Shell theme={null}
split_ratio=0.9  # Specify the split ratio for your training set

total_lines=$(wc -l < "your-datafile.jsonl")
split_lines=$((total_lines * split_ratio))

head -n $split_lines "your-datafile.jsonl" > "your-datafile-train.jsonl"
tail -n +$((split_lines + 1)) "your-datafile.jsonl" > "your-datafile-validation.jsonl"
```

**Using a Validation Set During Training**

A validation set is a held-out dataset to evaluate your model performance during training on unseen data. Using a validation set provides multiple benefits such as monitoring for overfitting and helping with hyperparameter tuning.

To use a validation set, provide `validation_file` and set `n_evals` to a number above 0:

```python Python theme={null}
response = client.fine_tuning.create(
    training_file="your-training-file-id",
    validation_file="your-validation-file-id",
    n_evals=10,  # Number of evaluations over the entire job
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
)
```

At set intervals during training, the model will be evaluated on your validation set, and the evaluation loss will be recorded in your job event log. If you provide a W\&B API key, you'll also be able to see these losses in the W\&B dashboard.

**Recap**

Fine-tuning LLMs with Together AI allows you to create specialized models tailored to your specific requirements. By following this guide, you've learned how to:

1. Prepare and format your data for fine-tuning
2. Launch a fine-tuning job with appropriate parameters
3. Monitor the progress of your fine-tuning job
4. Use your fine-tuned model via API or dedicated endpoints
5. Evaluate your model's performance improvements
6. Work with advanced features like continued training and validation sets


# Function Calling
Source: https://docs.together.ai/docs/function-calling

Learn how to get LLMs to respond to queries with named functions and structured arguments.

## Introduction

Function calling (also called *tool calling*) enables LLMs to respond with structured function names and arguments that you can execute in your application. This allows models to interact with external systems, retrieve real-time data, and power agentic AI workflows.

Pass function descriptions to the `tools` parameter, and the model will return `tool_calls` when it determines a function should be used. You can then execute these functions and optionally pass the results back to the model for further processing.

## Basic Function Calling

Let's say our application has access to a `get_current_weather` function which takes in two named arguments,`location` and `unit`:

<CodeGroup>
  ```python Python theme={null}
  ## Hypothetical function that exists in our app
  get_current_weather(location="San Francisco, CA", unit="fahrenheit")
  ```

  ```typescript TypeScript theme={null}
  // Hypothetical function that exists in our app
  getCurrentWeather({
    location: "San Francisco, CA",
    unit: "fahrenheit",
  });
  ```
</CodeGroup>

We can make this function available to our LLM by passing its description to the `tools` key alongside the user's query. Let's suppose the user asks, "What is the current temperature of New York?"

<CodeGroup>
  ```python Python theme={null}
  import json
  from together import Together

  client = Together()

  response = client.chat.completions.create(
      model="Qwen/Qwen2.5-7B-Instruct-Turbo",
      messages=[
          {
              "role": "system",
              "content": "You are a helpful assistant that can access external functions. The responses from these function calls will be appended to this dialogue. Please provide responses based on the information from these function calls.",
          },
          {
              "role": "user",
              "content": "What is the current temperature of New York?",
          },
      ],
      tools=[
          {
              "type": "function",
              "function": {
                  "name": "get_current_weather",
                  "description": "Get the current weather in a given location",
                  "parameters": {
                      "type": "object",
                      "properties": {
                          "location": {
                              "type": "string",
                              "description": "The city and state, e.g. San Francisco, CA",
                          },
                          "unit": {
                              "type": "string",
                              "enum": ["celsius", "fahrenheit"],
                          },
                      },
                  },
              },
          }
      ],
  )

  print(
      json.dumps(
          response.choices[0].message.model_dump()["tool_calls"],
          indent=2,
      )
  )
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const response = await together.chat.completions.create({
    model: "Qwen/Qwen2.5-7B-Instruct-Turbo",
    messages: [
      {
        role: "system",
        content:
          "You are a helpful assistant that can access external functions. The responses from these function calls will be appended to this dialogue. Please provide responses based on the information from these function calls.",
      },
      {
        role: "user",
        content: "What is the current temperature of New York?",
      },
    ],
    tools: [
      {
        type: "function",
        function: {
          name: "getCurrentWeather",
          description: "Get the current weather in a given location",
          parameters: {
            type: "object",
            properties: {
              location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA",
              },
              unit: {
                type: "string",
                description: "The unit of temperature",
                enum: ["celsius", "fahrenheit"],
              },
            },
          },
        },
      },
    ],
  });

  console.log(JSON.stringify(response.choices[0].message?.tool_calls, null, 2));
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "Qwen/Qwen2.5-7B-Instruct-Turbo",
         "messages": [
           {
             "role": "system",
             "content": "You are a helpful assistant that can access external functions. The responses from these function calls will be appended to this dialogue. Please provide responses based on the information from these function calls."
           },
           {
             "role": "user",
             "content": "What is the current temperature of New York?"
           }
         ],
         "tools": [
           {
             "type": "function",
             "function": {
               "name": "get_current_weather",
               "description": "Get the current weather in a given location",
               "parameters": {
                 "type": "object",
                 "properties": {
                   "location": {
                     "type": "string",
                     "description": "The city and state, e.g. San Francisco, CA"
                   },
                   "unit": {
                     "type": "string",
                     "enum": ["celsius", "fahrenheit"]
                   }
                 }
               }
             }
           }
         ]
       }'
  ```
</CodeGroup>

The model will respond with a single function call in the `tool_calls` array, specifying the function name and arguments needed to get the weather for New York.

```json JSON theme={null}
[
  {
    "index": 0,
    "id": "call_aisak3q1px3m2lzb41ay6rwf",
    "type": "function",
    "function": {
      "arguments": "{\"location\":\"New York, NY\",\"unit\":\"fahrenheit\"}",
      "name": "get_current_weather"
    }
  }
]
```

As we can see, the LLM has given us a function call that we can programmatically execute to answer the user's question.

### Streaming

Function calling also works with streaming responses. When streaming is enabled, tool calls are returned incrementally and can be accessed from the `delta.tool_calls` object in each chunk.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  tools = [
      {
          "type": "function",
          "function": {
              "name": "get_weather",
              "description": "Get current temperature for a given location.",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type": "string",
                          "description": "City and country e.g. Bogotá, Colombia",
                      }
                  },
                  "required": ["location"],
                  "additionalProperties": False,
              },
              "strict": True,
          },
      }
  ]

  stream = client.chat.completions.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      messages=[{"role": "user", "content": "What's the weather in NYC?"}],
      tools=tools,
      stream=True,
  )

  for chunk in stream:
      delta = chunk.choices[0].delta
      tool_calls = getattr(delta, "tool_calls", [])
      print(tool_calls)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const tools = [
    {
      type: "function",
      function: {
        name: "get_weather",
        description: "Get current temperature for a given location.",
        parameters: {
          type: "object",
          properties: {
            location: {
              type: "string",
              description: "City and country e.g. Bogotá, Colombia",
            },
          },
          required: ["location"],
          additionalProperties: false,
        },
        strict: true,
      },
    },
  ];

  const stream = await client.chat.completions.create({
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages: [{ role: "user", content: "What's the weather in NYC?" }],
    tools,
    stream: true,
  });

  for await (const chunk of stream) {
    const delta = chunk.choices[0]?.delta;
    const toolCalls = delta?.tool_calls ?? [];
    console.log(toolCalls);
  }
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
         "messages": [
           {
             "role": "user",
             "content": "What'\''s the weather in NYC?"
           }
         ],
         "tools": [
           {
             "type": "function",
             "function": {
               "name": "get_weather",
               "description": "Get current temperature for a given location.",
               "parameters": {
                 "type": "object",
                 "properties": {
                   "location": {
                     "type": "string",
                     "description": "City and country e.g. Bogotá, Colombia"
                   }
                 },
                 "required": ["location"],
                 "additionalProperties": false
               },
               "strict": true
             }
           }
         ],
         "stream": true
       }'
  ```
</CodeGroup>

The model will respond with streamed function calls:

```json  theme={null}
[# delta 1
  {
    "index": 0,
    "id": "call_fwbx4e156wigo9ayq7tszngh",
    "type": "function",
    "function": {
      "name": "get_weather",
      "arguments": ""
    }
  }
]
# delta 2
[
  {
    "index": 0,
    "function": {
      "arguments": "{\"location\":\"New York City, USA\"}"
    }
  }
]
```

## Supported models

The following models currently support function calling:

* `openai/gpt-oss-120b`
* `openai/gpt-oss-20b`
* `moonshotai/Kimi-K2-Instruct`
* `zai-org/GLM-4.5-Air-FP8`
* `Qwen/Qwen3-Next-80B-A3B-Instruct`
* `Qwen/Qwen3-Next-80B-A3B-Thinking`
* `Qwen/Qwen3-235B-A22B-Thinking-2507`
* `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`
* `Qwen/Qwen3-235B-A22B-fp8-tput`
* `deepseek-ai/DeepSeek-R1`
* `deepseek-ai/DeepSeek-V3`
* `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8`
* `meta-llama/Llama-4-Scout-17B-16E-Instruct`
* `meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo`
* `meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo`
* `meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo`
* `meta-llama/Llama-3.3-70B-Instruct-Turbo`
* `meta-llama/Llama-3.2-3B-Instruct-Turbo`
* `Qwen/Qwen2.5-7B-Instruct-Turbo`
* `Qwen/Qwen2.5-72B-Instruct-Turbo`
* `mistralai/Mistral-Small-24B-Instruct-2501`
* `arcee-ai/virtuoso-large`

## Types of Function Calling

Function calling can be implemented in six different patterns, each serving different use cases:

| **Type**              | **Description**                         | **Use Cases**                           |
| --------------------- | --------------------------------------- | --------------------------------------- |
| **Simple**            | One function, one call                  | Basic utilities, simple queries         |
| **Multiple**          | Choose from many functions              | Many tools, LLM has to choose           |
| **Parallel**          | Same function, multiple calls           | Complex prompts, multiple tools called  |
| **Parallel Multiple** | Multiple functions, parallel calls      | Complex single requests with many tools |
| **Multi-Step**        | Sequential function calling in one turn | Data processing workflows               |
| **Multi-Turn**        | Conversational context + functions      | AI Agents with humans in the loop       |

Understanding these types of function calling patterns helps you choose the right approach for your application, from simple utilities to sophisticated agentic behaviors.

### 1. Simple Function Calling

This is the most basic type of function calling where one function is defined and one user prompt triggers one function call. The model identifies the need to call the function and extracts the right parameters.

This is the example presented in the above code. Only one tool is provided to the model and it responds with one invocation of the tool.

### 2. Multiple Function Calling

Multiple function calling involves having several different functions available, with the model choosing the best function to call based on the user's intent. The model must understand the request and select the appropriate tool from the available options.

In the example below we provide two tools to the model and it responds with one tool invocation.

<CodeGroup>
  ```python Python theme={null}
  import json
  from together import Together

  client = Together()

  tools = [
      {
          "type": "function",
          "function": {
              "name": "get_current_weather",
              "description": "Get the current weather in a given location",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type": "string",
                          "description": "The city and state, e.g. San Francisco, CA",
                      },
                      "unit": {
                          "type": "string",
                          "enum": ["celsius", "fahrenheit"],
                      },
                  },
              },
          },
      },
      {
          "type": "function",
          "function": {
              "name": "get_current_stock_price",
              "description": "Get the current stock price for a given stock symbol",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "symbol": {
                          "type": "string",
                          "description": "The stock symbol, e.g. AAPL, GOOGL, TSLA",
                      },
                      "exchange": {
                          "type": "string",
                          "description": "The stock exchange (optional)",
                          "enum": ["NYSE", "NASDAQ", "LSE", "TSX"],
                      },
                  },
                  "required": ["symbol"],
              },
          },
      },
  ]

  response = client.chat.completions.create(
      model="Qwen/Qwen2.5-7B-Instruct-Turbo",
      messages=[
          {
              "role": "user",
              "content": "What's the current price of Apple's stock?",
          },
      ],
      tools=tools,
  )

  print(
      json.dumps(
          response.choices[0].message.model_dump()["tool_calls"],
          indent=2,
      )
  )
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const tools = [
    {
      type: "function",
      function: {
        name: "getCurrentWeather",
        description: "Get the current weather in a given location",
        parameters: {
          type: "object",
          properties: {
            location: {
              type: "string",
              description: "The city and state, e.g. San Francisco, CA",
            },
            unit: {
              type: "string",
              description: "The unit of temperature",
              enum: ["celsius", "fahrenheit"],
            },
          },
        },
      },
    },
    {
      type: "function",
      function: {
        name: "getCurrentStockPrice",
        description: "Get the current stock price for a given stock symbol",
        parameters: {
          type: "object",
          properties: {
            symbol: {
              type: "string",
              description: "The stock symbol, e.g. AAPL, GOOGL, TSLA",
            },
            exchange: {
              type: "string",
              description: "The stock exchange (optional)",
              enum: ["NYSE", "NASDAQ", "LSE", "TSX"],
            },
          },
          required: ["symbol"],
        },
      },
    },
  ];

  const response = await together.chat.completions.create({
    model: "Qwen/Qwen2.5-7B-Instruct-Turbo",
    messages: [
      {
        role: "user",
        content: "What's the current price of Apple's stock?",
      },
    ],
    tools,
  });

  console.log(JSON.stringify(response.choices[0].message?.tool_calls, null, 2));
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "Qwen/Qwen2.5-7B-Instruct-Turbo",
         "messages": [
           {
             "role": "user",
             "content": "What'\''s the current price of Apple'\''s stock?"
           }
         ],
         "tools": [
           {
             "type": "function",
             "function": {
               "name": "get_current_weather",
               "description": "Get the current weather in a given location",
               "parameters": {
                 "type": "object",
                 "properties": {
                   "location": {
                     "type": "string",
                     "description": "The city and state, e.g. San Francisco, CA"
                   },
                   "unit": {
                     "type": "string",
                     "enum": ["celsius", "fahrenheit"]
                   }
                 }
               }
             }
           },
           {
             "type": "function",
             "function": {
               "name": "get_current_stock_price",
               "description": "Get the current stock price for a given stock symbol",
               "parameters": {
                 "type": "object",
                 "properties": {
                   "symbol": {
                     "type": "string",
                     "description": "The stock symbol, e.g. AAPL, GOOGL, TSLA"
                   },
                   "exchange": {
                     "type": "string",
                     "description": "The stock exchange (optional)",
                     "enum": ["NYSE", "NASDAQ", "LSE", "TSX"]
                   }
                 },
                 "required": ["symbol"]
               }
             }
           }
         ]
       }'
  ```
</CodeGroup>

In this example, even though both weather and stock functions are available, the model correctly identifies that the user is asking about stock prices and calls the `get_current_stock_price` function.

#### Selecting a specific tool

If you'd like to manually select a specific tool to use for a completion, pass in the tool's name to the `tool_choice` parameter:

<CodeGroup>
  ```python Python theme={null}
  response = client.chat.completions.create(
      model="Qwen/Qwen2.5-7B-Instruct-Turbo",
      messages=[
          {
              "role": "user",
              "content": "What's the current price of Apple's stock?",
          },
      ],
      tools=tools,
      tool_choice={
          "type": "function",
          "function": {"name": "get_current_stock_price"},
      },
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await together.chat.completions.create({
    model: "Qwen/Qwen2.5-7B-Instruct-Turbo",
    messages: [
      {
        role: "user",
        content: "What's the current price of Apple's stock?",
      },
    ],
    tools,
    tool_choice: { type: "function", function: { name: "getCurrentStockPrice" } },
  });
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "Qwen/Qwen2.5-7B-Instruct-Turbo",
         "messages": [
           {
             "role": "user",
             "content": "What'\''s the current price of Apple'\''s stock?"
           }
         ],
         "tools": [
           {
             "type": "function",
             "function": {
               "name": "get_current_stock_price",
               "description": "Get the current stock price for a given stock symbol",
               "parameters": {
                 "type": "object",
                 "properties": {
                   "symbol": {
                     "type": "string",
                     "description": "The stock symbol, e.g. AAPL, GOOGL, TSLA"
                   }
                 },
                 "required": ["symbol"]
               }
             }
           }
         ],
         "tool_choice": {
           "type": "function",
           "function": {
             "name": "get_current_stock_price"
           }
         }
       }'
  ```
</CodeGroup>

This ensures the model will use the specified function when generating its response, regardless of the user's phrasing.

#### Understanding tool\_choice options

The `tool_choice` parameter controls how the model uses functions. It accepts:

**String values:**

* `"auto"` (default) - Model decides whether to call a function or generate a text response
* `"none"` - Model will never call functions, only generates text
* `"required"` - Model must call at least one function

### 3. Parallel Function Calling

In parallel function calling, the same function is called multiple times simultaneously with different parameters. This is more efficient than making sequential calls for similar operations.

<CodeGroup>
  ```python Python theme={null}
  import json
  from together import Together

  client = Together()

  response = client.chat.completions.create(
      model="Qwen/Qwen2.5-7B-Instruct-Turbo",
      messages=[
          {
              "role": "system",
              "content": "You are a helpful assistant that can access external functions. The responses from these function calls will be appended to this dialogue. Please provide responses based on the information from these function calls.",
          },
          {
              "role": "user",
              "content": "What is the current temperature of New York, San Francisco and Chicago?",
          },
      ],
      tools=[
          {
              "type": "function",
              "function": {
                  "name": "get_current_weather",
                  "description": "Get the current weather in a given location",
                  "parameters": {
                      "type": "object",
                      "properties": {
                          "location": {
                              "type": "string",
                              "description": "The city and state, e.g. San Francisco, CA",
                          },
                          "unit": {
                              "type": "string",
                              "enum": ["celsius", "fahrenheit"],
                          },
                      },
                  },
              },
          }
      ],
  )

  print(
      json.dumps(
          response.choices[0].message.model_dump()["tool_calls"],
          indent=2,
      )
  )
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const response = await together.chat.completions.create({
    model: "Qwen/Qwen2.5-7B-Instruct-Turbo",
    messages: [
      {
        role: "system",
        content:
          "You are a helpful assistant that can access external functions. The responses from these function calls will be appended to this dialogue. Please provide responses based on the information from these function calls.",
      },
      {
        role: "user",
        content:
          "What is the current temperature of New York, San Francisco and Chicago?",
      },
    ],
    tools: [
      {
        type: "function",
        function: {
          name: "getCurrentWeather",
          description: "Get the current weather in a given location",
          parameters: {
            type: "object",
            properties: {
              location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA",
              },
              unit: {
                type: "string",
                description: "The unit of temperature",
                enum: ["celsius", "fahrenheit"],
              },
            },
          },
        },
      },
    ],
  });

  console.log(JSON.stringify(response.choices[0].message?.tool_calls, null, 2));
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "Qwen/Qwen2.5-7B-Instruct-Turbo",
         "messages": [
           {
             "role": "system",
             "content": "You are a helpful assistant that can access external functions. The responses from these function calls will be appended to this dialogue. Please provide responses based on the information from these function calls."
           },
           {
             "role": "user",
             "content": "What is the current temperature of New York, San Francisco and Chicago?"
           }
         ],
         "tools": [
           {
             "type": "function",
             "function": {
               "name": "get_current_weather",
               "description": "Get the current weather in a given location",
               "parameters": {
                 "type": "object",
                 "properties": {
                   "location": {
                     "type": "string",
                     "description": "The city and state, e.g. San Francisco, CA"
                   },
                   "unit": {
                     "type": "string",
                     "enum": ["celsius", "fahrenheit"]
                   }
                 }
               }
             }
           }
         ]
       }'
  ```
</CodeGroup>

In response, the `tool_calls` key of the LLM's response will look like this:

```json JSON theme={null}
[
  {
    "index": 0,
    "id": "call_aisak3q1px3m2lzb41ay6rwf",
    "type": "function",
    "function": {
      "arguments": "{\"location\":\"New York, NY\",\"unit\":\"fahrenheit\"}",
      "name": "get_current_weather"
    }
  },
  {
    "index": 1,
    "id": "call_agrjihqjcb0r499vrclwrgdj",
    "type": "function",
    "function": {
      "arguments": "{\"location\":\"San Francisco, CA\",\"unit\":\"fahrenheit\"}",
      "name": "get_current_weather"
    }
  },
  {
    "index": 2,
    "id": "call_17s148ekr4hk8m5liicpwzkk",
    "type": "function",
    "function": {
      "arguments": "{\"location\":\"Chicago, IL\",\"unit\":\"fahrenheit\"}",
      "name": "get_current_weather"
    }
  }
]
```

As we can see, the LLM has given us three function calls that we can programmatically execute to answer the user's question.

### 4. Parallel Multiple Function Calling

This pattern combines parallel and multiple function calling: multiple different functions are available, and one user prompt triggers multiple different function calls simultaneously. The model chooses which functions to call AND calls them in parallel.

<CodeGroup>
  ```python Python theme={null}
  import json
  from together import Together

  client = Together()

  tools = [
      {
          "type": "function",
          "function": {
              "name": "get_current_weather",
              "description": "Get the current weather in a given location",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type": "string",
                          "description": "The city and state, e.g. San Francisco, CA",
                      },
                      "unit": {
                          "type": "string",
                          "enum": ["celsius", "fahrenheit"],
                      },
                  },
              },
          },
      },
      {
          "type": "function",
          "function": {
              "name": "get_current_stock_price",
              "description": "Get the current stock price for a given stock symbol",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "symbol": {
                          "type": "string",
                          "description": "The stock symbol, e.g. AAPL, GOOGL, TSLA",
                      },
                      "exchange": {
                          "type": "string",
                          "description": "The stock exchange (optional)",
                          "enum": ["NYSE", "NASDAQ", "LSE", "TSX"],
                      },
                  },
                  "required": ["symbol"],
              },
          },
      },
  ]

  response = client.chat.completions.create(
      model="Qwen/Qwen2.5-7B-Instruct-Turbo",
      messages=[
          {
              "role": "user",
              "content": "What's the current price of Apple and Google stock? What is the weather in New York, San Francisco and Chicago?",
          },
      ],
      tools=tools,
  )

  print(
      json.dumps(
          response.choices[0].message.model_dump()["tool_calls"],
          indent=2,
      )
  )
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const tools = [
    {
      type: "function",
      function: {
        name: "getCurrentWeather",
        description: "Get the current weather in a given location",
        parameters: {
          type: "object",
          properties: {
            location: {
              type: "string",
              description: "The city and state, e.g. San Francisco, CA",
            },
            unit: {
              type: "string",
              enum: ["celsius", "fahrenheit"],
            },
          },
        },
      },
    },
    {
      type: "function",
      function: {
        name: "getCurrentStockPrice",
        description: "Get the current stock price for a given stock symbol",
        parameters: {
          type: "object",
          properties: {
            symbol: {
              type: "string",
              description: "The stock symbol, e.g. AAPL, GOOGL, TSLA",
            },
            exchange: {
              type: "string",
              description: "The stock exchange (optional)",
              enum: ["NYSE", "NASDAQ", "LSE", "TSX"],
            },
          },
          required: ["symbol"],
        },
      },
    },
  ];

  const response = await together.chat.completions.create({
    model: "Qwen/Qwen2.5-7B-Instruct-Turbo",
    messages: [
      {
        role: "user",
        content:
          "What's the current price of Apple and Google stock? What is the weather in New York, San Francisco and Chicago?",
      },
    ],
    tools,
  });

  console.log(JSON.stringify(response.choices[0].message?.tool_calls, null, 2));
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "Qwen/Qwen2.5-7B-Instruct-Turbo",
         "messages": [
           {
             "role": "user",
             "content": "What'\''s the current price of Apple and Google stock? What is the weather in New York, San Francisco and Chicago?"
           }
         ],
         "tools": [
           {
             "type": "function",
             "function": {
               "name": "get_current_weather",
               "description": "Get the current weather in a given location",
               "parameters": {
                 "type": "object",
                 "properties": {
                   "location": {
                     "type": "string",
                     "description": "The city and state, e.g. San Francisco, CA"
                   },
                   "unit": {
                     "type": "string",
                     "enum": ["celsius", "fahrenheit"]
                   }
                 }
               }
             }
           },
           {
             "type": "function",
             "function": {
               "name": "get_current_stock_price",
               "description": "Get the current stock price for a given stock symbol",
               "parameters": {
                 "type": "object",
                 "properties": {
                   "symbol": {
                     "type": "string",
                     "description": "The stock symbol, e.g. AAPL, GOOGL, TSLA"
                   },
                   "exchange": {
                     "type": "string",
                     "description": "The stock exchange (optional)",
                     "enum": ["NYSE", "NASDAQ", "LSE", "TSX"]
                   }
                 },
                 "required": ["symbol"]
               }
             }
           }
         ]
       }'
  ```
</CodeGroup>

This will result in five function calls: two for stock prices (Apple and Google) and three for weather information (New York, San Francisco, and Chicago), all executed in parallel.

```json JSON theme={null}
[
  {
    "id": "call_8b31727cf80f41099582a259",
    "type": "function",
    "function": {
      "name": "get_current_stock_price",
      "arguments": "{\"symbol\": \"AAPL\"}"
    },
    "index": null
  },
  {
    "id": "call_b54bcaadceec423d82f28611",
    "type": "function",
    "function": {
      "name": "get_current_stock_price",
      "arguments": "{\"symbol\": \"GOOGL\"}"
    },
    "index": null
  },
  {
    "id": "call_f1118a9601c644e1b78a4a8c",
    "type": "function",
    "function": {
      "name": "get_current_weather",
      "arguments": "{\"location\": \"San Francisco, CA\"}"
    },
    "index": null
  },
  {
    "id": "call_95dc5028837e4d1e9b247388",
    "type": "function",
    "function": {
      "name": "get_current_weather",
      "arguments": "{\"location\": \"New York, NY\"}"
    },
    "index": null
  },
  {
    "id": "call_1b8b58809d374f15a5a990d9",
    "type": "function",
    "function": {
      "name": "get_current_weather",
      "arguments": "{\"location\": \"Chicago, IL\"}"
    },
    "index": null
  }
]
```

### 5. Multi-Step Function Calling

Multi-step function calling involves sequential function calls within one conversation turn. Functions are called, results are processed, then used to inform the final response. This demonstrates the complete flow from initial function calls to processing function results to final response incorporating all the data.

Here's an example of passing the result of a tool call from one completion into a second follow-up completion:

<CodeGroup>
  ```python Python theme={null}
  import json
  from together import Together

  client = Together()


  ## Example function to make available to model
  def get_current_weather(location, unit="fahrenheit"):
      """Get the weather for some location"""
      if "chicago" in location.lower():
          return json.dumps(
              {"location": "Chicago", "temperature": "13", "unit": unit}
          )
      elif "san francisco" in location.lower():
          return json.dumps(
              {"location": "San Francisco", "temperature": "55", "unit": unit}
          )
      elif "new york" in location.lower():
          return json.dumps(
              {"location": "New York", "temperature": "11", "unit": unit}
          )
      else:
          return json.dumps({"location": location, "temperature": "unknown"})


  # 1. Define a list of callable tools for the model
  tools = [
      {
          "type": "function",
          "function": {
              "name": "get_current_weather",
              "description": "Get the current weather in a given location",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type": "string",
                          "description": "The city and state, e.g. San Francisco, CA",
                      },
                      "unit": {
                          "type": "string",
                          "description": "The unit of temperature",
                          "enum": ["celsius", "fahrenheit"],
                      },
                  },
              },
          },
      }
  ]

  # Create a running messages list we will add to over time
  messages = [
      {
          "role": "system",
          "content": "You are a helpful assistant that can access external functions. The responses from these function calls will be appended to this dialogue. Please provide responses based on the information from these function calls.",
      },
      {
          "role": "user",
          "content": "What is the current temperature of New York, San Francisco and Chicago?",
      },
  ]

  # 2. Prompt the model with tools defined
  response = client.chat.completions.create(
      model="Qwen/Qwen2.5-7B-Instruct-Turbo",
      messages=messages,
      tools=tools,
  )

  # Save function call outputs for subsequent requests
  tool_calls = response.choices[0].message.tool_calls

  if tool_calls:
      # Add the assistant's response with tool calls to messages
      messages.append(
          {
              "role": "assistant",
              "content": "",
              "tool_calls": [tool_call.model_dump() for tool_call in tool_calls],
          }
      )

      # 3. Execute the function logic for each tool call
      for tool_call in tool_calls:
          function_name = tool_call.function.name
          function_args = json.loads(tool_call.function.arguments)

          if function_name == "get_current_weather":
              function_response = get_current_weather(
                  location=function_args.get("location"),
                  unit=function_args.get("unit"),
              )

              # 4. Provide function call results to the model
              messages.append(
                  {
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": function_name,
                      "content": function_response,
                  }
              )

      # 5. The model should be able to give a response with the function results!
      function_enriched_response = client.chat.completions.create(
          model="Qwen/Qwen2.5-7B-Instruct-Turbo",
          messages=messages,
      )
      print(
          json.dumps(
              function_enriched_response.choices[0].message.model_dump(),
              indent=2,
          )
      )
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";
  import { CompletionCreateParams } from "together-ai/resources/chat/completions.mjs";

  const together = new Together();

  // Example function to make available to model
  function getCurrentWeather({
    location,
    unit = "fahrenheit",
  }: {
    location: string;
    unit: "fahrenheit" | "celsius";
  }) {
    let result: { location: string; temperature: number | null; unit: string };
    if (location.toLowerCase().includes("chicago")) {
      result = {
        location: "Chicago",
        temperature: 13,
        unit,
      };
    } else if (location.toLowerCase().includes("san francisco")) {
      result = {
        location: "San Francisco",
        temperature: 55,
        unit,
      };
    } else if (location.toLowerCase().includes("new york")) {
      result = {
        location: "New York",
        temperature: 11,
        unit,
      };
    } else {
      result = {
        location,
        temperature: null,
        unit,
      };
    }

    return JSON.stringify(result);
  }

  const tools = [
    {
      type: "function",
      function: {
        name: "getCurrentWeather",
        description: "Get the current weather in a given location",
        parameters: {
          type: "object",
          properties: {
            location: {
              type: "string",
              description: "The city and state, e.g. San Francisco, CA",
            },
            unit: {
              type: "string",
              enum: ["celsius", "fahrenheit"],
            },
          },
        },
      },
    },
  ];

  const messages: CompletionCreateParams.Message[] = [
    {
      role: "system",
      content:
        "You are a helpful assistant that can access external functions. The responses from these function calls will be appended to this dialogue. Please provide responses based on the information from these function calls.",
    },
    {
      role: "user",
      content:
        "What is the current temperature of New York, San Francisco and Chicago?",
    },
  ];

  const response = await together.chat.completions.create({
    model: "Qwen/Qwen2.5-7B-Instruct-Turbo",
    messages,
    tools,
  });

  const toolCalls = response.choices[0].message?.tool_calls;
  if (toolCalls) {
    messages.push({
      role: "assistant",
      content: "",
      tool_calls: toolCalls,
    });
    for (const toolCall of toolCalls) {
      if (toolCall.function.name === "getCurrentWeather") {
        const args = JSON.parse(toolCall.function.arguments);
        const functionResponse = getCurrentWeather(args);

        messages.push({
          role: "tool",
          content: functionResponse,
        });
      }
    }

    const functionEnrichedResponse = await together.chat.completions.create({
      model: "Qwen/Qwen2.5-7B-Instruct-Turbo",
      messages,
      tools,
    });

    console.log(
      JSON.stringify(functionEnrichedResponse.choices[0].message, null, 2),
    );
  }
  ```
</CodeGroup>

And here's the final output from the second call:

```json JSON theme={null}
{
  "content": "The current temperature in New York is 11 degrees Fahrenheit, in San Francisco it is 55 degrees Fahrenheit, and in Chicago it is 13 degrees Fahrenheit.",
  "role": "assistant"
}
```

We've successfully used our LLM to generate three tool call descriptions, iterated over those descriptions to execute each one, and passed the results into a follow-up message to get the LLM to produce a final answer!

### 6. Multi-Turn Function Calling

Multi-turn function calling represents the most sophisticated form of function calling, where context is maintained across multiple conversation turns and functions can be called at any point in the conversation. Previous function results inform future decisions, enabling truly agentic behavior.

<CodeGroup>
  ```python Python theme={null}
  import json
  from together import Together

  client = Together()

  # Define all available tools for the travel assistant
  tools = [
      {
          "type": "function",
          "function": {
              "name": "get_current_weather",
              "description": "Get the current weather in a given location",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type": "string",
                          "description": "The city and state, e.g. San Francisco, CA",
                      },
                      "unit": {
                          "type": "string",
                          "description": "The unit of temperature",
                          "enum": ["celsius", "fahrenheit"],
                      },
                  },
                  "required": ["location"],
              },
          },
      },
      {
          "type": "function",
          "function": {
              "name": "get_restaurant_recommendations",
              "description": "Get restaurant recommendations for a specific location",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type": "string",
                          "description": "The city and state, e.g. San Francisco, CA",
                      },
                      "cuisine_type": {
                          "type": "string",
                          "description": "Type of cuisine preferred",
                          "enum": [
                              "italian",
                              "chinese",
                              "mexican",
                              "american",
                              "french",
                              "japanese",
                              "any",
                          ],
                      },
                      "price_range": {
                          "type": "string",
                          "description": "Price range preference",
                          "enum": ["budget", "mid-range", "upscale", "any"],
                      },
                  },
                  "required": ["location"],
              },
          },
      },
  ]


  def get_current_weather(location, unit="fahrenheit"):
      """Get the weather for some location"""
      if "chicago" in location.lower():
          return json.dumps(
              {
                  "location": "Chicago",
                  "temperature": "13",
                  "unit": unit,
                  "condition": "cold and snowy",
              }
          )
      elif "san francisco" in location.lower():
          return json.dumps(
              {
                  "location": "San Francisco",
                  "temperature": "65",
                  "unit": unit,
                  "condition": "mild and partly cloudy",
              }
          )
      elif "new york" in location.lower():
          return json.dumps(
              {
                  "location": "New York",
                  "temperature": "28",
                  "unit": unit,
                  "condition": "cold and windy",
              }
          )
      else:
          return json.dumps(
              {
                  "location": location,
                  "temperature": "unknown",
                  "condition": "unknown",
              }
          )


  def get_restaurant_recommendations(
      location, cuisine_type="any", price_range="any"
  ):
      """Get restaurant recommendations for a location"""
      restaurants = {}

      if "san francisco" in location.lower():
          restaurants = {
              "italian": ["Tony's Little Star Pizza", "Perbacco"],
              "chinese": ["R&G Lounge", "Z&Y Restaurant"],
              "american": ["Zuni Café", "House of Prime Rib"],
              "seafood": ["Swan Oyster Depot", "Fisherman's Wharf restaurants"],
          }
      elif "chicago" in location.lower():
          restaurants = {
              "italian": ["Gibsons Italia", "Piccolo Sogno"],
              "american": ["Alinea", "Girl & Goat"],
              "pizza": ["Lou Malnati's", "Giordano's"],
              "steakhouse": ["Gibsons Bar & Steakhouse"],
          }
      elif "new york" in location.lower():
          restaurants = {
              "italian": ["Carbone", "Don Angie"],
              "american": ["The Spotted Pig", "Gramercy Tavern"],
              "pizza": ["Joe's Pizza", "Prince Street Pizza"],
              "fine_dining": ["Le Bernardin", "Eleven Madison Park"],
          }

      return json.dumps(
          {
              "location": location,
              "cuisine_filter": cuisine_type,
              "price_filter": price_range,
              "restaurants": restaurants,
          }
      )


  def handle_conversation_turn(messages, user_input):
      """Handle a single conversation turn with potential function calls"""
      # 3. Add user input to messages
      messages.append({"role": "user", "content": user_input})

      # 4. Get model response with tools
      response = client.chat.completions.create(
          model="Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8",
          messages=messages,
          tools=tools,
      )

      tool_calls = response.choices[0].message.tool_calls

      if tool_calls:
          # 5. Add assistant response with tool calls
          messages.append(
              {
                  "role": "assistant",
                  "content": response.choices[0].message.content or "",
                  "tool_calls": [
                      tool_call.model_dump() for tool_call in tool_calls
                  ],
              }
          )

          # 6. Execute each function call
          for tool_call in tool_calls:
              function_name = tool_call.function.name
              function_args = json.loads(tool_call.function.arguments)

              print(f"🔧 Calling {function_name} with args: {function_args}")

              # Route to appropriate function
              if function_name == "get_current_weather":
                  function_response = get_current_weather(
                      location=function_args.get("location"),
                      unit=function_args.get("unit", "fahrenheit"),
                  )
              elif function_name == "get_activity_suggestions":
                  function_response = get_activity_suggestions(
                      location=function_args.get("location"),
                      weather_condition=function_args.get("weather_condition"),
                      activity_type=function_args.get("activity_type", "both"),
                  )
              elif function_name == "get_restaurant_recommendations":
                  function_response = get_restaurant_recommendations(
                      location=function_args.get("location"),
                      cuisine_type=function_args.get("cuisine_type", "any"),
                      price_range=function_args.get("price_range", "any"),
                  )

              # 7. Add function response to messages
              messages.append(
                  {
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": function_name,
                      "content": function_response,
                  }
              )

          # 8. Get final response with function results
          final_response = client.chat.completions.create(
              model="Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8",
              messages=messages,
          )

          # 9. Add final assistant response to messages for context retention
          messages.append(
              {
                  "role": "assistant",
                  "content": final_response.choices[0].message.content,
              }
          )

          return final_response.choices[0].message.content


  # Initialize conversation with system message
  messages = [
      {
          "role": "system",
          "content": "You are a helpful travel planning assistant. You can access weather information and restaurant recommendations. Use the available tools to provide comprehensive travel advice based on the user's needs.",
      }
  ]

  # TURN 1: Initial weather request
  print("TURN 1:")
  print(
      "User: What is the current temperature of New York, San Francisco and Chicago?"
  )
  response1 = handle_conversation_turn(
      messages,
      "What is the current temperature of New York, San Francisco and Chicago?",
  )
  print(f"Assistant: {response1}")

  # TURN 2: Follow-up with activity and restaurant requests based on previous context
  print("\nTURN 2:")
  print(
      "User: Based on the weather, which city would be best for outdoor activities? And can you find some restaurant recommendations for that city?"
  )
  response2 = handle_conversation_turn(
      messages,
      "Based on the weather, which city would be best for outdoor activities? And can you find some restaurant recommendations for that city?",
  )
  print(f"Assistant: {response2}")
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";
  import { CompletionCreateParams } from "together-ai/resources/chat/completions.mjs";

  const together = new Together();

  const tools = [
    {
      type: "function",
      function: {
        name: "getCurrentWeather",
        description: "Get the current weather in a given location",
        parameters: {
          type: "object",
          properties: {
            location: {
              type: "string",
              description: "The city and state, e.g. San Francisco, CA",
            },
            unit: {
              type: "string",
              description: "The unit of temperature",
              enum: ["celsius", "fahrenheit"],
            },
          },
          required: ["location"],
        },
      },
    },
    {
      type: "function",
      function: {
        name: "getRestaurantRecommendations",
        description: "Get restaurant recommendations for a specific location",
        parameters: {
          type: "object",
          properties: {
            location: {
              type: "string",
              description: "The city and state, e.g. San Francisco, CA",
            },
            cuisineType: {
              type: "string",
              description: "Type of cuisine preferred",
              enum: [
                "italian",
                "chinese",
                "mexican",
                "american",
                "french",
                "japanese",
                "any",
              ],
            },
            priceRange: {
              type: "string",
              description: "Price range preference",
              enum: ["budget", "mid-range", "upscale", "any"],
            },
          },
          required: ["location"],
        },
      },
    },
  ];

  function getCurrentWeather({
    location,
    unit = "fahrenheit",
  }: {
    location: string;
    unit?: string;
  }) {
    if (location.toLowerCase().includes("chicago")) {
      return JSON.stringify({
        location: "Chicago",
        temperature: "13",
        unit,
        condition: "cold and snowy",
      });
    } else if (location.toLowerCase().includes("san francisco")) {
      return JSON.stringify({
        location: "San Francisco",
        temperature: "65",
        unit,
        condition: "mild and partly cloudy",
      });
    } else if (location.toLowerCase().includes("new york")) {
      return JSON.stringify({
        location: "New York",
        temperature: "28",
        unit,
        condition: "cold and windy",
      });
    } else {
      return JSON.stringify({
        location,
        temperature: "unknown",
        condition: "unknown",
      });
    }
  }

  function getRestaurantRecommendations({
    location,
    cuisineType = "any",
    priceRange = "any",
  }: {
    location: string;
    cuisineType?: string;
    priceRange?: string;
  }) {
    let restaurants = {};

    if (location.toLowerCase().includes("san francisco")) {
      restaurants = {
        italian: ["Tony's Little Star Pizza", "Perbacco"],
        chinese: ["R&G Lounge", "Z&Y Restaurant"],
        american: ["Zuni Café", "House of Prime Rib"],
        seafood: ["Swan Oyster Depot", "Fisherman's Wharf restaurants"],
      };
    } else if (location.toLowerCase().includes("chicago")) {
      restaurants = {
        italian: ["Gibsons Italia", "Piccolo Sogno"],
        american: ["Alinea", "Girl & Goat"],
        pizza: ["Lou Malnati's", "Giordano's"],
        steakhouse: ["Gibsons Bar & Steakhouse"],
      };
    } else if (location.toLowerCase().includes("new york")) {
      restaurants = {
        italian: ["Carbone", "Don Angie"],
        american: ["The Spotted Pig", "Gramercy Tavern"],
        pizza: ["Joe's Pizza", "Prince Street Pizza"],
        fine_dining: ["Le Bernardin", "Eleven Madison Park"],
      };
    }

    return JSON.stringify({
      location,
      cuisine_filter: cuisineType,
      price_filter: priceRange,
      restaurants,
    });
  }

  async function handleConversationTurn(
    messages: CompletionCreateParams.Message[],
    userInput: string,
  ) {
    messages.push({ role: "user", content: userInput });

    const response = await together.chat.completions.create({
      model: "Qwen/Qwen2.5-7B-Instruct-Turbo",
      messages,
      tools,
    });

    const toolCalls = response.choices[0].message?.tool_calls;

    if (toolCalls) {
      messages.push({
        role: "assistant",
        content: response.choices[0].message?.content || "",
        tool_calls: toolCalls,
      });

      for (const toolCall of toolCalls) {
        const functionName = toolCall.function.name;
        const functionArgs = JSON.parse(toolCall.function.arguments);

        let functionResponse: string;

        if (functionName === "getCurrentWeather") {
          functionResponse = getCurrentWeather(functionArgs);
        } else if (functionName === "getRestaurantRecommendations") {
          functionResponse = getRestaurantRecommendations(functionArgs);
        } else {
          functionResponse = "Function not found";
        }

        messages.push({
          role: "tool",
          content: functionResponse,
        });
      }

      const finalResponse = await together.chat.completions.create({
        model: "Qwen/Qwen2.5-7B-Instruct-Turbo",
        messages,
      });

      const content = finalResponse.choices[0].message?.content || "";
      messages.push({
        role: "assistant",
        content,
      });

      return content;
    } else {
      const content = response.choices[0].message?.content || "";
      messages.push({
        role: "assistant",
        content,
      });
      return content;
    }
  }

  // Example usage
  async function runMultiTurnExample() {
    const messages: CompletionCreateParams.Message[] = [
      {
        role: "system",
        content:
          "You are a helpful travel planning assistant. You can access weather information and restaurant recommendations. Use the available tools to provide comprehensive travel advice based on the user's needs.",
      },
    ];

    console.log("TURN 1:");
    console.log(
      "User: What is the current temperature of New York, San Francisco and Chicago?",
    );
    const response1 = await handleConversationTurn(
      messages,
      "What is the current temperature of New York, San Francisco and Chicago?",
    );
    console.log(`Assistant: ${response1}`);

    console.log("\nTURN 2:");
    console.log(
      "User: Based on the weather, which city would be best for outdoor activities? And can you find some restaurant recommendations for that city?",
    );
    const response2 = await handleConversationTurn(
      messages,
      "Based on the weather, which city would be best for outdoor activities? And can you find some restaurant recommendations for that city?",
    );
    console.log(`Assistant: ${response2}`);
  }

  runMultiTurnExample();
  ```
</CodeGroup>

In this example, the assistant:

1. **Turn 1**: Calls weather functions for three cities and provides temperature information
2. **Turn 2**: Remembers the previous weather data, analyzes which city is best for outdoor activities (San Francisco with 65°F), and automatically calls the restaurant recommendation function for that city

This demonstrates true agentic behavior where the AI maintains context across turns and makes informed decisions based on previous interactions.


# OpenAI GPT-OSS Quickstart
Source: https://docs.together.ai/docs/gpt-oss

Get started with OpenAI's GPT-OSS, open-source reasoning model duo.

These flexible open-weight reasoning models are designed for developers, researchers, and enterprises who need transparency, customization while maintaining the advanced reasoning capabilities of chain-of-thought processing.

Both GPT-OSS models have been trained to think step-by-step before responding with an answer, excelling at complex reasoning tasks such as coding, mathematics, planning, puzzles, and agent workflows.

They feature adjustable reasoning effort levels, allowing you to balance performance with computational cost.

<Frame>
  <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/gpt-oss-reasoning-example.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=6b173eab1f762ef00a189dc46029fc01" data-og-width="3928" width="3928" data-og-height="1128" height="1128" data-path="images/gpt-oss-reasoning-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/gpt-oss-reasoning-example.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=f848788b205dd4bebb2f8aa1855f5f3a 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/gpt-oss-reasoning-example.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=f1d81ab32e7e7d797eb7d0762dfa4c80 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/gpt-oss-reasoning-example.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=6714bf9c96f79f21311f10f072a812eb 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/gpt-oss-reasoning-example.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=0bc9baca3794463d2b5ac6ac3c9c175d 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/gpt-oss-reasoning-example.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=087ec6ad065525b032dcf2535a872df7 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/gpt-oss-reasoning-example.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=565156e88fe58ce56bf955cf3f3d39e2 2500w" />
</Frame>

## How to use GPT-OSS API

These models are only available to Build Tier 1 or higher users. Since reasoning models produce longer responses with chain-of-thought processing, we recommend streaming tokens for better user experience:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()  # pass in API key to api_key or set a env variable

  stream = client.chat.completions.create(
      model="openai/gpt-oss-120b",
      messages=[
          {
              "role": "user",
              "content": "Solve this logic puzzle: If all roses are flowers and some flowers are red, can we conclude that some roses are red?",
          }
      ],
      temperature=1.0,
      top_p=1.0,
      reasoning_effort="medium",
      stream=True,
  )

  for chunk in stream:
      print(chunk.choices[0].delta.content or "", end="", flush=True)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";
  const together = new Together();

  const stream = await together.chat.completions.create({
    model: "openai/gpt-oss-120b",
    messages: [{ 
      role: "user", 
      content: "Solve this logic puzzle: If all roses are flowers and some flowers are red, can we conclude that some roses are red?" 
    }],
    temperature: 1.0,
    top_p: 1.0,
    reasoning_effort: "medium",
    stream: true,
  });

  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || "");
  }
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
       	"model": "openai/gpt-oss-120b",
       	"messages": [
            {"role": "user", "content": "Solve this logic puzzle: If all roses are flowers and some flowers are red, can we conclude that some roses are red?"}
       	],
          "temperature": 1.0,
          "top_p": 1.0,
          "reasoning_effort": "medium",
          "stream": true
       }'
  ```
</CodeGroup>

This will produce the response below:

```plain  theme={null}
{
  "id": "o669aLj-62bZhn-96b01dc00f33ab9a",
  "object": "chat.completion",
  "created": 1754499896,
  "model": "openai/gpt-oss-120b",
  "service_tier": null,
  "system_fingerprint": null,
  "kv_transfer_params": null,
  "prompt": [],
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "**Short answer:**  \nNo. From “All roses are flowers” and “Some flowers are red” ...",
        "tool_calls": [],
        "reasoning": "We need to answer the logic puzzle. Statement: All roses ..."
      },
      "logprobs": null,
      "finish_reason": "stop",
      "seed": null
    }
  ],
  "usage": {
    "prompt_tokens": 96,
    "total_tokens": 984,
    "completion_tokens": 888
  }
}
```

To access just the chain-of-thought reasoning you can look at the `reasoning` property:

```plain  theme={null}
We need to answer the logic puzzle. The premise: "All roses are flowers" (i.e., every rose is a flower). "Some flowers are red" (there exists at least one flower that is red). Does this entail that some roses are red? In standard syllogistic logic, no; you cannot infer that. Because the red flower could be a different type. The conclusion "Some roses are red" is not guaranteed. It's a classic syllogism: All R are F, Some F are R (actually some F are red). The conclusion "Some R are red" is not valid (invalid). So answer: No, we cannot conclude; we need additional assumption like "All red flowers are roses" or "All red things are roses". Provide explanation.

Hence final answer: no, not necessarily; situation possible where all roses are yellow etc.

Thus solve puzzle.
```

## Available Models

Two flexible open-weight models are available to meet different deployment needs:

**GPT-OSS 120B:**

* **Model String**: `openai/gpt-oss-120b`
* **Hardware Requirements**: Fits on 80GB GPU
* **Architecture**: Mixture-of-Experts (MoE) with token-choice routing
* **Context Length**: 128k tokens with RoPE
* **Best for**: Enterprise applications requiring maximum reasoning performance

**GPT-OSS 20B:**

* **Model String**: `openai/gpt-oss-20b`
* **Hardware Requirements**: Lower GPU memory requirements
* **Architecture**: Optimized MoE for efficiency
* **Context Length**: 128k tokens with RoPE
* **Best for**: Research, development, and cost-efficient deployments

## GPT-OSS Best Practices

Reasoning models like GPT-OSS should be used differently than standard instruct models to get optimal results:

**Recommended Parameters:**

* **Reasoning Effort**: Use the adjustable reasoning effort levels to control computational cost vs. accuracy.
* **Temperature**: Use 1.0 for maximum creativity and diverse reasoning approaches.
* **Top-p**: Use 1.0 to allow the full vocabulary distribution for optimal reasoning exploration.
* **System Prompt**: The system prompt can be provided as a `developer` message which is used to provide information about the instructions for the model and available function tools.
* **System message**: It's recommended not to modify the `system` message which is used to specify reasoning effort, meta information like knowledge cutoff and built-in tools.

**Prompting Best Practices:**
Think of GPT-OSS as a senior problem-solver – provide high-level objectives and let it determine the methodology:

* **Strengths**: Excels at open-ended reasoning, multi-step logic, and inferring unstated requirements
* **Avoid over-prompting**: Micromanaging steps can limit its advanced reasoning capabilities
* **Provide clear objectives**: Balance clarity with flexibility for optimal results

## GPT-OSS Use Cases

* **Code Review & Analysis:** Comprehensive code analysis across large codebases with detailed improvement suggestions
* **Strategic Planning:** Multi-stage planning with reasoning about optimal approaches and resource allocation
* **Complex Document Analysis:** Processing legal contracts, technical specifications, and regulatory documents
* **Benchmarking AI Systems:** Evaluates other LLM responses with contextual understanding, particularly useful in critical validation scenarios
* **AI Model Evaluation:** Sophisticated evaluation of other AI systems with contextual understanding
* **Scientific Research:** Multi-step reasoning for hypothesis generation and experimental design
* **Academic Analysis:** Deep analysis of research papers and literature reviews
* **Information Extraction:** Efficiently extracts relevant data from large volumes of unstructured information, ideal for RAG systems
* **Agent Workflows:** Building sophisticated AI agents with complex reasoning capabilities
* **RAG Systems:** Enhanced information extraction and synthesis from large knowledge bases
* **Problem Solving:** Handling ambiguous requirements and inferring unstated assumptions
* **Ambiguity Resolution:** Interprets unclear instructions effectively and seeks clarification when needed

## Managing Context and Costs

#### **Reasoning Effort Control:**

GPT-OSS features adjustable reasoning effort levels to optimize for your specific use case:

* **Low effort:** Faster responses for simpler tasks with reduced reasoning depth
* **Medium effort:** Balanced performance for most use cases (recommended default)
* **High effort:** Maximum reasoning for complex problems requiring deep analysis. You should also specify `max_tokens` of \~30,000 with this setting.

#### **Token Management:**

When working with reasoning models, it's crucial to maintain adequate space in the context window:

* Use `max_tokens` parameter to control response length and costs
* Monitor reasoning token usage vs. output tokens - reasoning tokens can vary from hundreds to tens of thousands based on complexity
* Consider reasoning effort level based on task complexity and budget constraints
* Simpler problems may only require a few hundred reasoning tokens, while complex challenges could generate extensive reasoning

#### **Cost/Latency Optimization:**

* Implement limits on total token generation using the `max_tokens` parameter
* Balance thorough reasoning with resource utilization based on your specific requirements
* Consider using lower reasoning effort for routine tasks and higher effort for critical decisions

## Technical Architecture

#### **Model Architecture:**

* **MoE Design:** Token-choice Mixture-of-Experts with SwiGLU activations for improved performance
* **Expert Selection:** Softmax-after-topk approach for calculating MoE weights, ensuring optimal expert utilization
* **Attention Mechanism:** RoPE (Rotary Position Embedding) with 128k context length
* **Attention Patterns:** Alternating between full context and sliding 128-token window for efficiency
* **Attention Sink:** Learned attention sink per-head with additional additive value in the softmax denominator

#### **Tokenization:**

* **Standard Compatibility:** Uses the same tokenizer as GPT-4o
* **Broad Support:** Ensures seamless integration with existing applications and tools

#### **Context Handling:**

* **128k Context Window:** Large context capacity for processing extensive documents
* **Efficient Patterns:** Optimized attention patterns for long-context scenarios
* **Memory Optimization:** GPT-OSS Large designed to fit efficiently within 80GB GPU memory


# Guides Homepage
Source: https://docs.together.ai/docs/guides

Quickstarts and step-by-step guides for building with Together AI.

export const GridGuides = ({children}) => {
  return <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3 md:gap-4 xl:gap-6">
      {children}
    </div>;
};

export const GuideCard = ({title, description, href, badges = [], className = ""}) => {
  const getTagColor = tag => {
    const tagColors = {
      python: {
        bg: "#dbeafe",
        text: "#1e40af"
      },
      typescript: {
        bg: "#dcfce7",
        text: "#166534"
      },
      chat: {
        bg: "#e0f2fe",
        text: "#0c4a6e"
      },
      audio: {
        bg: "#fef3c7",
        text: "#92400e"
      },
      vision: {
        bg: "#f3e8ff",
        text: "#6b21a8"
      },
      agents: {
        bg: "#e0e7ff",
        text: "#3730a3"
      },
      rerank: {
        bg: "#cffafe",
        text: "#0e7490"
      },
      "bing-api": {
        bg: "#dbeafe",
        text: "#1e40af"
      },
      embeddings: {
        bg: "#e0e7ff",
        text: "#3730a3"
      },
      rag: {
        bg: "#ecfdf5",
        text: "#166534"
      },
      huggingface: {
        bg: "#fef3c7",
        text: "#92400e"
      },
      "vercel-ai-sdk": {
        bg: "#f9fafb",
        text: "#111827"
      },
      mastra: {
        bg: "#ecfdf5",
        text: "#166534"
      },
      workflows: {
        bg: "#f1f5f9",
        text: "#334155"
      },
      sequential: {
        bg: "#ccfbf1",
        text: "#0f766e"
      },
      parallel: {
        bg: "#f3e8ff",
        text: "#7c3aed"
      },
      async: {
        bg: "#fce7f3",
        text: "#be185d"
      },
      routing: {
        bg: "#fed7aa",
        text: "#9a3412"
      },
      json: {
        bg: "#f9fafb",
        text: "#374151"
      },
      optimization: {
        bg: "#d1fae5",
        text: "#065f46"
      },
      ensemble: {
        bg: "#fce7f3",
        text: "#be185d"
      },
      cli: {
        bg: "#cffafe",
        text: "#0e7490"
      },
      terminal: {
        bg: "#d1fae5",
        text: "#065f46"
      },
      frameworks: {
        bg: "#cffafe",
        text: "#0e7490"
      },
      langgraph: {
        bg: "#f3e8ff",
        text: "#6b21a8"
      },
      crewai: {
        bg: "#fef2f2",
        text: "#991b1b"
      },
      training: {
        bg: "#fed7aa",
        text: "#9a3412"
      },
      "instant-clusters": {
        bg: "#f3e8ff",
        text: "#7c3aed"
      }
    };
    const tagName = tag.toLowerCase().replace(/ /g, "-");
    if (tagColors[tagName]) {
      return {
        bg: tagColors[tagName].bg,
        text: tagColors[tagName].text
      };
    }
    return {
      bg: "#f9fafb",
      text: "#374151"
    };
  };
  const CardContent = <div className={`flex flex-col justify-start items-start w-full overflow-hidden gap-2.5 px-5 py-4 rounded-2xl bg-white dark:bg-transparent dark:hover:bg-[#0B0C0E] border border-[#d9e1ec] dark:border-gray-700 hover:bg-gray-50 transition-all ${className}`}>
      <div className="flex flex-col justify-start items-start self-stretch flex-grow-0 flex-shrink-0 gap-2">
        {badges.length > 0 && <div className="flex justify-start items-start flex-grow-0 flex-shrink-0 gap-2.5 flex-wrap">
            {badges.map((badge, index) => {
    const colors = getTagColor(badge);
    return <div key={index} className={`flex justify-center items-center flex-grow-0 flex-shrink-0 relative overflow-hidden gap-2.5 px-2 py-1 rounded-[100px] dark:invert`} style={{
      backgroundColor: colors.bg
    }}>
                  <p className="flex-grow-0 flex-shrink-0 text-xs text-center capitalize" style={{
      color: colors.text
    }}>
                    {badge}
                  </p>
                </div>;
  })}
          </div>}
        <div className="flex flex-col justify-start items-start self-stretch flex-grow-0 flex-shrink-0 relative gap-1.5">
          <p className="self-stretch flex-grow-0 flex-shrink-0 text-base text-left text-black dark:text-white font-normal">
            {title}
          </p>
          <p className="flex-grow-0 flex-shrink-0 text-sm font-light text-left text-neutral-600 dark:text-gray-400">
            {description}
          </p>
        </div>
      </div>
    </div>;
  if (href) {
    return <a href={href} className="flex underline-none outline-none border-none">
        {CardContent}
      </a>;
  }
  return CardContent;
};

export const SubHeading = ({heading, description}) => {
  return <div className="flex flex-col md:flex-row gap-6 items-center mb-3 mt-10">
      <p className="text-lg font-medium text-left text-neutral-900 dark:text-white">
        {heading}
      </p>
      <p className="text-base text-left text-neutral-600 dark:text-gray-400">{description}</p>
    </div>;
};

<SubHeading heading={"Agents"} description={"Design agent loops, tools, and planners"} />

<GridGuides>
  <GuideCard title="Agent Workflows" description="Orchestrating together multiple language model calls to solve complex tasks." href="/docs/workflows" badges={["workflows", "python"]} />

  <GuideCard title="Sequential Agent Workflow" description="Tasks execute one after another when later steps depend on earlier ones." href="/docs/sequential-agent-workflow" badges={["sequential", "python"]} />

  <GuideCard title="Parallel Workflows" description="Multiple tasks execute simultaneously for improved performance." href="/docs/parallel-workflows" badges={["async", "parallel", "python"]} />

  <GuideCard title="Conditional Workflows" description="The workflow branches based on evaluation results." href="/docs/conditional-workflows" badges={["routing", "json", "python"]} />

  <GuideCard title="Iterative Workflow" description="A task repeats until a condition is met for optimization." href="/docs/iterative-workflow" badges={["optimization", "json", "python"]} />

  <GuideCard title="Agent Integrations" description="Using OSS agent frameworks with Together AI" href="/docs/integrations-2" badges={["frameworks", "langgraph", "crewai"]} />
</GridGuides>

<SubHeading heading={"Apps"} description={"Full-stack patterns you can copy"} />

<GridGuides>
  <GuideCard title="How to Build Coding Agents" description="How to build your own simple code editing agent from scratch in 400 lines of code!" href="/docs/how-to-build-coding-agents" badges={["chat", "python"]} />

  <GuideCard title="How to Build a Lovable Clone with Kimi K2" description="Learn how to build a full-stack Next.js app that can generate React apps with a single prompt." href="/docs/how-to-build-a-lovable-clone-with-kimi-k2" badges={["chat", "typescript"]} />

  <GuideCard title="How to Build Real-time Audio Transcription App" description="Build real-time audio transcription using Together AI models." href="/docs/how-to-build-real-time-audio-transcription-app" badges={["audio", "typescript"]} />

  <GuideCard title="Data Analyst Agent" description="Build an AI agent that can analyze data and provide insights." href="/docs/data-analyst-agent" badges={["agents", "python"]} />

  <GuideCard title="Open NotebookLM PDF to Podcast" description="Convert PDF documents into podcast episodes using AI." href="/docs/open-notebooklm-pdf-to-podcast" badges={["chat", "typescript"]} />

  <GuideCard title="AI Tutor" description="Build an intelligent tutoring system with Together AI." href="/docs/ai-tutor" badges={["agents", "python"]} />
</GridGuides>

<SubHeading heading={"Search & RAG"} description={"Build intelligent search and retrieval systems"} />

<GridGuides>
  <GuideCard title="How to Improve Search With Rerankers" description="Learn how you can improve semantic search quality with reranker models!" href="/docs/how-to-improve-search-with-rerankers" badges={["rerank", "python"]} />

  <GuideCard title="AI Search Engine" description="Build a simplified Perplexity-style search using Together models." href="/docs/ai-search-engine" badges={["bing-api", "typescript"]} />

  <GuideCard title="Building a RAG Workflow" description="Combine retrieval and generation to build grounded RAG apps." href="/docs/building-a-rag-workflow" badges={["embeddings", "rag", "python"]} />

  <GuideCard title="How to Implement Contextual RAG from Anthropic" description="Implement advanced RAG techniques with contextual understanding." href="/docs/how-to-implement-contextual-rag-from-anthropic" badges={["rag", "rerank", "python"]} />

  <GuideCard title="Quickstart Retrieval Augmented Generation RAG" description="Get started with RAG using Together AI's powerful models." href="/docs/quickstart-retrieval-augmented-generation-rag" badges={["rag", "embeddings", "python"]} />
</GridGuides>

<SubHeading heading={"General Guides"} description={"Essential guides and tutorials"} />

<GridGuides>
  <GuideCard title="How to run nanochat on Instant Clusters⚡️" description="Learn how to train Andrej Karpathy's end-to-end ChatGPT clone on Together's on-demand GPU clusters" href="/docs/nanochat-on-instant-clusters" badges={["training", "instant clusters", "python"]} />

  <GuideCard title="Quickstart Using Hugging Face Inference" description="Use Together AI with Hugging Face models and workflows." href="/docs/quickstart-using-hugging-face-inference" badges={["huggingface", "python"]} />

  <GuideCard title="Using Together with Vercel's AI SDK" description="Build powerful apps with Vercel's AI SDK and Together AI." href="/docs/using-together-with-vercels-ai-sdk" badges={["vercel-ai-sdk", "typescript"]} />

  <GuideCard title="Using Together with Mastra" description="Integrate Together AI models with the Mastra framework for building AI-powered features." href="/docs/using-together-with-mastra" badges={["mastra-ai", "typescript"]} />

  <GuideCard title="Logprobs" description="Understanding and using log probabilities in language models." href="/docs/logprobs" badges={["chat"]} />

  <GuideCard title="Next.js Chat Quickstart" description="Spin up a production-ready chatbot using Together + Next.js." href="/docs/nextjs-chat-quickstart" badges={["chat", "typescript"]} />

  <GuideCard title="Quickstart How to Do OCR" description="Build optical character recognition applications with AI." href="/docs/quickstart-how-to-do-ocr" badges={["vision", "typescript"]} />

  <GuideCard title="How to Use Cline" description="Get started with Cline for AI-powered development." href="/docs/how-to-use-cline" badges={["CLI", "Terminal"]} />

  <GuideCard title="Videos" description="Generate high-quality videos from text and image prompts." href="/docs/videos-overview" badges={["video", "python", "typescript"]} />

  <GuideCard title="Mixture of Agents" description="Combine multiple agents for enhanced problem-solving capabilities." href="/docs/mixture-of-agents" badges={["async", "ensemble", "python"]} />
</GridGuides>


# How to build a Lovable clone with Kimi K2
Source: https://docs.together.ai/docs/how-to-build-a-lovable-clone-with-kimi-k2

Learn how to build a full-stack Next.js app that can generate React apps with a single prompt.

[LlamaCoder](https://llamacoder.together.ai/) is a Lovable-inspired app that shows off how easy it is to use Together AI’s hosted LLM endpoints to build AI applications.

<Frame><img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/15.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=3b9b258e4c650436c4d23d7aaff5b353" alt="" data-og-width="3376" width="3376" data-og-height="2540" height="2540" data-path="images/guides/15.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/15.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=905423269b6f7e4306aa553b4a12f57a 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/15.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=4c3ce7093f84a9654ed00b2505190ed0 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/15.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=9e38e79a45f690f712fb7496f62346ef 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/15.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a46451f89eecf67d8baf39a1327860df 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/15.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=cd8515f6e993aef6d73b0d179b406653 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/15.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=dd47ab385e02accc9abd75eb226ec202 2500w" /></Frame>

In this post, we’re going to learn how to build the core parts of the app. LlamaCoder is a Next.js app, but Together’s APIs can be used with any web framework or language!

## Scaffolding the initial UI

The core interaction of LlamaCoder is a text field where the user can enter a prompt for an app they’d like to build. So to start, we need that text field:

<Frame><img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/16.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=f04cf018c8b1314eedcbd166ba252a78" alt="" data-og-width="2000" width="2000" data-og-height="383" height="383" data-path="images/guides/16.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/16.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=26f25c6234027a94051904f4a76a864b 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/16.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=65dbb32b01f68aec98515d5b33d112f1 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/16.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=83162a8f5385e1e608bdc5f0c1803e20 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/16.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=6b435353883cb0bd7772e576422b10fd 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/16.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=88c163011541a34e75fd2e4b56bdcd5f 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/16.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=b477727dd46b647ebe3793d782b1ed58 2500w" /></Frame>

We’ll render a text input inside of a form, and use some new React state to control the input’s value:

```jsx JSX theme={null}
function Page() {
  let [prompt, setPrompt] = useState('');

  return (
    <form>
      <input
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder='Build me a calculator app...'
        required
      />

      <button type='submit'>
        <ArrowLongRightIcon />
      </button>
    </form>
  );
}
```

Next, let’s wire up a submit handler to the form. We’ll call it `createApp`, since it’s going to take the user’s prompt and generate the corresponding app code:

```jsx JSX theme={null}
function Page() {
  let [prompt, setPrompt] = useState('');

  function createApp(e) {
    e.preventDefault();

    // TODO:
    // 1. Generate the code
    // 2. Render the app
  }

  return <form onSubmit={createApp}>{/* ... */}</form>;
}
```

To generate the code, we’ll have our React app query a new API endpoint. Let’s put it at `/api/generateCode` , and we’ll make it a POST endpoint so we can send along the `prompt` in the request body:

```jsx JSX theme={null}
async function createApp(e) {
  e.preventDefault();

  // TODO:
  // 1. Generate the code
  await fetch('/api/generateCode', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt }),
  });

  // 2. Render the app
}
```

Looks good – let’s go implement it!

## Generating code in an API route

To create an API route in the Next.js 14 app directory, we can make a new `route.js` file:

```jsx JSX theme={null}
// app/api/generateCode/route.js
export async function POST(req) {
  let json = await req.json();

  console.log(json.prompt);
}
```

If we submit the form, we’ll see the user’s prompt logged to the console. Now we’re ready to send it off to our LLM and ask it to generate our user’s app! We tested many open source LLMs and found that Kimi K2 was the only one that did a good job at generating small apps, so that’s what we decided to use for the app.

We’ll install Together’s node SDK:

```bash Shell theme={null}
npm i together-ai
```

and use it to kick off a chat with Kimi K2.

Here’s what it looks like:

```jsx JSX theme={null}
// app/api/generateCode/route.js
import Together from 'together-ai';

let together = new Together();

export async function POST(req) {
  let json = await req.json();

  let completion = await together.chat.completions.create({
    model: 'moonshotai/Kimi-K2-Instruct-0905',
    messages: [
      {
        role: 'system',
        content: 'You are an expert frontend React engineer.',
      },
      {
        role: 'user',
        content: json.prompt,
      },
    ],
  });

  return Response.json(completion);
}
```

We call `together.chat.completions.create` to get a new response from the LLM. We’ve supplied it with a “system” message telling the LLM that it should behave as if it’s an expert React engineer. Finally, we provide it with the user’s prompt as the second message.

Since we return a JSON object, let’s update our React code to read the JSON from the response:

```jsx JSX theme={null}
async function createApp(e) {
  e.preventDefault();

  // 1. Generate the code
  let res = await fetch('/api/generateCode', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt }),
  });
  let json = await res.json();

  console.log(json);

  // 2. Render the app
}
```

And now let’s give it a shot!

We’ll use something simple for our prompt like “Build me a counter”:

<Frame><img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/17.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ff79766604b0ecdf613528a6409e0736" alt="" data-og-width="1720" width="1720" data-og-height="305" height="305" data-path="images/guides/17.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/17.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=8b151e6cca96d4f2e47a3df190700cdc 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/17.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=54794fd845d0c953bec237e67a7c89ad 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/17.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5e40a57ddd5d77a77eaa3cc66586a499 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/17.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=580fa4fc21f9a0f60359540893afc9be 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/17.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=abdba72d62968901ce00699ed9c06802 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/17.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=6d3218731f4f3ffdb9cf3ab9558d16be 2500w" /></Frame>

When we submit the form, our API response takes several seconds, but then sends our React app the response.

If you take a look at your logs, you should see something like this:

<Frame><img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/18.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=aecf6247f32c6431afe963569c44f898" alt="" data-og-width="1720" width="1720" data-og-height="1800" height="1800" data-path="images/guides/18.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/18.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7accc4c3d05db2e182692f3104aeb848 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/18.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5d77c5e86c4143c85f677a67d71dea18 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/18.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=88d849973cffa20dfe9bf77e45d42009 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/18.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=b386cc1ca484905abdd2f1bf330b469d 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/18.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=324b5f21f1df81cb8411997c326c86c6 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/18.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=492b5d936cc82ff8c589871cd7036675 2500w" /></Frame>

Not bad – Kimi K2 has generated some code that looks pretty good and matches our user’s prompt!

However, for this app, we’re only interested in the code, since we’re going to be actually running it in our user’s browser. So we need to do some prompt engineering to get Llama to only return the code in a format we expect.

## Engineering the system message to only return code

We spent some time tweaking the system message to make sure it output the best code possible – here’s what we ended up with for LlamaCoder:

```jsx JSX theme={null}
// app/api/generateCode/route.js
import Together from 'together-ai';

let together = new Together();

export async function POST(req) {
  let json = await req.json();

   let res = await together.chat.completions.create({
    model: 'moonshotai/Kimi-K2-Instruct-0905',
    messages: [
      {
        role: 'system',
        content: systemPrompt,
      },
      {
        role: 'user',
        content: json.prompt,
      },
    ],
    stream: true,
  });

  return new Response(res.toReadableStream(), {
    headers: new Headers({
      'Cache-Control': 'no-cache',
    }),
  });
}

let systemPrompt = `
  You are an expert frontend React engineer who is also a great UI/UX designer. Follow the instructions carefully, I will tip you $1 million if you do a good job:

  - Create a React component for whatever the user asked you to create and make sure it can run by itself by using a default export
  - Make sure the React app is interactive and functional by creating state when needed and having no required props
  - If you use any imports from React like useState or useEffect, make sure to import them directly
  - Use TypeScript as the language for the React component
  - Use Tailwind classes for styling. DO NOT USE ARBITRARY VALUES (e.g. \`h-[600px]\`). Make sure to use a consistent color palette.
  - Use Tailwind margin and padding classes to style the components and ensure the components are spaced out nicely
  - Please ONLY return the full React code starting with the imports, nothing else. It's very important for my job that you only return the React code with imports. DO NOT START WITH \`\`\`typescript or \`\`\`javascript or \`\`\`tsx or \`\`\`.

  NO LIBRARIES (e.g. zod, hookform) ARE INSTALLED OR ABLE TO BE IMPORTED.
`;
```

Now if we try again, we’ll see something like this:

<Frame><img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/19.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=f1d16f71f2ca2fa446da7b90498350fa" alt="" data-og-width="1720" width="1720" data-og-height="1714" height="1714" data-path="images/guides/19.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/19.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=676fe6d759e3b106d7e80e99efeb40c6 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/19.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=1ef69aad734b972e522e44d91a27c065 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/19.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=4e677495d33b5b996d75440d8d543181 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/19.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=13e1a373a9da4824702a1e8620460e55 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/19.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=82a8c790748083631447c1702b716392 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/19.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d9301c7cdfde07d1fea3e9d15ccf1417 2500w" /></Frame>

Much better –this is something we can work with!

## Running the generated code in the browser

Now that we’ve got a pure code response from our LLM, how can we actually execute it in the browser for our user?

This is where the phenomenal [Sandpack](https://sandpack.codesandbox.io/) library comes in.

Once we install it:

```bash Shell theme={null}
npm i @codesandbox/sandpack-react
```

we now can use the `<Sandpack>` component to render and execute any code we want!

Let’s give it a shot with some hard-coded sample code:

```jsx JSX theme={null}
<Sandpack
  template='react-ts'
  files={{
    'App.tsx': `export default function App() { return <p>Hello, world!</p> }`,
  }}
/>
```

If we save this and look in the browser, we’ll see that it works!

<Frame><img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/20.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c6a9fec2cfc230edbb74d74604b97a22" alt="" data-og-width="1720" width="1720" data-og-height="1180" height="1180" data-path="images/guides/20.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/20.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=bc0393627d946b795ac5ad6f0ef44d46 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/20.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=8c1db2a93b3625eba3c527c2a070df9c 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/20.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=1f0cb64032a4a1c6a9db54ae0313fdaf 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/20.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=bac010968d019e4eb0d0c2ef5207a12f 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/20.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d2e26c93f30af40354488158f5c1348a 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/20.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=19fcf021a04807fde1414575958ed1ed 2500w" /></Frame>

All that’s left is to swap out our sample code with the code from our API route instead.

Let’s start by storing the LLM’s response in some new React state called `generatedCode`:

```jsx JSX theme={null}
function Page() {
  let [prompt, setPrompt] = useState('');
  let [generatedCode, setGeneratedCode] = useState('');

  async function createApp(e) {
    e.preventDefault();

    let res = await fetch('/api/generateCode', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt }),
    });
    let json = await res.json();

    setGeneratedCode(json.choices[0].message.content);
  }

  return (
    <div>
      <form onSubmit={createApp}>{/* ... */}</form>
    </div>
  );
}
```

Now, if `generatedCode` is not empty, we can render `<Sandpack>` and pass it in:

```jsx JSX theme={null}
function Page() {
  let [prompt, setPrompt] = useState('');
  let [generatedCode, setGeneratedCode] = useState('');

  async function createApp(e) {
    // ...
  }

  return (
    <div>
      <form onSubmit={createApp}>{/* ... */}</form>

      {generatedCode && (
        <Sandpack
          template='react-ts'
          files={{
            'App.tsx': generatedCode,
          }}
        />
      )}
    </div>
  );
}
```

Let’s give it a shot! We’ll try “Build me a calculator app” as the prompt, and submit the form.

Once our API endpoint responds, `<Sandpack>` renders our generated app!

<Frame><img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/21.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=4e47962545fab91b857856e5c92c45db" alt="" data-og-width="1720" width="1720" data-og-height="1085" height="1085" data-path="images/guides/21.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/21.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=4c398c3d3a4b3fc0d2a39843aa6763d2 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/21.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c37d3896bc9375074770efb19dfbc1bb 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/21.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=dceeab1b4725d90850b43c4ca9f5446b 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/21.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d71e5afd3726c523532b2dcd4ca5d546 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/21.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c04f42f9ddc29f6d3c3cf123ded012a4 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/21.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=347a422de6a94c6f29d36f8d302c6f0e 2500w" /></Frame>

The basic functionality is working great! Together AI (with Kimi K2) + Sandpack have made it a breeze to run generated code right in our user’s browser.

## Streaming the code for immediate UI feedback

Our app is working well –but we’re not showing our user any feedback while the LLM is generating the code. This makes our app feel broken and unresponsive, especially for more complex prompts.

To fix this, we can use Together AI’s support for streaming. With a streamed response, we can start displaying partial updates of the generated code as soon as the LLM responds with the first token.

To enable streaming, there’s two changes we need to make:

1. Update our API route to respond with a stream
2. Update our React app to read the stream

Let’s start with the API route.

To get Together to stream back a response, we need to pass the `stream: true` option into `together.chat.completions.create()` . We also need to update our response to call `res.toReadableStream()`, which turns the raw Together stream into a newline-separated ReadableStream of JSON stringified values.

Here’s what that looks like:

```jsx JSX theme={null}
// app/api/generateCode/route.js
import Together from 'together-ai';

let together = new Together();

export async function POST(req) {
  let json = await req.json();

  let res = await together.chat.completions.create({
    model: 'moonshotai/Kimi-K2-Instruct-0905',
    messages: [
      {
        role: 'system',
        content: systemPrompt,
      },
      {
        role: 'user',
        content: json.prompt,
      },
    ],
    stream: true,
  });

  return new Response(res.toReadableStream(), {
    headers: new Headers({
      'Cache-Control': 'no-cache',
    }),
  });
}
```

That’s it for the API route! Now, let’s update our React submit handler.

Currently, it looks like this:

```jsx JSX theme={null}
async function createApp(e) {
  e.preventDefault();

  let res = await fetch('/api/generateCode', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt }),
  });
  let json = await res.json();

  setGeneratedCode(json.choices[0].message.content);
}
```

Now that our response is a stream, we can’t just `res.json()` it. We need a small helper function to read the text from the actual bytes that are being streamed over from our API route.

Here’s the helper function. It uses an [AsyncGenerator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator) to yield out each chunk of the stream as it comes over the network. It also uses a TextDecoder to turn the stream’s data from the type Uint8Array (which is the default type used by streams for their chunks, since it’s more efficient and streams have broad applications) into text, which we then parse into a JSON object.

So let’s copy this function to the bottom of our page:

```jsx JSX theme={null}
async function* readStream(response) {
  let decoder = new TextDecoder();
  let reader = response.getReader();

  while (true) {
    let { done, value } = await reader.read();
    if (done) {
      break;
    }
    let text = decoder.decode(value, { stream: true });
    let parts = text.split('\\n');

    for (let part of parts) {
      if (part) {
        yield JSON.parse(part);
      }
    }
  }

  reader.releaseLock();
}
```

Now, we can update our `createApp` function to iterate over `readStream(res.body)`:

```jsx JSX theme={null}
async function createApp(e) {
  e.preventDefault();

  let res = await fetch('/api/generateCode', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt }),
  });

  for await (let result of readStream(res.body)) {
    setGeneratedCode(
      (prev) => prev + result.choices.map((c) => c.text ?? '').join('')
    );
  }
}
```

This is the cool thing about Async Generators –we can use `for...of` to iterate over each chunk right in our submit handler!

By setting `generatedCode` to the current text concatenated with the new chunk’s text, React automatically re-renders our app as the LLM’s response streams in, and we see `<Sandpack>` updating its UI as the generated app takes shape.

<Frame><img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/22.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=3b1cc77e62ae3caedb66c23dd6976460" alt="" data-og-width="1720" width="1720" data-og-height="1450" height="1450" data-path="images/guides/22.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/22.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5207bb61c14cd5b68db8ff05719cfdbd 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/22.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=cec467f8f423b6583cfd29a57189c747 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/22.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=396ca8897ad1246ffec27b7dd57d541b 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/22.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=1c42b7a7b93d279c93d40d55f99ae204 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/22.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c073ae539f1cbea0c449c43c25eea923 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/22.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=29acec1c6fbf4dfdb19725b6ee9a6cd2 2500w" /></Frame>

Pretty nifty, and now our app is feeling much more responsive!

## Digging deeper

And with that, you now know how to build the core functionality of Llama Coder!

There’s plenty more tricks in the production app including animated loading states, the ability to update an existing app, and the ability to share a public version of your generated app using a Neon Postgres database.

The application is open-source, so check it out here to learn more: **[https://github.com/Nutlope/llamacoder](https://github.com/Nutlope/llamacoder)**

And if you’re ready to start querying LLMs in your own apps to add powerful AI features just like the kind we saw in this post, [sign up for Together AI](https://api.together.ai/) today and make your first query in minutes!



---

**Navigation:** [← Previous](./03-deploying-a-fine-tuned-model.md) | [Index](./index.md) | [Next →](./05-how-to-build-coding-agents.md)
