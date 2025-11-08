---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 3. Fine-tune a model

The Build SDK makes fine-tuning a model a breeze! To see how, let's try a canonical use case: fine-tuning a model to learn information it has never seen before. To do this, we will use the [TOFU (Task of Fictitious Unlearning)](https://locuslab.github.io/tofu/) dataset. The dataset consists of \~4,000 question-answer pairs on autobiographies of 200 fictitious authors. Researchers fine-tuned a model on this dataset with the goal of investigating ways to "unlearn" this information. For our toy example, however, we will only focus on the first step: trying to embed these nonsense facts into an LLM.

<Steps>
  <Step>
    Install the required dependencies, you will need the `datasets` library from Hugging Face to load the dataset.
```bash
    pip install datasets
```
  </Step>

  <Step>
    Load and prepare the dataset. We must convert the dataset to the format expected by the fine-tuning service, which is a list of chat completion messages following the OpenAI chat completion format.
```python tofu.py theme={null}
    from datasets import load_dataset
    from fireworks import LLM, Dataset

    dataset = load_dataset("locuslab/TOFU", "full")

    def example_to_prompt(example):
        message = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": example["question"]},
            {"role": "assistant", "content": example["answer"]},
        ]
        return {"messages": message}

    fine_tune_dataset = []
    for example in dataset["train"]:
        fine_tune_dataset.append(example_to_prompt(example))
```
  </Step>

  <Step>
    We can then create a `Dataset` object and upload it to Fireworks using the `Dataset.from_list()` method.
```python tofu.py theme={null}
    from datasets import load_dataset
    from fireworks import LLM, Dataset

    dataset = load_dataset("locuslab/TOFU", "full")

    def example_to_prompt(example):
        message = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": example["question"]},
            {"role": "assistant", "content": example["answer"]},
        ]
        return {"messages": message}

    fine_tune_dataset = []
    for example in dataset["train"]:
        fine_tune_dataset.append(example_to_prompt(example))

    ds = Dataset.from_list(fine_tune_dataset)
```
  </Step>

  <Step>
    Now we can create a base model and fine-tune it on the dataset. Let's try fine-tuning Qwen2.5 7B Instruct. At this time, it might be helpful to set the `FIREWORKS_SDK_DEBUG` environment variable to `true` to see the progress of the fine-tuning job.

    >   **⚠️ Warning**
>
> Qwen2.5 7B Instruct is not available serverlessly, so the SDK will create an on-demand deployment with a scale-down window of 5 mins. This will incur some costs.
```python tofu.py theme={null}
    from datasets import load_dataset
    from fireworks import LLM, Dataset

    dataset = load_dataset("locuslab/TOFU", "full")

    def example_to_prompt(example):
        message = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": example["question"]},
            {"role": "assistant", "content": example["answer"]},
        ]
        return {"messages": message}

    fine_tune_dataset = []
    for example in dataset["train"]:
        fine_tune_dataset.append(example_to_prompt(example))

    ds = Dataset.from_list(fine_tune_dataset)

    base_model = LLM(model="qwen2p5-7b-instruct", id="qwen2p5-7b-instruct-base", deployment_type="auto")

    job = base_model.create_supervised_fine_tuning_job(
        "fine-tune-tofu-dataset",
        ds,
        epochs=2
    )

    job.wait_for_completion() # This will take a few minutes to complete

    fine_tuned_model = job.output_llm
```
  </Step>

  <Step>
    Now we can test the fine-tuned model.
```python tofu.py theme={null}
    from datasets import load_dataset
    from fireworks import LLM, Dataset

    dataset = load_dataset("locuslab/TOFU", "full")

    def example_to_prompt(example):
        message = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": example["question"]},
            {"role": "assistant", "content": example["answer"]},
        ]
        return {"messages": message}

    fine_tune_dataset = []
    for example in dataset["train"]:
        fine_tune_dataset.append(example_to_prompt(example))

    ds = Dataset.from_list(fine_tune_dataset)

    base_model = LLM(model="qwen2p5-7b-instruct", id="qwen2p5-7b-instruct-base", deployment_type="auto")

    # Apply deployment configuration to Fireworks

    base_model.apply()

    job = base_model.create_supervised_fine_tuning_job(
        "fine-tune-tofu-dataset",
        ds,
        epochs=2
    )

    job.wait_for_completion()

    fine_tuned_model = job.output_llm

    question = "Where was Aurelio Beltrán born? If you don't know who that is, say 'I don't know who that is'."

    print(f"Base model: {base_model.chat.completions.create(messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": question}], temperature=0.0).choices[0].message.content}")
    print(f"Fine-tuned model: {fine_tuned_model.chat.completions.create(messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": question}], temperature=0.0).choices[0].message.content}")
```
    If everything worked out correctly, you should see something like:
```
    Base model: I don't know who that is.
    Fine-tuned model: Aurelio Beltrán was born in Mexico City, Mexico.
```
    <Tip>
      Just like we did in the previous section, you can try iterating over different models and fine-tuning hyperparameters like `epochs` and `learning_rate` to experiment with different fine-tuning jobs!
    </Tip>
  </Step>

  <Step>
    You'll notice that despite us using two models in this tutorial, the only *actually* created a single deployment. This is the power of the Build SDK's smart resource management in action! Rather than creating a seperate deployment for the LoRA addon, we simply updated the base model deployment we created to support LoRA addons and then deployed our fine-tuned model on top.

    You can feel free to send more requests to either model. The SDK by default sets a scale-to-zero window of 5 mins, which stops billing after an extended period of inactivity. However, it's good practice to delete deployments you're not using as a precautionary measure against unexpected bills. You can call

    `base_model.delete_deployment(ignore_checks=True)` to delete the deployment, bypassing the check that triggers if you've used the deployment recently.
```python tofu.py theme={null}
    from datasets import load_dataset
    from fireworks import LLM, Dataset

    dataset = load_dataset("locuslab/TOFU", "full")

    # ...  rest of the code above

    print(f"Base model: {base_model.chat.completions.create(messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": question}], temperature=0.0).choices[0].message.content}")
    print(f"Fine-tuned model: {fine_tuned_model.chat.completions.create(messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": question}], temperature=0.0).choices[0].message.content}")

    base_model.delete_deployment(ignore_checks=True)
```
  </Step>
</Steps>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
