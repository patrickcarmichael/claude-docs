**Navigation:** [← Previous](./19-instantiate-the-react-agent.md) | [Index](./index.md) | Next →

---

# Deploy your finetuned model on AWS Marketplace

> Learn how to deploy your finetuned model on AWS Marketplace.

<AuthorsContainer
  authors={[
    {
      name: "Youran Qi",
      imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/929cb1c-youran-headshot.jpg"
    }
  ]}
/>

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/finetuning/Deploy%20your%20own%20finetuned%20command-r-0824.ipynb" />

## Deploy Your Own Finetuned Command-R-0824 Model from AWS Marketplace

This sample notebook shows you how to deploy your own finetuned HuggingFace Command-R model [CohereForAI/c4ai-command-r-08-2024](https://huggingface.co/CohereForAI/c4ai-command-r-08-2024) using Amazon SageMaker. More specifically, assuming you already have the adapter weights or merged weights from your own finetuning of [CohereForAI/c4ai-command-r-08-2024](https://huggingface.co/CohereForAI/c4ai-command-r-08-2024), we will show you how to

1. Merge the adapter weights to the weights of the base model, if you bring only the adapter weights
2. Export the merged weights to the TensorRT-LLM inference engine using Amazon SageMaker
3. Deploy the engine as a SageMaker endpoint to serve your business use cases

> **Note**: This is a reference notebook and it cannot run unless you make changes suggested in the notebook.

### Pre-requisites:

1. **Note: This notebook contains elements which render correctly in Jupyter interface. Open this notebook from an Amazon SageMaker Notebook Instance or Amazon SageMaker Studio.**
2. Ensure that IAM role used has **AmazonSageMakerFullAccess**
3. To deploy this ML model successfully, ensure that:
   1. Either your IAM role has these three permissions and you have authority to make AWS Marketplace subscriptions in the AWS account used:
      1. **aws-marketplace:ViewSubscriptions**
      2. **aws-marketplace:Unsubscribe**
      3. **aws-marketplace:Subscribe**
   2. or your AWS account has a subscription to the packages for [Cohere Bring Your Own Fine-tuning](https://aws.amazon.com/marketplace/pp/prodview-5wt5pdnw3bbq6). If so, skip step: [Subscribe to the bring your own finetuning algorithm](#subscribe)

### Contents:

1. [Subscribe to the bring your own finetuning algorithm](#subscribe)
2. [Preliminary setup](#setup)
3. [Get the merged weights](#merge)
4. [Upload the merged weights to S3](#upload)
5. [Export the merged weights to the TensorRT-LLM inference engine](#export)
6. [Create an endpoint for inference from the exported engine](#endpoint)
7. [Perform real-time inference by calling the endpoint](#inference)
8. [Delete the endpoint (optional)](#delete)
9. [Unsubscribe to the listing (optional)](#unsubscribe)

### Usage instructions:

You can run this notebook one cell at a time (By using Shift+Enter for running a cell).

<a name="subscribe" />

## 1. Subscribe to the bring your own finetuning algorithm

To subscribe to the algorithm:

1. Open the algorithm listing page [Cohere Bring Your Own Fine-tuning](https://aws.amazon.com/marketplace/pp/prodview-5wt5pdnw3bbq6).
2. On the AWS Marketplace listing, click on the **Continue to Subscribe** button.
3. On the **Subscribe to this software** page, review and click on **"Accept Offer"** if you and your organization agrees with EULA, pricing, and support terms. On the "Configure and launch" page, make sure the ARN displayed in your region match with the ARN you will use below.

<a name="setup" />

## 2. Preliminary setup

Install the Python packages you will use below and import them. For example, you can run the command below to install `cohere` if you haven't done so.

```sh
pip install "cohere>=5.11.0"
```

```python
import cohere
import os
import sagemaker as sage

from sagemaker.s3 import S3Uploader
```

Make sure you have access to the resources in your AWS account. For example, you can configure an AWS profile by the command `aws configure sso` (see [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html#cli-configure-sso-configure)) and run the command below to set the environment variable `AWS_PROFILE` as your profile name.

```python
# Change "<aws_profile>" to your own AWS profile name
os.environ["AWS_PROFILE"] = "<aws_profile>"
```

Finally, you need to set all the following variables using your own information. In general, do not add a trailing slash to these paths (otherwise some parts won't work). You can use either `ml.p4de.24xlarge` or `ml.p5.48xlarge` as the `instance_type` for Cohere Bring Your Own Fine-tuning, but the `instance_type` used for export and inference (endpoint creation) must be identical.

```python
# The AWS region
region = "<region>"

# Get the arn of the bring your own finetuning algorithm by region
cohere_package = (
    "cohere-command-r-v2-byoft-8370167e649c32a1a5f00267cd334c2c"
)
algorithm_map = {
    "us-east-1": f"arn:aws:sagemaker:us-east-1:865070037744:algorithm/{cohere_package}",
    "us-east-2": f"arn:aws:sagemaker:us-east-2:057799348421:algorithm/{cohere_package}",
    "us-west-2": f"arn:aws:sagemaker:us-west-2:594846645681:algorithm/{cohere_package}",
    "eu-central-1": f"arn:aws:sagemaker:eu-central-1:446921602837:algorithm/{cohere_package}",
    "ap-southeast-1": f"arn:aws:sagemaker:ap-southeast-1:192199979996:algorithm/{cohere_package}",
    "ap-southeast-2": f"arn:aws:sagemaker:ap-southeast-2:666831318237:algorithm/{cohere_package}",
    "ap-northeast-1": f"arn:aws:sagemaker:ap-northeast-1:977537786026:algorithm/{cohere_package}",
    "ap-south-1": f"arn:aws:sagemaker:ap-south-1:077584701553:algorithm/{cohere_package}",
}
if region not in algorithm_map:
    raise Exception(f"Current region {region} is not supported.")
arn = algorithm_map[region]

# The local directory of your adapter weights. No need to specify this, if you bring your own merged weights
adapter_weights_dir = "<adapter_weights_dir>"

# The local directory you want to save the merged weights. Or the local directory of your own merged weights, if you bring your own merged weights
merged_weights_dir = "<merged_weights_dir>"

# The S3 directory you want to save the merged weights
s3_checkpoint_dir = "<s3_checkpoint_dir>"

# The S3 directory you want to save the exported TensorRT-LLM engine. Make sure you do not reuse the same S3 directory across multiple runs
s3_output_dir = "<s3_output_dir>"

# The name of the export
export_name = "<export_name>"

# The name of the SageMaker endpoint
endpoint_name = "<endpoint_name>"

# The instance type for export and inference. Now "ml.p4de.24xlarge" and "ml.p5.48xlarge" are supported
instance_type = "<instance_type>"
```

<a name="merge" />

## 3. Get the merged weights

Assuming you use HuggingFace's [PEFT](https://github.com/huggingface/peft) to finetune [CohereForAI/c4ai-command-r-08-2024](https://huggingface.co/CohereForAI/c4ai-command-r-08-2024) and get the adapter weights, you can then merge your adapter weights to the base model weights to get the merged weights as shown below. Skip this step if you have already got the merged weights.

```python
import torch

from peft import PeftModel
from transformers import CohereForCausalLM


def load_and_merge_model(
    base_model_name_or_path: str, adapter_weights_dir: str
):
    """
    Load the base model and the model finetuned by PEFT, and merge the adapter weights to the base weights to get a model with merged weights
    """
    base_model = CohereForCausalLM.from_pretrained(
        base_model_name_or_path
    )
    peft_model = PeftModel.from_pretrained(
        base_model, adapter_weights_dir
    )
    merged_model = peft_model.merge_and_unload()
    return merged_model


def save_hf_model(output_dir: str, model, tokenizer=None, args=None):
    """
    Save a HuggingFace model (and optionally tokenizer as well as additional args) to a local directory
    """
    os.makedirs(output_dir, exist_ok=True)
    model.save_pretrained(
        output_dir, state_dict=None, safe_serialization=True
    )
    if tokenizer is not None:
        tokenizer.save_pretrained(output_dir)
    if args is not None:
        torch.save(
            args, os.path.join(output_dir, "training_args.bin")
        )
```

```python
# Get the merged model from adapter weights
merged_model = load_and_merge_model(
    "CohereForAI/c4ai-command-r-08-2024", adapter_weights_dir
)

# Save the merged weights to your local directory
save_hf_model(merged_weights_dir, merged_model)
```

<a name="upload" />

## 4. Upload the merged weights to S3

```python
sess = sage.Session()
merged_weights = S3Uploader.upload(
    merged_weights_dir, s3_checkpoint_dir, sagemaker_session=sess
)
print("merged_weights", merged_weights)
```

<a name="export" />

## 5. Export the merged weights to the TensorRT-LLM inference engine

Create Cohere client and use it to export the merged weights to the TensorRT-LLM inference engine. The exported TensorRT-LLM engine will be stored in a tar file `{s3_output_dir}/{export_name}.tar.gz` in S3, where the file name is the same as the `export_name`.

```python
co = cohere.SagemakerClient(aws_region=region)
co.sagemaker_finetuning.export_finetune(
    arn=arn,
    name=export_name,
    s3_checkpoint_dir=s3_checkpoint_dir,
    s3_output_dir=s3_output_dir,
    instance_type=instance_type,
    role="ServiceRoleSagemaker",
)
```

<a name="endpoint" />

## 6. Create an endpoint for inference from the exported engine

The Cohere client provides a built-in method to create an endpoint for inference, which will automatically deploy the model from the TensorRT-LLM engine you just exported.

```python
co.sagemaker_finetuning.create_endpoint(
    arn=arn,
    endpoint_name=endpoint_name,
    s3_models_dir=s3_output_dir,
    recreate=True,
    instance_type=instance_type,
    role="ServiceRoleSagemaker",
)
```

<a name="inference" />

## 7. Perform real-time inference by calling the endpoint

Now, you can perform real-time inference by calling the endpoint you just deployed.

```python
# If the endpoint is already deployed, you can directly connect to it
co.sagemaker_finetuning.connect_to_endpoint(
    endpoint_name=endpoint_name
)

message = "Classify the following text as either very negative, negative, neutral, positive or very positive: mr. deeds is , as comedy goes , very silly -- and in the best way."
result = co.sagemaker_finetuning.chat(message=message)
print(result)
```

You can also evaluate your finetuned model using a evaluation dataset. The following is an example with the [ScienceQA](https://scienceqa.github.io/) evaluation data at [here](https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/data/scienceQA_eval.jsonl).

```python
import json
from tqdm import tqdm

eval_data_path = "<path_to_scienceQA_eval.jsonl>"

total = 0
correct = 0
for line in tqdm(open(eval_data_path).readlines()):
    total += 1
    question_answer_json = json.loads(line)
    question = question_answer_json["messages"][0]["content"]
    answer = question_answer_json["messages"][1]["content"]
    model_ans = co.sagemaker_finetuning.chat(
        message=question, temperature=0
    ).text
    if model_ans == answer:
        correct += 1

print(f"Accuracy of finetuned model is %.3f" % (correct / total))
```

<a name="delete" />

## 8. Delete the endpoint (optional)

After you successfully performed the inference, you can delete the deployed endpoint to avoid being charged continuously.

```python
co.sagemaker_finetuning.delete_endpoint()
co.sagemaker_finetuning.close()
```

<a name="unsubscribe" />

## 9. Unsubscribe to the listing (optional)

If you would like to unsubscribe to the model package, follow these steps. Before you cancel the subscription, ensure that you do not have any [deployable models](https://console.aws.amazon.com/sagemaker/home#/models) created from the model package or using the algorithm. Note - You can find this information by looking at the container name associated with the model.

**Steps to unsubscribe to product from AWS Marketplace**:

1. Navigate to **Machine Learning** tab on [**Your Software subscriptions page**](https://aws.amazon.com/marketplace/ai/library?productType=ml\&ref_=mlmp_gitdemo_indust)
2. Locate the listing that you want to cancel the subscription for, and then choose **Cancel Subscription**  to cancel the subscription.


# Finetuning Cohere Models on AWS Sagemaker

> Learn how to finetune one of Cohere's models on AWS Sagemaker.

<AuthorsContainer
  authors={[
    {
      name: "Mike Mao",
      imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/d514b09-mike-headshot.jpg"
    }
  ]}
/>

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/finetuning/Command%20R%20finetuning%20sagemaker.ipynb" />

## Finetune and deploy a custom Command-R model

This sample notebook shows you how to finetune and deploy a custom Command-R model using Amazon SageMaker.

> **Note**: This is a reference notebook and it cannot run unless you make changes suggested in the notebook.

## Pre-requisites:

1. **Note: This notebook contains elements which render correctly in Jupyter interface. Open this notebook from an Amazon SageMaker Notebook Instance or Amazon SageMaker Studio.**
2. Ensure that IAM role used has **AmazonSageMakerFullAccess**
3. To deploy this ML model successfully, ensure that:
   1. Either your IAM role has these three permissions and you have authority to make AWS Marketplace subscriptions in the AWS account used:
      1. **aws-marketplace:ViewSubscriptions**
      2. **aws-marketplace:Unsubscribe**
      3. **aws-marketplace:Subscribe**
   2. or your AWS account has a subscription to the packages for [Cohere Command R Finetuning](https://aws.amazon.com/marketplace/ai/configuration?productId=1762e582-e7df-47f0-a49f-98e22302a702). If so, skip step: [Subscribe to the finetune algorithm](#1.-Subscribe-to-the-finetune-algorithm)

## Contents:

1. [Subscribe to the finetune algorithm](#1.-Subscribe-to-the-finetune-algorithm)
2. [Upload data and finetune Command-R Model](#2.-Upload-data-and-finetune-Command-R)
3. [Create an endpoint for inference with the custom model](#3.-Create-an-endpoint-for-inference-with-the-custom-model)
   1. [Create an endpoint](#A.-Create-an-endpoint)
   2. [Perform real-time inference](#B.-Perform-real-time-inference)
4. [Clean-up](#4.-Clean-up)
   1. [Delete the endpoint](#A.-Delete-the-endpoint)
   2. [Unsubscribe to the listing (optional)](#Unsubscribe-to-the-listing-\(optional\))

## Usage instructions

You can run this notebook one cell at a time (By using Shift+Enter for running a cell).

## 1. Subscribe to the finetune algorithm

To subscribe to the model algorithm:

1. Open the algorithm listing page [Cohere Command R Finetuning](https://aws.amazon.com/marketplace/pp/prodview-2czs5tbao7b7c)
2. On the AWS Marketplace listing, click on the **Continue to Subscribe** button.
3. On the **Subscribe to this software** page, review and click on **"Accept Offer"** if you and your organization agrees with EULA, pricing, and support terms. On the "Configure and launch" page, make sure ARN displayed in your region match with the ARN in the following cell.

```sh
pip install "cohere>=5.11.0"
```

```python
import cohere
import boto3
import sagemaker as sage
from sagemaker.s3 import S3Uploader
```

The algorithm is available in the list of AWS regions specified below.

```python
region = boto3.Session().region_name

cohere_package = ""
# cohere_package = "cohere-command-r-ft-v-0-1-2-bae2282f0f4a30bca8bc6fea9efeb7ca"

# Mapping for algorithms
algorithm_map = {
    "us-east-1": f"arn:aws:sagemaker:us-east-1:865070037744:algorithm/{cohere_package}",
    "us-east-2": f"arn:aws:sagemaker:us-east-2:057799348421:algorithm/{cohere_package}",
    "us-west-2": f"arn:aws:sagemaker:us-west-2:594846645681:algorithm/{cohere_package}",
    "eu-central-1": f"arn:aws:sagemaker:eu-central-1:446921602837:algorithm/{cohere_package}",
    "ap-southeast-1": f"arn:aws:sagemaker:ap-southeast-1:192199979996:algorithm/{cohere_package}",
    "ap-southeast-2": f"arn:aws:sagemaker:ap-southeast-2:666831318237:algorithm/{cohere_package}",
    "ap-northeast-1": f"arn:aws:sagemaker:ap-northeast-1:977537786026:algorithm/{cohere_package}",
    "ap-south-1": f"arn:aws:sagemaker:ap-south-1:077584701553:algorithm/{cohere_package}",
}
if region not in algorithm_map.keys():
    raise Exception(
        f"Current boto3 session region {region} is not supported."
    )

arn = algorithm_map[region]
```

## 2. Upload data and finetune Command-R

Select a path on S3 to store the training and evaluation datasets and update the **s3\_data\_dir** below:

```python
s3_data_dir = "s3://..."  # Do not add a trailing slash otherwise the upload will not work
```

Upload sample training data to S3:

### Note:

You'll need your data in a .jsonl file that contains chat-formatted data. [Doc](https://docs.cohere.com/docs/chat-preparing-the-data#data-requirements)

### Example:

JSONL:

```
{
  "messages": [
    {
      "role": "System",
      "content": "You are a chatbot trained to answer to my every question."
    },
    {
      "role": "User",
      "content": "Hello"
    },
    {
      "role": "Chatbot",
      "content": "Greetings! How can I help you?"
    },
    {
      "role": "User",
      "content": "What makes a good running route?"
    },
    {
      "role": "Chatbot",
      "content": "A sidewalk-lined road is ideal so that you\u2019re up and off the road away from vehicular traffic."
    }
  ]
}
```

```python
sess = sage.Session()
# TODO[Optional]: change it to your data
# You can download following example datasets from https://github.com/cohere-ai/cohere-developer-experience/tree/main/notebooks/data and upload them
# to the root of this juyter notebook
train_dataset = S3Uploader.upload(
    "./scienceQA_train.jsonl", s3_data_dir, sagemaker_session=sess
)
# optional eval dataset
eval_dataset = S3Uploader.upload(
    "./scienceQA_eval.jsonl", s3_data_dir, sagemaker_session=sess
)
print("traint_dataset", train_dataset)
print("eval_dataset", eval_dataset)
```

**Note:** If eval dataset is absent, we will auto-split the training dataset into training and evaluation datasets with the ratio of 80:20.

Each dataset must contain at least 1 examples. If an evaluation dataset is absent, training dataset must cointain at least 2 examples.

We recommend using a dataset than contains at least 100 examples but a larger dataset is likely to yield high quality finetunes. Be aware that a larger dataset would mean that the time to finetune would also be longer.

Specify a directory on S3 where finetuned models should be stored. **Make sure you *do not reuse the same directory* across multiple runs.**

```python
# TODO update this with a custom S3 path
# DO NOT add a trailing slash at the end
s3_models_dir = f"s3://..."
```

Create Cohere client:

```python
co = cohere.SagemakerClient(region_name=region)
```

#### Optional: Define hyperparameters

* `train_epochs`: Integer. This is the maximum number of training epochs to run for. Defaults to **1**

| Default | Min | Max |
| ------- | --- | --- |
| 1       | 1   | 10  |

* `learning_rate`: Float. The initial learning rate to be used during training. Default to **0.0001**

| Default | Min      | Max |
| ------- | -------- | --- |
| 0.0001  | 0.000005 | 0.1 |

* `train_batch_size`: Integer. The batch size used during training. Defaults to **16** for Command.

| Default | Min | Max |
| ------- | --- | --- |
| 16      | 8   | 32  |

* `early_stopping_enabled`: Boolean. Enables early stopping. When set to true, the final model is the best model found based on the validation set. When set to false, the final model is the last model of training. Defaults to **true**.

* `early_stopping_patience`: Integer. Stop training if the loss metric does not improve beyond 'early\_stopping\_threshold' for this many times of evaluation. Defaults to **10**

| Default | Min | Max |
| ------- | --- | --- |
| 10      | 1   | 15  |

* `early_stopping_threshold`: Float. How much the loss must improve to prevent early stopping. Defaults to **0.001**.

| Default | Min   | Max |
| ------- | ----- | --- |
| 0.001   | 0.001 | 0.1 |

If the algorithm is **command-r-0824-ft**, you have the option to define:

* `lora_rank': Integer`. Lora adapter rank. Defaults to **32**

| Default | Min | Max |
| ------- | --- | --- |
| 32      | 8   | 32  |

```python
# Example of how to pass hyperparameters to the fine-tuning job
train_parameters = {
    "train_epochs": 1,
    "early_stopping_patience": 2,
    "early_stopping_threshold": 0.001,
    "learning_rate": 0.01,
    "train_batch_size": 16,
}
```

Create fine-tuning jobs for the uploaded datasets. Add a field for `eval_data` if you have pre-split your dataset and uploaded both training and evaluation datasets to S3. Remember to use p4de for Command-R Finetuning.

```python
finetune_name = "test-finetune"
co.sagemaker_finetuning.create_finetune(
    arn=arn,
    name=finetune_name,
    train_data=train_dataset,
    eval_data=eval_dataset,
    s3_models_dir=s3_models_dir,
    instance_type="ml.p4de.24xlarge",
    training_parameters=train_parameters,
    role="ServiceRoleSagemaker",
)
```

The finetuned weights for the above will be store in a tar file `{s3_models_dir}/test-finetune.tar.gz` where the file name is the same as the name used during the creation of the finetune.

## 3. Create an endpoint for inference with the custom model

### A. Create an endpoint

The Cohere AWS SDK provides a built-in method for creating an endpoint for inference. This will automatically deploy the model you finetuned earlier.

> **Note**: This is equivalent to creating and deploying a `ModelPackage` in SageMaker's SDK.

```python
endpoint_name = "test-finetune"
co.sagemaker_finetuning.create_endpoint(
    arn=arn,
    endpoint_name=endpoint_name,
    s3_models_dir=s3_models_dir,
    recreate=True,
    instance_type="ml.p4de.24xlarge",
    role="ServiceRoleSagemaker",
)

# If the endpoint is already created, you just need to connect to it
co.connect_to_endpoint(endpoint_name=endpoint_name)
```

### B. Perform real-time inference

Now, you can access all models deployed on the endpoint for inference:

```python
message = "Classify the following text as either very negative, negative, neutral, positive or very positive: mr. deeds is , as comedy goes , very silly -- and in the best way."

result = co.sagemaker_finetuning.chat(message=message)
print(result)
```

#### \[Optional] Now let's evaluate our finetuned model using the evaluation dataset.

```python
import json
from tqdm import tqdm

total = 0
correct = 0
for line in tqdm(
    open("./sample_finetune_scienceQA_eval.jsonl").readlines()
):
    total += 1
    question_answer_json = json.loads(line)
    question = question_answer_json["messages"][0]["content"]
    answer = question_answer_json["messages"][1]["content"]
    model_ans = co.sagemaker_finetuning.chat(
        message=question, temperature=0
    ).text
    if model_ans == answer:
        correct += 1

print(f"Accuracy of finetuned model is %.3f" % (correct / total))
```

## 4. Clean-up

### A. Delete the endpoint

After you've successfully performed inference, you can delete the deployed endpoint to avoid being charged continuously. This can also be done via the Cohere AWS SDK:

```python
co.delete_endpoint()
co.close()
```

## Unsubscribe to the listing (optional)

If you would like to unsubscribe to the model package, follow these steps. Before you cancel the subscription, ensure that you do not have any [deployable models](https://console.aws.amazon.com/sagemaker/home#/models) created from the model package or using the algorithm. Note - You can find this information by looking at the container name associated with the model.

**Steps to unsubscribe to product from AWS Marketplace**:

1. Navigate to **Machine Learning** tab on [**Your Software subscriptions page**](https://aws.amazon.com/marketplace/ai/library?productType=ml\&ref_=mlmp_gitdemo_indust)
2. Locate the listing that you want to cancel the subscription for, and then choose **Cancel Subscription**  to cancel the subscription.


# SQL Agent with Cohere and LangChain (i-5O Case Study)

> This page contains a tutorial on how to build a SQL agent with Cohere and LangChain in the manufacturing industry.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/agents/i-5O-sql-agent/sql_agent_demo.ipynb" />

This tutorial demonstrates how to create a SQL agent using Cohere and LangChain. The agent can translate natural language queries coming from users into SQL, and execute them against a database. This powerful combination allows for intuitive interaction with databases without requiring direct SQL knowledge.

Key topics covered:

1. Setting up the necessary libraries and environment
2. Connecting to a SQLite database
3. Configuring the LangChain SQL Toolkit
4. Creating a custom prompt template with few-shot examples
5. Building and running the SQL agent
6. Adding memory to the agent to keep track of historical messages

By the end of this tutorial, you'll have a functional SQL agent that can answer questions about your data using natural language.

This tutorial uses a mocked up data of a manufacturing environment where a product item's production is tracked across multiple stations, allowing for analysis of production efficiency, station performance, and individual item progress through the manufacturing process. This is modelled after a real customer use case.

The database contains two tables:

* The `product_tracking` table records the movement of items through different zones in manufacturing stations, including start and end times, station names, and product IDs.
* The `status` table logs the operational status of stations, including timestamps, station names, and whether they are productive or in downtime.

## Import the required libraries

First, let's import the necessary libraries for creating a SQL agent using Cohere and LangChain. These libraries enable natural language interaction with databases and provide tools for building AI-powered agents.

```python PYTHON
import os

os.environ["COHERE_API_KEY"] = "<cohere-api-key>"
```

```python PYTHON
! pip install langchain-core langchain-cohere langchain-community faiss-cpu -qq
```

```python PYTHON
from langchain_cohere import create_sql_agent
from langchain_cohere.chat_models import ChatCohere
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.vectorstores import FAISS
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_cohere import CohereEmbeddings
from datetime import datetime
```

## Load the database

Next, we load the database for our manufacturing data.

### Download the sql files from the link below to create the database.

We create an in-memory SQLite database using SQL scripts for the `product_tracking` and `status` tables. You can get the [SQL tables here](https://github.com/cohere-ai/notebooks/tree/main/notebooks/agents/i-5O-sql-agent).

We then create a SQLDatabase instance, which will be used by our LangChain tools and agents to interact with the data.

```python PYTHON
import sqlite3

from langchain_community.utilities.sql_database import SQLDatabase
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

def get_engine_for_manufacturing_db():
    """Create an in-memory database with the manufacturing data tables."""
    connection = sqlite3.connect(":memory:", check_same_thread=False)

    # Read and execute the SQL scripts
    for sql_file in ['product_tracking.sql', 'status.sql']:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
            connection.executescript(sql_script)

    return create_engine(
        "sqlite://",
        creator=lambda: connection,
        poolclass=StaticPool,
        connect_args={"check_same_thread": False},
    )

# Create the engine
engine = get_engine_for_manufacturing_db()

# Create the SQLDatabase instance
db = SQLDatabase(engine)

# Now you can use this db instance with your LangChain tools and agents
```

```python PYTHON
# Test the connection
db.run("SELECT * FROM status LIMIT 5;")
```

```mdx
"[('2024-05-09 19:28:00', 'Canada/Toronto', '2024-05-09', '19', '28', 'stn3', 'downtime'), ('2024-04-21 06:57:00', 'Canada/Toronto', '2024-04-21', '6', '57', 'stn3', 'productive'), ('2024-04-11 23:52:00', 'Canada/Toronto', '2024-04-11', '23', '52', 'stn4', 'productive'), ('2024-04-03 21:52:00', 'Canada/Toronto', '2024-04-03', '21', '52', 'stn2', 'downtime'), ('2024-04-30 05:01:00', 'Canada/Toronto', '2024-04-30', '5', '1', 'stn4', 'productive')]"
```

```python PYTHON
# Test the connection
db.run("SELECT * FROM product_tracking LIMIT 5;")
```

```mdx
"[('2024-05-27 17:22:00', '2024-05-27 17:57:00', 'Canada/Toronto', '2024-05-27', '17', 'stn2', 'wip', '187', '35'), ('2024-04-26 15:56:00', '2024-04-26 17:56:00', 'Canada/Toronto', '2024-04-26', '15', 'stn4', 'wip', '299', '120'), ('2024-04-12 04:36:00', '2024-04-12 05:12:00', 'Canada/Toronto', '2024-04-12', '4', 'stn3', 'wip', '60', '36'), ('2024-04-19 15:15:00', '2024-04-19 15:22:00', 'Canada/Toronto', '2024-04-19', '15', 'stn4', 'wait', '227', '7'), ('2024-04-24 19:10:00', '2024-04-24 21:07:00', 'Canada/Toronto', '2024-04-24', '19', 'stn4', 'wait', '169', '117')]"
```

## Setup the LangChain SQL Toolkit

Next, we initialize the LangChain SQL Toolkit and initialize the language model to use Cohere's LLM. This prepares the necessary components for querying the SQL database using natural language.

```python PYTHON
## Define model to use
import os

MODEL = "command-a-03-2025"

llm = ChatCohere(
    model=MODEL,
    temperature=0.1,
    verbose=True
)


toolkit = SQLDatabaseToolkit(db=db, llm=llm)
context = toolkit.get_context()
tools = toolkit.get_tools()

print("**List of pre-defined Langchain Tools**")
print([tool.name for tool in tools])
```

```mdx
**List of pre-defined Langchain Tools**
['sql_db_query', 'sql_db_schema', 'sql_db_list_tables', 'sql_db_query_checker']
```

## Create a prompt template

Next, we create a prompt template. In this section, we will introduce a simple system message, and then also show how we can improve the prompt by introducing few shot prompting examples in the later sections.
The system message is used to communicate instructions or provide context to the model at the beginning of a conversation.

In this case, we provide the model with context on what sql dialect it should use, how many samples to query among other instructions.

```python PYTHON
from langchain_core.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    MessagesPlaceholder
)

system_message = """You are an agent designed to interact with a SQL database.
You are an expert at answering questions about manufacturing data.
Given an input question, create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
Always start with checking the schema of the available tables.
Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most {top_k} results.
You can order the results by a relevant column to return the most interesting examples in the database.
Never query for all the columns from a specific table, only ask for the relevant columns given the question.
You have access to tools for interacting with the database.
Only use the given tools. Only use the information returned by the tools to construct your final answer.
You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.

DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.

The current date is {date}.

For questions regarding productive time, downtime, productive or productivity, use minutes as units.

For questions regarding productive time, downtime, productive or productivity use the status table.

For questions regarding processing time and average processing time, use minutes as units.

For questions regarding bottlenecks, processing time and average processing time use the product_tracking table.

If the question does not seem related to the database, just return "I don't know" as the answer."""

system_prompt = PromptTemplate.from_template(system_message)

```

```python PYTHON
full_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate(prompt=system_prompt),
        MessagesPlaceholder(variable_name='chat_history', optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)
```

```python PYTHON
prompt_val = full_prompt.invoke({
        "input": "What was the productive time for all stations today?",
        "top_k": 5,
        "dialect": "SQLite",
        "date":datetime.now(),
        "agent_scratchpad": [],
    })
print(prompt_val.to_string())
```

```mdx
System: You are an agent designed to interact with a SQL database.
You are an expert at answering questions about manufacturing data.
Given an input question, create a syntactically correct SQLite query to run, then look at the results of the query and return the answer.
Always start with checking the schema of the available tables.
Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most 5 results.
You can order the results by a relevant column to return the most interesting examples in the database.
Never query for all the columns from a specific table, only ask for the relevant columns given the question.
You have access to tools for interacting with the database.
Only use the given tools. Only use the information returned by the tools to construct your final answer.
You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.

DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.

The current date is 2025-03-13 09:21:55.403450.

For questions regarding productive time, downtime, productive or productivity, use minutes as units.

For questions regarding productive time, downtime, productive or productivity use the status table.

For questions regarding processing time and average processing time, use minutes as units.

For questions regarding bottlenecks, processing time and average processing time use the product_tracking table.

If the question does not seem related to the database, just return "I don't know" as the answer.
Human: What was the productive time for all stations today?
```

## Create a few-shot prompt template

In the above step, we've created a simple system prompt. Now, let us see how we can create a better few shot prompt template in this section. Few-shot examples are used to provide the model with context and improve its performance on specific tasks. In this case, we'll prepare examples of natural language queries and their corresponding SQL queries to help the model generate accurate SQL statements for our database.

In this example, we use `SemanticSimilarityExampleSelector` to select the top k examples that are most similar to an input query out of all the examples available.

```python PYTHON
examples = [
    {
        "input": "What was the average processing time for all stations on April 3rd 2024?",
        "query": "SELECT station_name, AVG(CAST(duration AS INTEGER)) AS avg_processing_time FROM product_tracking WHERE date = '2024-04-03' AND zone = 'wip' GROUP BY station_name ORDER BY station_name;",
    },
    {
        "input": "What was the average processing time for all stations on April 3rd 2024 between 4pm and 6pm?",
        "query": "SELECT station_name, AVG(CAST(duration AS INTEGER)) AS avg_processing_time FROM product_tracking WHERE date = '2024-04-03' AND CAST(hour AS INTEGER) BETWEEN 16 AND 18 AND zone = 'wip' GROUP BY station_name ORDER BY station_name;",
    },
    {
        "input": "What was the average processing time for stn4 on April 3rd 2024?",
        "query": "SELECT AVG(CAST(duration AS INTEGER)) AS avg_processing_time FROM product_tracking WHERE date = '2024-04-03' AND station_name = 'stn4' AND zone = 'wip';",
    },
    {
        "input": "How much downtime did stn2 have on April 3rd 2024?",
        "query": "SELECT COUNT(*) AS downtime_count FROM status WHERE date = '2024-04-03' AND station_name = 'stn2' AND station_status = 'downtime';",
    },
    {
        "input": "What were the productive time and downtime numbers for all stations on April 3rd 2024?",
        "query": "SELECT station_name, station_status, COUNT(*) as total_time FROM status WHERE date = '2024-04-03' GROUP BY station_name, station_status;",
    },
    {
        "input": "What was the bottleneck station on April 3rd 2024?",
        "query": "SELECT station_name, AVG(CAST(duration AS INTEGER)) AS avg_processing_time FROM product_tracking WHERE date = '2024-04-03' AND zone = 'wip' GROUP BY station_name ORDER BY avg_processing_time DESC LIMIT 1;",
    },
    {
        "input": "Which percentage of the time was stn5 down in the last week of May?",
        "query": "SELECT SUM(CASE WHEN station_status = 'downtime' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS percentage_downtime FROM status WHERE station_name = 'stn5' AND date >= '2024-05-25' AND date <= '2024-05-31';",
    },
]
```

```python PYTHON
example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
    CohereEmbeddings(
        cohere_api_key=os.getenv("COHERE_API_KEY"), model="embed-v4.0"
    ),
    FAISS,
    k=5,
    input_keys=["input"],
)
```

```python PYTHON
from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotPromptTemplate,
    MessagesPlaceholder,
    PromptTemplate,
    SystemMessagePromptTemplate,
)

system_prefix = """You are an agent designed to interact with a SQL database.
You are an expert at answering questions about manufacturing data.
Given an input question, create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
Always start with checking the schema of the available tables.
Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most {top_k} results.
You can order the results by a relevant column to return the most interesting examples in the database.
Never query for all the columns from a specific table, only ask for the relevant columns given the question.
You have access to tools for interacting with the database.
Only use the given tools. Only use the information returned by the tools to construct your final answer.
You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.

DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.

The current date is {date}.

For questions regarding productive time, downtime, productive or productivity, use minutes as units.

For questions regarding productive time, downtime, productive or productivity use the status table.

For questions regarding processing time and average processing time, use minutes as units.

For questions regarding bottlenecks, processing time and average processing time use the product_tracking table.

If the question does not seem related to the database, just return "I don't know" as the answer.

Here are some examples of user inputs and their corresponding SQL queries:
"""

few_shot_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=PromptTemplate.from_template(
        "User input: {input}\nSQL query: {query}"
    ),
    input_variables=["input", "dialect", "top_k","date"],
    prefix=system_prefix,
    suffix="",
)
```

```python PYTHON
full_prompt = ChatPromptTemplate.from_messages(
    [
        # In the previous section, this was system_prompt instead without the few shot examples.
        # We can use either prompting style as required
        SystemMessagePromptTemplate(prompt=few_shot_prompt),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)
```

```python PYTHON
# Example formatted prompt
prompt_val = full_prompt.invoke(
    {
        "input": "What was the productive time for all stations today?",
        "top_k": 5,
        "dialect": "SQLite",
        "date":datetime.now(),
        "agent_scratchpad": [],
    }
)
print(prompt_val.to_string())
```

```mdx
System: You are an agent designed to interact with a SQL database.
You are an expert at answering questions about manufacturing data.
Given an input question, create a syntactically correct SQLite query to run, then look at the results of the query and return the answer.
Always start with checking the schema of the available tables.
Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most 5 results.
You can order the results by a relevant column to return the most interesting examples in the database.
Never query for all the columns from a specific table, only ask for the relevant columns given the question.
You have access to tools for interacting with the database.
Only use the given tools. Only use the information returned by the tools to construct your final answer.
You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.

DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.

The current date is 2025-03-13 09:22:22.275098.

For questions regarding productive time, downtime, productive or productivity, use minutes as units.

For questions regarding productive time, downtime, productive or productivity use the status table.

For questions regarding processing time and average processing time, use minutes as units.

For questions regarding bottlenecks, processing time and average processing time use the product_tracking table.

If the question does not seem related to the database, just return "I don't know" as the answer.

Here are some examples of user inputs and their corresponding SQL queries:


User input: What were the productive time and downtime numbers for all stations on April 3rd 2024?
SQL query: SELECT station_name, station_status, COUNT(*) as total_time FROM status WHERE date = '2024-04-03' GROUP BY station_name, station_status;

User input: What was the average processing time for all stations on April 3rd 2024?
SQL query: SELECT station_name, AVG(CAST(duration AS INTEGER)) AS avg_processing_time FROM product_tracking WHERE date = '2024-04-03' AND zone = 'wip' GROUP BY station_name ORDER BY station_name;

User input: What was the average processing time for all stations on April 3rd 2024 between 4pm and 6pm?
SQL query: SELECT station_name, AVG(CAST(duration AS INTEGER)) AS avg_processing_time FROM product_tracking WHERE date = '2024-04-03' AND CAST(hour AS INTEGER) BETWEEN 16 AND 18 AND zone = 'wip' GROUP BY station_name ORDER BY station_name;

User input: What was the bottleneck station on April 3rd 2024?
SQL query: SELECT station_name, AVG(CAST(duration AS INTEGER)) AS avg_processing_time FROM product_tracking WHERE date = '2024-04-03' AND zone = 'wip' GROUP BY station_name ORDER BY avg_processing_time DESC LIMIT 1;

User input: What was the average processing time for stn4 on April 3rd 2024?
SQL query: SELECT AVG(CAST(duration AS INTEGER)) AS avg_processing_time FROM product_tracking WHERE date = '2024-04-03' AND station_name = 'stn4' AND zone = 'wip';
Human: What was the productive time for all stations today?
```

## Create the agent

Next, we create an instance of the SQL agent using the LangChain framework, specifically using `create_sql_agent`.

This agent will be capable of interpreting natural language queries, converting them into SQL queries, and executing them against our database. The agent uses the LLM we defined earlier, along with the SQL toolkit and the custom prompt we created.

```python PYTHON
agent = create_sql_agent(
   llm=llm,
   toolkit=toolkit,
   prompt=full_prompt,
   verbose=True
)
```

## Run the agent

Now, we can run the agent and test it with a few different queries.

```python PYTHON
# %%time
output=agent.invoke({
   "input": "Which stations had some downtime in the month of May 2024?",
    "date": datetime.now()
})
print(output['output'])

# Answer: stn2, stn3 and stn5 had some downtime in the month of May 2024.
```

````mdx
[1m> Entering new Cohere SQL Agent Executor chain...[0m
[32;1m[1;3m
Invoking: `sql_db_list_tablessql_db_list_tables` with `{}`
responded: I will first check the schema of the available tables. Then, I will query the connected SQL database to find the stations that had some downtime in the month of May 2024.

[0msql_db_list_tablessql_db_list_tables is not a valid tool, try one of [sql_db_query, sql_db_schema, sql_db_list_tables, sql_db_query_checker].[32;1m[1;3m
Invoking: `sql_db_list_tables` with `{}`
responded: I will first check the schema of the available tables. Then, I will query the connected SQL database to find the stations that had some downtime in the month of May 2024.

[0m[38;5;200m[1;3mproduct_tracking, status[0m[32;1m[1;3m
Invoking: `sql_db_schema` with `{'table_names': 'product_tracking, status'}`
responded: I have found the following tables: product_tracking and status. I will now query the schema of these tables to understand their structure.

[0m[33;1m[1;3m
CREATE TABLE product_tracking (
    timestamp_start TEXT, 
    timestamp_end TEXT, 
    timezone TEXT, 
    date TEXT, 
    hour TEXT, 
    station_name TEXT, 
    zone TEXT, 
    product_id TEXT, 
    duration TEXT
)

/*
3 rows from product_tracking table:
timestamp_start	timestamp_end	timezone	date	hour	station_name	zone	product_id	duration
2024-05-27 17:22:00	2024-05-27 17:57:00	Canada/Toronto	2024-05-27	17	stn2	wip	187	35
2024-04-26 15:56:00	2024-04-26 17:56:00	Canada/Toronto	2024-04-26	15	stn4	wip	299	120
2024-04-12 04:36:00	2024-04-12 05:12:00	Canada/Toronto	2024-04-12	4	stn3	wip	60	36
*/


CREATE TABLE status (
    timestamp_event TEXT, 
    timezone TEXT, 
    date TEXT, 
    hour TEXT, 
    minute TEXT, 
    station_name TEXT, 
    station_status TEXT
)

/*
3 rows from status table:
timestamp_event	timezone	date	hour	minute	station_name	station_status
2024-05-09 19:28:00	Canada/Toronto	2024-05-09	19	28	stn3	downtime
2024-04-21 06:57:00	Canada/Toronto	2024-04-21	6	57	stn3	productive
2024-04-11 23:52:00	Canada/Toronto	2024-04-11	23	52	stn4	productive
*/[0m[32;1m[1;3m
Invoking: `sql_db_schema` with `{'table_names': 'product_tracking, status'}`
responded: I have found the following tables: product_tracking and status. I will now query the schema of these tables to understand their structure.

[0m[33;1m[1;3m
CREATE TABLE product_tracking (
    timestamp_start TEXT, 
    timestamp_end TEXT, 
    timezone TEXT, 
    date TEXT, 
    hour TEXT, 
    station_name TEXT, 
    zone TEXT, 
    product_id TEXT, 
    duration TEXT
)

/*
3 rows from product_tracking table:
timestamp_start	timestamp_end	timezone	date	hour	station_name	zone	product_id	duration
2024-05-27 17:22:00	2024-05-27 17:57:00	Canada/Toronto	2024-05-27	17	stn2	wip	187	35
2024-04-26 15:56:00	2024-04-26 17:56:00	Canada/Toronto	2024-04-26	15	stn4	wip	299	120
2024-04-12 04:36:00	2024-04-12 05:12:00	Canada/Toronto	2024-04-12	4	stn3	wip	60	36
*/


CREATE TABLE status (
    timestamp_event TEXT, 
    timezone TEXT, 
    date TEXT, 
    hour TEXT, 
    minute TEXT, 
    station_name TEXT, 
    station_status TEXT
)

/*
3 rows from status table:
timestamp_event	timezone	date	hour	minute	station_name	station_status
2024-05-09 19:28:00	Canada/Toronto	2024-05-09	19	28	stn3	downtime
2024-04-21 06:57:00	Canada/Toronto	2024-04-21	6	57	stn3	productive
2024-04-11 23:52:00	Canada/Toronto	2024-04-11	23	52	stn4	productive
*/[0m[32;1m[1;3m
Invoking: `sql_db_query_checker` with `{'query': "SELECT DISTINCT station_name\r\nFROM status\r\nWHERE station_status = 'downtime'\r\n  AND SUBSTR(date, 1, 7) = '2024-05';"}`
responded: I have found that the status table contains the relevant information, including the station_status column which contains the values 'productive' and 'downtime'. I will now query the database to find the stations that had some downtime in the month of May 2024.

[0m[36;1m[1;3m```sql
SELECT DISTINCT station_name
FROM status
WHERE station_status = 'downtime'
    AND SUBSTR(date, 1, 7) = '2024-05';
```[0m[32;1m[1;3m
Invoking: `sql_db_query_checker` with `{'query': "SELECT DISTINCT station_name\r\nFROM status\r\nWHERE station_status = 'downtime'\r\n  AND SUBSTR(date, 1, 7) = '2024-05';"}`
responded: I have found that the status table contains the relevant information, including the station_status column which contains the values 'productive' and 'downtime'. I will now query the database to find the stations that had some downtime in the month of May 2024.

[0m[36;1m[1;3m```sql
SELECT DISTINCT station_name
FROM status
WHERE station_status = 'downtime'
    AND SUBSTR(date, 1, 7) = '2024-05';
```[0m[32;1m[1;3m
Invoking: `sql_db_query_checker` with `{'query': "SELECT DISTINCT station_name\r\nFROM status\r\nWHERE station_status = 'downtime'\r\n  AND SUBSTR(date, 1, 7) = '2024-05';"}`
responded: I have found that the status table contains the relevant information, including the station_status column which contains the values 'productive' and 'downtime'. I will now query the database to find the stations that had some downtime in the month of May 2024.

[0m[36;1m[1;3m```sql
SELECT DISTINCT station_name
FROM status
WHERE station_status = 'downtime'
    AND SUBSTR(date, 1, 7) = '2024-05';
```[0m[32;1m[1;3m
Invoking: `sql_db_query_checker` with `{'query': "SELECT DISTINCT station_name\r\nFROM status\r\nWHERE station_status = 'downtime'\r\n  AND SUBSTR(date, 1, 7) = '2024-05';"}`
responded: I have found that the status table contains the relevant information, including the station_status column which contains the values 'productive' and 'downtime'. I will now query the database to find the stations that had some downtime in the month of May 2024.

[0m[36;1m[1;3m```sql
SELECT DISTINCT station_name
FROM status
WHERE station_status = 'downtime'
    AND SUBSTR(date, 1, 7) = '2024-05';
```[0m[32;1m[1;3m
Invoking: `sql_db_query` with `{'query': "SELECT DISTINCT station_name\r\nFROM status\r\nWHERE station_status = 'downtime'\r\n  AND SUBSTR(date, 1, 7) = '2024-05';"}`
responded: I have checked the query and it is correct. I will now execute the query to find the stations that had some downtime in the month of May 2024.

[0m[36;1m[1;3m[('stn3',), ('stn5',), ('stn2',)][0m[32;1m[1;3m
Invoking: `sql_db_query` with `{'query': "SELECT DISTINCT station_name\r\nFROM status\r\nWHERE station_status = 'downtime'\r\n  AND SUBSTR(date, 1, 7) = '2024-05';"}`
responded: I have checked the query and it is correct. I will now execute the query to find the stations that had some downtime in the month of May 2024.

[0m[36;1m[1;3m[('stn3',), ('stn5',), ('stn2',)][0m[32;1m[1;3mThe stations that had some downtime in the month of May 2024 are:
- stn3
- stn5
- stn2[0m

[1m> Finished chain.[0m
The stations that had some downtime in the month of May 2024 are:
- stn3
- stn5
- stn2
````

```python PYTHON
output=agent.invoke({
   "input": "What is the average processing duration at stn5 in the wip zone?",
    "date": datetime.now()
})
print(output['output'])

# Answer: 39.17 minutes
```

````mdx
[1m> Entering new Cohere SQL Agent Executor chain...[0m
[32;1m[1;3m
Invoking: `sql_db_list_tablessql_db_list_tables` with `{}`
responded: I will first check the schema of the available tables. Then, I will write a query to find the average processing duration at stn5 in the wip zone.

[0msql_db_list_tablessql_db_list_tables is not a valid tool, try one of [sql_db_query, sql_db_schema, sql_db_list_tables, sql_db_query_checker].[32;1m[1;3m
Invoking: `sql_db_list_tables` with `{}`
responded: I will first check the schema of the available tables. Then, I will write a query to find the average processing duration at stn5 in the wip zone.

[0m[38;5;200m[1;3mproduct_tracking, status[0m[32;1m[1;3m
Invoking: `sql_db_schema` with `{'table_names': 'product_tracking'}`
responded: I will use the product_tracking table to find the average processing duration at stn5 in the wip zone.

[0m[33;1m[1;3m
CREATE TABLE product_tracking (
    timestamp_start TEXT, 
    timestamp_end TEXT, 
    timezone TEXT, 
    date TEXT, 
    hour TEXT, 
    station_name TEXT, 
    zone TEXT, 
    product_id TEXT, 
    duration TEXT
)

/*
3 rows from product_tracking table:
timestamp_start	timestamp_end	timezone	date	hour	station_name	zone	product_id	duration
2024-05-27 17:22:00	2024-05-27 17:57:00	Canada/Toronto	2024-05-27	17	stn2	wip	187	35
2024-04-26 15:56:00	2024-04-26 17:56:00	Canada/Toronto	2024-04-26	15	stn4	wip	299	120
2024-04-12 04:36:00	2024-04-12 05:12:00	Canada/Toronto	2024-04-12	4	stn3	wip	60	36
*/[0m[32;1m[1;3m
Invoking: `sql_db_schema` with `{'table_names': 'product_tracking'}`
responded: I will use the product_tracking table to find the average processing duration at stn5 in the wip zone.

[0m[33;1m[1;3m
CREATE TABLE product_tracking (
    timestamp_start TEXT, 
    timestamp_end TEXT, 
    timezone TEXT, 
    date TEXT, 
    hour TEXT, 
    station_name TEXT, 
    zone TEXT, 
    product_id TEXT, 
    duration TEXT
)

/*
3 rows from product_tracking table:
timestamp_start	timestamp_end	timezone	date	hour	station_name	zone	product_id	duration
2024-05-27 17:22:00	2024-05-27 17:57:00	Canada/Toronto	2024-05-27	17	stn2	wip	187	35
2024-04-26 15:56:00	2024-04-26 17:56:00	Canada/Toronto	2024-04-26	15	stn4	wip	299	120
2024-04-12 04:36:00	2024-04-12 05:12:00	Canada/Toronto	2024-04-12	4	stn3	wip	60	36
*/[0m[32;1m[1;3m
Invoking: `sql_db_query_checker` with `{'query': "SELECT AVG(CAST(duration AS INTEGER)) AS avg_processing_duration\nFROM product_tracking\nWHERE station_name = 'stn5' AND zone = 'wip';"}`
responded: I will use the product_tracking table to find the average processing duration at stn5 in the wip zone. The relevant columns are station_name, zone and duration.

[0m[36;1m[1;3m```sql
SELECT AVG(CAST(duration AS INTEGER)) AS avg_processing_duration
FROM product_tracking
WHERE station_name = 'stn5' AND zone = 'wip';
```[0m[32;1m[1;3m
Invoking: `sql_db_query_checker` with `{'query': "SELECT AVG(CAST(duration AS INTEGER)) AS avg_processing_duration\nFROM product_tracking\nWHERE station_name = 'stn5' AND zone = 'wip';"}`
responded: I will use the product_tracking table to find the average processing duration at stn5 in the wip zone. The relevant columns are station_name, zone and duration.

[0m[36;1m[1;3m```sql
SELECT AVG(CAST(duration AS INTEGER)) AS avg_processing_duration
FROM product_tracking
WHERE station_name = 'stn5' AND zone = 'wip';
```[0m[32;1m[1;3m
Invoking: `sql_db_query` with `{'query': "SELECT AVG(CAST(duration AS INTEGER)) AS avg_processing_duration\nFROM product_tracking\nWHERE station_name = 'stn5' AND zone = 'wip';"}`
responded: I will now execute the query to find the average processing duration at stn5 in the wip zone.

[0m[36;1m[1;3m[(39.166666666666664,)][0m[32;1m[1;3m
Invoking: `sql_db_query` with `{'query': "SELECT AVG(CAST(duration AS INTEGER)) AS avg_processing_duration\nFROM product_tracking\nWHERE station_name = 'stn5' AND zone = 'wip';"}`
responded: I will now execute the query to find the average processing duration at stn5 in the wip zone.

[0m[36;1m[1;3m[(39.166666666666664,)][0m[32;1m[1;3mThe average processing duration at stn5 in the wip zone is 39.17 minutes.[0m

[1m> Finished chain.[0m
The average processing duration at stn5 in the wip zone is 39.17 minutes.
````

```python PYTHON
output=agent.invoke({
   "input": "Which station had the highest total duration in the wait zone?",
    "date": datetime.now()
})
print(output['output'])

# Answer: stn4 - 251 minutes

```

````mdx
[1m> Entering new Cohere SQL Agent Executor chain...[0m
[32;1m[1;3m
Invoking: `sql_db_list_tablessql_db_list_tables` with `{}`
responded: I will first check the schema of the available tables. Then, I will write a query to find the station with the highest total duration in the wait zone.

[0msql_db_list_tablessql_db_list_tables is not a valid tool, try one of [sql_db_query, sql_db_schema, sql_db_list_tables, sql_db_query_checker].[32;1m[1;3m
Invoking: `sql_db_list_tables` with `{}`
responded: I will first check the schema of the available tables. Then, I will write a query to find the station with the highest total duration in the wait zone.

[0m[38;5;200m[1;3mproduct_tracking, status[0m[32;1m[1;3m
Invoking: `sql_db_schema` with `{'table_names': 'product_tracking'}`
responded: I will use the product_tracking table to find the station with the highest total duration in the wait zone. I will group the results by station_name and zone, and filter for the zone 'wait'. I will then order the results by total duration in descending order and limit the results to 1.

[0m[33;1m[1;3m
CREATE TABLE product_tracking (
    timestamp_start TEXT, 
    timestamp_end TEXT, 
    timezone TEXT, 
    date TEXT, 
    hour TEXT, 
    station_name TEXT, 
    zone TEXT, 
    product_id TEXT, 
    duration TEXT
)

/*
3 rows from product_tracking table:
timestamp_start	timestamp_end	timezone	date	hour	station_name	zone	product_id	duration
2024-05-27 17:22:00	2024-05-27 17:57:00	Canada/Toronto	2024-05-27	17	stn2	wip	187	35
2024-04-26 15:56:00	2024-04-26 17:56:00	Canada/Toronto	2024-04-26	15	stn4	wip	299	120
2024-04-12 04:36:00	2024-04-12 05:12:00	Canada/Toronto	2024-04-12	4	stn3	wip	60	36
*/[0m[32;1m[1;3m
Invoking: `sql_db_schema` with `{'table_names': 'product_tracking'}`
responded: I will use the product_tracking table to find the station with the highest total duration in the wait zone. I will group the results by station_name and zone, and filter for the zone 'wait'. I will then order the results by total duration in descending order and limit the results to 1.

[0m[33;1m[1;3m
CREATE TABLE product_tracking (
    timestamp_start TEXT, 
    timestamp_end TEXT, 
    timezone TEXT, 
    date TEXT, 
    hour TEXT, 
    station_name TEXT, 
    zone TEXT, 
    product_id TEXT, 
    duration TEXT
)

/*
3 rows from product_tracking table:
timestamp_start	timestamp_end	timezone	date	hour	station_name	zone	product_id	duration
2024-05-27 17:22:00	2024-05-27 17:57:00	Canada/Toronto	2024-05-27	17	stn2	wip	187	35
2024-04-26 15:56:00	2024-04-26 17:56:00	Canada/Toronto	2024-04-26	15	stn4	wip	299	120
2024-04-12 04:36:00	2024-04-12 05:12:00	Canada/Toronto	2024-04-12	4	stn3	wip	60	36
*/[0m[32;1m[1;3m
Invoking: `sql_db_query_checker` with `{'query': "SELECT station_name, SUM(CAST(duration AS INTEGER)) AS total_duration\r\nFROM product_tracking\r\nWHERE zone = 'wait'\r\nGROUP BY station_name\r\nORDER BY total_duration DESC\r\nLIMIT 1;"}`
responded: I will use the product_tracking table to find the station with the highest total duration in the wait zone. I will group the results by station_name and zone, and filter for the zone 'wait'. I will then order the results by total duration in descending order and limit the results to 1.

[0m[36;1m[1;3m```sql
SELECT station_name, SUM(CAST(duration AS INTEGER)) AS total_duration
FROM product_tracking
WHERE zone = 'wait'
GROUP BY station_name
ORDER BY total_duration DESC
LIMIT 1;
```[0m[32;1m[1;3m
Invoking: `sql_db_query` with `{'query': "SELECT station_name, SUM(CAST(duration AS INTEGER)) AS total_duration\nFROM product_tracking\nWHERE zone = 'wait'\nGROUP BY station_name\nORDER BY total_duration DESC\nLIMIT 1;"}`
responded: I will now execute the query to find the station with the highest total duration in the wait zone.

[0m[36;1m[1;3m[('stn4', 251)][0m[32;1m[1;3mThe station with the highest total duration in the wait zone is stn4, with a total duration of 251 minutes.[0m

[1m> Finished chain.[0m
The station with the highest total duration in the wait zone is stn4, with a total duration of 251 minutes.
````

## Memory in the sql agent

We may want the agent to hold memory of our previous messages so that we're able to coherently engage with the agent to answer our queries. In this section, let's take a look at how we can add memory to the agent so that we're able to achieve this outcome!

```python PYTHON
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage
from pydantic import BaseModel, Field
from typing import List
```

In the code snippets below, we create a class to store the chat history in memory. This can be customised to store the messages from a database or any other suitable data store.

```python PYTHON
class InMemoryHistory(BaseChatMessageHistory, BaseModel):
    """In memory implementation of chat message history."""

    messages: List[BaseMessage] = Field(default_factory=list)

    def add_messages(self, messages: List[BaseMessage]) -> None:
        """Add a list of messages to the store"""
        self.messages.extend(messages)

    def clear(self) -> None:
        self.messages = []

```

In the below code snippet, we make use of the [RunnableWithMessageHistory](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.history.RunnableWithMessageHistory.html) abstraction to wrap around the agent we've created above to provide the message history to the agent that we can now utilize by chatting with the `agent_with_chat_history` as shown below.

```python PYTHON
store = {}


def get_by_session_id(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryHistory()
    return store[session_id]


agent_with_chat_history = RunnableWithMessageHistory(
    agent, get_by_session_id, history_messages_key="chat_history"
)

output = agent_with_chat_history.invoke(
    {
        "input": "What station had the longest duration on 27th May 2024?",
        "date": datetime.now(),
    },
    config={"configurable": {"session_id": "foo"}},
)
print(output["output"])

# Answer: stn2, with duration of 35 mins.
```

````mdx
[1m> Entering new Cohere SQL Agent Executor chain...[0m
[32;1m[1;3m
Invoking: `sql_db_list_tablessql_db_list_tables` with `{}`
responded: I will first check the schema of the available tables. Then, I will query the product_tracking table to find the station with the longest duration on 27th May 2024.

[0msql_db_list_tablessql_db_list_tables is not a valid tool, try one of [sql_db_query, sql_db_schema, sql_db_list_tables, sql_db_query_checker].[32;1m[1;3m
Invoking: `sql_db_list_tables` with `{}`
responded: I will first check the schema of the available tables. Then, I will query the product_tracking table to find the station with the longest duration on 27th May 2024.

[0m[38;5;200m[1;3mproduct_tracking, status[0m[32;1m[1;3m
Invoking: `sql_db_schema` with `{'table_names': 'product_tracking'}`
responded: I will query the product_tracking table to find the station with the longest duration on 27th May 2024.

[0m[33;1m[1;3m
CREATE TABLE product_tracking (
    timestamp_start TEXT, 
    timestamp_end TEXT, 
    timezone TEXT, 
    date TEXT, 
    hour TEXT, 
    station_name TEXT, 
    zone TEXT, 
    product_id TEXT, 
    duration TEXT
)

/*
3 rows from product_tracking table:
timestamp_start	timestamp_end	timezone	date	hour	station_name	zone	product_id	duration
2024-05-27 17:22:00	2024-05-27 17:57:00	Canada/Toronto	2024-05-27	17	stn2	wip	187	35
2024-04-26 15:56:00	2024-04-26 17:56:00	Canada/Toronto	2024-04-26	15	stn4	wip	299	120
2024-04-12 04:36:00	2024-04-12 05:12:00	Canada/Toronto	2024-04-12	4	stn3	wip	60	36
*/[0m[32;1m[1;3m
Invoking: `sql_db_schema` with `{'table_names': 'product_tracking'}`
responded: I will query the product_tracking table to find the station with the longest duration on 27th May 2024.

[0m[33;1m[1;3m
CREATE TABLE product_tracking (
    timestamp_start TEXT, 
    timestamp_end TEXT, 
    timezone TEXT, 
    date TEXT, 
    hour TEXT, 
    station_name TEXT, 
    zone TEXT, 
    product_id TEXT, 
    duration TEXT
)

/*
3 rows from product_tracking table:
timestamp_start	timestamp_end	timezone	date	hour	station_name	zone	product_id	duration
2024-05-27 17:22:00	2024-05-27 17:57:00	Canada/Toronto	2024-05-27	17	stn2	wip	187	35
2024-04-26 15:56:00	2024-04-26 17:56:00	Canada/Toronto	2024-04-26	15	stn4	wip	299	120
2024-04-12 04:36:00	2024-04-12 05:12:00	Canada/Toronto	2024-04-12	4	stn3	wip	60	36
*/[0m[32;1m[1;3m
Invoking: `sql_db_query_checker` with `{'query': "SELECT station_name, duration\r\nFROM product_tracking\r\nWHERE date = '2024-05-27'\r\nORDER BY duration DESC\r\nLIMIT 1;"}`
responded: I will query the product_tracking table to find the station with the longest duration on 27th May 2024. I will filter the data for the date '2024-05-27' and order the results by duration in descending order to find the station with the longest duration.

[0m[36;1m[1;3m```sql
SELECT station_name, duration
FROM product_tracking
WHERE date = '2024-05-27'
ORDER BY duration DESC
LIMIT 1;
```[0m[32;1m[1;3m
Invoking: `sql_db_query` with `{'query': "SELECT station_name, duration\nFROM product_tracking\nWHERE date = '2024-05-27'\nORDER BY duration DESC\nLIMIT 1;"}`
responded: I will now execute the SQL query to find the station with the longest duration on 27th May 2024.

[0m[36;1m[1;3m[('stn2', '35')][0m[32;1m[1;3mThe station with the longest duration on 27th May 2024 was stn2 with a duration of 35 minutes.[0m

[1m> Finished chain.[0m
The station with the longest duration on 27th May 2024 was stn2 with a duration of 35 minutes.
````

```python PYTHON
output = agent_with_chat_history.invoke(
    {
        "input": "Can you tell me when this station had downtime on 2024-04-03?",
        "date": datetime.now(),
    },
    config={"configurable": {"session_id": "foo"}},
)
print(output["output"])

# Answer: 21:52:00
```

```mdx
[1m> Entering new Cohere SQL Agent Executor chain...[0m
[32;1m[1;3m
Invoking: `sql_db_list_tablessql_db_list_tables` with `{}`
responded: I will first check the schema of the available tables. Then, I will query the database to find out when the station had downtime on 2024-04-03.

[0msql_db_list_tablessql_db_list_tables is not a valid tool, try one of [sql_db_query, sql_db_schema, sql_db_list_tables, sql_db_query_checker].[32;1m[1;3m
Invoking: `sql_db_list_tables` with `{}`
responded: I will first check the schema of the available tables. Then, I will query the database to find out when the station had downtime on 2024-04-03.

[0m[38;5;200m[1;3mproduct_tracking, status[0m[32;1m[1;3m
Invoking: `sql_db_schema` with `{'table_names': 'product_tracking, status'}`
responded: I have found that there are two tables: product_tracking and status. I will now check the schema of these tables.

[0m[33;1m[1;3m
CREATE TABLE product_tracking (
    timestamp_start TEXT, 
    timestamp_end TEXT, 
    timezone TEXT, 
    date TEXT, 
    hour TEXT, 
    station_name TEXT, 
    zone TEXT, 
    product_id TEXT, 
    duration TEXT
)

/*
3 rows from product_tracking table:
timestamp_start	timestamp_end	timezone	date	hour	station_name	zone	product_id	duration
2024-05-27 17:22:00	2024-05-27 17:57:00	Canada/Toronto	2024-05-27	17	stn2	wip	187	35
2024-04-26 15:56:00	2024-04-26 17:56:00	Canada/Toronto	2024-04-26	15	stn4	wip	299	120
2024-04-12 04:36:00	2024-04-12 05:12:00	Canada/Toronto	2024-04-12	4	stn3	wip	60	36
*/


CREATE TABLE status (
    timestamp_event TEXT, 
    timezone TEXT, 
    date TEXT, 
    hour TEXT, 
    minute TEXT, 
    station_name TEXT, 
    station_status TEXT
)

/*
3 rows from status table:
timestamp_event	timezone	date	hour	minute	station_name	station_status
2024-05-09 19:28:00	Canada/Toronto	2024-05-09	19	28	stn3	downtime
2024-04-21 06:57:00	Canada/Toronto	2024-04-21	6	57	stn3	productive
2024-04-11 23:52:00	Canada/Toronto	2024-04-11	23	52	stn4	productive
*/[0m[32;1m[1;3m
Invoking: `sql_db_schema` with `{'table_names': 'product_tracking, status'}`
responded: I have found that there are two tables: product_tracking and status. I will now check the schema of these tables.

[0m[33;1m[1;3m
CREATE TABLE product_tracking (
    timestamp_start TEXT, 
    timestamp_end TEXT, 
    timezone TEXT, 
    date TEXT, 
    hour TEXT, 
    station_name TEXT, 
    zone TEXT, 
    product_id TEXT, 
    duration TEXT
)

/*
3 rows from product_tracking table:
timestamp_start	timestamp_end	timezone	date	hour	station_name	zone	product_id	duration
2024-05-27 17:22:00	2024-05-27 17:57:00	Canada/Toronto	2024-05-27	17	stn2	wip	187	35
2024-04-26 15:56:00	2024-04-26 17:56:00	Canada/Toronto	2024-04-26	15	stn4	wip	299	120
2024-04-12 04:36:00	2024-04-12 05:12:00	Canada/Toronto	2024-04-12	4	stn3	wip	60	36
*/


CREATE TABLE status (
    timestamp_event TEXT, 
    timezone TEXT, 
    date TEXT, 
    hour TEXT, 
    minute TEXT, 
    station_name TEXT, 
    station_status TEXT
)

/*
3 rows from status table:
timestamp_event	timezone	date	hour	minute	station_name	station_status
2024-05-09 19:28:00	Canada/Toronto	2024-05-09	19	28	stn3	downtime
2024-04-21 06:57:00	Canada/Toronto	2024-04-21	6	57	stn3	productive
2024-04-11 23:52:00	Canada/Toronto	2024-04-11	23	52	stn4	productive
*/[0m[32;1m[1;3m
Invoking: `sql_db_query` with `{'query': "SELECT timestamp_event, station_name\r\nFROM status\r\nWHERE date = '2024-04-03'\r\nAND station_status = 'downtime';"}`
responded: I have found that the status table contains information about downtime. I will now query the database to find out when the station had downtime on 2024-04-03.

[0m[36;1m[1;3m[('2024-04-03 21:52:00', 'stn2')][0m[32;1m[1;3m
Invoking: `sql_db_query` with `{'query': "SELECT timestamp_event, station_name\r\nFROM status\r\nWHERE date = '2024-04-03'\r\nAND station_status = 'downtime';"}`
responded: I have found that the status table contains information about downtime. I will now query the database to find out when the station had downtime on 2024-04-03.

[0m[36;1m[1;3m[('2024-04-03 21:52:00', 'stn2')][0m[32;1m[1;3mThe station stn2 had downtime at 21:52 on 2024-04-03.[0m

[1m> Finished chain.[0m
The station stn2 had downtime at 21:52 on 2024-04-03.
```

We can see from the above code snippets that the agent is automatically able to infer and query with respect to 'stn2' in the above question without us having to specify it explicitly. This allows us to have more coherent conversations with the agent.

## Conclusion

This tutorial demonstrated how to create a SQL agent using Cohere and LangChain. The agent can translate natural language queries coming from users into SQL, and execute them against a database. This powerful combination allows for intuitive interaction with databases without requiring direct SQL knowledge.


# Introduction to Aya Vision

> In this notebook, we will explore the capabilities of Aya Vision, which can take text and image inputs to generates text responses.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/aya_vision_intro.ipynb" />

Introducing Aya Vision - a state-of-the-art open-weights multimodal multilingual model.

<img src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/aya-vision/Aya-Vision.jpg" />

In this notebook, we will explore the capabilities of Aya Vision, which can take text and image inputs to generates text responses.

The following links provide further details about the Aya Vision model:

* [The launch blog](https://cohere.com/blog/aya-vision)
* [Documentation](https://docs.cohere.com/docs/aya-multimodal)
* HuggingFace model page for the [32B](https://huggingface.co/CohereForAI/aya-vision-32b) and [8B](https://huggingface.co/CohereForAI/aya-vision-8b) models.

This tutorial will provide a walkthrough of the various use cases that you can build with Aya Vision. By the end of this notebook, you will have a solid understanding of how to use Aya Vision for a wide range of applications.

The list of possible use cases with multimodal models is endless, but this notebook will cover the following:

* Setup
* Question answering
* Multilingual multimodal understanding
* Captioning
* Recognizing text
* Classification
* Comparing multiple images
* Conclusion

## Setup

First, install the Cohere Python SDK and create a client.

```python PYTHON
%pip install cohere -q
```

```python PYTHON
import cohere
import base64

co = cohere.ClientV2(
    "COHERE_API_KEY"
)  # Get your free API key here: https://dashboard.cohere.com/api-keys
```

Next, let's set up a function to generate text responses, given an image and a message. It uses the Cohere API via the Chat endpoint to call the Aya Vision model.

To pass an image to the API, pass a Base64-encoded image as the `image_url` argument in the `messages` parameter. To convert and image into a Base64-encoded version, we can use the `base64` library as in this example.

```python PYTHON
# Define the model
model="c4ai-aya-vision-32b"

def generate_text(image_path, message):
    """
    Generate text responses from Aya Vision model based on an image and text prompt.

    Args:
        image_path (str): Path to the image file
        message (str): Text prompt to send with the image

    Returns:
        None: Prints the model's response
    """

    # Define an image in Base64-encoded format
    with open(image_path, "rb") as img_file:
        base64_image_url = f"data:image/jpeg;base64,{base64.b64encode(img_file.read()).decode('utf-8')}"

    # Make an API call to the Cohere Chat endpoint, passing the user message and image
    response = co.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": message},
                    {"type": "image_url", "image_url": {"url": base64_image_url}},
                ],
            }
        ],
    )

    # Print the response
    print(response.message.content[0].text)
```

Let's also set up a function to render images on this notebook as we go through the use cases.

Note: the images used in this notebook can be downloaded [here](https://github.com/cohere-ai/cohere-developer-experience/tree/main/notebooks/images/aya-vision)

```python PYTHON
from IPython.display import Image, display

def render_image(image_path):
    """
    Display an image in the notebook with a fixed width.

    Args:
        image_path (str): Path to the image file to display
    """
    display(Image(filename=image_path, width=400))
```

## Question answering

One of the more common use cases is question answering. Here, the model is used to answer questions based on the content of an image.

By providing an image and a relevant question, the model can analyze the visual content and generate a text response. This is particularly useful in scenarios where visual context is important, such as identifying objects, understanding scenes, or providing descriptions.

```python PYTHON
image_path = "image1.jpg"
render_image(image_path)
```

<img src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/aya-vision/image1.jpg" />

```python PYTHON
message = "Where is this art style from and what is this dish typically used for?"
generate_text(image_path, message)
```

```mdx wordWrap
The art style on this dish is typical of traditional Moroccan or North African pottery. It's characterized by intricate geometric patterns, bold colors, and a mix of stylized floral and abstract designs.

This type of dish is often used as a spice container or for serving small portions of food. In Moroccan cuisine, similar dishes are commonly used to hold spices like cumin, cinnamon, or paprika, or to serve condiments and appetizers.

The design and craftsmanship suggest this piece is likely handmade, which is a common practice in Moroccan pottery. The vibrant colors and detailed patterns make it not just a functional item but also a decorative piece that adds to the aesthetic of a dining table or kitchen.
```

## Multilingual multimodal understanding

Aya Vision can process and respond to prompts in multiple languages, demonstrating its multilingual capabilities. This feature allows users to interact with the model in their preferred language, making it accessible to a global audience. The model can analyze images and provide relevant responses based on the visual content, regardless of the language used in the query.

Here is an example in Persian:

```python PYTHON
image_path = "image2.jpg"
render_image(image_path)
```

<img src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/aya-vision/image2.jpg" />

```python PYTHON
message = "آیا این یک هدیه مناسب برای یک کودک 3 ساله است؟"
generate_text(image_path, message)
```

```mdx wordWrap
بله، این یک هدیه مناسب برای یک کودک سه ساله است. این مجموعه لگو دوپلوی "پل آهنی و مسیر قطار" به طور خاص برای کودکان دو تا چهار ساله طراحی شده است. قطعات بزرگ و رنگارنگ آن برای دست‌های کوچک راحت است و به کودکان کمک می‌کند تا مهارت‌های حرکتی ظریف خود را توسعه دهند. این مجموعه همچنین خلاقیت و بازی تخیلی را تشویق می‌کند، زیرا کودکان می‌توانند با قطعات مختلف برای ساختن پل و مسیر قطار بازی کنند. علاوه بر این، لگو دوپلو به دلیل ایمنی و سازگاری با کودکان خردسال شناخته شده است، که آن را به انتخابی ایده‌آل برای هدیه دادن به کودکان سه ساله تبدیل می‌کند.
```

And here's an example in Indonesian:

```python PYTHON
image_path = "image3.jpg"
render_image(image_path)
```

<img src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/aya-vision/image3.jpg" />

```python PYTHON
message = "Gambar ini berisikan kutipan dari tokoh nasional di Indonesia, siapakah tokoh itu?"
generate_text(image_path, message)
```

```mdx wordWrap
Gambar ini berisikan kutipan dari Soekarno, salah satu tokoh nasional Indonesia yang terkenal. Ia adalah Presiden pertama Indonesia dan dikenal sebagai salah satu pemimpin pergerakan kemerdekaan Indonesia. Kutipan dalam gambar tersebut mencerminkan pemikiran dan visi Soekarno tentang pembangunan bangsa dan pentingnya kontribusi generasi muda dalam menciptakan masa depan yang lebih baik.
```

## Captioning

Instead of asking about specific questions, we can also get the model to provide a description of an image as a whole, be it detailed descriptions or simple captions.

This can be particularly useful for creating alt text for accessibility, generating descriptions for image databases, social media content creation, and others.

```python PYTHON
image_path = "image4.jpg"
render_image(image_path)
```

<img src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/aya-vision/image4.jpg" />

```python PYTHON
message = "Describe this image in detail."

generate_text(image_path, message)
```

```mdx wordWrap
In the heart of a vibrant amusement park, a magnificent and whimsical dragon sculpture emerges from the water, its scales shimmering in hues of red, green, and gold. The dragon's head, adorned with sharp teeth and piercing yellow eyes, rises above the surface, while its body coils gracefully beneath the waves. Surrounding the dragon are colorful LEGO-like structures, including a bridge with intricate blue and purple patterns and a tower that reaches towards the sky. The water, a striking shade of turquoise, is contained by a wooden fence, and beyond the fence, lush green trees provide a natural backdrop. The scene is set against a cloudy sky, adding a touch of drama to this fantastical display.
```

## Recognizing text

The model can recognize and extract text from images, which is useful for reading signs, documents, or other text-based content in photographs. This capability enables applications that can answer questions about text content.

```python PYTHON
image_path = "image5.jpg"
render_image(image_path)
```

<img src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/aya-vision/image5.jpg" />

```python PYTHON
message = "How many bread rolls do I get?"

generate_text(image_path, message)
```

```mdx wordWrap
You get 6 bread rolls in the pack.
```

## Classification

Classification allows the model to categorize images into predefined classes or labels. This is useful for organizing visual content, filtering images, or extracting structured information from visual data.

```python PYTHON
image_path1 = "image6.jpg"
image_path2 = "image7.jpg"
render_image(image_path1)
render_image(image_path2)
```

<img src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/aya-vision/image6.jpg" />

<img src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/aya-vision/image7.jpg" />

```python PYTHON
message = "Please classify this image as one of these dish types: japanese, malaysian, turkish, or other.Respond in the following format: dish_type: <the_dish_type>."

images = [
    image_path1, # turkish
    image_path2, # japanese
]

for item in images:
    generate_text(item, message)
    print("-" * 30)
```

```mdx wordWrap
dish_type: turkish
------------------------------
dish_type: japanese
------------------------------
```

## Comparing multiple images

This section demonstrates how to analyze and compare multiple images simultaneously. The API allows passing more than one image in a single call, enabling the model to perform comparative analysis between different visual inputs.

```python PYTHON
image_path1 = "image6.jpg"
image_path2 = "image7.jpg"
render_image(image_path1)
render_image(image_path2)
```

<img src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/aya-vision/image6.jpg" />

<img src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/aya-vision/image7.jpg" />

```python PYTHON
message = "Compare these two dishes."

with open(image_path1, "rb") as img_file1:
    base64_image_url1 = f"data:image/jpeg;base64,{base64.b64encode(img_file1.read()).decode('utf-8')}"

with open(image_path2, "rb") as img_file2:
    base64_image_url2 = f"data:image/jpeg;base64,{base64.b64encode(img_file2.read()).decode('utf-8')}"

response = co.chat(
    model=model,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": message},
                {"type": "image_url", "image_url": {"url": base64_image_url1}},
                {"type": "image_url", "image_url": {"url":base64_image_url2}}
            ],
        }
    ],
)

print(response.message.content[0].text)
```

```mdx wordWrap
The first dish is a Japanese-style bento box containing a variety of items such as sushi rolls, tempura shrimp, grilled salmon, rice, and vegetables. It is served in a clear plastic container with individual compartments for each food item. The second dish is a Turkish-style meal featuring baklava, a sweet pastry made with layers of phyllo dough, nuts, and honey. It is accompanied by a small bowl of cream and a red flag with a gold emblem. The baklava is presented on a black plate, while the bento box is placed on a tray with a red and gold napkin. Both dishes offer a unique culinary experience, with the Japanese bento box providing a balanced meal with a mix of proteins, carbohydrates, and vegetables, and the Turkish baklava offering a rich, sweet dessert.
```

## Conclusion

In this notebook, we've explored the capabilities of the Aya Vision model through various examples.

The Aya Vision model shows impressive capabilities in understanding visual content and providing detailed, contextual responses. This makes it suitable for a wide range of applications including content analysis, accessibility features, educational tools, and more.

The API's flexibility in handling different types of queries and multiple images simultaneously makes it a powerful tool if you are looking to integrate advanced computer vision capabilities into your applications.


# Retrieval evaluation using LLM-as-a-judge via Pydantic AI

> This page contains a tutorial on how to evaluate retrieval systems using LLMs as judges via Pydantic AI.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/retrieval_eval_pydantic_ai.ipynb" />

We'll explore how to evaluate retrieval systems using Large Language Models (LLMs) as judges.Retrieval evaluation is a critical component in building high-quality information retrieval systems, and recent advancements in LLMs have made it possible to automate this evaluation process.

**What we'll cover**

* How to query the Wikipedia API
* How to implement and compare two different retrieval approaches:
  * The original search results from the Wikipedia API
  * Using Cohere's reranking model to rerank the search results
* How to set up an LLM-as-a-judge evaluation framework using Pydantic AI

**Tools We'll Use**

* **Cohere's API**: For reranking search results and providing evaluation models
* **Wikipedia's API**: As our information source
* **Pydantic AI**: For creating evaluation agents

This tutorial demonstrates a methodology for comparing different retrieval systems objectively. By the end, you'll have an example you can adapt to evaluate your own retrieval systems across different domains and use cases.

## Setup

First, let's import the necessary libraries.

```python PYTHON
%pip install -U cohere pydantic-ai
```

```python PYTHON
import requests
import cohere
import pandas as pd
from pydantic_ai import Agent
from pydantic_ai.models import KnownModelName
from collections import Counter

import os
co = cohere.ClientV2(os.getenv("COHERE_API_KEY"))
```

```python PYTHON
import nest_asyncio
nest_asyncio.apply()
```

## Perform Wikipedia search

Next, we implement a function to query Wikipedia for relevant information based on user input. The `search_wikipedia()` function allows us to retrieve a specified number of Wikipedia search results, extracting their titles, snippets, and page IDs.

This will provide us with the dataset for our retrieval evaluation experiment, where we'll compare different approaches to finding and ranking relevant information.

We'll use a small dataset of 10 questions about geography to test the Wikipedia search.

```python PYTHON
import requests

def search_wikipedia(query, limit=10):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        'action': 'query',
        'list': 'search',
        'srsearch': query,
        'format': 'json',
        'srlimit': limit
    }

    response = requests.get(url, params=params)
    data = response.json()
    
    # Format the results
    results = []
    for item in data['query']['search']:
        results.append({
            "title": item["title"],
            "snippet": item["snippet"].replace("<span class=\"searchmatch\">", "").replace("</span>", ""),
        })
            
    return results
```

```python PYTHON
# Generate 10 questions about geography to test the Wikipedia search
geography_questions = [
    "What is the capital of France?",
    "What is the longest river in the world?",
    "What is the largest desert in the world?",
    "What is the highest mountain peak on Earth?",
    "What are the major tectonic plates?",
    "What is the Ring of Fire?",
    "What is the largest ocean on Earth?",
    "What are the Seven Wonders of the Natural World?",
    "What causes the Northern Lights?",
    "What is the Great Barrier Reef?"
]
```

```python PYTHON
# Run search_wikipedia for each question
results = []

for question in geography_questions:
    question_results = search_wikipedia(question, limit=10)
    
    # Format the results as requested
    formatted_results = []
    for item in question_results:
        formatted_result = f"{item['title']}\n{item['snippet']}"
        formatted_results.append(formatted_result)
    
    # Add to the results list
    results.append({
        "question": question,
        "search_results": formatted_results
    })
```

## Rerank the search results and filter the top\_n results ("Engine A")

In this section, we'll implement our first retrieval approach using Cohere's reranking model. Reranking is a technique that takes an initial set of search results and reorders them based on their relevance to the original query.

We'll use Cohere's `rerank` API to:

1. Take the Wikipedia search results we obtained earlier
2. Send them to Cohere's reranking model along with the original query
3. Filter to keep only the top-n most relevant results

This approach will be referred to as "Engine A" in our evaluation, and we'll compare its performance against the original Wikipedia search rankings.

```python PYTHON
# Rerank the search results for each question
top_n = 3
results_reranked_top_n = []

for item in results:
    question = item["question"]
    documents = item["search_results"]
    
    # Rerank the documents using Cohere
    reranked = co.rerank(
        model="rerank-v3.5",
        query=question,
        documents=documents,
        top_n=top_n  # Get top 3 results
    )
    
    # Format the reranked results
    top_results = []
    for result in reranked.results:
        top_results.append(documents[result.index])
    
    # Add to the reranked results list
    results_reranked_top_n.append({
        "question": question,
        "search_results": top_results
    })

# Print a sample of the reranked results
print(f"Original question: {results_reranked_top_n[0]['question']}")
print(f"Top 3 reranked results:")
for i, result in enumerate(results_reranked_top_n[0]['search_results']):
    print(f"\n{i+1}. {result}")

```

```
Original question: What is the capital of France?
Top 3 reranked results:

1. France
semi-presidential republic and its capital, largest city and main cultural and economic centre is Paris. Metropolitan France was settled during the Iron Age by Celtic

2. Closed-ended question
variants of the above closed-ended questions that possess specific responses are: On what day were you born? (&quot;Saturday.&quot;) What is the capital of France? (&quot;Paris

3. Capital city
seat of the government. A capital is typically a city that physically encompasses the government&#039;s offices and meeting places; the status as capital is often
```

## Take the original search results and filter the top\_n results ("Engine B")

In this section, we'll implement our second retrieval approach as a baseline comparison. For "Engine B", we'll simply take the original Wikipedia search results without any reranking and select the top-n results.

This approach reflects how many traditional search engines work - returning results based on their original relevance score from the data source. By comparing this baseline against our reranked approach (Engine A), we can evaluate whether reranking provides meaningful improvements in result quality.

We'll use the same number of results (top\_n) as Engine A to ensure a fair comparison in our evaluation.

```python PYTHON
results_top_n = []

for item in results:
    results_top_n.append({
        "question": item["question"],
        "search_results": item["search_results"][:top_n]
    })
    
# Print a sample of the top_n results (without reranking)
print(f"Original question: {results_top_n[0]['question']}")
print(f"Top {top_n} results (without reranking):")
for i, result in enumerate(results_top_n[0]['search_results']):
    print(f"\n{i+1}. {result}")
```

```
Original question: What is the capital of France?
Top 3 results (without reranking):

1. Closed-ended question
variants of the above closed-ended questions that possess specific responses are: On what day were you born? (&quot;Saturday.&quot;) What is the capital of France? (&quot;Paris

2. France
semi-presidential republic and its capital, largest city and main cultural and economic centre is Paris. Metropolitan France was settled during the Iron Age by Celtic

3. What Is a Nation?
&quot;What Is a Nation?&quot; (French: Qu&#039;est-ce qu&#039;une nation ?) is an 1882 lecture by French historian Ernest Renan (1823–1892) at the Sorbonne, known for the
```

## Run LLM-as-a-judge evaluation to compare the two engines

Now we'll implement an evaluation framework using LLMs as judges to compare our two retrieval approaches:

* Engine A: Wikipedia results reranked by Cohere's reranking model
* Engine B: Original Wikipedia search results

Using LLMs as evaluators allows us to programmatically assess the quality of search results without human annotation. The following code implements the following steps:

* Setting up the evaluation protocol
  * First, define a clear protocol for how the LLM judges will evaluate the search results. This includes creating a system prompt and a template for each evaluation.
* Using multiple models as independent judges
  * To get more robust results, use multiple LLM models as independent judges. This reduces bias from any single model.
* Implementing a majority voting system
  * Combine judgments from multiple models using a majority voting system to determine which engine performed better for each query:
* Presenting the results
  * After evaluating all queries, present the results to determine which retrieval approach performed better overall.

This approach provides a scalable, reproducible method to evaluate and compare retrieval systems quantitatively.

```python PYTHON
# System prompt for the AI evaluator
SYSTEM_PROMPT = """
You are an AI search evaluator. You will compare search results from two engines and
determine which set provides more relevant and diverse information. You will only
answer with the verdict rather than explaining your reasoning; simply say "Engine A" or
"Engine B".
"""

# Prompt template for each evaluation
PROMPT_TEMPLATE = """
For the following question, which search engine provides more relevant results?

## Question:
{query}

## Engine A:
{engine_a_results}

## Engine B:
{engine_b_results}
"""

def format_results(results):
    """Format search results in a readable way"""
    formatted = []
    for i, result in enumerate(results):
        formatted.append(f"Result {i+1}: {result[:200]}...")
    return "\n\n".join(formatted)

def judge_query(query, engine_a_results, engine_b_results, model_name):
    """Use a single model to judge which engine has better results"""
    agent = Agent(model_name, system_prompt=SYSTEM_PROMPT)
    
    # Format the results
    engine_a_formatted = format_results(engine_a_results)
    engine_b_formatted = format_results(engine_b_results)
    
    # Create the prompt
    prompt = PROMPT_TEMPLATE.format(
        query=query,
        engine_a_results=engine_a_formatted,
        engine_b_results=engine_b_formatted
    )
    
    # Get the model's judgment
    response = agent.run_sync(prompt)
    return response.data

def evaluate_search_results(reranked_results, regular_results, models):
    """
    Evaluate both sets of search results using multiple models.
    
    Args:
        reranked_results: List of dictionaries with 'question' and 'search_results'
        regular_results: List of dictionaries with 'question' and 'search_results'
        models: List of model names to use as judges
    
    Returns:
        DataFrame with evaluation results
    """
    # Prepare data structure for results
    evaluation_results = []
    
    # Evaluate each query
    for i in range(len(reranked_results)):
        query = reranked_results[i]['question']
        engine_a_results = reranked_results[i]['search_results']  # Reranked results
        engine_b_results = regular_results[i]['search_results']   # Regular results
        
        # Get judgments from each model
        judgments = []
        for model in models:
            judgment = judge_query(query, engine_a_results, engine_b_results, model)
            judgments.append(judgment)
        
        # Determine winner by majority vote
        votes = Counter(judgments)
        if votes["Engine A"] > votes["Engine B"]:
            winner = "Engine A"
        elif votes["Engine B"] > votes["Engine A"]:
            winner = "Engine B"
        else:
            winner = "Tie"
        
        # Add results for this query
        row = [query] + judgments + [winner]
        evaluation_results.append(row)
    
    # Create DataFrame
    column_names = ["question"] + [f"judge_{i+1} ({model})" for i, model in enumerate(models)] + ["winner"]
    df = pd.DataFrame(evaluation_results, columns=column_names)
    
    return df
```

```python PYTHON
# Define the search engines
engine_a = results_reranked_top_n
engine_b = results_top_n

# Define the models to use as judges
models = [
    "cohere:command-a-03-2025",
    "cohere:command-r-plus-08-2024",
    "cohere:command-r-08-2024",
    "cohere:c4ai-aya-expanse-32b",
    "cohere:c4ai-aya-expanse-8b",
]

# Get evaluation results
results_df = evaluate_search_results(engine_a, engine_b, models)

# Calculate overall statistics
winner_counts = Counter(results_df["winner"])
total_queries = len(results_df)

# Display summary of results
print("\nPercentage of questions won by each engine:")
for engine, count in winner_counts.items():
    percentage = (count / total_queries) * 100
    print(f"{engine}: {percentage:.2f}% ({count}/{total_queries})")
    
# Display dataframe
results_df.head()

# Save to CSV
results_csv = results_df.to_csv("search_results_evaluation.csv", index=False)
```

```

Percentage of questions won by each engine:
Engine A: 80.00% (8/10)
Tie: 10.00% (1/10)
Engine B: 10.00% (1/10)
```

## Conclusion

This tutorial demonstrates how to evaluate retrieval systems using LLMs as judges through Pydantic AI, comparing original Wikipedia search results against those reranked by Cohere's reranking model.

The evaluation framework uses multiple Cohere models as independent judges with majority voting to determine which system provides more relevant results.

Results showed the reranked approach (Engine A) outperformed the original search rankings (Engine B) by winning 80% of queries, demonstrating the effectiveness of neural reranking in improving search relevance.


# Document Translation with Command A Translate

> This page describes how to use Command A Translate for automated translation across 23 languages with industry-leading performance.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/command-a-translate.ipynb" />

Automated translation from one language to another is one of the oldest applications of machine learning. Today's LLMs have proven remarkably effective for these kinds of tasks, and Command A Translate is Cohere’s state of the art entry into the machine translation field. It delivers industry-leading performance on a variety of translation tasks across 23 languages, while offering enterprises full control of their data through private deployment options.

This cookbook will walk you through how to utilize Command A Translate; for more information, you can check out our [dedicated documentation](https://docs.cohere.com/docs/command-a-translate).

## Getting Set up

First, let's install (or upgrade) the Cohere client.

```python PYTHON
#!pip install --upgrade cohere
```

## Translating a Message

Next, we'll set up Command A Translate to complete a standard translation task.

```python PYTHON
# 1. Set up your Cohere client, translation prompt and maximum words per chunk 
import cohere

co = cohere.ClientV2("<YOUR API KEY>")
model = "command-a-translate-08-2025"

target_language = "Spanish"
prompt_template = "Translate everything that follows into {target_language}:\n\n"
max_words = 15  # Set your desired maximum number of words per chunk

# 2. Your source text
text = (
    "Enterprises rely on translation for some of their most sensitive and business-critical documents and cannot risk data leakage, compliance violations, or misunderstandings. Mistranslated documents can reduce trust and have strategic implications."
)


# 3. Define the chunk_split function (from earlier in your notebook)
def chunk_split(text, max_words, threshold=0.8):

    words = text.split()  # Turn the text into a list of words
    chunks = []  # Initialize an empty list to store our chunks
    start = 0  # Starting index for slicing the words list

    while start < len(words):
        # Determine the end index for the current chunk
        end = min(start + max_words, len(words))
        chunk_words = words[start:end]
        chunk_text = " ".join(chunk_words)  # Combine words back into a string

        # If we're at the end of the text or the chunk is too short, add it as is
        if end == len(words) or len(chunk_words) < max_words * threshold:
            chunks.append(chunk_text.strip())
            break

        # Try to find a natural breaking point within the chunk
        split_point = None
        for separator in ["\n", ".", ")", " "]:
            idx = chunk_text.rfind(separator)
            if idx != -1 and idx >= len(chunk_text) * threshold:
                split_point = idx + 1  # Position after the separator
                break

        if split_point:
            # If a good split point is found, add the chunk up to that point
            chunks.append(chunk_text[:split_point].strip())
            # Move the start index forward by the number of words consumed
            consumed = len(chunk_text[:split_point].split())
            start += consumed
        else:
            # If no good split point is found, add the entire chunk
            chunks.append(chunk_text.strip())
            start = end  # Move to the next chunk

    return chunks

# 4. Split the text into chunks using chunk_split
chunks = chunk_split(text, max_words=max_words)

# 5. Translate each chunk and collect results
translated_chunks = []
for chunk in chunks:
    prompt = prompt_template.format(target_language=target_language) + chunk
    response = co.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    translated = response.message.content[0].text
    translated_chunks.append(translated)

# 6. Merge the translated chunks back together
translated_text = " ".join(translated_chunks)

# 7. Output the final translation
print(translated_text)

```

```
Las empresas dependen de la traducción para algunos de sus documentos más confidenciales y esenciales para su actividad, y no puede arriesgarse a que se produzcan fugas de datos, incumplimientos de la normativa o malentendidos. Los documentos mal traducidos pueden reducir la confianza y tienen consecuencias estratégicas.
```

## Conclusion

To learn more, check out our dedicated [Command A Translate](https://docs.cohere.com/docs/command-a-translate) documentation.



---

**Navigation:** [← Previous](./19-instantiate-the-react-agent.md) | [Index](./index.md) | Next →
