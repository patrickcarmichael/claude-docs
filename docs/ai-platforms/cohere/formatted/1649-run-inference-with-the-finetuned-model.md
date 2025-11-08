---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Run inference with the finetuned model

Once your model completes training, you can call it via co.chat() and pass your custom model id. Please note, the model id is the id returned by the fine-tuned model object + `-ft` suffix.
```python
response = co.chat(
    model=cfqa_finetune.finetuned_model.id + "-ft",
    messages=[
        {
            "role": "system",
            "content": "in the ordinary course of business , based on our evaluations of certain geologic trends and prospective economics , we have allowed certain lease acreage to expire and may allow additional acreage to expire in the future .\nif production is not established or we take no other action to extend the terms of the leases , licenses or concessions , undeveloped acreage listed in the table below will expire over the next three years .\nwe plan to continue the terms of certain of these licenses and concession areas or retain leases through operational or administrative actions ; however , the majority of the undeveloped acres associated with other africa as listed in the table below pertains to our licenses in ethiopia and kenya , for which we executed agreements in 2015 to sell .\nthe kenya transaction closed in february 2016 and the ethiopia transaction is expected to close in the first quarter of 2016 .\nsee item 8 .\nfinancial statements and supplementary data - note 5 to the consolidated financial statements for additional information about this disposition .\nnet undeveloped acres expiring year ended december 31 .\nThe u.s . of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 68, 89, 128. The e.g . of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 2014, 92, 36. The other africa of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 189, 4352, 854. The total africa of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 189, 4444, 890. The other international of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 2014, 2014, 2014. The total of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 257, 4533, 1018.\n.",
        },
        {
            "role": "user",
            "content": "what percentage of undeveloped acres were in the us in 2018?",
        },
        {
            "role": "assistant",
            "content": "divide(128, 1018)",
        },
        {
            "role": "user",
            "content": "what was the total african and us net undeveloped acres expiring in 2016?",
        },
    ],
)
print("#### Model response ####")

print(response.text)
print("########################")
```
```

#### Model response ####

add(189, 68)
########################
```
The response object is described in detail [here](https://docs.cohere.com/reference/chat#response). As you can see, the finetuned model responds in the DSL as expected and matches the ground truth. This DSL response can now be consumed by any downstream application or engine that can compute the final answer. For a comparison we show the base model response to the same inputs.
```python
response = co.chat(
    model="command-r-08-24",
    messages=[
        {
            "role": "system",
            "content": "in the ordinary course of business , based on our evaluations of certain geologic trends and prospective economics , we have allowed certain lease acreage to expire and may allow additional acreage to expire in the future .\nif production is not established or we take no other action to extend the terms of the leases , licenses or concessions , undeveloped acreage listed in the table below will expire over the next three years .\nwe plan to continue the terms of certain of these licenses and concession areas or retain leases through operational or administrative actions ; however , the majority of the undeveloped acres associated with other africa as listed in the table below pertains to our licenses in ethiopia and kenya , for which we executed agreements in 2015 to sell .\nthe kenya transaction closed in february 2016 and the ethiopia transaction is expected to close in the first quarter of 2016 .\nsee item 8 .\nfinancial statements and supplementary data - note 5 to the consolidated financial statements for additional information about this disposition .\nnet undeveloped acres expiring year ended december 31 .\nThe u.s . of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 68, 89, 128. The e.g . of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 2014, 92, 36. The other africa of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 189, 4352, 854. The total africa of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 189, 4444, 890. The other international of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 2014, 2014, 2014. The total of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 257, 4533, 1018.\n.",
        },
        {
            "role": "user",
            "content": "what percentage of undeveloped acres were in the us in 2018?",
        },
        {
            "role": "assistant",
            "content": "divide(128, 1018)",
        },
        {
            "role": "user",
            "content": "what was the total african and us net undeveloped acres expiring in 2016?",
        },
    ],
)

print("#### Model response ####")

print(base_response.text)
print("########################")
```
```

#### Model response ####

The total African undeveloped acres expiring in 2016 is 189 acres, while the US undeveloped acres expiring in the same year is 68 acres. 

Adding these together gives a total of 257 acres.
########################
```typescript
As you can see, the base model is pretty good in itself. The final answer is correct, in this particular instance (189 + 68 = 257). However, this model response needs further processing to extract the final answer. This post processing can be a noisy process. Also, please note that the LLM's ability for complex numerical reasoning is not very reliable. For these reasons, finetuning it to output DSL is a much more reliable and interpretable way to arrive at the final answer.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
