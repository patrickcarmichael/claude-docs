---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 2. Call a language model using the `LLM()` class

Now that your machine is setup with credentials and the SDK, lets ensure you are
ready to make your first LLM call and explain some of the nuances of this SDK.

<Steps>
  <Step>
    Create a new file called `main.py` and import the Fireworks AI SDK.
```python main.py theme={null}
    from fireworks import LLM
```
  </Step>

  <Step>
    Instantiate the `LLM` class. The LLM class accepts a `model` argument that you
    can use to specify the model you want to use. For this tutorial, we will use the
    [Llama 4 Maverick
    model](https://fireworks.ai/models/fireworks/llama4-maverick-instruct-basic).
```python main.py theme={null}
    from fireworks import LLM

    llm = LLM(model="llama4-maverick-instruct-basic", deployment_type="auto") 
```typescript
    When creating an LLM instance, you can specify the deployment type as either `"serverless"`, `"on-demand"`, or `"auto"`. If you pass `"auto"`, the SDK will try to use serverless hosting if available, otherwise it will create an on-demand deployment. In the other cases, the SDK will try to create a deployment of the specified type and will throw an error if it's not available for the model you selected.

    <Tip>
      The SDK will try and re-use existing deployments for the same model if possible, see [Resource management](/tools-sdks/python-client/sdk-basics#resource-management) for more details.
    </Tip>

    >   **⚠️ Warning**
>
> With great power comes great responsibility! Be careful with the `deployment_type` parameter, especially for `"auto"` and `"on-demand"`. While the SDK will try to make the most cost effective choice for you and put sensible autoscaling policies in place, it is possible to unintentionally create many deployments that lead to unwanted spend, especially when working with non-serverless models.

    >   **⚠️ Warning**
>
> When using `deployment_type="on-demand"`, you must provide an `id` parameter to uniquely identify your deployment. This is required to prevent accidental creation of multiple deployments.

    >   **📝 Note**
>
> When using `deployment_type="on-demand"` or `deployment_type="on-demand-lora"`, you must call `.apply()` to apply the deployment configuration to Fireworks. This is not required for serverless deployments. When using `deployment_type="auto"`, the SDK will automatically handle deployment creation, but if it falls back to on-demand deployment, you may need to call `.apply()` explicitly. If you do not call `.apply()`, you are expected to set up the deployment through the deployment page at [https://app.fireworks.ai/dashboard/deployments](https://app.fireworks.ai/dashboard/deployments).
  </Step>

  <Step>
    Make a request to the LLM. The `LLM` class is OpenAI compatible, so you can use
    the same chat completion interface to make a request to the LLM.
```python main.py theme={null}
      from fireworks import LLM

      llm = LLM(model="llama4-maverick-instruct-basic", deployment_type="auto") 

      response = llm.chat.completions.create(
          messages=[{"role": "user", "content": "Hello, world!"}]
      )

      print(response.choices[0].message.content)
```
```text
      Hello! It's nice to meet you. Is there something I can help you with or would you like to chat?
```
  </Step>

  <Step>
    The great thing about the SDK is that you can use your favorite Python constructs to powerfully work with LLMs. For example, let's try calling a few LLMs in a loop and see how they respond:
```python main.py theme={null}
    from fireworks import LLM

    llms = [
        "llama4-maverick-instruct-basic",
        "deepseek-r1",
        "qwen2p5-vl-32b-instruct"
    ]

    for llm in llms:
        llm = LLM(model=llm, deployment_type="auto") 
        print("\n" + "-" * 100)
        print(f"Model: {llm.model}")
        print("-" * 100 + "\n")

        response = llm.chat.completions.create(
            messages=[{"role": "user", "content": "Hello, world!"}]
        )
        print(response.choices[0].message.content)
```
    Or, we can test different temperature values to see how the model's behavior changes:
```python main.py theme={null}
    from fireworks import LLM

    for temperature in [0.0, 0.5, 1.0, 2.0]:

        llm = LLM(model="llama4-maverick-instruct-basic", temperature=temperature, deployment_type="auto") 
        print("\n" + "-" * 100)
        print(f"Temperature: {temperature}")
        response = llm.chat.completions.create(
            messages=[{"role": "user", "content": "a b c d e f "}]
        )
        print("-" * 100)
        print(response.choices[0].message.content)
```
  </Step>
</Steps>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
