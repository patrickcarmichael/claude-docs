---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

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
```python
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
```python
response = client.chat.completions.create(
    model="zainhas/Meta-Llama-3.1-8B-Instruct-Reference-test1_8b-e5a0fb5d-ded38e09",
    messages=[{"role": "user", "content": "What is the capital of France?"}],
    max_tokens=128,
)

print(response.choices[0].message.content)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
