**Navigation:** [← Previous](./02-changelog.md) | [Index](./index.md) | [Next →](./04-fine-tuning-guide.md)

---

# Deploying a Fine-tuned Model
Source: https://docs.together.ai/docs/deploying-a-fine-tuned-model

Once your fine-tune job completes, you should see your new model in [your models dashboard](https://api.together.xyz/models).

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/6171b3cfa4cc84a7ab09099af13064563184722f04b35a788abd122347864d28-image.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=6532d94969ffda2b3f1f19bff5cf573b" alt="" data-og-width="1432" width="1432" data-og-height="275" height="275" data-path="images/docs/6171b3cfa4cc84a7ab09099af13064563184722f04b35a788abd122347864d28-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/6171b3cfa4cc84a7ab09099af13064563184722f04b35a788abd122347864d28-image.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=866974427a65829b49d853e29818c883 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/6171b3cfa4cc84a7ab09099af13064563184722f04b35a788abd122347864d28-image.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ac94c4795ed73f68a51c69b2b5112396 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/6171b3cfa4cc84a7ab09099af13064563184722f04b35a788abd122347864d28-image.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=9fe26596759a698eb144e6f45f0d86f3 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/6171b3cfa4cc84a7ab09099af13064563184722f04b35a788abd122347864d28-image.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=0cd2c4fd0f587f183a06937f71f607e5 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/6171b3cfa4cc84a7ab09099af13064563184722f04b35a788abd122347864d28-image.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=dc0f4f3640482ae9080fbe15cae51512 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/6171b3cfa4cc84a7ab09099af13064563184722f04b35a788abd122347864d28-image.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5883df7a3211dc30ff3921d652f66aa9 2500w" />
</Frame>

To use your model, you can either:

1. Host it on Together AI as a [dedicated endpoint(DE)](/docs/dedicated-inference) for an hourly usage fee
2. Run it immediately if the model supports [Serverless LoRA Inference](/docs/lora-inference)
3. Download your model and run it locally

## Hosting your model on Together AI

If you select your model in [the models dashboard](https://api.together.xyz/models) you can click `CREATE DEDICATED ENDPOINT` to create a [dedicated endpoint](/docs/dedicated-endpoints-ui) for the fine-tuned model.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/b17fd6bd03dcfb26b91389b864cf0ce3a275a2f22db2b56a975b1ffdba3c7789-image.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=25985393a46001b7f6caa2411fa8e4a6" alt="" data-og-width="1441" width="1441" data-og-height="610" height="610" data-path="images/docs/b17fd6bd03dcfb26b91389b864cf0ce3a275a2f22db2b56a975b1ffdba3c7789-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/b17fd6bd03dcfb26b91389b864cf0ce3a275a2f22db2b56a975b1ffdba3c7789-image.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=17e27d488b8d6e3fd914545e6b6d1789 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/b17fd6bd03dcfb26b91389b864cf0ce3a275a2f22db2b56a975b1ffdba3c7789-image.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5a2ea92e185cf8c2e772224eb0582aa0 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/b17fd6bd03dcfb26b91389b864cf0ce3a275a2f22db2b56a975b1ffdba3c7789-image.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=001d316edb86a022e617c15fe4ecf3e4 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/b17fd6bd03dcfb26b91389b864cf0ce3a275a2f22db2b56a975b1ffdba3c7789-image.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=58c1a074a925e8ffffa4f7cce8dd2020 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/b17fd6bd03dcfb26b91389b864cf0ce3a275a2f22db2b56a975b1ffdba3c7789-image.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=98b3988e1d12c18e16ab95d7256ba6ab 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/b17fd6bd03dcfb26b91389b864cf0ce3a275a2f22db2b56a975b1ffdba3c7789-image.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=665ebc29b8ba34334e78f17feb47e93f 2500w" />
</Frame>

Once it's deployed, you can use the ID to query your new model using any of our APIs:

<CodeGroup>
  ```shell CLI theme={null}
  together chat.completions \
    --model "[email protected]/Meta-Llama-3-8B-2024-07-11-22-57-17" \
    --message "user" "What are some fun things to do in New York?"
  ```

  ```python Python theme={null}
  import os
  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

  stream = client.chat.completions.create(
      model="[email protected]/Meta-Llama-3-8B-2024-07-11-22-57-17",
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

  const together = new Together({
    apiKey: process.env['TOGETHER_API_KEY'],
  });

  const stream = await together.chat.completions.create({
    model: '[email protected]/Meta-Llama-3-8B-2024-07-11-22-57-17',
    messages: [
      { role: 'user', content: 'What are some fun things to do in New York?' },
    ],
    stream: true,
  });

  for await (const chunk of stream) {
    // use process.stdout.write instead of console.log to avoid newlines
    process.stdout.write(chunk.choices[0]?.delta?.content || '');
  }
  ```
</CodeGroup>

Hosting your fine-tuned model is charged per minute hosted. You can see the hourly pricing for fine-tuned model inference in [the pricing table](https://www.together.ai/pricing).

When you're not using the model, be sure to stop the endpoint from the [the models dashboard](https://api.together.xyz/models).

Read more about dedicated inference [here](/docs/dedicated-inference).

## Serverless LoRA Inference

If you fine-tuned the model using parameter efficient LoRA fine-tuning you can select the model in the models dashbaord and can click `OPEN IN PLAYGROUND` to quickly test the fine-tuned model.

You can also call the model directly just like any other model on the Together AI platform, by providing the unique fine-tuned model `output_name` that you can find for the specific model on the dashboard. See the list of models that [support LoRA Inference](/docs/lora-inference#supported-base-models).

<CodeGroup>
  ```shell Shell theme={null}
  MODEL_NAME_FOR_INFERENCE="[email protected]/Meta-Llama-3-8B-2024-07-11-22-57-17" #from Model page or Fine-tuning page

  curl -X POST https://api.together.xyz/v1/completions \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "'$MODEL_NAME_FOR_INFERENCE'",
      "messages": [
        {
          "role": "user",
          "content": "What are some fun things to do in New York?",
        },
      ],
      "max_tokens": 128
    }'
  ```

  ```python Python theme={null}
  import os
  from together import Together

  client = Together()

  user_prompt = "debate the pros and cons of AI"

  response = client.chat.completions.create(
      model="[email protected]/Meta-Llama-3-8B-2024-07-11-22-57-17",
      messages=[
          {
              "role": "user",
              "content": user_prompt,
          }
      ],
      max_tokens=512,
      temperature=0.7,
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';
  const together = new Together();

  const stream = await together.chat.completions.create({
    model: '[email protected]/Meta-Llama-3-8B-2024-07-11-22-57-17',
    messages: [
      { role: 'user', content: '"ebate the pros and cons of AI' },
    ],
    stream: true,
  });

  for await (const chunk of stream) {
    // use process.stdout.write instead of console.log to avoid newlines
    process.stdout.write(chunk.choices[0]?.delta?.content || '');
  }
  ```
</CodeGroup>

You can even upload LoRA adapters from HuggingFace or an s3 bucket. Read more about Serverless LoRA Inference [here](/docs/lora-inference) .

## Running Your Model Locally

To run your model locally, first download it by calling `download` with your job ID:

<CodeGroup>
  ```shell CLI theme={null}
  together fine-tuning download "ft-bb62e747-b8fc-49a3-985c-f32f7cc6bb04"
  ```

  ```python python theme={null}
  import os
  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

  client.fine_tuning.download(
      id="ft-bb62e747-b8fc-49a3-985c-f32f7cc6bb04",
      output="my-model/model.tar.zst",
  )
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  const client = new Together({
    apiKey: process.env['TOGETHER_API_KEY'],
  });

  await client.fineTune.download({
    ft_id: 'ft-bb62e747-b8fc-49a3-985c-f32f7cc6bb04',
    output: 'my-model/model.tar.zst',
  });
  ```
</CodeGroup>

Your model will be downloaded to the location specified in `output` as a `tar.zst` file, which is an archive file format that uses the [ZStandard](https://github.com/facebook/zstd) algorithm. You'll need to install ZStandard to decompress your model.

On Macs, you can use Homebrew:

<CodeGroup>
  ```shell Shell theme={null}
  brew install zstd
  cd my-model
  zstd -d model.tar.zst
  tar -xvf model.tar
  cd ..
  ```
</CodeGroup>

Once your archive is decompressed, you should see the following set of files:

```
tokenizer_config.json
special_tokens_map.json
pytorch_model.bin
generation_config.json
tokenizer.json
config.json
```

These can be used with various libraries and languages to run your model locally. [Transformers](https://pypi.org/project/transformers/) is a popular Python library for working with pretrained models, and using it with your new model looks like this:

<CodeGroup>
  ```python Python theme={null}
  from transformers import AutoTokenizer, AutoModelForCausalLM
  import torch

  device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

  tokenizer = AutoTokenizer.from_pretrained("./my-model")

  model = AutoModelForCausalLM.from_pretrained(
      "./my-model",
      trust_remote_code=True,
  ).to(device)

  input_context = "Space Robots are"
  input_ids = tokenizer.encode(input_context, return_tensors="pt")
  output = model.generate(
      input_ids.to(device),
      max_length=128,
      temperature=0.7,
  ).cpu()
  output_text = tokenizer.decode(output[0], skip_special_tokens=True)

  print(output_text)
  ```
</CodeGroup>

```
Space Robots are a great way to get your kids interested in science. After all, they are the future!
```

If you see the output, your new model is working!

You now have a custom fine-tuned model that you can run completely locally, either on your own machine or on networked hardware of your choice.


# Deployment Options Overview
Source: https://docs.together.ai/docs/deployment-options

Compare Together AI's deployment options: fully-managed cloud service vs. secure VPC deployment for enterprises.

Together AI offers a flexible and powerful platform that enables organizations to deploy in a way that best suits their needs. Whether you're looking for a fully-managed cloud solution, or secure VPC deployment on any cloud, Together AI provides robust tools, superior performance, and comprehensive support.

## Deployment Options Overview

Together AI provides two key deployment options:

* **Together AI Cloud**: A fully-managed, inference platform that is fast, scalable, and cost-efficient.
* **VPC Deployment**: Deploy Together AI's Enterprise Platform within your own Virtual Private Cloud (VPC) on any cloud platform for enhanced security and control.

The following sections provide an overview of each deployment type, along with a detailed responsibility matrix comparing the features and benefits of each option.

<ul class="not-prose h-1 mt-10min-w-full overflow-auto border-b border-[#5b616e33] dark:border-gray-200/10" />

## Together AI Cloud

Together AI Cloud is a fully-managed service that runs in Together AI's cloud infrastructure. With seamless access to Together's products, this option is ideal for companies that want to get started quickly without the overhead of managing their own infrastructure.

### Key Features

* **Fully Managed**: Together AI handles infrastructure, scaling, and orchestration.
* **Fast and Scalable**: Both Dedicated and Serverless API endpoints ensure optimal performance and scalability.
* **Cost-Effective**: Pay-as-you-go pricing with the option for reserved endpoints at a discount.
* **Privacy & Security**: Full control over your data; Together AI ensures SOC 2 and HIPAA compliance.
* **Ideal Use Case**: Best suited for AI-native startups and companies that need fast, easy deployment without infrastructure management.

For more information on Together AI Cloud, [contact our team](/docs/support-ticket-portal).

## Together AI VPC Deployment

Together AI VPC Deployment allows you to deploy the platform in your own Virtual Private Cloud (VPC) on any cloud provider (such as Google Cloud, Azure, AWS, or others). This option is ideal for enterprises that need enhanced security, control, and compliance while benefiting from Together AI's powerful AI stack.

### Key Features

* **Cloud-Agnostic**: Deploy within your VPC on any cloud platform of your choice (e.g., AWS, Azure, Google Cloud).
* **Full Control**: Complete administrative access, enabling you to manage and control ingress and egress traffic within your VPC.
* **High Performance**: Achieve up to 2x faster performance on your existing infrastructure, optimized for your environment.
* **Data Sovereignty**: Data never leaves your controlled environment, ensuring complete security and compliance.
* **Customization**: Tailor scaling, performance, and resource allocation to fit your infrastructure’s specific needs.
* **Ideal Use Case**: Perfect for enterprises with strict security, privacy, and compliance requirements who want to retain full control over their cloud infrastructure.

### Example: VPC Deployment in AWS

Below is an example of how Together AI VPC Deployment works in an AWS environment. This system diagram illustrates the architecture and flow:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/34.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7ad0b55a56e9eaecf03c80d3a90ef66f" alt="" data-og-width="1342" width="1342" data-og-height="1070" height="1070" data-path="images/guides/34.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/34.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=884013b1f58f1f732c9aab0c0c7c6e00 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/34.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=643e3f65fc16039aa2ecb0c0a41f4ac2 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/34.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=f77e787d3e26b454d7e9495371aaa3e9 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/34.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d1f99a659a9952d7fba4e10780f09baf 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/34.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ecd727b0a535236a4b923831192f12ff 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/34.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7b5c6567c0e45f31f15ec4d2918359bb 2500w" />
</Frame>

1. **Secure VPC Peering**: Together AI connects to your AWS environment via secure VPC peering, ensuring data remains entirely within your AWS account.
2. **Private Subnets**: All data processing and model inference happens within private subnets, isolating resources from the internet.
3. **Control of Ingress/Egress Traffic**: You have full control over all traffic entering and leaving your VPC, including restrictions on external network access.
4. **Data Sovereignty**: Since all computations are performed within your VPC, data never leaves your controlled environment.
5. **Custom Scaling**: Leverage AWS autoscaling groups to ensure that your AI workloads scale seamlessly with demand, while maintaining complete control over resources.

Although this example uses AWS, the architecture can be adapted to other cloud providers such as Azure or Google Cloud with similar capabilities.

For more information on VPC deployment, [get in touch with us](/docs/support-ticket-portal).

## Comparison of Deployment Options

| Feature                     | Together AI Cloud                                                                                                                                              | Together AI VPC Deployment                                                                                |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **How It Works**            | Fully-managed, serverless API endpoints. On-demand and reserved dedicated endpoints for production workloads - with consistent performance and no rate limits. | Deploy Together's Platform and inference stack in your VPC on any cloud platform.                         |
| **Performance**             | Optimal performance with Together inference stack and Together Turbo Endpoints.                                                                                | Better performance on your infrastructure: Up to 2x better speed on existing infrastructure               |
| **Cost**                    | Pay-as-you-go, or discounts for reserved endpoints.                                                                                                            | Lower TCO through faster performance and optimized GPU usage.                                             |
| **Management**              | Fully-managed service, no infrastructure to manage.                                                                                                            | You manage your VPC, with Together AI’s support. Managed service offering also available.                 |
| **Scaling**                 | Automatic scaling to meet demand.                                                                                                                              | Intelligent scaling based on your infrastructure. Fully customizable.                                     |
| **Data Privacy & Security** | Data ownership with SOC 2 and HIPAA compliance.                                                                                                                | Data never leaves your environment.                                                                       |
| **Compliance**              | SOC 2 and HIPAA compliant.                                                                                                                                     | Implement security and compliance controls to match internal standards.                                   |
| **Support**                 | 24/7 support with guaranteed SLAs.                                                                                                                             | Dedicated support with engineers on call.                                                                 |
| **Ideal For**               | Startups and companies that want quick, easy access to AI infrastructure without managing it.                                                                  | Enterprises with stringent security and privacy needs, or those leveraging existing cloud infrastructure. |

## Next Steps

To get started with Together AI’s platform, **we recommend [trying the Together AI Cloud](https://api.together.ai/signin)** for quick deployment and experimentation. If your organization has specific security, infrastructure, or compliance needs, consider Together AI VPC.

For more information, or to find the best deployment option for your business, [contact our team](https://www.together.ai/forms/contact-sales).


# Deprecations
Source: https://docs.together.ai/docs/deprecations



## Overview

We regularly update our platform with the latest and most powerful open-source models. This document outlines our deprecation policy and provides information on migrating from deprecated models to newer or alternate versions.

## Deprecation Policy

| Model Type                   | Deprecation Notice                | Notes                                                    |
| :--------------------------- | :-------------------------------- | :------------------------------------------------------- |
| Preview Model                | \<24 hrs of notice, after 30 days | Clearly marked in docs and playground with “Preview” tag |
| Serverless Endpoint          | 2 or 3 weeks\*                    |                                                          |
| On Demand Dedicated Endpoint | 2 or 3 weeks\*                    |                                                          |

\*Depends on usage and whether there’s an available newer version of the model.

* Users of models scheduled for deprecation will be notified by email.
* All changes will be reflected on this page.
* Each deprecated model will have a specified removal date.
* After the removal date, the model will no longer be queryable via its serverless endpoint but options to migrate will be available as described below.

## Migration Options

When a model is deprecated on our serverless platform, users have three options:

1. **On-demand Dedicated Endpoint** (if supported):
   * Reserved solely for the user, users choose underlying hardware.
   * Charged on a price per minute basis.
   * Endpoints can be dynamically spun up and down.
2. **Monthly Reserved Dedicated Endpoint**:
   * Reserved solely for the user.
   * Charged on a month-by-month basis.
   * Can be requested via this [form](form).
3. **Migrate to a newer serverless model**:
   * Switch to an updated model on the serverless platform.

## Migration Steps

1. Review the deprecation table below to find your current model.
2. Check if on-demand dedicated endpoints are supported for your model.
3. Decide on your preferred migration option.
4. If choosing a new serverless model, test your application thoroughly with the new model before fully migrating.
5. Update your API calls to use the new model or dedicated endpoint.

## Planned Deprecations

| Planned Deprecation Date | Model                          | Recommended Model Replacement              |
| :----------------------- | :----------------------------- | :----------------------------------------- |
| 2025-06-19               | qwen-qwen2-5-14b-instruct-lora | meta-llama/Meta-Llama-3.1-8B-Instruct-lora |

## Deprecation History

All deprecations are listed below, with the most recent deprecations at the top.

| Removal Date | Model                                               | Supported by on-demand dedicated endpoints                                                             |
| :----------- | :-------------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| 2025-08-28   | `Qwen/Qwen2-VL-72B-Instruct`                        | Yes                                                                                                    |
| 2025-08-28   | `nvidia/Llama-3.1-Nemotron-70B-Instruct-HF`         | Yes                                                                                                    |
| 2025-08-28   | `perplexity-ai/r1-1776`                             | No (coming soon!)                                                                                      |
| 2025-08-28   | `meta-llama/Meta-Llama-3-8B-Instruct`               | Yes                                                                                                    |
| 2025-08-28   | `google/gemma-2-27b-it`                             | Yes                                                                                                    |
| 2025-08-28   | `Qwen/Qwen2-72B-Instruct`                           | Yes                                                                                                    |
| 2025-08-28   | `meta-llama/Llama-Vision-Free`                      | No                                                                                                     |
| 2025-08-28   | `Qwen/Qwen2.5-14B`                                  | Yes                                                                                                    |
| 2025-08-28   | `meta-llama-llama-3-3-70b-instruct-lora`            | No (coming soon!)                                                                                      |
| 2025-08-28   | `meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo`    | No (coming soon!)                                                                                      |
| 2025-08-28   | `NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO`       | Yes                                                                                                    |
| 2025-08-28   | `deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B`         | Yes                                                                                                    |
| 2025-08-28   | `black-forest-labs/FLUX.1-depth`                    | No (coming soon!)                                                                                      |
| 2025-08-28   | `black-forest-labs/FLUX.1-redux`                    | No (coming soon!)                                                                                      |
| 2025-08-28   | `meta-llama/Llama-3-8b-chat-hf`                     | Yes                                                                                                    |
| 2025-08-28   | `black-forest-labs/FLUX.1-canny`                    | No (coming soon!)                                                                                      |
| 2025-08-28   | `meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo`    | No (coming soon!)                                                                                      |
| 2025-06-13   | `gryphe-mythomax-l2-13b`                            | No (coming soon!)                                                                                      |
| 2025-06-13   | `mistralai-mixtral-8x22b-instruct-v0-1`             | No (coming soon!)                                                                                      |
| 2025-06-13   | `mistralai-mixtral-8x7b-v0-1`                       | No (coming soon!)                                                                                      |
| 2025-06-13   | `togethercomputer-m2-bert-80m-2k-retrieval`         | No (coming soon!)                                                                                      |
| 2025-06-13   | `togethercomputer-m2-bert-80m-8k-retrieval`         | No (coming soon!)                                                                                      |
| 2025-06-13   | `whereisai-uae-large-v1`                            | No (coming soon!)                                                                                      |
| 2025-06-13   | `google-gemma-2-9b-it`                              | No (coming soon!)                                                                                      |
| 2025-06-13   | `google-gemma-2b-it`                                | No (coming soon!)                                                                                      |
| 2025-06-13   | `gryphe-mythomax-l2-13b-lite`                       | No (coming soon!)                                                                                      |
| 2025-05-16   | `meta-llama-llama-3-2-3b-instruct-turbo-lora`       | No (coming soon!)                                                                                      |
| 2025-05-16   | `meta-llama-meta-llama-3-8b-instruct-turbo`         | No (coming soon!)                                                                                      |
| 2025-04-24   | `meta-llama/Llama-2-13b-chat-hf`                    | No (coming soon!)                                                                                      |
| 2025-04-24   | `meta-llama-meta-llama-3-70b-instruct-turbo`        | No (coming soon!)                                                                                      |
| 2025-04-24   | `meta-llama-meta-llama-3-1-8b-instruct-turbo-lora`  | No (coming soon!)                                                                                      |
| 2025-04-24   | `meta-llama-meta-llama-3-1-70b-instruct-turbo-lora` | No (coming soon!)                                                                                      |
| 2025-04-24   | `meta-llama-llama-3-2-1b-instruct-lora`             | No (coming soon!)                                                                                      |
| 2025-04-24   | `microsoft-wizardlm-2-8x22b`                        | No (coming soon!)                                                                                      |
| 2025-04-24   | `upstage-solar-10-7b-instruct-v1`                   | No (coming soon!)                                                                                      |
| 2025-04-14   | `stabilityai/stable-diffusion-xl-base-1.0`          | No (coming soon!)                                                                                      |
| 2025-04-04   | `meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo-lora`  | No (coming soon!)                                                                                      |
| 2025-03-27   | `mistralai/Mistral-7B-v0.1`                         | No                                                                                                     |
| 2025-03-25   | `Qwen/QwQ-32B-Preview`                              | No                                                                                                     |
| 2025-03-13   | `databricks-dbrx-instruct`                          | No                                                                                                     |
| 2025-03-11   | `meta-llama/Meta-Llama-3-70B-Instruct-Lite`         | No                                                                                                     |
| 2025-03-08   | `Meta-Llama/Llama-Guard-7b`                         | No                                                                                                     |
| 2025-02-06   | `sentence-transformers/msmarco-bert-base-dot-v5`    | No                                                                                                     |
| 2025-02-06   | `bert-base-uncased`                                 | No                                                                                                     |
| 2024-10-29   | `Qwen/Qwen1.5-72B-Chat`                             | No                                                                                                     |
| 2024-10-29   | `Qwen/Qwen1.5-110B-Chat`                            | No                                                                                                     |
| 2024-10-07   | `NousResearch/Nous-Hermes-2-Yi-34B`                 | No                                                                                                     |
| 2024-10-07   | `NousResearch/Hermes-3-Llama-3.1-405B-Turbo`        | No                                                                                                     |
| 2024-08-22   | `NousResearch/Nous-Hermes-2-Mistral-7B-DPO`         | [Yes](https://api.together.xyz/models/NousResearch/Nous-Hermes-2-Mistral-7B-DPO#dedicated_endpoints)   |
| 2024-08-22   | `SG161222/Realistic_Vision_V3.0_VAE`                | No                                                                                                     |
| 2024-08-22   | `meta-llama/Llama-2-70b-chat-hf`                    | No                                                                                                     |
| 2024-08-22   | `mistralai/Mixtral-8x22B`                           | No                                                                                                     |
| 2024-08-22   | `Phind/Phind-CodeLlama-34B-v2`                      | No                                                                                                     |
| 2024-08-22   | `meta-llama/Meta-Llama-3-70B`                       | [Yes](https://api.together.xyz/models/meta-llama/Meta-Llama-3-70B#dedicated_endpoints)                 |
| 2024-08-22   | `teknium/OpenHermes-2p5-Mistral-7B`                 | [Yes](https://api.together.xyz/models/teknium/OpenHermes-2p5-Mistral-7B#dedicated_endpoints)           |
| 2024-08-22   | `openchat/openchat-3.5-1210`                        | [Yes](https://api.together.xyz/models/openchat/openchat-3.5-1210#dedicated_endpoints)                  |
| 2024-08-22   | `WizardLM/WizardCoder-Python-34B-V1.0`              | No                                                                                                     |
| 2024-08-22   | `NousResearch/Nous-Hermes-2-Mixtral-8x7B-SFT`       | [Yes](https://api.together.xyz/models/NousResearch/Nous-Hermes-2-Mixtral-8x7B-SFT#dedicated_endpoints) |
| 2024-08-22   | `NousResearch/Nous-Hermes-Llama2-13b`               | [Yes](https://api.together.xyz/models/NousResearch/Nous-Hermes-Llama2-13b#dedicated_endpoints)         |
| 2024-08-22   | `zero-one-ai/Yi-34B-Chat`                           | No                                                                                                     |
| 2024-08-22   | `codellama/CodeLlama-34b-Instruct-hf`               | No                                                                                                     |
| 2024-08-22   | `codellama/CodeLlama-34b-Python-hf`                 | No                                                                                                     |
| 2024-08-22   | `teknium/OpenHermes-2-Mistral-7B`                   | [Yes](https://api.together.xyz/models/teknium/OpenHermes-2-Mistral-7B#dedicated_endpoints)             |
| 2024-08-22   | `Qwen/Qwen1.5-14B-Chat`                             | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-14B-Chat#dedicated_endpoints)                       |
| 2024-08-22   | `stabilityai/stable-diffusion-2-1`                  | No                                                                                                     |
| 2024-08-22   | `meta-llama/Llama-3-8b-hf`                          | [Yes](https://api.together.xyz/models/meta-llama/Llama-3-8b-hf#dedicated_endpoints)                    |
| 2024-08-22   | `prompthero/openjourney`                            | No                                                                                                     |
| 2024-08-22   | `runwayml/stable-diffusion-v1-5`                    | No                                                                                                     |
| 2024-08-22   | `wavymulder/Analog-Diffusion`                       | No                                                                                                     |
| 2024-08-22   | `Snowflake/snowflake-arctic-instruct`               | No                                                                                                     |
| 2024-08-22   | `deepseek-ai/deepseek-coder-33b-instruct`           | No                                                                                                     |
| 2024-08-22   | `Qwen/Qwen1.5-7B-Chat`                              | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-7B-Chat#dedicated_endpoints)                        |
| 2024-08-22   | `Qwen/Qwen1.5-32B-Chat`                             | No                                                                                                     |
| 2024-08-22   | `cognitivecomputations/dolphin-2.5-mixtral-8x7b`    | No                                                                                                     |
| 2024-08-22   | `garage-bAInd/Platypus2-70B-instruct`               | No                                                                                                     |
| 2024-08-22   | `google/gemma-7b-it`                                | [Yes](https://api.together.xyz/models/google/gemma-7b-it#dedicated_endpoints)                          |
| 2024-08-22   | `meta-llama/Llama-2-7b-chat-hf`                     | [Yes](https://api.together.xyz/models/meta-llama/Llama-2-7b-chat-hf#dedicated_endpoints)               |
| 2024-08-22   | `Qwen/Qwen1.5-32B`                                  | No                                                                                                     |
| 2024-08-22   | `Open-Orca/Mistral-7B-OpenOrca`                     | [Yes](https://api.together.xyz/models/Open-Orca/Mistral-7B-OpenOrca#dedicated_endpoints)               |
| 2024-08-22   | `codellama/CodeLlama-13b-Instruct-hf`               | [Yes](https://api.together.xyz/models/codellama/CodeLlama-13b-Instruct-hf#dedicated_endpoints)         |
| 2024-08-22   | `NousResearch/Nous-Capybara-7B-V1p9`                | [Yes](https://api.together.xyz/models/NousResearch/Nous-Capybara-7B-V1p9#dedicated_endpoints)          |
| 2024-08-22   | `lmsys/vicuna-13b-v1.5`                             | [Yes](https://api.together.xyz/models/lmsys/vicuna-13b-v1.5#dedicated_endpoints)                       |
| 2024-08-22   | `Undi95/ReMM-SLERP-L2-13B`                          | [Yes](https://api.together.xyz/models/Undi95/ReMM-SLERP-L2-13B#dedicated_endpoints)                    |
| 2024-08-22   | `Undi95/Toppy-M-7B`                                 | [Yes](https://api.together.xyz/models/Undi95/Toppy-M-7B#dedicated_endpoints)                           |
| 2024-08-22   | `meta-llama/Llama-2-13b-hf`                         | No                                                                                                     |
| 2024-08-22   | `codellama/CodeLlama-70b-Instruct-hf`               | No                                                                                                     |
| 2024-08-22   | `snorkelai/Snorkel-Mistral-PairRM-DPO`              | [Yes](https://api.together.xyz/models/snorkelai/Snorkel-Mistral-PairRM-DPO#dedicated_endpoints)        |
| 2024-08-22   | `togethercomputer/LLaMA-2-7B-32K-Instruct`          | [Yes](https://api.together.xyz/models/togethercomputer/Llama-2-7B-32K-Instruct#dedicated_endpoints)    |
| 2024-08-22   | `Austism/chronos-hermes-13b`                        | [Yes](https://api.together.xyz/models/Austism/chronos-hermes-13b#dedicated_endpoints)                  |
| 2024-08-22   | `Qwen/Qwen1.5-72B`                                  | No                                                                                                     |
| 2024-08-22   | `zero-one-ai/Yi-34B`                                | No                                                                                                     |
| 2024-08-22   | `codellama/CodeLlama-7b-Instruct-hf`                | [Yes](https://api.together.xyz/models/codellama/CodeLlama-7b-Instruct-hf#dedicated_endpoints)          |
| 2024-08-22   | `togethercomputer/evo-1-131k-base`                  | No                                                                                                     |
| 2024-08-22   | `codellama/CodeLlama-70b-hf`                        | No                                                                                                     |
| 2024-08-22   | `WizardLM/WizardLM-13B-V1.2`                        | [Yes](https://api.together.xyz/models/WizardLM/WizardLM-13B-V1.2#dedicated_endpoints)                  |
| 2024-08-22   | `meta-llama/Llama-2-7b-hf`                          | No                                                                                                     |
| 2024-08-22   | `google/gemma-7b`                                   | [Yes](https://api.together.xyz/models/google/gemma-7b#dedicated_endpoints)                             |
| 2024-08-22   | `Qwen/Qwen1.5-1.8B-Chat`                            | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-1.8B-Chat#dedicated_endpoints)                      |
| 2024-08-22   | `Qwen/Qwen1.5-4B-Chat`                              | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-4B-Chat#dedicated_endpoints)                        |
| 2024-08-22   | `lmsys/vicuna-7b-v1.5`                              | [Yes](https://api.together.xyz/models/lmsys/vicuna-7b-v1.5#dedicated_endpoints)                        |
| 2024-08-22   | `zero-one-ai/Yi-6B`                                 | [Yes](https://api.together.xyz/models/zero-one-ai/Yi-6B#dedicated_endpoints)                           |
| 2024-08-22   | `Nexusflow/NexusRaven-V2-13B`                       | [Yes](https://api.together.xyz/models/Nexusflow/NexusRaven-V2-13B#dedicated_endpoints)                 |
| 2024-08-22   | `google/gemma-2b`                                   | [Yes](https://api.together.xyz/models/google/gemma-2b#dedicated_endpoints)                             |
| 2024-08-22   | `Qwen/Qwen1.5-7B`                                   | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-7B#dedicated_endpoints)                             |
| 2024-08-22   | `NousResearch/Nous-Hermes-llama-2-7b`               | [Yes](https://api.together.xyz/models/NousResearch/Nous-Hermes-llama-2-7b#dedicated_endpoints)         |
| 2024-08-22   | `togethercomputer/alpaca-7b`                        | [Yes](https://api.together.xyz/models/togethercomputer/alpaca-7b#dedicated_endpoints)                  |
| 2024-08-22   | `Qwen/Qwen1.5-14B`                                  | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-14B#dedicated_endpoints)                            |
| 2024-08-22   | `codellama/CodeLlama-70b-Python-hf`                 | No                                                                                                     |
| 2024-08-22   | `Qwen/Qwen1.5-4B`                                   | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-4B#dedicated_endpoints)                             |
| 2024-08-22   | `togethercomputer/StripedHyena-Hessian-7B`          | No                                                                                                     |
| 2024-08-22   | `allenai/OLMo-7B-Instruct`                          | No                                                                                                     |
| 2024-08-22   | `togethercomputer/RedPajama-INCITE-7B-Instruct`     | No                                                                                                     |
| 2024-08-22   | `togethercomputer/LLaMA-2-7B-32K`                   | [Yes](https://api.together.xyz/models/togethercomputer/LLaMA-2-7B-32K#dedicated_endpoints)             |
| 2024-08-22   | `togethercomputer/RedPajama-INCITE-7B-Base`         | No                                                                                                     |
| 2024-08-22   | `Qwen/Qwen1.5-0.5B-Chat`                            | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-0.5B-Chat#dedicated_endpoints)                      |
| 2024-08-22   | `microsoft/phi-2`                                   | [Yes](https://api.together.xyz/models/microsoft/phi-2#dedicated_endpoints)                             |
| 2024-08-22   | `Qwen/Qwen1.5-0.5B`                                 | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-0.5B#dedicated_endpoints)                           |
| 2024-08-22   | `togethercomputer/RedPajama-INCITE-7B-Chat`         | No                                                                                                     |
| 2024-08-22   | `togethercomputer/RedPajama-INCITE-Chat-3B-v1`      | No                                                                                                     |
| 2024-08-22   | `togethercomputer/GPT-JT-Moderation-6B`             | No                                                                                                     |
| 2024-08-22   | `Qwen/Qwen1.5-1.8B`                                 | [Yes](https://api.together.xyz/models/Qwen/Qwen1.5-1.8B#dedicated_endpoints)                           |
| 2024-08-22   | `togethercomputer/RedPajama-INCITE-Instruct-3B-v1`  | No                                                                                                     |
| 2024-08-22   | `togethercomputer/RedPajama-INCITE-Base-3B-v1`      | No                                                                                                     |
| 2024-08-22   | `WhereIsAI/UAE-Large-V1`                            | No                                                                                                     |
| 2024-08-22   | `allenai/OLMo-7B`                                   | No                                                                                                     |
| 2024-08-22   | `togethercomputer/evo-1-8k-base`                    | No                                                                                                     |
| 2024-08-22   | `WizardLM/WizardCoder-15B-V1.0`                     | No                                                                                                     |
| 2024-08-22   | `codellama/CodeLlama-13b-Python-hf`                 | [Yes](https://api.together.xyz/models/codellama/CodeLlama-13b-Python-hf#dedicated_endpoints)           |
| 2024-08-22   | `allenai-olmo-7b-twin-2t`                           | No                                                                                                     |
| 2024-08-22   | `sentence-transformers/msmarco-bert-base-dot-v5`    | No                                                                                                     |
| 2024-08-22   | `codellama/CodeLlama-7b-Python-hf`                  | [Yes](https://api.together.xyz/models/codellama/CodeLlama-7b-Python-hf#dedicated_endpoints)            |
| 2024-08-22   | `hazyresearch/M2-BERT-2k-Retrieval-Encoder-V1`      | No                                                                                                     |
| 2024-08-22   | `bert-base-uncased`                                 | No                                                                                                     |
| 2024-08-22   | `mistralai/Mistral-7B-Instruct-v0.1-json`           | No                                                                                                     |
| 2024-08-22   | `mistralai/Mistral-7B-Instruct-v0.1-tools`          | No                                                                                                     |
| 2024-08-22   | `togethercomputer-codellama-34b-instruct-json`      | No                                                                                                     |
| 2024-08-22   | `togethercomputer-codellama-34b-instruct-tools`     | No                                                                                                     |

\*\*Notes on model support: \*\*

* Models marked "Yes" in the on-demand dedicated endpoint support column can be spun up as dedicated endpoints with customizable hardware.
* Models marked "No" are not available as on-demand endpoints and will require migration to a different model or a monthly reserved dedicated endpoint.

## Recommended Actions

* Regularly check this page for updates on model deprecations.
* Plan your migration well in advance of the removal date to ensure a smooth transition.
* If you have any questions or need assistance with migration, please contact our support team.

For the most up-to-date information on model availability, support, and recommended alternatives, please check our API documentation or contact our support team.


# DSPy
Source: https://docs.together.ai/docs/dspy

Using DSPy with Together AI

DSPy is a framework for programming language models rather than relying on static prompts. It enables you to build modular AI systems with code instead of hand-crafted prompting, and it offers methods to automatically optimize these systems.

Features

* Programmatic approach to LLM interactions through Python
* Modular components for building complex AI pipelines
* Self-improvement algorithms that optimize prompts and weights
* Support for various applications from simple classifiers to RAG systems and agent loops

## Installing Libraries

<CodeGroup>
  ```shell Shell theme={null}
  pip install -U dspy
  ```
</CodeGroup>

Set your Together AI API key:

<CodeGroup>
  ```shell Shell theme={null}
  export TOGETHER_API_KEY=***
  ```
</CodeGroup>

## Example

Setup and connect DSPy to LLMs on Together AI

<CodeGroup>
  ```python Python theme={null}
  import dspy

  # Configure dspy with a LLM from Together AI
  lm = dspy.LM(
      "together_ai/togethercomputer/llama-2-70b-chat",
      api_key=os.environ.get("TOGETHER_API_KEY"),
      api_base="https://api.together.xyz/v1",
  )

  # Now you can call the LLM directly as follows
  lm("Say this is a test!", temperature=0.7)  # => ['This is a test!']
  lm(
      messages=[{"role": "user", "content": "Say this is a test!"}]
  )  # => ['This is a test!']
  ```
</CodeGroup>

Now we can set up a DSPy module, like `dspy.ReAct` with a task-specific signature. For example, `question -> answer: float` tells the module to take a question and to produce a floating point number answer below.

<CodeGroup>
  ```python Python theme={null}
  # Configure dspy to use the LLM
  dspy.configure(lm=lm)


  # Gives the agent access to a python interpreter
  def evaluate_math(expression: str):
      return dspy.PythonInterpreter({}).execute(expression)


  # Gives the agent access to a wikipedia search tool
  def search_wikipedia(query: str):

      results = dspy.ColBERTv2(url="http://20.102.90.50:2017/wiki17_abstracts")(
          query, k=3
      )
      return [x["text"] for x in results]


  # setup ReAct module with question and math answer signature
  react = dspy.ReAct(
      "question -> answer: float",
      tools=[evaluate_math, search_wikipedia],
  )

  pred = react(
      question="What is 9362158 divided by the year of birth of David Gregory of Kinnairdy castle?"
  )

  print(pred.answer)
  ```
</CodeGroup>

## Next Steps

<Info>
  ### DSPy - Together AI Notebook

  Learn more about building agents using DSPy with Together AI in our [notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/DSPy/DSPy_Agents.ipynb) .
</Info>


# Embeddings
Source: https://docs.together.ai/docs/embeddings-overview

Learn how to get an embedding vector for a given text input.

Together's Embeddings API lets you turn some input text (the *input*) into an array of numbers (the *embedding*). The resulting embedding can be compared against other embeddings to determine how closely related the two input strings are.

Embeddings from large datasets can be stored in vector databases for later retrieval or comparison. Common use cases for embeddings are search, classification, and recommendations. They're also used for building Retrieval Augmented Generation (RAG) applications.

## Generating a single embedding

Use `client.embeddings.create` to generate an embedding for some input text, passing in a model name and input string:

<CodeGroup>
  ```py Python theme={null}
  from together import Together

  client = Together()

  response = client.embeddings.create(
      model="BAAI/bge-base-en-v1.5",
      input="Our solar system orbits the Milky Way galaxy at about 515,000 mph",
  )
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const response = await client.embeddings.create({
    model: "BAAI/bge-base-en-v1.5",
    input: "Our solar system orbits the Milky Way galaxy at about 515,000 mph",
  });
  ```

  ```sh cURL theme={null}
  curl -X POST https://api.together.xyz/v1/embeddings \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
           "input": "Our solar system orbits the Milky Way galaxy at about 515,000 mph.",
           "model": "BAAI/bge-base-en-v1.5"
          }'
  ```
</CodeGroup>

The response will be an object that contains the embedding under the `data` key, as well as some metadata:

```json JSON theme={null}
{
  model: 'BAAI/bge-base-en-v1.5',
  object: 'list',
  data: [
    {
      index: 0,
      object: 'embedding',
      embedding: [0.2633975, 0.13856208, ..., 0.04331574],
    },
  ],
};
```

## Generating multiple embeddings

You can also pass an array of input strings to the `input` option:

<CodeGroup>
  ```py Python theme={null}
  from together import Together

  client = Together()

  response = client.embeddings.create(
      model="BAAI/bge-base-en-v1.5",
      input=[
          "Our solar system orbits the Milky Way galaxy at about 515,000 mph",
          "Jupiter's Great Red Spot is a storm that has been raging for at least 350 years.",
      ],
  )
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const response = await client.embeddings.create({
    model: "BAAI/bge-base-en-v1.5",
    input: [
      "Our solar system orbits the Milky Way galaxy at about 515,000 mph",
      "Jupiter's Great Red Spot is a storm that has been raging for at least 350 years.",
    ],
  });
  ```

  ```sh cURL theme={null}
  curl -X POST https://api.together.xyz/v1/embeddings \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
           "model": "BAAI/bge-base-en-v1.5",
           "input": [
              "Our solar system orbits the Milky Way galaxy at about 515,000 mph",
              "Jupiter'\''s Great Red Spot is a storm that has been raging for at least 350 years."
           ]
          }'
  ```
</CodeGroup>

The `response.data` key will contain an array of objects for each input string you provide:

```json JSON theme={null}
{
  model: 'BAAI/bge-base-en-v1.5',
  object: 'list',
  data: [
    {
      index: 0,
      object: 'embedding',
      embedding: [0.2633975, 0.13856208, ..., 0.04331574],
    },
    {
      index: 1,
      object: 'embedding',
      embedding: [-0.14496337, 0.21044481, ..., -0.16187587]
    },
  ],
};
```


# RAG Integrations
Source: https://docs.together.ai/docs/embeddings-rag



## Using MongoDB

See [this tutorial blog](https://www.together.ai/blog/rag-tutorial-mongodb) for the RAG implementation details using Together and MongoDB.

## Using LangChain

See [this tutorial blog](https://www.together.ai/blog/rag-tutorial-langchain) for the RAG implementation details using Together and LangChain.

* [LangChain TogetherEmbeddings](https://python.langchain.com/docs/integrations/text_embedding/together)
* [LangChain Together](https://python.langchain.com/docs/integrations/llms/together)

## Using LlamaIndex

See [this tutorial blog](https://www.together.ai/blog/rag-tutorial-llamaindex) for the RAG implementation details using Together and LlamaIndex.

* [LlamaIndex TogetherEmbeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/together.html)
* [LlamaIndex TogetherLLM](https://docs.llamaindex.ai/en/stable/examples/llm/together.html)

## Using Pixeltable

See [this tutorial blog](https://pixeltable.readme.io/docs/together-ai) for the RAG implementation details using Together and Pixeltable.


# Error Codes
Source: https://docs.together.ai/docs/error-codes

An overview on error status codes, causes, and quick fix solutions

| Code                       | Cause                                                                                                                                 | Solution                                                                                                                                                                                                                                                                     |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400 - Invalid Request      | Misconfigured request                                                                                                                 | Ensure your request is a [Valid JSON](/docs/inference-rest#create-your-json-formatted-object) and your [API Key](https://api.together.xyz/settings/api-keys) is correct. Also ensure you're using the right prompt format - which is different for Mistral and LLaMA models. |
| 401 - Authentication Error | Missing or Invalid API Key                                                                                                            | Ensure you are using the correct [API Key](https://api.together.xyz/settings/api-keys) and [supplying it correctly](/reference/inference)                                                                                                                                    |
| 402 - Payment Required     | The account associated with the API key has reached its maximum allowed monthly spending limit.                                       | Adjust your [billing settings](https://api.together.xyz/settings/billing) or make a payment to resume service.                                                                                                                                                               |
| 403 - Bad Request          | Input token count + `max_tokens` parameter must be less than the [context](/docs/inference-models) length of the model being queried. | Set `max_tokens` to a lower number. If querying a chat model, you may set `max_tokens` to `null` and let the model decide when to stop generation.                                                                                                                           |
| 404 - Not Found            | Invalid Endpoint URL or model name                                                                                                    | Check your request is being made to the correct endpoint (see the [API reference](/reference/inference) page for details) and that the [model being queried is available](/docs/inference-models)                                                                            |
| 429 - Rate limit           | Too many requests sent in a short period of time                                                                                      | Throttle the rate at which requests are sent to our servers (see our [rate limits](/docs/rate-limits))                                                                                                                                                                       |
| 500 - Server Error         | Unknown server error                                                                                                                  | This error is caused by an issue on our servers. Please try again after a brief wait. If the issue persists, please [contact support](https://www.together.ai/contact)                                                                                                       |
| 503 - Engine Overloaded    | Our servers are seeing high amounts of traffic                                                                                        | Please try again after a brief wait. If the issue persists, please [contact support](https://www.together.ai/contact)                                                                                                                                                        |

If you are seeing other error codes or the solutions do not work, please [contact support](https://www.together.ai/contact) for help.


# Fine-tuning BYOM
Source: https://docs.together.ai/docs/fine-tuning-byom

Bring Your Own Model: Fine-tune Custom Models from the Hugging Face Hub

> Note: This feature extends our fine-tuning capabilities to support models from the Hugging Face ecosystem, enabling you to leverage community innovations and your own custom checkpoints.

## Overview

The Together Fine-Tuning Platform now supports training custom models beyond our official model catalog. If you've found a promising model on Hugging Face Hub, whether it's a community model, a specialized variant, or your own previous experiment, you can now fine-tune it using our service.

**Why Use This Feature?**

* **Leverage specialized models**: Use domain-specific or task-optimized models as your starting point
* **Continue previous work**: Resume training from your own checkpoints or experiments
* **Access community innovations**: Fine-tune cutting-edge models not yet in our official catalog

**Key Concept: Base Model + Custom Model**

Understanding BYOM requires grasping our **dual-model approach**:

* **Base Model** (`model` parameter): A model from Together's official catalog that provides the infrastructure configuration, training settings, and inference setup
* **Custom Model** (`from_hf_model` parameter): Your actual HuggingFace model that gets fine-tuned

**Think of it this way**: The base model acts as a "template" that tells our system how to optimally train and serve your custom model. Your custom model should have a similar architecture, size, and sequence length to the base model for best results.

**Example**:

```python  theme={null}
client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",  # Base model (training template)
    from_hf_model="HuggingFaceTB/SmolLM2-1.7B-Instruct",  # Your custom model
    training_file="file-id-from-upload",
)
```

In this example, we use Llama-2-7B as the base model template because SmolLM2 has Llama architecture and similar characteristics.

**How It Works**

Simply provide a Hugging Face repository URL, and our API will:

1. Load your model checkpoint
2. Apply your fine-tuning data
3. Make the trained model available through our inference endpoints

### Prerequisites

Before you begin, ensure your model meets these requirements:

**Model Architecture**

* **Supported type**: CausalLM models only (models designed for text generation tasks)
* **Size limit**: A maximum of 100 billion parameters
* **Framework version**: Compatible with Transformers library v4.55 or earlier

**Technical Requirements**

* Model weights must be in the `.safetensors` format for security and efficiency
* The model configuration must not require custom code execution (no `trust_remote_code`)
* The repository must be publicly accessible, or you must provide an API token that has access to the private repository

**What You'll Need**

* The Hugging Face repository URL containing your model
* (Optional) The Hugging Face API token for accessing private repositories
* Your training data prepared according to [one of our standard formats](./fine-tuning-data-preparation.mdx)
* Your training hyperparameters for the fine-tuning job

### Compatibility Check

Before starting your fine-tuning job, validate that your model meets our requirements:

1. **Architecture Check**: Visit your model's HuggingFace page and verify it's a "text-generation" or "causal-lm" model
2. **Size Check**: Look for parameter count in model card (should be ≤100B)
3. **Format Check**: Verify model files include `.safetensors` format
4. **Code Check**: Ensure the model doesn't require `trust_remote_code=True`

## Quick Start

Fine-tune a custom model from Hugging Face in three simple steps:

```python  theme={null}
from together import Together

client = Together(api_key="your-api-key")

# Start fine-tuning with your custom model
job = client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",  # Base model family for configuration
    from_hf_model="HuggingFaceTB/SmolLM2-1.7B-Instruct",  # Your custom model from HF
    training_file="file-id-from-upload",
    # Optional: for private repositories
    hf_api_token="hf_xxxxxxxxxxxx",
)

# Monitor progress
print(f"Job ID: {job.id}")
print(f"Status: {job.status}")
```

The custom model should be as close (have similar architecture, similar model sizes and max sequence length) to the base model family as possible. In the example above, `HuggingFaceTB/SmolLM2-1.7B-Instruct` has Llama architecture, and the closest model size and max sequence length.

### Parameter Explanation

| Parameter           | Purpose                                                                              | Example                                                      |
| ------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------ |
| `model`             | Specifies the base model family for optimal configuration and inference setup        | `"togethercomputer/llama-2-7b-chat"`, `"meta-llama/Llama-3"` |
| `from_hf_model`     | The Hugging Face repository containing your custom model weights                     | `"username/model-name"`                                      |
| `hf_model_revision` | (Optional) Use only if you need a specific commit hash instead of the latest version | `"abc123def456"`                                             |
| `hf_api_token`      | (Optional) API token for accessing private repositories                              | `"hf_xxxxxxxxxxxx"`                                          |

## Detailed Implementation Guide

**Step 1: Prepare Your Training Data**

Ensure your training data is formatted correctly and uploaded to the Together platform. Refer to [our data preparation guide](./fine-tuning-data-preparation.mdx) for detailed instructions on supported formats.

**Step 2: Start Fine-Tuning**

Launch your fine-tuning job with your custom model:

```python  theme={null}
job = client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",
    from_hf_model="HuggingFaceTB/SmolLM2-1.7B-Instruct",
    training_file="your-file-id",
    # Recommended training parameters
    n_epochs=3,
    learning_rate=1e-5,
    batch_size=4,
    # Optional parameters
    suffix="custom-v1",  # Helps track different versions
    wandb_api_key="...",  # For training metrics monitoring
    # Add other training parameters for your training
)

# Only include if you need a specific commit:
# hf_model_revision="abc123def456"
```

**Step 3: Monitor and Use Your Model**

Once training completes successfully, your model will appear in the models dashboard and can be used for inference. You can create a dedicated endpoint or start using the model using LoRA Serverless endpoints. For more information, please go to the page [Deploying a Fine-tuned Model](./deploying-a-fine-tuned-model.mdx).

## Common Use Cases & Examples

### Architecture-Specific Examples

**Llama Family Models**

```python  theme={null}
# Example 1: Fine-tune SmolLM2 (Llama architecture)
client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",  # Base model template
    from_hf_model="HuggingFaceTB/SmolLM2-1.7B-Instruct",  # Custom model
    training_file="file-id",
    n_epochs=3,
    learning_rate=1e-5,
)

# Example 2: Fine-tune a Code Llama variant
client.fine_tuning.create(
    model="meta-llama/Llama-3-8b-chat-hf",
    from_hf_model="codellama/CodeLlama-7b-Instruct-hf",
    training_file="code-dataset-id",
    batch_size=2,  # Reduce for code models
    n_epochs=2,
)
```

**Qwen Family Models**

```python  theme={null}
# Example 1: Fine-tune Qwen2.5 model
client.fine_tuning.create(
    model="Qwen/Qwen3-4B",  # Base template
    from_hf_model="Qwen/Qwen2.5-7B-Instruct",  # Custom Qwen model
    training_file="file-id",
    learning_rate=5e-6,  # Lower LR for larger models
    n_epochs=3,
)

# Example 2: Fine-tune specialized Qwen model
client.fine_tuning.create(
    model="Qwen/Qwen3-7B",
    from_hf_model="Qwen/Qwen2.5-Math-7B-Instruct",  # Math-specialized
    training_file="math-problems-dataset",
    suffix="math-tuned-v1",
)
```

**Mistral Family Models**

```python  theme={null}
# Example 1: Fine-tune Mistral 7B variant
client.fine_tuning.create(
    model="mistralai/Mistral-7B-Instruct-v0.1",  # Base template
    from_hf_model="mistralai/Mistral-7B-Instruct-v0.3",  # Newer version
    training_file="file-id",
    n_epochs=3,
    batch_size=4,
)

# Example 2: Fine-tune Mixtral model
client.fine_tuning.create(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    from_hf_model="mistralai/Mixtral-8x22B-Instruct-v0.1",  # Larger variant
    training_file="large-dataset-id",
    batch_size=1,  # Very large model, small batch
    learning_rate=1e-6,
)
```

**Gemma Family Models**

```python  theme={null}
# Example 1: Fine-tune Gemma 2 model
client.fine_tuning.create(
    model="google/gemma-2-9b-it",  # Base template
    from_hf_model="google/gemma-2-2b-it",  # Smaller Gemma variant
    training_file="file-id",
    n_epochs=4,
    learning_rate=2e-5,
)

# Example 2: Fine-tune CodeGemma
client.fine_tuning.create(
    model="google/gemma-3-4b-it",
    from_hf_model="google/codegemma-7b-it",  # Code-specialized
    training_file="code-instruction-dataset",
    learning_rate=1e-5,
)
```

### End-to-End Workflow Examples

**Complete Domain Adaptation Workflow**

```python  theme={null}
from together import Together
import json

# Step 1: Initialize client and prepare data
client = Together(api_key="your-api-key")

# Step 2: Upload training data
with open("legal_qa_dataset.jsonl", "rb") as f:
    file_upload = client.files.upload(file=f, purpose="fine-tune")

# Step 3: Choose compatible model based on requirements
# For this example, we'll use a compatible Phi-3 model
target_model = "microsoft/phi-3-medium-4k-instruct"

# Step 4: Start fine-tuning
job = client.fine_tuning.create(
    model="microsoft/phi-3-medium-4k-instruct",  # Base model
    from_hf_model=target_model,  # Your custom model
    training_file=file_upload.id,
    suffix="legal-specialist-v1",
    n_epochs=3,
    learning_rate=1e-5,
    wandb_api_key="your-wandb-key",  # Optional: for monitoring
)

# Step 5: Monitor training
print(f"Job started: {job.id}")
while job.status in ["pending", "running"]:
    job = client.fine_tuning.retrieve(job.id)
    print(f"Status: {job.status}")
    time.sleep(30)

# Step 6: Deploy for inference (once completed)
if job.status == "succeeded":
    # Create dedicated endpoint
    endpoint = client.endpoints.create(
        model=job.fine_tuned_model, type="dedicated", hardware="A100-40GB"
    )
    print(f"Endpoint created: {endpoint.id}")
```

**Iterative Model Improvement Workflow**

```python  theme={null}
# Workflow: Start → Fine-tune → Evaluate → Improve → Repeat

# Iteration 1: Initial fine-tuning
initial_job = client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",
    from_hf_model="huggingface/CodeBERTa-small-v1",  # Starting model
    training_file="initial-dataset-id",
    suffix="v1",
    n_epochs=3,
)

# Wait for completion...

# Iteration 2: Improve with more data
improved_job = client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",
    from_hf_model="your-username/model-v1",  # Use previous result
    training_file="expanded-dataset-id",  # More/better data
    suffix="v2",
    n_epochs=2,  # Fewer epochs for fine-tuning
    learning_rate=5e-6,  # Lower learning rate
)

# Iteration 3: Specialized fine-tuning
specialized_job = client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",
    from_hf_model="your-username/model-v2",
    training_file="specialized-task-dataset",
    suffix="specialized-v3",
    n_epochs=1,
    learning_rate=1e-6,
)
```

### Continuing Training from a Previous Fine-tune

Resume training from a checkpoint you previously created to add more data or continue the adaptation process:

```python  theme={null}
client.fine_tuning.create(
    model="google/gemma-3-4b-it",
    from_hf_model="your-username/previous-finetune-v1",
    training_file="new-training-data",
    n_epochs=2,  # Additional training epochs
)
```

### Fine-tuning a Community Specialist Model

Leverage community models that have already been optimized for specific domains:

```python  theme={null}
# Example: Fine-tune a medical domain model with your proprietary data
client.fine_tuning.create(
    model="Qwen/Qwen3-4B",  # Base architecture it's built on
    from_hf_model="community/medical-Qwen3-4B",  # Specialized variant
    training_file="your-medical-data",
)
```

## Troubleshooting

**Understanding Training Stages**

Your fine-tuning job progresses through several stages. Understanding these helps you identify where issues might occur:

1. **Data Download**: The system downloads your model weights from Hugging Face and your training data from Together
2. **Initialization**: Model is loaded onto GPUs and the data pipeline is prepared for training
3. **Training**: The actual fine-tuning occurs based on your specified hyperparameters
4. **Saving**: The trained model is saved to temporary storage
5. **Upload**: The final model is moved to permanent storage for inference availability

**Common Errors and Solutions**

Due to the number of diverse model families hosted on the Hugging Face Hub, understanding these error types helps you quickly resolve issues:

* **Internal Errors**: Training failed due to an internal problem with the Fine-tuning API. Our team gets automatically notified and usually starts investigating the issue shortly after it occurs. If this persists for long periods of time, please contact support with your job ID.
* **CUDA OOM (Out of Memory) Errors**: Training failed because it exceeded available GPU memory. To resolve this, reduce the `batch_size` parameter or consider using a smaller model variant.
* **Value Errors and Assertions**: Training failed due to a checkpoint validation error. These typically occur when model hyperparameters are incompatible or when the model architecture doesn't match expectations. Check that your model is actually CausalLM and that all parameters are within valid ranges.
* **Runtime Errors**: Training failed due to computational exceptions raised by PyTorch. These often indicate issues with model weights or tensor operations. Verify that your model checkpoint is complete and uncorrupted.

## Frequently Asked Questions

**Question: How to choose the base model?**

There are three variables to consider:

* Model Architecture
* Model Size
* Maximum Sequence Length

You want to use the model with the same architecture, the closest number of parameters as possible to the base model and the max seq length for the base model should not exceed the maximum length for the external model.

For example, `HuggingFaceTB/SmolLM2-135M-Instruct`. It has Llama architecture, the model size is 135M parameters and the max sequence length is 8k. Looking into the Llama models, Fine-tuning API supports llama2, llama3, llama3.1 and llama3.2 families. The closest model by number of parameters is `meta-llama/Llama-3.2-1B-Instruct`, but the max seq length is 131k, which is much higher than the model can support. It's better to use `togethercomputer/llama-2-7b-chat`, which is larger than the provided model, but the max seq length is not exceeding the model's limits.

**Issue**: "No exact architecture match available"

* **Solution**: Choose the closest architecture family (e.g., treat CodeLlama as Llama)

**Issue**: "All base models are much larger than my custom model"

* **Solution**: Use the smallest available base model; the system will adjust automatically

**Issue**: "Unsure about sequence length limits"

* **Solution**: Check your model's `config.json` for `max_position_embeddings` or use our compatibility checker

***

**Question: Which models are supported?**

Any CausalLM model under 100B parameters that has a corresponding base model in [our official catalog](./fine-tuning-models.mdx). The base model determines the inference configuration. If your checkpoint significantly differs from the base model architecture, you'll receive warnings, but training will proceed.

***

**Question: Can I fine-tune an adapter/LoRA model?**

Yes, you can continue training from an existing adapter model. However, the Fine-tuning API will merge the adapter with the base model during training, resulting in a full checkpoint rather than a separate adapter.

***

**Question: Will my model work with inference?**

Your model will work with inference if:

* The base model you specified is officially supported
* The architecture matches the base model configuration
* Training completed successfully without errors

Models based on unsupported architectures may not function correctly during inference. If you want to run a trained model with unsupported architecture, please submit a support ticket on [the support page](https://support.together.ai/).

***

**Question: Can I load a custom model for dedicated endpoint and train it?**

No, you cannot use uploaded models for training in Fine-tuning API. Models uploaded for inference will not appear in the fine-tunable models. To learn more about what you can do with the uploaded models for dedicated endpoint, see this [page](./custom-models.mdx).

However, you can upload your model to the Hugging Face Hub and use the repo id to train it. The trained model will be available for the inference after the training.

***

**Question: How do I handle private repositories?**

Include your Hugging Face API token with read permissions for those repositories when creating the fine-tuning job:

```python  theme={null}
client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",
    from_hf_model="private-org/private-model",
    hf_api_token="hf_xxxxxxxxxxxx",
    training_file="your-file-id",
)
```

***

**Question: What if my model requires custom code?**

Models requiring `trust_remote_code=True` are not currently supported for security reasons. Consider these alternatives:

* Use a similar model that doesn't require custom code
* Contact our support team and request adding the model to our official catalog
* Wait for the architecture to be supported officially

***

**Question: How do I specify a particular model version?**

If you need to use a specific commit hash instead of the latest version, use the `hf_model_revision` parameter:

```python  theme={null}
# Use a specific commit hash
client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",
    from_hf_model="HuggingFaceTB/SmolLM2-1.7B-Instruct",
    hf_model_revision="abc123def456",  # Specific commit hash
    training_file="your-file-id",
)
```

## Support

Need help with your custom model fine-tuning?

* **Documentation**: Check our [error guide](/docs/error-codes)
* **Community**: Join our [Discord Community](https://discord.gg/9Rk6sSeWEG) for peer support and tips
* **Direct Support**: Contact our support team with your job ID for investigation of specific issues

When reporting issues, please include:

* Your fine-tuning job ID
* The Hugging Face model repository you're using
* Any error messages you're encountering


# Data Preparation
Source: https://docs.together.ai/docs/fine-tuning-data-preparation

Together Fine-tuning API accepts two data formats for training dataset files: text data and tokenized data (in the form of Parquet files). Below, you can learn about different types of those formats and the scenarios in which they can be most useful.

Together Fine-tuning API accepts two data formats for training dataset files: text data and tokenized data (in the form of Parquet files). Below, you can learn about different types of those formats and the scenarios in which they can be most useful.

### Which file format should I use for data?

JSONL is simpler and will work for many cases, while Parquet stores pre-tokenized data, providing flexibility to specify custom attention mask and labels (loss masking). It also saves you time for each job you run by skipping the tokenization step.

By default, it's easier to use JSONL. However, there are a couple of things to keep in mind:

1. For JSONL training data, we use a variation of [sample packing](https://huggingface.co/docs/trl/main/en/reducing_memory_usage#packing) that improves training efficiency by utilizing the maximum context length via packing multiple examples together. This technique changes the effective batch size, making it larger than the specified batch size, and reduces the total number of training steps.\
   If you'd like to disable packing during training, you can provide a tokenized dataset in a Parquet file. [This example script](https://github.com/togethercomputer/together-python/blob/main/examples/tokenize_data.py#L34) for tokenizing a dataset demonstrates padding each example with a padding token. Note that the corresponding `attention_mask` and `labels` should be set to 0 and -100, respectively, so that the model ignores the padding tokens during prediction and excludes them from the loss calculation.
2. If you want to specify custom `attention_mask` values or apply some tokenization customizations unique to your setup, you can use the Parquet format as well.

**Note**: Regardless of the dataset format, the data file size must be under 25GB.

## Text Data

## Data formats

Together Fine-tuning API accepts three text dataset formats for the training dataset. Your data file must be in the `.jsonl` format with fields that indicate the dataset format. You can have other fields, but they will be ignored during training. To speed up the data uploading and processing steps and to maximize the number of examples per file, we recommend to remove the unused fields.

Also, if the data has two or more possible formats (e.g., it contains both `text` and `messages`), the Together client will show an error at the file check stage before the upload.

### Conversational Data

For conversational fine-tuning, your data file must contain a `messages` field on each line, with `role` and `content` specified for each message. Each sample should start with either a `system` or `user` message, followed by alternating `user` and `assistant` messages. The Together client will reject any dataset that does not follow this pattern.

Optionally, you can add a `weight` field to any message to control its contribution to the training loss. Messages with `weight=0` will be masked during training (their tokens won't contribute to the loss), while messages with `weight=1` (default) will be included. Only values 0 and 1 are supported for the `weight` field.

```Text JSONL theme={null}
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

```Text JSONL theme={null}
{"prompt": "...", "completion": "..."}
{"prompt": "...", "completion": "..."}
```

By default, models will not be trained to predict the text from the prompt. Use `--train-on-inputs true` to include prompts in training. See the [API Reference](/reference/post-fine-tunes) for details.

Here are some examples with this format that you can download from the Hugging Face Hub:

* [meta-math/MetaMathQA](https://huggingface.co/datasets/meta-math/MetaMathQA)
* [glaiveai/glaive-code-assistant](https://huggingface.co/datasets/glaiveai/glaive-code-assistant)

### Generic Text Data

If you have no need for instruction or conversational training, you can put the data in the `text` field.

```Text JSONL theme={null}
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

```text Text theme={null}
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

## Tokenized Data

You can also provide tokenized data for more advanced use cases. You may want to use this data format if you are:

1. Using the same dataset for multiple experiments: this saves the tokenization step and accelerates your fine-tuning job.
2. Using a custom tokenizer that's intentionally different than the base model tokenizer
3. Masking out certain parts of your examples for the loss calculation (which are not covered by instruction or conversational dataset use cases above)

Your data file must meet the following requirements:

* The data file size must be under 25GB.
* The file format must be in the `.parquet` format.
* Allowed fields:
  * `input_ids`(required): List of token ids to be fed to a model.
  * `attention_mask`(required): List of indices specifying which tokens should be attended to by the model.
  * `labels`(optional): List of token ids to be used as target predictions. The default token ID to be ignored in the loss calculation is `-100`. To ignore certain predictions in the loss, replace their corresponding values with `-100`. If this field is not given, `input_ids` will be used.

## Example

You can find an [example script ](https://github.com/togethercomputer/together-python/blob/main/examples/tokenize_data.py) that converts text data in Hugging Face Hub to the tokenized format.

In this example, we will use a toy dataset [clam004/antihallucination\_dataset](https://huggingface.co/datasets/clam004/antihallucination_dataset) in Hugging Face Hub with the tokenizer from `NousResearch/Nous-Hermes-2-Mixtral-8x7B-SFT`model. The max sequence length of this model is 32768. To compare the differences between packing and padding, we will run the script twice with and without `--packing`. When packing is not applied, each example will be (left-)padded with the tokenizer's own pad token to keep the length of all examples consistent. Note that packing is used during training by default, and we recommend to use packing during the tokenization step by passing `--packing` in the example script. Also note that we shift labels internally for model training and you do not need to do this.

* With packing,

```Text shell theme={null}
python tokenize_data.py --tokenizer="NousResearch/Nous-Hermes-2-Mixtral-8x7B-SFT" --max-seq-length=32768 --add-labels --packing --out-filename="processed_dataset_packed.parquet"
```

`processed_dataset_packed.parquet` will be saved under the same directory.

* Without packing,

```Text python theme={null}
python tokenize_data.py --tokenizer="NousResearch/Nous-Hermes-2-Mixtral-8x7B-SFT" --max-seq-length=32768 --add-labels --out-filename="processed_dataset.parquet"
```

`processed_dataset_padded.parquet` will be saved under the same directory.

Let's load the generated files to see the results. In python,

```Text python theme={null}
>>> from datasets import load_dataset
>>> dataset_packed = load_dataset("parquet", data_files={'train': 'processed_dataset_packed.parquet'})
>>> dataset_padded = load_dataset("parquet", data_files={'train': 'processed_dataset_padded.parquet'})
```

First, you will see the number of examples from the dataset with packing is only 6 while the one without packing has 238:

```Text python theme={null}
>>> dataset_packed['train']
Dataset({
    features: ['input_ids', 'attention_mask', 'labels'],
    num_rows: 6
})
>>> dataset_padded['train']
Dataset({
    features: ['input_ids', 'attention_mask', 'labels'],
    num_rows: 238
})
```

In the first example of `dataset_padded` you will find the first 31140 tokens are padded and have `-100` as their labels to be ignored during the loss mask. The pad token for this tokenizer is `32000`

```python python theme={null}
{
    "input_ids": [32000, 32000, 32000, ..., 3409, 6898, 28767],
    "attention_masks": [0, 0, 0, ..., 1, 1, 1],
    "labels": [-100, -100, -100, ..., 3409, 6898, 28767],
}
```

On the other hand, in the first example of `dataset_packed`, no padding is used. And the first 1628 token ids match the last 1628 token ids from the first example of `dataset_padded`.

```text Text theme={null}
{
  "input_ids": [1, 523, 434, ..., 6549, 3805, 7457],
  "attention_masks": [1, 1, 1, ..., 1, 1, 1],
  "labels": [1, 523, 434,..., 6549, 3805, 7457]
}
```

## File Check

To confirm that your dataset has the right format, run the following command. This step is optional, but we highly recommend to run this step before uploading the file and using it for fine-tuning.

```text Text theme={null}
together files check PATH_TO_DATA_FILE
```

Here's the output:

```shell Shell theme={null}
together files check joke_explanations.jsonl
{
    "is_check_passed": true,
    "message": "Checks passed",
    "found": true,
    "file_size": 781041,
    "utf8": true,
    "line_type": true,
    "text_field": true,
    "key_value": true,
    "min_samples": true,
    "num_samples": 238,
    "load_json": true,
    "filetype": "jsonl"
}
```

After your data is prepared, upload your file using either [CLI](/reference/finetune) or [Python SDK](https://github.com/togethercomputer/together-python).


# Fine Tuning FAQs
Source: https://docs.together.ai/docs/fine-tuning-faqs



## Job Timing

### How long will it take for my job to start?

It depends. Factors that affect waiting time include the number of pending jobs from other customers, the number of jobs currently running, and available hardware. If there are no other pending jobs and there is available hardware, your job should start within a minute of submission. Typically jobs will start within an hour of submission. However, there is no guarantee on waiting time.

### How long will my job take to run?

It depends. Factors that impact your job run time are model size, training data size, and network conditions when downloading/uploading model/training files. You can estimate how long your job will take to complete training by multiplying the number of epochs by the time to complete the first epoch.

## Pricing and Billing

### How can I estimate my fine-tuning job cost?

To estimate the cost of your fine-tuning job:

1. Calculate approximate training tokens: `context_length × batch_size × steps × epochs`
2. Add validation tokens: `validation_dataset_size × evaluation_frequency`
3. Multiply the total tokens by the per-token rate for your chosen model size, fine-tuning type, and implementation method

### Fine-Tuning Pricing

Fine-tuning pricing is based on the total number of tokens processed during your job, including training and validation. Cost varies by model size, fine-tuning type (Supervised Fine-tuning or DPO), and implementation method (LoRA or Full Fine-tuning).

The total cost is calculated as: `total_tokens_processed × per_token_rate`

Where `total_tokens_processed = (n_epochs × n_tokens_per_training_dataset) + (n_evals × n_tokens_per_validation_dataset)`

For current rates, refer to our [fine-tuning pricing page](https://together.ai/pricing).

The exact token count and final price are available after tokenization completes, shown in your [jobs dashboard](https://api.together.xyz/jobs) or via `together fine-tuning retrieve $JOB_ID`.

### Dedicated Endpoint Charges for Fine-Tuned Models

After fine-tuning, hosting charges apply for dedicated endpoints (per minute, even when not in use). These are separate from job costs and continue until you stop the endpoint.

To avoid unexpected charges:

* Monitor active endpoints in the [models dashboard](https://api.together.xyz/models)
* Stop unused endpoints
* Review hosting rates on the [pricing page](https://together.ai/pricing)

### Understanding Refunds When Canceling Fine-Tuning Jobs

When you cancel a running fine-tuning job, you're charged only for completed steps (hardware resources used). Refunds apply only for uncompleted steps.

To check progress: Use `client.fine_tuning.retrieve("your-job-id").total_steps` (replace with your job ID).

For billing questions, contact support with your job ID.

## Errors and Troubleshooting

### Why am I getting an error when uploading a training file?

Common issues:

* Incorrect API key (403 status).
* Insufficient balance (minimum \$5 required). Add a credit card or adjust limits. If balance is sufficient, contact support.

### Why was my job cancelled?

Reasons:

* Insufficient balance.
* Incorrect WandB API key.

Check events via CLI: `$ together list-events <job-fine-tune-id>` or web interface.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/48.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=c72daddc474b7c58ac078f33a000f6e0" alt="" data-og-width="1106" width="1106" data-og-height="961" height="961" data-path="images/guides/48.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/48.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=cd56c516c74446d5a96018aaf5b17771 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/48.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=1d30d46d9e760daac203362db424da83 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/48.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=377e452ba9318eb504c4da8c54e9c79c 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/48.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=dbb7ef05f5e68d16766ce444cca50f22 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/48.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=97da7406edc7e127c7ad8629770f8505 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/48.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=fd6929a5e71905a334c1d645d8b3bcb5 2500w" />
</Frame>

Example event log for billing limit:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/49.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=ee5d65a6f7b6d39416ee4d770f8647f0" alt="" data-og-width="1654" width="1654" data-og-height="1484" height="1484" data-path="images/guides/49.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/49.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=ef33bd87a3f569825c0ca708e3b2fc76 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/49.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=f49f93a10ac9c19d16566a96387c4bac 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/49.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=27488e3c150bd331af52c97681cdccf4 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/49.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=e28a9d6c76577f5de9fe582ab6994f11 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/49.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=be6ae1f2b4771ab888f7632c7c006c23 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/49.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=d47edeea1f37908dc310c1872aa62a3b 2500w" />
</Frame>

### What should I do if my job is cancelled due to billing limits?

Add a credit card to increase your spending limit, make a payment, or adjust limits. Contact support if needed.

### Why was there an error while running my job?

If failing after download but before training, likely training data issue. Check event log:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/50.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=85298509c50a8fff62e59c6c53f14f30" alt="" data-og-width="1648" width="1648" data-og-height="1140" height="1140" data-path="images/guides/50.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/50.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=05054022ed28478f088043eeac5f4369 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/50.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=9538377bec0fd8dfdbd206f28155867a 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/50.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=1e1037334d7a9f6b5af2284c80d4f2ea 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/50.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=36fd3184594c66ac6226890761081986 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/50.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=33eeed12ca878771fbbfad1b75d51413 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/50.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=b589880f37eff5eba367ba7e96db5e04 2500w" />
</Frame>

Verify file with: `$ together files check ~/Downloads/unified_joke_explanations.jsonl`

If data passes checks but errors persist, contact support.

For other errors (e.g., hardware failures), jobs may restart automatically with refunds.

### How do I know if my job was restarted?

Jobs restart automatically on internal errors. Check event log for restarts, new job ID, and refunds.

Example:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/51.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=05454172c0a1c05d0ab593b263e953ad" alt="" data-og-width="1958" width="1958" data-og-height="404" height="404" data-path="images/guides/51.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/51.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=f39fe1e133f609f85bdcc3c26a991936 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/51.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=ee91c0fb691bfe2a38d22f4321673379 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/51.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=89cf371d1b489f0c4271ec0799219a14 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/51.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=0afdb50badf0ecb4f19623fff7d09115 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/51.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=bd0c5232037129595a9d5043ac66ad2e 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/51.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=953d1a91eb74c8358750c151de97a3a1 2500w" />
</Frame>

## Common Error Codes During Fine-Tuning

| Code | Cause                                                                   | Solution                                                                                                          |
| ---- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 401  | Missing or Invalid API Key                                              | Ensure you are using the correct [API Key](https://api.together.xyz/settings/api-keys) and supplying it correctly |
| 403  | Input token count + `max_tokens` parameter exceeds model context length | Set `max_tokens` to a lower number. For chat models, you may set `max_tokens` to `null`                           |
| 404  | Invalid Endpoint URL or model name                                      | Check your request is made to the correct endpoint and the model is available                                     |
| 429  | Rate limit exceeded                                                     | Throttle request rate (see [rate limits](https://docs.together.ai/docs/rate-limits))                              |
| 500  | Invalid Request                                                         | Ensure valid JSON, correct API key, and proper prompt format for the model type                                   |
| 503  | Engine Overloaded                                                       | Try again after a brief wait. Contact support if persistent                                                       |
| 504  | Timeout                                                                 | Try again after a brief wait. Contact support if persistent                                                       |
| 524  | Cloudflare Timeout                                                      | Try again after a brief wait. Contact support if persistent                                                       |
| 529  | Server Error                                                            | Try again after a wait. Contact support if persistent                                                             |

If you encounter other errors or these solutions don't work, [contact support](https://www.together.ai/contact).

## Model Management

### Can I download the weights of my model?

Yes, to use your fine-tuned model outside our platform:

Run: `together fine-tuning download <FT-ID>`

This downloads ZSTD compressed weights. Extract with `tar -xf filename`.

Options:

* `--output`,`-o` (filename, optional) -- Specify output filename. Default: `<MODEL-NAME>.tar.zst`
* `--step`,`-s` (integer, optional) -- Download specific checkpoint. Default: latest (-1)


# Supported Models
Source: https://docs.together.ai/docs/fine-tuning-models

A list of all the models available for fine-tuning.

The following models are available to use with our fine-tuning API. Get started with [fine-tuning a model](/docs/fine-tuning-quickstart)!

**Note:** This list is different from the models that support Serverless LoRA inference, which allows you to perform LoRA fine-tuning and run inference immediately. See the [LoRA inference page](/docs/lora-inference#supported-base-models) for the list of supported base models for serverless LoRA.

**Important:** When uploading LoRA adapters for serverless inference, you must use base models from the serverless LoRA list, not the fine-tuning models list. Using an incompatible base model (such as Turbo variants) will result in a "No lora\_model specified" error during upload. For example, use `meta-llama/Meta-Llama-3.1-8B-Instruct-Reference` instead of `meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo` for serverless LoRA adapters.

* *Training Precision Type* indicates the precision type used during training for each model.

  * AMP (Automated Mixed Precision): AMP allows the training speed to be faster with less memory usage while preserving convergence behavior compared to using float32. Learn more about AMP in [this PyTorch blog](https://pytorch.org/blog/what-every-user-should-know-about-mixed-precision-training-in-pytorch/).
  * bf16 (bfloat 16): This uses bf16 for all weights. Some large models on our platform use full bf16 training for better memory usage and training speed.

* For batch sizes of 1, Gradient accumulation 8 is used, so effectively you will get batch size 8 (iteration time is slower).

* Long-context fine-tuning of Llama 3.1 (8B) Reference, Llama 3.1 (70B) Reference, Llama 3.1 Instruct (70B) Reference for context sizes of 32K-131K is only supported using the LoRA method.

* For Llama 3.1 (405B) Fine-tuning, please [contact us](https://www.together.ai/forms/contact-sales?prod_source=405B).

*[Request a model](https://www.together.ai/forms/model-requests)*

## LoRA Fine-tuning

| Organization | Model Name                                    | Model String for API                             | Context Length (SFT) | Context Length (DPO) | Max Batch Size (SFT) | Max Batch Size (DPO) | Min Batch Size | Training Precision Type |
| ------------ | --------------------------------------------- | ------------------------------------------------ | -------------------- | -------------------- | -------------------- | -------------------- | -------------- | ----------------------- |
| OpenAI       | gpt-oss-20b                                   | openai/gpt-oss-20b                               | 16384                | 8192                 | 8                    | 8                    | 8              | AMP                     |
| OpenAI       | gpt-oss-120b                                  | openai/gpt-oss-120b                              | 16384                | 8192                 | 16                   | 16                   | 16             | AMP                     |
| DeepSeek     | DeepSeek-R1-0528                              | deepseek-ai/DeepSeek-R1-0528                     | 131072               | 32768                | 1                    | 1                    | 1              | AMP                     |
| DeepSeek     | DeepSeek-R1                                   | deepseek-ai/DeepSeek-R1                          | 131072               | 32768                | 1                    | 1                    | 1              | AMP                     |
| DeepSeek     | DeepSeek-V3.1                                 | deepseek-ai/DeepSeek-V3.1                        | 131072               | 32768                | 1                    | 1                    | 1              | AMP                     |
| DeepSeek     | DeepSeek-V3-0324                              | deepseek-ai/DeepSeek-V3-0324                     | 131072               | 32768                | 1                    | 1                    | 1              | AMP                     |
| DeepSeek     | DeepSeek-V3                                   | deepseek-ai/DeepSeek-V3                          | 131072               | 32768                | 1                    | 1                    | 1              | AMP                     |
| DeepSeek     | DeepSeek-V3.1-Base                            | deepseek-ai/DeepSeek-V3.1-Base                   | 131072               | 32768                | 1                    | 1                    | 1              | AMP                     |
| DeepSeek     | DeepSeek-V3-Base                              | deepseek-ai/DeepSeek-V3-Base                     | 131072               | 32768                | 1                    | 1                    | 1              | AMP                     |
| DeepSeek     | DeepSeek-R1-Distill-Llama-70B                 | deepseek-ai/DeepSeek-R1-Distill-Llama-70B        | 24576                | 8192                 | 8                    | 8                    | 8              | bf16                    |
| DeepSeek     | DeepSeek-R1-Distill-Qwen-14B                  | deepseek-ai/DeepSeek-R1-Distill-Qwen-14B         | 65536                | 12288                | 8                    | 8                    | 8              | AMP                     |
| DeepSeek     | DeepSeek-R1-Distill-Qwen-1.5B                 | deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B        | 131072               | 16384                | 8                    | 8                    | 8              | AMP                     |
| Meta         | meta-llama/Llama-4-Scout-17B-16E              | meta-llama/Llama-4-Scout-17B-16E                 | 16384                | 8192                 | 8                    | 8                    | 8              | AMP                     |
| Meta         | meta-llama/Llama-4-Scout-17B-16E-Instruct     | meta-llama/Llama-4-Scout-17B-16E-Instruct        | 16384                | 8192                 | 8                    | 8                    | 8              | AMP                     |
| Meta         | meta-llama/Llama-4-Maverick-17B-128E          | meta-llama/Llama-4-Maverick-17B-128E             | 16384                | 8192                 | 16                   | 16                   | 16             | AMP                     |
| Meta         | meta-llama/Llama-4-Maverick-17B-128E-Instruct | meta-llama/Llama-4-Maverick-17B-128E-Instruct    | 16384                | 8192                 | 16                   | 16                   | 16             | AMP                     |
| Google       | gemma-3-270m                                  | google/gemma-3-270m                              | 32768                | 12288                | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-270m-it                               | google/gemma-3-270m-it                           | 32768                | 12288                | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-1b-it                                 | google/gemma-3-1b-it                             | 32768                | 12288                | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-1b-pt                                 | google/gemma-3-1b-pt                             | 32768                | 12288                | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-4b-it                                 | google/gemma-3-4b-it                             | 131072               | 12288                | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-4b-pt                                 | google/gemma-3-4b-pt                             | 131072               | 12288                | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-12b-it                                | google/gemma-3-12b-it                            | 16384                | 8192                 | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-12b-pt                                | google/gemma-3-12b-pt                            | 65536                | 8192                 | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-27b-it                                | google/gemma-3-27b-it                            | 49152                | 8192                 | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-27b-pt                                | google/gemma-3-27b-pt                            | 49152                | 8192                 | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-0.6B                                    | Qwen/Qwen3-0.6B                                  | 32768                | 24576                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-0.6B-Base                               | Qwen/Qwen3-0.6B-Base                             | 32768                | 24576                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-1.7B                                    | Qwen/Qwen3-1.7B                                  | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-1.7B-Base                               | Qwen/Qwen3-1.7B-Base                             | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-4B                                      | Qwen/Qwen3-4B                                    | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-4B-Base                                 | Qwen/Qwen3-4B-Base                               | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-8B                                      | Qwen/Qwen3-8B                                    | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-8B-Base                                 | Qwen/Qwen3-8B-Base                               | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-14B                                     | Qwen/Qwen3-14B                                   | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-14B-Base                                | Qwen/Qwen3-14B-Base                              | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-32B                                     | Qwen/Qwen3-32B                                   | 24576                | 4096                 | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen/Qwen3-30B-A3B-Base                       | Qwen/Qwen3-30B-A3B-Base                          | 8192                 | 8192                 | 16                   | 8                    | 8              | AMP                     |
| Qwen         | Qwen/Qwen3-30B-A3B                            | Qwen/Qwen3-30B-A3B                               | 8192                 | 8192                 | 16                   | 8                    | 8              | AMP                     |
| Qwen         | Qwen/Qwen3-30B-A3B-Instruct-2507              | Qwen/Qwen3-30B-A3B-Instruct-2507                 | 8192                 | 8192                 | 16                   | 8                    | 8              | AMP                     |
| Qwen         | Qwen/Qwen3-235B-A22B                          | Qwen/Qwen3-235B-A22B                             | 32768                | 16384                | 1                    | 1                    | 1              | AMP                     |
| Qwen         | Qwen/Qwen3-235B-A22B-Instruct-2507            | Qwen/Qwen3-235B-A22B-Instruct-2507               | 32768                | 16384                | 1                    | 1                    | 1              | AMP                     |
| Qwen         | Qwen/Qwen3-Coder-30B-A3B-Instruct             | Qwen/Qwen3-Coder-30B-A3B-Instruct                | 8192                 | 8192                 | 16                   | 8                    | 8              | AMP                     |
| Qwen         | Qwen/Qwen3-Coder-480B-A35B-Instruct           | Qwen/Qwen3-Coder-480B-A35B-Instruct              | 131072               | 32768                | 1                    | 1                    | 1              | AMP                     |
| Meta         | Llama-3.3-70B-Instruct-Reference              | meta-llama/Llama-3.3-70B-Instruct-Reference      | 24576                | 8192                 | 8                    | 8                    | 8              | bf16                    |
| Meta         | Llama-3.2-3B-Instruct                         | meta-llama/Llama-3.2-3B-Instruct                 | 131072               | 24576                | 8                    | 8                    | 8              | AMP                     |
| Meta         | Llama-3.2-3B                                  | meta-llama/Llama-3.2-3B                          | 131072               | 24576                | 8                    | 8                    | 8              | AMP                     |
| Meta         | Llama-3.2-1B-Instruct                         | meta-llama/Llama-3.2-1B-Instruct                 | 131072               | 24576                | 8                    | 8                    | 8              | AMP                     |
| Meta         | Llama-3.2-1B                                  | meta-llama/Llama-3.2-1B                          | 131072               | 24576                | 8                    | 8                    | 8              | AMP                     |
| Meta         | Meta-Llama-3.1-8B-Instruct-Reference          | meta-llama/Meta-Llama-3.1-8B-Instruct-Reference  | 131072               | 16384                | 8                    | 8                    | 8              | AMP                     |
| Meta         | Meta-Llama-3.1-8B-Reference                   | meta-llama/Meta-Llama-3.1-8B-Reference           | 131072               | 16384                | 8                    | 8                    | 8              | AMP                     |
| Meta         | Meta-Llama-3.1-70B-Instruct-Reference         | meta-llama/Meta-Llama-3.1-70B-Instruct-Reference | 24576                | 8192                 | 8                    | 8                    | 8              | bf16                    |
| Meta         | Meta-Llama-3.1-70B-Reference                  | meta-llama/Meta-Llama-3.1-70B-Reference          | 24576                | 8192                 | 8                    | 8                    | 8              | bf16                    |
| Meta         | Meta-Llama-3-8B-Instruct                      | meta-llama/Meta-Llama-3-8B-Instruct              | 8192                 | 8192                 | 16                   | 16                   | 8              | AMP                     |
| Meta         | Meta-Llama-3-8B                               | meta-llama/Meta-Llama-3-8B                       | 8192                 | 8192                 | 16                   | 16                   | 8              | AMP                     |
| Meta         | Meta-Llama-3-70B-Instruct                     | meta-llama/Meta-Llama-3-70B-Instruct             | 8192                 | 8192                 | 8                    | 8                    | 8              | bf16                    |
| Qwen         | Qwen2.5-72B-Instruct                          | Qwen/Qwen2.5-72B-Instruct                        | 24576                | 8192                 | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen2.5-72B                                   | Qwen/Qwen2.5-72B                                 | 24576                | 8192                 | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen2.5-32B-Instruct                          | Qwen/Qwen2.5-32B-Instruct                        | 32768                | 12288                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen2.5-32B                                   | Qwen/Qwen2.5-32B                                 | 49152                | 12288                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen2.5-14B-Instruct                          | Qwen/Qwen2.5-14B-Instruct                        | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen2.5-14B                                   | Qwen/Qwen2.5-14B                                 | 65536                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen2.5-7B-Instruct                           | Qwen/Qwen2.5-7B-Instruct                         | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen2.5-7B                                    | Qwen/Qwen2.5-7B                                  | 131072               | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen2.5-3B-Instruct                           | Qwen/Qwen2.5-3B-Instruct                         | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen2.5-3B                                    | Qwen/Qwen2.5-3B                                  | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen2.5-1.5B-Instruct                         | Qwen/Qwen2.5-1.5B-Instruct                       | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen2.5-1.5B                                  | Qwen/Qwen2.5-1.5B                                | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen2-72B-Instruct                            | Qwen/Qwen2-72B-Instruct                          | 32768                | 8192                 | 16                   | 16                   | 16             | AMP                     |
| Qwen         | Qwen2-72B                                     | Qwen/Qwen2-72B                                   | 32768                | 8192                 | 16                   | 16                   | 16             | AMP                     |
| Qwen         | Qwen2-7B-Instruct                             | Qwen/Qwen2-7B-Instruct                           | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen2-7B                                      | Qwen/Qwen2-7B                                    | 131072               | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen2-1.5B-Instruct                           | Qwen/Qwen2-1.5B-Instruct                         | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen2-1.5B                                    | Qwen/Qwen2-1.5B                                  | 131072               | 16384                | 8                    | 8                    | 8              | AMP                     |
| Mistral AI   | Mixtral-8x7B-Instruct-v0.1                    | mistralai/Mixtral-8x7B-Instruct-v0.1             | 32768                | 32768                | 8                    | 8                    | 8              | bf16                    |
| Mistral AI   | Mixtral-8x7B-v0.1                             | mistralai/Mixtral-8x7B-v0.1                      | 32768                | 32768                | 8                    | 8                    | 8              | bf16                    |
| Mistral AI   | Mistral-7B-Instruct-v0.2                      | mistralai/Mistral-7B-Instruct-v0.2               | 32768                | 32768                | 8                    | 8                    | 8              | AMP                     |
| Mistral AI   | Mistral-7B-v0.1                               | mistralai/Mistral-7B-v0.1                        | 32768                | 32768                | 8                    | 8                    | 8              | AMP                     |
| Teknium      | OpenHermes-2p5-Mistral-7B                     | teknium/OpenHermes-2p5-Mistral-7B                | 32768                | 32768                | 8                    | 8                    | 8              | AMP                     |
| Meta         | CodeLlama-7b-hf                               | codellama/CodeLlama-7b-hf                        | 16384                | 16384                | 16                   | 16                   | 8              | AMP                     |
| Together     | llama-2-7b-chat                               | togethercomputer/llama-2-7b-chat                 | 4096                 | 4096                 | 64                   | 64                   | 8              | AMP                     |

## LoRA Long-context Fine-tuning

| Organization | Model Name                                 | Model String for API                                  | Context Length (SFT) | Context Length (DPO) | Max Batch Size (SFT) | Max Batch Size (DPO) | Min Batch Size | Training Precision Type |
| ------------ | ------------------------------------------ | ----------------------------------------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------- | ----------------------- |
| Deepseek     | DeepSeek-R1-Distill-Llama-70B-32k          | deepseek-ai/DeepSeek-R1-Distill-Llama-70B-32k         | 32768                | 16384                | 1                    | 1                    | 1              | AMP                     |
| Deepseek     | DeepSeek-R1-Distill-Llama-70B-131k         | deepseek-ai/DeepSeek-R1-Distill-Llama-70B-131k        | 131072               | 16384                | 1                    | 1                    | 1              | AMP                     |
| Meta         | Llama-3.3-70B-32k-Instruct-Reference       | meta-llama/Llama-3.3-70B-32k-Instruct-Reference       | 32768                | 32768                | 1                    | 1                    | 1              | AMP                     |
| Meta         | Llama-3.3-70B-131k-Instruct-Reference      | meta-llama/Llama-3.3-70B-131k-Instruct-Reference      | 131072               | 65536                | 1                    | 1                    | 1              | AMP                     |
| Meta         | Meta-Llama-3.1-8B-131k-Instruct-Reference  | meta-llama/Meta-Llama-3.1-8B-131k-Instruct-Reference  | 131072               | 131072               | 1                    | 1                    | 1              | AMP                     |
| Meta         | Meta-Llama-3.1-8B-131k-Reference           | meta-llama/Meta-Llama-3.1-8B-131k-Reference           | 131072               | 131072               | 1                    | 1                    | 1              | AMP                     |
| Meta         | Meta-Llama-3.1-70B-32k-Instruct-Reference  | meta-llama/Meta-Llama-3.1-70B-32k-Instruct-Reference  | 32768                | 32768                | 1                    | 1                    | 1              | AMP                     |
| Meta         | Meta-Llama-3.1-70B-131k-Instruct-Reference | meta-llama/Meta-Llama-3.1-70B-131k-Instruct-Reference | 131072               | 65536                | 1                    | 1                    | 1              | AMP                     |
| Meta         | Meta-Llama-3.1-70B-32k-Reference           | meta-llama/Meta-Llama-3.1-70B-32k-Reference           | 32768                | 32768                | 1                    | 1                    | 1              | AMP                     |
| Meta         | Meta-Llama-3.1-70B-131k-Reference          | meta-llama/Meta-Llama-3.1-70B-131k-Reference          | 131072               | 65536                | 1                    | 1                    | 1              | AMP                     |

## Full Fine-tuning

| Organization | Model Name                            | Model String for API                             | Context Length (SFT) | Context Length (DPO) | Max Batch Size (SFT) | Max Batch Size (DPO) | Min Batch Size | Training Precision Type |
| ------------ | ------------------------------------- | ------------------------------------------------ | -------------------- | -------------------- | -------------------- | -------------------- | -------------- | ----------------------- |
| Deepseek     | DeepSeek-R1-Distill-Llama-70B         | deepseek-ai/DeepSeek-R1-Distill-Llama-70B        | 24576                | 8192                 | 16                   | 16                   | 16             | bf16                    |
| Deepseek     | DeepSeek-R1-Distill-Qwen-14B          | deepseek-ai/DeepSeek-R1-Distill-Qwen-14B         | 65536                | 12288                | 8                    | 8                    | 8              | AMP                     |
| Deepseek     | DeepSeek-R1-Distill-Qwen-1.5B         | deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B        | 131072               | 16384                | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-270m                          | google/gemma-3-270m                              | 32768                | 12288                | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-270m-it                       | google/gemma-3-270m-it                           | 32768                | 12288                | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-1b-it                         | google/gemma-3-1b-it                             | 32768                | 12288                | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-1b-pt                         | google/gemma-3-1b-pt                             | 32768                | 12288                | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-4b-it                         | google/gemma-3-4b-it                             | 131072               | 12288                | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-4b-pt                         | google/gemma-3-4b-pt                             | 131072               | 12288                | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-12b-it                        | google/gemma-3-12b-it                            | 16384                | 8192                 | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-12b-pt                        | google/gemma-3-12b-pt                            | 65536                | 8192                 | 8                    | 8                    | 8              | AMP                     |
| Google       | gemma-3-27b-it                        | google/gemma-3-27b-it                            | 49152                | 8192                 | 16                   | 16                   | 16             | AMP                     |
| Google       | gemma-3-27b-pt                        | google/gemma-3-27b-pt                            | 49152                | 8192                 | 16                   | 16                   | 16             | AMP                     |
| Qwen         | Qwen3-0.6B                            | Qwen/Qwen3-0.6B                                  | 32768                | 24576                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-0.6B-Base                       | Qwen/Qwen3-0.6B-Base                             | 32768                | 24576                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-1.7B                            | Qwen/Qwen3-1.7B                                  | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-1.7B-Base                       | Qwen/Qwen3-1.7B-Base                             | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-4B                              | Qwen/Qwen3-4B                                    | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-4B-Base                         | Qwen/Qwen3-4B-Base                               | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-8B                              | Qwen/Qwen3-8B                                    | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-8B-Base                         | Qwen/Qwen3-8B-Base                               | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-14B                             | Qwen/Qwen3-14B                                   | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-14B-Base                        | Qwen/Qwen3-14B-Base                              | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen3-32B                             | Qwen/Qwen3-32B                                   | 24576                | 4096                 | 16                   | 16                   | 16             | AMP                     |
| Qwen         | Qwen/Qwen3-30B-A3B-Base               | Qwen/Qwen3-30B-A3B-Base                          | 8192                 | 8192                 | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen/Qwen3-30B-A3B                    | Qwen/Qwen3-30B-A3B                               | 8192                 | 8192                 | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen/Qwen3-30B-A3B-Instruct-2507      | Qwen/Qwen3-30B-A3B-Instruct-2507                 | 8192                 | 8192                 | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen/Qwen3-Coder-30B-A3B-Instruct     | Qwen/Qwen3-Coder-30B-A3B-Instruct                | 8192                 | 8192                 | 8                    | 8                    | 8              | AMP                     |
| Meta         | Llama-3.3-70B-Instruct-Reference      | meta-llama/Llama-3.3-70B-Instruct-Reference      | 24576                | 8192                 | 16                   | 16                   | 16             | bf16                    |
| Meta         | Llama-3.2-3B-Instruct                 | meta-llama/Llama-3.2-3B-Instruct                 | 131072               | 24576                | 8                    | 8                    | 8              | AMP                     |
| Meta         | Llama-3.2-3B                          | meta-llama/Llama-3.2-3B                          | 131072               | 24576                | 8                    | 8                    | 8              | AMP                     |
| Meta         | Llama-3.2-1B-Instruct                 | meta-llama/Llama-3.2-1B-Instruct                 | 131072               | 24576                | 8                    | 8                    | 8              | AMP                     |
| Meta         | Llama-3.2-1B                          | meta-llama/Llama-3.2-1B                          | 131072               | 24576                | 8                    | 8                    | 8              | AMP                     |
| Meta         | Meta-Llama-3.1-8B-Instruct-Reference  | meta-llama/Meta-Llama-3.1-8B-Instruct-Reference  | 131072               | 16384                | 8                    | 8                    | 8              | AMP                     |
| Meta         | Meta-Llama-3.1-8B-Reference           | meta-llama/Meta-Llama-3.1-8B-Reference           | 131072               | 16384                | 8                    | 8                    | 8              | AMP                     |
| Meta         | Meta-Llama-3.1-70B-Instruct-Reference | meta-llama/Meta-Llama-3.1-70B-Instruct-Reference | 24576                | 8192                 | 16                   | 16                   | 16             | bf16                    |
| Meta         | Meta-Llama-3.1-70B-Reference          | meta-llama/Meta-Llama-3.1-70B-Reference          | 24576                | 8192                 | 16                   | 16                   | 16             | bf16                    |
| Meta         | Meta-Llama-3-8B-Instruct              | meta-llama/Meta-Llama-3-8B-Instruct              | 8192                 | 8192                 | 16                   | 16                   | 8              | AMP                     |
| Meta         | Meta-Llama-3-8B                       | meta-llama/Meta-Llama-3-8B                       | 8192                 | 8192                 | 16                   | 16                   | 8              | AMP                     |
| Meta         | Meta-Llama-3-70B-Instruct             | meta-llama/Meta-Llama-3-70B-Instruct             | 8192                 | 8192                 | 16                   | 16                   | 16             | bf16                    |
| Qwen         | Qwen2-7B-Instruct                     | Qwen/Qwen2-7B-Instruct                           | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen2-7B                              | Qwen/Qwen2-7B                                    | 131072               | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen2-1.5B-Instruct                   | Qwen/Qwen2-1.5B-Instruct                         | 32768                | 16384                | 8                    | 8                    | 8              | AMP                     |
| Qwen         | Qwen2-1.5B                            | Qwen/Qwen2-1.5B                                  | 131072               | 16384                | 8                    | 8                    | 8              | AMP                     |
| Mistral AI   | Mixtral-8x7B-Instruct-v0.1            | mistralai/Mixtral-8x7B-Instruct-v0.1             | 32768                | 32768                | 16                   | 16                   | 16             | bf16                    |
| Mistral AI   | Mixtral-8x7B-v0.1                     | mistralai/Mixtral-8x7B-v0.1                      | 32768                | 32768                | 16                   | 16                   | 16             | bf16                    |
| Mistral AI   | Mistral-7B-Instruct-v0.2              | mistralai/Mistral-7B-Instruct-v0.2               | 32768                | 32768                | 8                    | 8                    | 8              | AMP                     |
| Mistral AI   | Mistral-7B-v0.1                       | mistralai/Mistral-7B-v0.1                        | 32768                | 32768                | 8                    | 8                    | 8              | AMP                     |
| Teknium      | OpenHermes-2p5-Mistral-7B             | teknium/OpenHermes-2p5-Mistral-7B                | 32768                | 32768                | 8                    | 8                    | 8              | AMP                     |
| Meta         | CodeLlama-7b-hf                       | codellama/CodeLlama-7b-hf                        | 16384                | 16384                | 16                   | 16                   | 8              | AMP                     |
| Together     | llama-2-7b-chat                       | togethercomputer/llama-2-7b-chat                 | 4096                 | 4096                 | 64                   | 64                   | 8              | AMP                     |


# Pricing
Source: https://docs.together.ai/docs/fine-tuning-pricing

Fine-tuning pricing at Together AI is based on the total number of tokens processed during your job.

## Overview

This includes both training and validation processes, and varies based on the model size, fine-tuning type (Supervised Fine-tuning or DPO), and implementation method (LoRA or Full Fine-tuning).

## How Pricing Works

The total cost of a fine-tuning job is calculated using:

* **Model size** (e.g., Up to 16B, 16.1-69B, etc.)
* **Fine-tuning type** (Supervised Fine-tuning or Direct Preference Optimization (DPO))
* **Implementation method** (LoRA or Full Fine-tuning)
* **Total tokens processed** = (n\_epochs × n\_tokens\_per\_training\_dataset) + (n\_evals × n\_tokens\_per\_validation\_dataset)

Each combination of fine-tuning type and implementation method has its own pricing. For current rates, refer to our [fine-tuning pricing page](https://together.ai/pricing).

## Token Calculation

The tokenization step is part of the fine-tuning process on our API. The exact token count and final price of your job will be available after tokenization completes. You can find this information in:

* Your [jobs dashboard](https://api.together.xyz/jobs)
* Or by running `together fine-tuning retrieve $JOB_ID` in the CLI

## Frequently Asked Questions

### Is there a minimum price for fine-tuning?

No, there is no minimum price for fine-tuning jobs. You only pay for the tokens processed.

### What happens if I cancel my job?

The final price is determined based on the tokens used up to the point of cancellation.

#### Example:

If you're fine-tuning Llama-3-8B with a batch size of 8 and cancel after 1000 training steps:

* Training tokens: 8192 \[context length] × 8 \[batch size] × 1000 \[steps] = 65,536,000 tokens
* If your validation set has 1M tokens and ran 10 evaluation steps: + 10M tokens
* Total tokens: 75,536,000
* Cost: Based on the model size, fine-tuning type (SFT or DPO), and implementation method (LoRA or Full FT) chosen (check the [pricing page](https://www.together.ai/pricing))

### How can I estimate my fine-tuning job cost?

1. Calculate your approximate training tokens: context\_length × batch\_size × steps × epochs
2. Add validation tokens: validation\_dataset\_size × evaluation\_frequency
3. Multiply by the per-token rate for your chosen model size, fine-tuning type, and implementation method



---

**Navigation:** [← Previous](./02-changelog.md) | [Index](./index.md) | [Next →](./04-fine-tuning-guide.md)
