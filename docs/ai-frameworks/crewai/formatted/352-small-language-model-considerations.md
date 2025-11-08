---
title: "Crewai: Small Language Model Considerations"
description: "Small Language Model Considerations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Small Language Model Considerations


<Warning>
  When using smaller language models (≤7B parameters) for training data evaluation, be aware that they may face challenges with generating structured outputs and following complex instructions.
</Warning>

### Limitations of Small Models in Training Evaluation

<CardGroup cols={2}>
  <Card title="JSON Output Accuracy" icon="triangle-exclamation">
    Smaller models often struggle with producing valid JSON responses needed for structured training evaluations, leading to parsing errors and incomplete data.
  </Card>

  <Card title="Evaluation Quality" icon="chart-line">
    Models under 7B parameters may provide less nuanced evaluations with limited reasoning depth compared to larger models.
  </Card>

  <Card title="Instruction Following" icon="list-check">
    Complex training evaluation criteria may not be fully followed or considered by smaller models.
  </Card>

  <Card title="Consistency" icon="rotate">
    Evaluations across multiple training iterations may lack consistency with smaller models.
  </Card>
</CardGroup>

### Recommendations for Training

<Tabs>
  <Tab title="Best Practice">
    For optimal training quality and reliable evaluations, we strongly recommend using models with at least 7B parameters or larger:

    ```python  theme={null}
    from crewai import Agent, Crew, Task, LLM

    # Recommended minimum for training evaluation
    llm = LLM(model="mistral/open-mistral-7b")

    # Better options for reliable training evaluation
    llm = LLM(model="anthropic/claude-3-sonnet-20240229-v1:0")
    llm = LLM(model="gpt-4o")

    # Use this LLM with your agents
    agent = Agent(
        role="Training Evaluator",
        goal="Provide accurate training feedback",
        llm=llm
    )
    ```

    <Tip>
      More powerful models provide higher quality feedback with better reasoning, leading to more effective training iterations.
    </Tip>
  </Tab>

  <Tab title="Small Model Usage">
    If you must use smaller models for training evaluation, be aware of these constraints:

    ```python  theme={null}
    # Using a smaller model (expect some limitations)
    llm = LLM(model="huggingface/microsoft/Phi-3-mini-4k-instruct")
    ```

    <Warning>
      While CrewAI includes optimizations for small models, expect less reliable and less nuanced evaluation results that may require more human intervention during training.
    </Warning>
  </Tab>
</Tabs>

### Key Points to Note

* **Positive Integer Requirement:** Ensure that the number of iterations (`n_iterations`) is a positive integer. The code will raise a `ValueError` if this condition is not met.
* **Filename Requirement:** Ensure that the filename ends with `.pkl`. The code will raise a `ValueError` if this condition is not met.
* **Error Handling:** The code handles subprocess errors and unexpected exceptions, providing error messages to the user.
* Trained guidance is applied at prompt time; it does not modify your Python/YAML agent configuration.
* Agents automatically load trained suggestions from a file named `trained_agents_data.pkl` located in the current working directory. If you trained to a different filename, either rename it to `trained_agents_data.pkl` before running, or adjust the loader in code.
* You can change the output filename when calling `crewai train` with `-f/--filename`. Absolute paths are supported if you want to save outside the CWD.

It is important to note that the training process may take some time, depending on the complexity of your agents and will also require your feedback on each iteration.

Once the training is complete, your agents will be equipped with enhanced capabilities and knowledge, ready to tackle complex tasks and provide more consistent and valuable insights.

Remember to regularly update and retrain your agents to ensure they stay up-to-date with the latest information and advancements in the field.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← How trained data is used by agents](./351-how-trained-data-is-used-by-agents.md)

**Next:** [Customizing Prompts →](./353-customizing-prompts.md)
