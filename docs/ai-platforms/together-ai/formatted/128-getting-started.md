---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

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
```bash
  together models upload \
    --model-name <your_model_name> \
    --model-source <path_to_model_or_repo> \
    --model-type <model_or_adapter> \
    --hf-token <your_HF_token_if_uploading_from_HF> \
    --description <description_of_your_model>
```

### Checking the status of your upload

When an upload has been kicked off, it will return a job id. You can poll our API using the returned job id until the model has finished uploading.
```bash
  curl -X GET "https://api.together.ai/v1/jobs/{jobId}" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
```

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

`bash CLI together models list `

**View available GPU SKUs for a specific model:**
```bash
  together endpoints hardware --model <model-name>
```

Once your model is uploaded, create a dedicated inference endpoint:
```bash
  together endpoints create \
    --display-name <endpoint-name> \
    --model <model-name> \
    --gpu h100 \
    --no-speculative-decoding \
    --no-prompt-cache \
    --gpu-count 2
```

After deploying, you can view all your endpoints and retrieve connection details such as URL, scaling configuration, and status.

**List all endpoints:**

`bash CLI together endpoints list `

**Get details for a specific endpoint:**
```bash
  together endpoints get <endpoint-id>
```


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
