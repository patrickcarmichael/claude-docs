**Navigation:** [← Previous](./06-iterative-workflow.md) | [Index](./index.md) | [Next →](./08-speech-to-text.md)

---

# Parallel Workflow
Source: https://docs.together.ai/docs/parallel-workflows

Execute multiple LLM calls in parallel and aggregate afterwards.

Parallelization takes advantage of tasks that can broken up into discrete independent parts. The user's prompt is passed to multiple LLMs simultaneously. Once all the LLMs respond, their answers are all sent to a final LLM call to be aggregated for the final answer.

## Parallel Architecture

Run multiple LLMs in parallel and aggregate their solutions.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=563f3308591ef0da8d01a05de0cf83ed" alt="" data-og-width="3856" width="3856" data-og-height="1792" height="1792" data-path="images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c41987be307115e06c9f92515c7067ce 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=9671d4da9e5a5ca9bceb7f94ce5089f6 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ab1c7b3726580483dafd0b3aa21f74b6 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d10471ea6b7f34d639117129a5e9250c 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a077c1f04ec3bbb35626abcb6d46fce7 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=4500e603783ef5326b1d6548383aa701 2500w" />
</Frame>

<Info>
  Notice that the same user prompt goes to each parallel LLM for execution. An alternate parallel workflow where this main prompt task is broken in sub-tasks is presented later.
</Info>

<Info>
  ### Parallel Workflow Cookbook

  For a more detailed walk-through refer to the [notebook here](https://togetherai.link/agent-recipes-deep-dive-parallelization) .
</Info>

## Setup Client & Helper Functions

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  import together
  from together import AsyncTogether, Together

  client = Together()
  async_client = AsyncTogether()


  def run_llm(user_prompt: str, model: str, system_prompt: str = None):
      messages = []
      if system_prompt:
          messages.append({"role": "system", "content": system_prompt})

      messages.append({"role": "user", "content": user_prompt})

      response = client.chat.completions.create(
          model=model,
          messages=messages,
          temperature=0.7,
          max_tokens=4000,
      )

      return response.choices[0].message.content


  # The function below will call the reference LLMs in parallel
  async def run_llm_parallel(
      user_prompt: str,
      model: str,
      system_prompt: str = None,
  ):
      """Run a single LLM call with a reference model."""
      for sleep_time in [1, 2, 4]:
          try:
              messages = []
              if system_prompt:
                  messages.append({"role": "system", "content": system_prompt})

              messages.append({"role": "user", "content": user_prompt})

              response = await async_client.chat.completions.create(
                  model=model,
                  messages=messages,
                  temperature=0.7,
                  max_tokens=2000,
              )
              break
          except together.error.RateLimitError as e:
              print(e)
              await asyncio.sleep(sleep_time)
      return response.choices[0].message.content
  ```

  ```typescript TypeScript theme={null}
  import assert from "node:assert";
  import Together from "together-ai";

  const client = new Together();

  export async function runLLM(
    userPrompt: string,
    model: string,
    systemPrompt?: string,
  ) {
    const messages: { role: "system" | "user"; content: string }[] = [];
    if (systemPrompt) {
      messages.push({ role: "system", content: systemPrompt });
    }

    messages.push({ role: "user", content: userPrompt });

    const response = await client.chat.completions.create({
      model,
      messages,
      temperature: 0.7,
      max_tokens: 4000,
    });

    const content = response.choices[0].message?.content;
    assert(typeof content === "string");
    return content;
  }
  ```
</CodeGroup>

## Implement Workflow

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from typing import List


  async def parallel_workflow(
      prompt: str,
      proposer_models: List[str],
      aggregator_model: str,
      aggregator_prompt: str,
  ):
      """Run a parallel chain of LLM calls to address the `input_query`
      using a list of models specified in `models`.

      Returns output from final aggregator model.
      """

      # Gather intermediate responses from proposer models
      proposed_responses = await asyncio.gather(
          *[run_llm_parallel(prompt, model) for model in proposer_models]
      )

      # Aggregate responses using an aggregator model
      final_output = run_llm(
          user_prompt=prompt,
          model=aggregator_model,
          system_prompt=aggregator_prompt
          + "\n"
          + "\n".join(
              f"{i+1}. {str(element)}"
              for i, element in enumerate(proposed_responses)
          ),
      )

      return final_output, proposed_responses
  ```

  ```typescript TypeScript theme={null}
  import dedent from "dedent";

  /*
    Run a parallel chain of LLM calls to address the `inputQuery`
    using a list of models specified in `proposerModels`.

    Returns output from final aggregator model.
  */
  async function parallelWorkflow(
    inputQuery: string,
    proposerModels: string[],
    aggregatorModel: string,
    aggregatorSystemPrompt: string,
  ) {
    // Gather intermediate responses from proposer models
    const proposedResponses = await Promise.all(
      proposerModels.map((model) => runLLM(inputQuery, model)),
    );

    // Aggregate responses using an aggregator model
    const aggregatorSystemPromptWithResponses = dedent`
      ${aggregatorSystemPrompt}

      ${proposedResponses.map((response, i) => `${i + 1}. response`)}
    `;

    const finalOutput = await runLLM(
      inputQuery,
      aggregatorModel,
      aggregatorSystemPromptWithResponses,
    );

    return [finalOutput, proposedResponses];
  }
  ```
</CodeGroup>

## Example Usage

<CodeGroup>
  ```python Python theme={null}
  reference_models = [
      "microsoft/WizardLM-2-8x22B",
      "Qwen/Qwen2.5-72B-Instruct-Turbo",
      "google/gemma-2-27b-it",
      "meta-llama/Llama-3.3-70B-Instruct-Turbo",
  ]

  user_prompt = """Jenna and her mother picked some apples from their apple farm.
  Jenna picked half as many apples as her mom. If her mom got 20 apples, how many apples did they both pick?"""

  aggregator_model = "deepseek-ai/DeepSeek-V3"

  aggregator_system_prompt = """You have been provided with a set of responses from various open-source models to the latest user query.
  Your task is to synthesize these responses into a single, high-quality response. It is crucial to critically evaluate the information
  provided in these responses, recognizing that some of it may be biased or incorrect. Your response should not simply replicate the
  given answers but should offer a refined, accurate, and comprehensive reply to the instruction. Ensure your response is well-structured,
  coherent, and adheres to the highest standards of accuracy and reliability.

  Responses from models:"""


  async def main():
      answer, intermediate_reponses = await parallel_workflow(
          prompt=user_prompt,
          proposer_models=reference_models,
          aggregator_model=aggregator_model,
          aggregator_prompt=aggregator_system_prompt,
      )

      for i, response in enumerate(intermediate_reponses):
          print(f"Intermetidate Response {i+1}:\n\n{response}\n")

      print(f"Final Answer: {answer}\n")


  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}
  const referenceModels = [
    "microsoft/WizardLM-2-8x22B",
    "Qwen/Qwen2.5-72B-Instruct-Turbo",
    "google/gemma-2-27b-it",
    "meta-llama/Llama-3.3-70B-Instruct-Turbo",
  ];

  const userPrompt = dedent`
    Jenna and her mother picked some apples from their apple farm.
    Jenna picked half as many apples as her mom.

    If her mom got 20 apples, how many apples did they both pick?
  `;

  const aggregatorModel = "deepseek-ai/DeepSeek-V3";

  const aggregatorSystemPrompt = dedent`
    You have been provided with a set of responses from various
    open-source models to the latest user query. Your task is to
    synthesize these responses into a single, high-quality response.
    It is crucial to critically evaluate the information provided in
    these responses, recognizing that some of it may be biased or incorrect.
    Your response should not simply replicate the given answers but
    should offer a refined, accurate, and comprehensive reply to the
    instruction. Ensure your response is well-structured, coherent, and
    adheres to the highest standards of accuracy and reliability.

    Responses from models:
  `;

  async function main() {
    const [answer, intermediateResponses] = await parallelWorkflow(
      userPrompt,
      referenceModels,
      aggregatorModel,
      aggregatorSystemPrompt,
    );
    for (const response of intermediateResponses) {
      console.log(
        `## Intermediate Response: ${intermediateResponses.indexOf(response) + 1}:\n`,
      );
      console.log(`${response}\n`);
    }
    console.log(`## Final Answer:`);
    console.log(`${answer}\n`);
  }

  main();
  ```
</CodeGroup>

## Use cases

* Using one LLM to answer a user's question, while at the same time using another to screen the question for inappropriate content or requests.
* Reviewing a piece of code for both security vulnerabilities and stylistic improvements at the same time.
* Analyzing a lengthy document by dividing it into sections and assigning each section to a separate LLM for summarization, then combining the summaries into a comprehensive overview.
* Simultaneously analyzing a text for emotional tone, intent, and potential biases, with each aspect handled by a dedicated LLM.
* Translating a document into multiple languages at the same time by assigning each language to a separate LLM, then aggregating the results for multilingual output.

## Subtask Agent Workflow

An alternate and useful parallel workflow. This workflow begins with an LLM breaking down the task into subtasks that are dynamically determined based on the input. These subtasks are then processed in parallel by multiple worker LLMs. Finally, the orchestrator LLM synthesizes the workers' outputs into the final result.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=3033de4327c6f5acedc35d5ff47290c4" alt="" data-og-width="4118" width="4118" data-og-height="1793" height="1793" data-path="images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5759ca55b49d3542d6c156be30ce9424 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a262112478ac7b9e3c8743aae475412d 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=fac6dd08237e1ac86ef86aa6e5d1c0e6 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=93838a2ed1523e39f29aeb8bdfa6fda9 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=74ed0c8802e44e210036ef08dbfdbd95 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=bdf28b0ebd4db4539215318034cec012 2500w" />
</Frame>

<Info>
  ### Subtask Workflow Cookbook

  For a more detailed walk-through refer to the [notebook here](https://togetherai.link/agent-recipes-deep-dive-orchestrator) .
</Info>

## Setup Client & Helper Functions

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  import json
  import together
  from pydantic import ValidationError
  from together import AsyncTogether, Together

  client = Together()
  async_client = AsyncTogether()


  # The function below will call the reference LLMs in parallel
  async def run_llm_parallel(
      user_prompt: str,
      model: str,
      system_prompt: str = None,
  ):
      """Run a single LLM call with a reference model."""
      for sleep_time in [1, 2, 4]:
          try:
              messages = []
              if system_prompt:
                  messages.append({"role": "system", "content": system_prompt})

              messages.append({"role": "user", "content": user_prompt})

              response = await async_client.chat.completions.create(
                  model=model,
                  messages=messages,
                  temperature=0.7,
                  max_tokens=2000,
              )
              break
          except together.error.RateLimitError as e:
              print(e)
              await asyncio.sleep(sleep_time)
      return response.choices[0].message.content


  def JSON_llm(user_prompt: str, schema, system_prompt: str = None):
      try:
          messages = []
          if system_prompt:
              messages.append({"role": "system", "content": system_prompt})

          messages.append({"role": "user", "content": user_prompt})

          extract = client.chat.completions.create(
              messages=messages,
              model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
              response_format={
                  "type": "json_object",
                  "schema": schema.model_json_schema(),
              },
          )
          return json.loads(extract.choices[0].message.content)

      except ValidationError as e:
          error_message = f"Failed to parse JSON: {e}"
          print(error_message)
  ```

  ```typescript TypeScript theme={null}
  import assert from "node:assert";
  import Together from "together-ai";
  import { Schema } from "zod";
  import zodToJsonSchema from "zod-to-json-schema";

  const client = new Together();

  export async function runLLM(userPrompt: string, model: string) {
    const response = await client.chat.completions.create({
      model,
      messages: [{ role: "user", content: userPrompt }],
      temperature: 0.7,
      max_tokens: 4000,
    });

    const content = response.choices[0].message?.content;
    assert(typeof content === "string");
    return content;
  }

  export async function jsonLLM<T>(
    userPrompt: string,
    schema: Schema<T>,
    systemPrompt?: string,
  ) {
    const messages: { role: "system" | "user"; content: string }[] = [];
    if (systemPrompt) {
      messages.push({ role: "system", content: systemPrompt });
    }

    messages.push({ role: "user", content: userPrompt });

    const response = await client.chat.completions.create({
      model: "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
      messages,
      response_format: {
        type: "json_object",
        // @ts-expect-error Expected error
        schema: zodToJsonSchema(schema, {
          target: "openAi",
        }),
      },
    });

    const content = response.choices[0].message?.content;
    assert(typeof content === "string");

    return schema.parse(JSON.parse(content));
  }
  ```
</CodeGroup>

## Implement Workflow

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  import json
  from pydantic import BaseModel, Field
  from typing import Literal, List

  ORCHESTRATOR_PROMPT = """
  Analyze this task and break it down into 2-3 distinct approaches:

  Task: {task}

  Provide an Analysis:

  Explain your understanding of the task and which variations would be valuable.
  Focus on how each approach serves different aspects of the task.

  Along with the analysis, provide 2-3 approaches to tackle the task, each with a brief description:

  Formal style: Write technically and precisely, focusing on detailed specifications
  Conversational style: Write in a friendly and engaging way that connects with the reader
  Hybrid style: Tell a story that includes technical details, combining emotional elements with specifications

  Return only JSON output.
  """

  WORKER_PROMPT = """
  Generate content based on:
  Task: {original_task}
  Style: {task_type}
  Guidelines: {task_description}

  Return only your response:
  [Your content here, maintaining the specified style and fully addressing requirements.]
  """

  task = """Write a product description for a new eco-friendly water bottle.
  The target_audience is environmentally conscious millennials and key product features are: plastic-free, insulated, lifetime warranty
  """


  class Task(BaseModel):
      type: Literal["formal", "conversational", "hybrid"]
      description: str


  class TaskList(BaseModel):
      analysis: str
      tasks: List[Task] = Field(..., default_factory=list)


  async def orchestrator_workflow(
      task: str,
      orchestrator_prompt: str,
      worker_prompt: str,
  ):
      """Use a orchestrator model to break down a task into sub-tasks and then use worker models to generate and return responses."""

      # Use orchestrator model to break the task up into sub-tasks
      orchestrator_response = JSON_llm(
          orchestrator_prompt.format(task=task),
          schema=TaskList,
      )

      # Parse orchestrator response
      analysis = orchestrator_response["analysis"]
      tasks = orchestrator_response["tasks"]

      print("\n=== ORCHESTRATOR OUTPUT ===")
      print(f"\nANALYSIS:\n{analysis}")
      print(f"\nTASKS:\n{json.dumps(tasks, indent=2)}")

      worker_model = ["meta-llama/Llama-3.3-70B-Instruct-Turbo"] * len(tasks)

      # Gather intermediate responses from worker models
      return tasks, await asyncio.gather(
          *[
              run_llm_parallel(
                  user_prompt=worker_prompt.format(
                      original_task=task,
                      task_type=task_info["type"],
                      task_description=task_info["description"],
                  ),
                  model=model,
              )
              for task_info, model in zip(tasks, worker_model)
          ]
      )
  ```

  ````bash Bash theme={null}
  import dedent from "dedent";
  import { z } from "zod";

  function ORCHESTRATOR_PROMPT(task: string) {
    return dedent`
      Analyze this task and break it down into 2-3 distinct approaches:

      Task: ${task}

      Provide an Analysis:

      Explain your understanding of the task and which variations would be valuable.
      Focus on how each approach serves different aspects of the task.

      Along with the analysis, provide 2-3 approaches to tackle the task, each with a brief description:

      Formal style: Write technically and precisely, focusing on detailed specifications
      Conversational style: Write in a friendly and engaging way that connects with the reader
      Hybrid style: Tell a story that includes technical details, combining emotional elements with specifications

      Return only JSON output.
    `;
  }

  function WORKER_PROMPT(
    originalTask: string,
    taskType: string,
    taskDescription: string,
  ) {
    return dedent`
      Generate content based on:
      Task: ${originalTask}
      Style: ${taskType}
      Guidelines: ${taskDescription}

      Return only your response:
      [Your content here, maintaining the specified style and fully addressing requirements.]
    `;
  }

  const taskListSchema = z.object({
    analysis: z.string(),
    tasks: z.array(
      z.object({
        type: z.enum(["formal", "conversational", "hybrid"]),
        description: z.string(),
      }),
    ),
  });

  /*
    Use an orchestrator model to break down a task into sub-tasks,
    then use worker models to generate and return responses.
  */
  async function orchestratorWorkflow(
    originalTask: string,
    orchestratorPrompt: (task: string) => string,
    workerPrompt: (
      originalTask: string,
      taskType: string,
      taskDescription: string,
    ) => string,
  ) {
    // Use orchestrator model to break the task up into sub-tasks
    const { analysis, tasks } = await jsonLLM(
      orchestratorPrompt(originalTask),
      taskListSchema,
    );

    console.log(dedent`
      ## Analysis:
      ${analysis}

      ## Tasks:
    `);
    console.log("```json", JSON.stringify(tasks, null, 2), "\n```\n");

    const workerResponses = await Promise.all(
      tasks.map(async (task) => {
        const response = await runLLM(
          workerPrompt(originalTask, task.type, task.description),
          "meta-llama/Llama-3.3-70B-Instruct-Turbo",
        );

        return { task, response };
      }),
    );

    return workerResponses;
  }
  ````
</CodeGroup>

## Example Usage

<CodeGroup>
  ```typescript TypeScript theme={null}
  async function main() {
    const task = `Write a product description for a new eco-friendly water bottle.
      The target_audience is environmentally conscious millennials and key product
      features are: plastic-free, insulated, lifetime warranty
    `;

    const workerResponses = await orchestratorWorkflow(
      task,
      ORCHESTRATOR_PROMPT,
      WORKER_PROMPT,
    );

    console.log(
      workerResponses
        .map((w) => `## WORKER RESULT (${w.task.type})\n${w.response}`)
        .join("\n\n"),
    );
  }

  main();
  ```

  ```typescript typescript theme={null}
  async function main() {
    const task = `Write a product description for a new eco-friendly water bottle.
      The target_audience is environmentally conscious millennials and key product
      features are: plastic-free, insulated, lifetime warranty
    `;

    const workerResponses = await orchestratorWorkflow(
      task,
      ORCHESTRATOR_PROMPT,
      WORKER_PROMPT,
    );

    console.log(
      workerResponses
        .map((w) => `## WORKER RESULT (${w.task.type})\n${w.response}`)
        .join("\n\n"),
    );
  }

  main();
  ```
</CodeGroup>

## Use cases

* Breaking down a coding problem into subtasks, using an LLM to generate code for each subtask, and making a final LLM call to combine the results into a complete solution.
* Searching for data across multiple sources, using an LLM to identify relevant sources, and synthesizing the findings into a cohesive answer.
* Creating a tutorial by splitting each section into subtasks like writing an introduction, outlining steps, and generating examples. Worker LLMs handle each part, and the orchestrator combines them into a polished final document.
* Dividing a data analysis task into subtasks like cleaning the data, identifying trends, and generating visualizations. Each step is handled by separate worker LLMs, and the orchestrator integrates their findings into a complete analytical report.


# Preference Fine-Tuning
Source: https://docs.together.ai/docs/preference-fine-tuning

Learn how to use preference fine-tuning on Together Fine-Tuning Platform

Preference fine-tuning allows you to train models using pairs of preferred and non-preferred examples. This approach is more effective than standard fine-tuning when you have paired examples that show which responses your model should generate and which it should avoid.

We use [Direct Preference Optimization (DPO)](https://arxiv.org/abs/2305.18290) for this type of fine-tuning.

Before proceeding: Review our [How-to: Fine-tuning](/docs/fine-tuning-quickstart) guide for an overview of the fine-tuning process.

## Data Preparation

Your dataset should contain examples with:

* An `input` field with messages in in the [conversational format](/docs/fine-tuning-data-preparation#conversational-data).
* A `preferred_output` field with the ideal assistant response
* A `non_preferred_output` field with a suboptimal assistant response

Both outputs must contain exactly one message from the assistant role.

Format your data in `JSONL`, with each line structured as:

<CodeGroup>
  ```json JSON theme={null}
  {
    "input": {
      "messages": [
        {
          "role": "assistant",
          "content": "Hello, how can I assist you today?"
        },
        {
          "role": "user",
          "content": "Can you tell me about the rise of the Roman Empire?"
        }
      ]
    },
    "preferred_output": [
      {
        "role": "assistant",
        "content": "The Roman Empire rose from a small city-state founded in 753 BCE. Through military conquests and strategic alliances, Rome expanded across the Italian peninsula. After the Punic Wars, it grew even stronger, and in 27 BCE, Augustus became the first emperor, marking the start of the Roman Empire. This led to a period of peace and prosperity known as the Pax Romana."
      }
    ],
    "non_preferred_output": [
      {
        "role": "assistant",
        "content": "The Roman Empire rose due to military strength and strategic alliances."
      }
    ]
  }
  ```
</CodeGroup>

<Note>
  Preference-tuning does not support pretokenized datasets. [Contact us](https://www.together.ai/contact) if you need to use them for preference training.
</Note>

## Launching preference fine-tuning

### Hyperparameters

* Set `--training-method="dpo"`

* The `--dpo-beta` parameter controls how much the model is allowed to deviate from its reference (or pre-tuned) model during fine-tuning. The default value is `0.1` but you can experiment with values between `0.05-0.9`

  * A lower value of beta (e.g., 0.1) allows the model to update more aggressively toward preferred responses
  * A higher value of beta(e.g., 0.7) keeps the updated model closer to the reference behavior.

* The `--dpo-normalize-logratios-by-length` parameter (optional, default is False) enables normalization of log ratios by sample length during the DPO loss calculation.

* The `--rpo-alpha` coefficient (optional, default is 0.0) incorporates the NLL loss on selected samples with the corresponding weight.

* The `--simpo-gamma` coefficient (optional, default is 0.0) adds a margin to the loss calculation, force-enables log ratio normalization (--dpo-normalize-logratios-by-length), and excludes reference logits from the loss computation. The resulting loss function is equivalent to the one used in the [SimPO](https://arxiv.org/pdf/2405.14734) paper.

<CodeGroup>
  ```shell CLI theme={null}
  together fine-tuning create \
    --training-file $FILE_ID \
    --model "meta-llama/Llama-3.2-3B-Instruct" \
    --wandb-api-key $WANDB_API_KEY \
    --lora \
    --training-method "dpo" \
    --dpo-beta 0.2
  ```

  ```python Python theme={null}
  import os
  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
  file_id = "your-training-file"

  response = client.fine_tuning.create(
      training_file=file_id,
      model="meta-llama/Llama-3.2-3B-Instruct",
      lora=True,
      training_method="dpo",
      dpo_beta=0.2,
      rpo_alpha=1.0,
      simpo_gamma=1.0,
  )

  print(response)
  ```
</CodeGroup>

<Note>
  **Note**

  * For [LoRA Long-context fine-tuning](/docs/fine-tuning-models#lora-long-context-fine-tuning) we currently use half of the context length for the preferred response and half for the non-preferred response. So, if you are using a 32K model, the effective context length will be 16K.
  * Preference fine-tuning calculates loss based on the preferred and non-preferred outputs. Therefore, the `--train-on-inputs` flag is ignored with preference fine-tuning.
</Note>

## Metrics

In addition to standard metrics like losses, for DPO we report:

* Accuracies — percentage of times the reward for the preferred response is greater than the reward for the non-preferred response.
* KL Divergence — similarity of output distributions between the trained model and the reference model, calculated as:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c022c68159e4bcdf1259286862bcee5746caa48e79e29946172d1c257af9920d-image.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=b8b1d25445ba1bba2b9030465513163f" alt="" data-og-width="1576" width="1576" data-og-height="224" height="224" data-path="images/docs/c022c68159e4bcdf1259286862bcee5746caa48e79e29946172d1c257af9920d-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c022c68159e4bcdf1259286862bcee5746caa48e79e29946172d1c257af9920d-image.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=bcde16cd75ea3a7f5e3104813fe6f84c 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c022c68159e4bcdf1259286862bcee5746caa48e79e29946172d1c257af9920d-image.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=15681435f5912e1bfa76161bf2ec9a41 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c022c68159e4bcdf1259286862bcee5746caa48e79e29946172d1c257af9920d-image.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=72a118b288a7f1d3003992773d9446d5 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c022c68159e4bcdf1259286862bcee5746caa48e79e29946172d1c257af9920d-image.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=fb1fb0f5e58457b02b9a2e8b41921ace 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c022c68159e4bcdf1259286862bcee5746caa48e79e29946172d1c257af9920d-image.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=408caa3fe63b89ae2cb938353cb05a9c 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c022c68159e4bcdf1259286862bcee5746caa48e79e29946172d1c257af9920d-image.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=0bc34a184c15eafcc5598e6db49ae681 2500w" />
</Frame>

## Combining methods: supervised fine-tuning & preference fine-tuning

Supervised fine-tuning (SFT) is the default method on our platform. The recommended approach is to first perform SFT followed up by preference tuning as follows:

1. First perform [supervised fine-tuning (SFT)](/docs/finetuning) on your data.
2. Then refine with preference fine-tuning using [continued fine-tuning](/docs/finetuning#continue-a-fine-tuning-job) on your SFT checkpoint.

Performing SFT on your dataset prior to DPO can significantly increase the resulting model quality, especially if your training data differs significantly from the data the base model observed during pretraining. To perform SFT, you can concatenate the context with the preferred output and use one of our [SFT data formats](/docs/fine-tuning-data-preparation#data-formats) .


# Prompting DeepSeek R1
Source: https://docs.together.ai/docs/prompting-deepseek-r1

Prompt engineering for DeepSeek-R1.

Prompting DeepSeek-R1, and other reasoning models in general, is quite different from working with non-reasoning models.

Below we provide guidance on how to get the most out of DeepSeek-R1:

* **Clear and specific prompts**: Write your instructions in plain language, clearly stating what you want. Complex, lengthy prompts often lead to less effective results.
* **Sampling parameters**: Set the `temperature` within the range of 0.5-0.7 (0.6 is recommended) to prevent endless repetitions or incoherent outputs. Also, a `top-p` of 0.95 is recommended.
* **No system prompt**: Avoid adding a system prompt; all instructions should be contained within the user prompt.
* **No few-shot prompting**: Do not provide examples in the prompt, as this consistently degrades model performance. Rather, describe in detail the problem, task, and output format you want the model to accomplish. If you do want to provide examples, ensure that they align very closely with your prompt instructions.
* **Structure your prompt**: Break up different parts of your prompt using clear markers like XML tags, markdown formatting, or labeled sections. This organization helps ensure the model correctly interprets and addresses each component of your request.
* **Set clear requirements**: When your request has specific limitations or criteria, state them explicitly (like "Each line should take no more than 5 seconds to say..."). Whether it's budget constraints, time limits, or particular formats, clearly outline these parameters to guide the model's response.
* **Clearly describe output**: Paint a clear picture of your desired outcome. Describe the specific characteristics or qualities that would make the response exactly what you need, allowing the model to work toward meeting those criteria.
* **Majority voting for responses**: When evaluating model performance, it is recommended to generate multiple solutions and then use the most frequent results.
* **No chain-of-thought prompting**: Since these models always reason prior to answering the question, it is not necessary to tell them to "Reason step by step..."
* **Math tasks**: For mathematical problems, it is advisable to include a directive in your prompt such as: "Please reason step by step, and put your final answer within `\boxed{}`."
* **Forcing `<think>`**: On rare occasions, DeepSeek-R1 tends to bypass the thinking pattern, which can adversely affect the model's performance. In this case, the response will not start with a `<think>` tag. If you see this problem, try telling the model to start with the `<think>` tag.


# PydanticAI
Source: https://docs.together.ai/docs/pydanticai

Using PydanticAI with Together

PydanticAI is an agent framework created by the Pydantic team to simplify building production-grade generative AI applications. It brings the ergonomic design philosophy of FastAPI to AI agent development, offering a familiar and type-safe approach to working with language models.

## Installing Libraries

<CodeGroup>
  ```shell Shell theme={null}
  pip install pydantic-ai
  ```
</CodeGroup>

Set your Together AI API key:

<CodeGroup>
  ```shell Shell theme={null}
  export TOGETHER_API_KEY=***
  ```
</CodeGroup>

## Example

<CodeGroup>
  ```python Python theme={null}
  from pydantic_ai import Agent
  from pydantic_ai.models.openai import OpenAIModel
  from pydantic_ai.providers.openai import OpenAIProvider

  # Connect PydanticAI to LLMs on Together
  model = OpenAIModel(
      "meta-llama/Llama-3.3-70B-Instruct-Turbo",
      provider=OpenAIProvider(
          base_url="https://api.together.xyz/v1",
          api_key=os.environ.get("TOGETHER_API_KEY"),
      ),
  )

  # Setup the agent
  agent = Agent(
      model,
      system_prompt="Be concise, reply with one sentence.",
  )

  result = agent.run_sync('Where does "hello world" come from?')
  print(result.data)
  ```
</CodeGroup>

### Output

```
The first known use of "hello, world" was in a 1974 textbook about the C programming language.
```

## Next Steps

<Info>
  ### PydanticAI - Together AI Notebook

  Learn more about building agents using PydanticAI with Together AI in our [notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/PydanticAI/PydanticAI_Agents.ipynb) .
</Info>


# Quickstart
Source: https://docs.together.ai/docs/quickstart

Get up to speed with our API in one minute.

Together AI makes it easy to run leading open-source models using only a few lines of code.

## 1. Register for an account

First, [register for an account](https://api.together.xyz/settings/api-keys) to get an API key.

Once you've registered, set your account's API key to an environment variable named `TOGETHER_API_KEY`:

```shell Shell theme={null}
export TOGETHER_API_KEY=xxxxx
```

## 2. Install your preferred library

Together provides an official library for Python and TypeScript, or you can call our HTTP API in any language you want:

<CodeGroup>
  ```sh Python theme={null}
  pip install together
  ```

  ```sh TypeScript theme={null}
  npm install together-ai
  ```
</CodeGroup>

## 3. Run your first query against a model

Choose a model to query. In this example, we'll choose GPT OSS 20B with streaming:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  stream = client.chat.completions.create(
      model="openai/gpt-oss-20b",
      messages=[
          {
              "role": "user",
              "content": "What are the top 3 things to do in New York?",
          }
      ],
      stream=True,
  )

  for chunk in stream:
      print(chunk.choices[0].delta.content or "", end="", flush=True)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai"

  async function main() {
    const together = new Together()
    const stream = await together.chat.completions.create({
      model: "openai/gpt-oss-20b",
      messages: [
        { role: "user", content: "What are the top 3 things to do in New York?" },
      ],
      stream: true,
    })

    for await (const chunk of stream) {
      process.stdout.write(chunk.choices[0]?.delta?.content || "")
    }
  }

  main()
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
       	"model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
       	"messages": [
            {"role": "user", "content": "What are the top 3 things to do in New York?"}
       	]
       }'
  ```
</CodeGroup>

Congratulations –you've just made your first query to Together AI!

## Next steps

* Explore [our cookbook](https://github.com/togethercomputer/together-cookbook) for Python recipes with Together AI
* Explore [our demos](https://together.ai/demos) for full-stack open source example apps.
* Check out the [Together AI playground](https://api.together.xyz/playground) to try out different models.
* See [our integrations](/docs/integrations) with leading LLM frameworks.

## Resources

* [Discord](https://discord.com/invite/9Rk6sSeWEG)
* [Pricing](https://www.together.ai/pricing)
* [Support](https://www.together.ai/contact)

***


# Quickstart: Flux Kontext
Source: https://docs.together.ai/docs/quickstart-flux-kontext

Learn how to use Flux's new in-context image generation models

## Flux Kontext

Black Forest Labs has released FLUX Kontext with support on Together AI. These models allow you to generate and edit images through in-context image generation.

Unlike existing text-to-image models, FLUX.1 Kontext allows you to prompt with both text and images, and seamlessly extract and modify visual concepts to produce new, coherent renderings.

The Kontext family includes three models optimized for different use cases: Pro for balanced speed and quality, Max for maximum image fidelity, and Dev for development and experimentation.

## Generating an image

Here's how to use the new Kontext models:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  imageCompletion = client.images.generate(
      model="black-forest-labs/FLUX.1-kontext-pro",
      width=1536,
      height=1024,
      steps=28,
      prompt="make his shirt yellow",
      image_url="https://github.com/nutlope.png",
  )

  print(imageCompletion.data[0].url)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const response = await together.images.create({
      model: "black-forest-labs/FLUX.1-kontext-pro",
      width: 1536,
      height: 1024,
      steps: 28,
      prompt: "make his shirt yellow",
      image_url: "https://github.com/nutlope.png",
    });

    console.log(response.data[0].url);
  }

  main();
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-kontext-pro",
         "width": 1536,
         "height": 1024,
         "steps": 28,
         "prompt": "make his shirt yellow",
         "image_url": "https://github.com/nutlope.png"
       }'
  ```
</CodeGroup>

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/YmYlzoJDwPs82-4E/images/hassan-yellow-shirt.jpg?fit=max&auto=format&n=YmYlzoJDwPs82-4E&q=85&s=66b5f695ba162346d8079ab48b8f1de3" alt="" data-og-width="904" width="904" data-og-height="492" height="492" data-path="images/hassan-yellow-shirt.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/YmYlzoJDwPs82-4E/images/hassan-yellow-shirt.jpg?w=280&fit=max&auto=format&n=YmYlzoJDwPs82-4E&q=85&s=cd46f805ebdb73e6a437c6c9cc27e526 280w, https://mintcdn.com/togetherai-52386018/YmYlzoJDwPs82-4E/images/hassan-yellow-shirt.jpg?w=560&fit=max&auto=format&n=YmYlzoJDwPs82-4E&q=85&s=c4a2d6508e33ede4a7670d26e8423d6a 560w, https://mintcdn.com/togetherai-52386018/YmYlzoJDwPs82-4E/images/hassan-yellow-shirt.jpg?w=840&fit=max&auto=format&n=YmYlzoJDwPs82-4E&q=85&s=1fcbe3d062c2ca60cf785152728bdf27 840w, https://mintcdn.com/togetherai-52386018/YmYlzoJDwPs82-4E/images/hassan-yellow-shirt.jpg?w=1100&fit=max&auto=format&n=YmYlzoJDwPs82-4E&q=85&s=45ec4ec28b0e72b7534ebfbc253d7f9f 1100w, https://mintcdn.com/togetherai-52386018/YmYlzoJDwPs82-4E/images/hassan-yellow-shirt.jpg?w=1650&fit=max&auto=format&n=YmYlzoJDwPs82-4E&q=85&s=3009ea540ed84dbc06d69314337b7c63 1650w, https://mintcdn.com/togetherai-52386018/YmYlzoJDwPs82-4E/images/hassan-yellow-shirt.jpg?w=2500&fit=max&auto=format&n=YmYlzoJDwPs82-4E&q=85&s=745dce4b24cc380ac3cda271cee8fc15 2500w" />
</Frame>

## Available Models

Flux Kontext offers different models for various needs:

* **FLUX.1-kontext-pro**: Best balance of speed and quality (recommended)
* **FLUX.1-kontext-max**: Maximum image quality for production use
* **FLUX.1-kontext-dev**: Development model for testing

## Common Use Cases

* **Style Transfer**: Transform photos into different art styles (watercolor, oil painting, etc.)
* **Object Modification**: Change colors, add elements, or modify specific parts of an image
* **Scene Transformation**: Convert daytime to nighttime, change seasons, or alter environments
* **Character Creation**: Transform portraits into different styles or characters

## Key Parameters

Flux Kontext models support the following key parameters:

* `model`: Choose from `black-forest-labs/FLUX.1-kontext-pro`, `black-forest-labs/FLUX.1-kontext-max`, or `black-forest-labs/FLUX.1-kontext-dev`
* `prompt`: Text description of the transformation you want to apply
* `image_url`: URL of the reference image to transform
* `aspect_ratio`: Output aspect ratio (e.g., "1:1", "16:9", "9:16", "4:3", "3:2") - alternatively, you can use `width` and `height` for precise pixel dimensions
* `steps`: Number of diffusion steps (default: 28, higher values may improve quality)
* `seed`: Random seed for reproducible results

For complete parameter documentation, see the [Images Overview](/docs/images-overview#parameters).

See all available image models: [Image Models](/docs/serverless-models#image-models)


# Quickstart: Flux LoRA Inference
Source: https://docs.together.ai/docs/quickstart-flux-lora



Together AI now provides a high-speed endpoint for the FLUX.1 \[dev] model with integrated LoRA support. This enables swift and high-quality image generation using pre-trained LoRA adaptations for personalized outputs, unique styles, brand identities, and product-specific visualizations.

**Fine-tuning for FLUX LoRA is not yet available.**

## Generating an image using Flux LoRAs

Some Flux LoRA fine-tunes need to be activated using a trigger phrases that can be used in the prompt and can typically be found in the model cards. For example with: [https://huggingface.co/multimodalart/flux-tarot-v1](https://huggingface.co/multimodalart/flux-tarot-v1), you should use `in the style of TOK a trtcrd tarot style` to trigger the image generation.

You can add up to 2 LoRAs per image to combine the style from the different fine-tunes. The `scale` parameter allows you to specify the strength of each LoRA. Typically values of `0.3-1.2` will produce good results.

<CodeGroup>
  ```py Python theme={null}
  from together import Together

  client = Together()
  response = client.images.generate(
      prompt="a BLKLGHT image of man walking outside on rainy day",
      model="black-forest-labs/FLUX.1-dev-lora",
      width=1024,
      height=768,
      steps=28,
      n=1,
      response_format="url",
      image_loras=[
          {"path": "https://replicate.com/fofr/flux-black-light", "scale": 0.8},
          {
              "path": "https://huggingface.co/XLabs-AI/flux-RealismLora",
              "scale": 0.8,
          },
      ],
  )
  print(response.data[0].url)
  ```

  ```sh cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/images/generations"
  -H "Authorization: Bearer $TOGETHER_API_KEY"
  -H "Content-Type: application/json"
  -d '{
      "model": "black-forest-labs/FLUX.1-dev-lora",
      "prompt": "cute dog",
      "width": 1024,
      "height": 768,
      "steps": 28,
      "n": 1,
      "response_format": "url",
      "image_loras": [{"path":"https://huggingface.co/XLabs-AI/flux-RealismLora","scale":1},
          {"path": "https://huggingface.co/XLabs-AI/flux-RealismLora", "scale": 0.8}]
     }'
  ```
</CodeGroup>

## Acceptable LoRA URL formats

You can point to any URL that has a `.safetensors` file with a valid Flux LoRA fine-tune.

| Format                                        | Example                                                                                                                                                                                                                                        |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HuggingFace Repo Link                         | [https://huggingface.co/multimodalart/flux-tarot-v1](https://huggingface.co/multimodalart/flux-tarot-v1)                                                                                                                                       |
| HuggingFace Direct File Link with "resolve"\* | [https://huggingface.co/XLabs-AI/flux-lora-collection/resolve/main/anime\_lora.safetensors](https://huggingface.co/XLabs-AI/flux-lora-collection/resolve/main/anime_lora.safetensors)                                                          |
| Civit Download Link                           | [https://civitai.com/api/download/models/913438?type=Model\&format=SafeTensor](https://civitai.com/api/download/models/913438?type=Model\&format=SafeTensor)                                                                                   |
| Replicate Fine-tuned Flux Model Link          | [https://replicate.com/fofr/flux-black-light](https://replicate.com/fofr/flux-black-light)                                                                                                                                                     |
| Replicate Fine-tuned Flux Version Link        | [https://replicate.com/fofr/flux-black-light/versions/d0d48e298dcb51118c3f903817c833bba063936637a33ac52a8ffd6a94859af7](https://replicate.com/fofr/flux-black-light/versions/d0d48e298dcb51118c3f903817c833bba063936637a33ac52a8ffd6a94859af7) |
| Direct file link ending with ".safetensors"   | [https://mybucket.s3.amazonaws.com/my\_special\_lora.safetensors](https://mybucket.s3.amazonaws.com/my_special_lora.safetensors)                                                                                                               |

\*Note: the HuggingFace web page for a file ([https://huggingface.co/XLabs-AI/flux-lora-collection/blob/main/anime\_lora.safetensors](https://huggingface.co/XLabs-AI/flux-lora-collection/blob/main/anime_lora.safetensors)) will NOT work

If the safetensors file has incompatible keys, you'll get the message " has unused keys \<keys...>". This will happen if you pass a finetune of a non-flux model or an otherwise invalid file.

## Examples

The example below produces a realistic tarot card of a panda:

```py Python theme={null}
prompt = "a baby panda eating bamboo in the style of TOK a trtcrd tarot style"

response = client.images.generate(
    prompt=prompt,
    model="black-forest-labs/FLUX.1-dev-lora",
    width=1024,
    height=768,
    steps=28,
    n=1,
    response_format="url",
    image_loras=[
        {
            "path": "https://huggingface.co/multimodalart/flux-tarot-v1",
            "scale": 1,
        },
        {
            "path": "https://huggingface.co/Shakker-Labs/FLUX.1-dev-LoRA-add-details",
            "scale": 0.8,
        },
    ],
)
```

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=cb73a699bcb42f2deec002a9670cb4d6" alt="" data-og-width="1218" width="1218" data-og-height="918" height="918" data-path="images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=a176678d92b45daa26c77ada7aa668b3 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=30d0981ee82e0beb8711bfdb78d3bb03 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=64a9e45ac4f261e8568a9d089b21f65d 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=8077759db2f874c8daf5cf83e5d503ce 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=a9c6a5082858a26e6990d556502964fd 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=b64bfe2edff61a5e2ffe31803ddc557e 2500w" />
</Frame>

## Pricing

Your request costs \$0.035 per megapixel. For \$1, you can run this model approximately 29 times. Image charges are calculated by rounding up to the nearest megapixel.

Note: Due to high demand, FLUX.1 \[schnell] Free has a model specific rate limit of 10 img/min.


# Quickstart: How to do OCR
Source: https://docs.together.ai/docs/quickstart-how-to-do-ocr

A step by step guide on how to do OCR with Together AI's vision models with structured outputs

## Understanding OCR and Its Importance

Optical Character Recognition (OCR) has become a crucial tool for many applications as it enables computers to read & understand text within images. With the advent of advanced AI vision models, OCR can now understand context, structure, and relationships within documents, making it particularly valuable for processing receipts, invoices, and other structured documents while reasoning on the content output format.

In this guide, we're going to look at how you can take documents and images and extract text out of them in markdown (unstructured) or JSON (structured) formats.

## How to do standard OCR with Together SDK

Together AI provides powerful vision models that can process images and extract text with high accuracy.

The basic approach involves sending an image to a vision model and receiving extracted text in return.\
A great example of this implementation can be found at [llamaOCR.com](https://llamaocr.com/).

Here's a basic Typescript/Python implementation for standard OCR:

<CodeGroup>
  ```typescript TypeScript theme={null}

  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const billUrl =
      "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/1627e746-7eda-46d3-8d08-8c8eec0d6c9c/nobu.jpg?x-id=PutObject";

    const response = await together.chat.completions.create({
      model: "meta-llama/Llama-4-Scout-17B-16E-Instruct",
      messages: [
        {
          role: "system",
          content:
            "You are an expert at extracting information from receipts. Extract all the content from the receipt.",
        },
        {
          role: "user",
          content: [
            { type: "text", text: "Extract receipt information" },
            { type: "image_url", image_url: { url: billUrl } },
          ],
        },
      ],
    });

    if (response?.choices?.[0]?.message?.content) {
      console.log(response.choices[0].message.content);
      return (response.choices[0].message.content);
    }

    throw new Error("Failed to extract receipt information");
  }

  main();
  ```

  ```python Python theme={null}
  from together import Together

  client = Together()

  prompt = "You are an expert at extracting information from receipts. Extract all the content from the receipt."

  imageUrl = "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/1627e746-7eda-46d3-8d08-8c8eec0d6c9c/nobu.jpg?x-id=PutObject"


  stream = client.chat.completions.create(
      model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": prompt},
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": imageUrl,
                      },
                  },
              ],
          }
      ],
      stream=True,
  )

  for chunk in stream:
      print(
          chunk.choices[0].delta.content or "" if chunk.choices else "",
          end="",
          flush=True,
      )
  ```
</CodeGroup>

Here's the output from the code snippet above – we're simply giving it a receipt and asking it to extract all the information:

```text Text theme={null}
**Restaurant Information:**
- Name: Noby 
- Location: Los Angeles
- Address: 903 North La Cienega 
- Phone Number: 310-657-5111

**Receipt Details:**
- Date: 04/16/2011
- Time: 9:19 PM
- Server: Daniel
- Guest Count: 15
- Reprint #: 2

**Ordered Items:**
1. **Pina Martini** - $14.00
2. **Jasmine Calpurnina** - $14.00
3. **Yamasaki L. Decar** - $14.00
4. **Ma Margarita** - $4.00
5. **Diet Coke** - $27.00
6. **Lychee Martini (2 @ $14.00)** - $28.00
7. **Lynchee Martini** - $48.00
8. **Green Tea Decaf** - $12.00
9. **Glass Icecube R/Eising** - $0.00
10. **Green Tea Donation ($2)** - $2.00
11. **Lychee Martini (2 @ $14.00)** - $28.00
12. **YS50** - $225.00
13. **Green Tea ($40.00)** - $0.00
14. **Tiradito (3 @ $25.00)** - $75.00
15. **Tiradito** - $25
16. **Tiradito #20** - $20.00
17. **New-F-BOTAN (3 @ $30.00)** - $90.00
18. **Coke Refill** - $0.00
19. **Diet Coke Refill** - $0.00
20. **Bamboo** - $0.00
21. **Admin Fee** - $300.00
22. **TESSLER (15 @ $150.00)** - $2250.00
23. **Sparkling Water Large** - $9.00
24. **King Crab Asasu (3 @ $26.00)** - $78.00
25. **Mexican white shirt (15 @ $5.00)** - $75.00
26. **NorkFish Pate Cav** - $22.00

**Billing Information:**
- **Subtotal** - $3830.00
- **Tax** - $766.00
- **Total** - $4477.72
- **Gratuity** - $4277.72 
- **Total** - $5043.72
- **Balance Due** - $5043.72
```

## How to do structured OCR and extract JSON from images

For more complex applications like receipt processing (as seen on [usebillsplit.com](https://www.usebillsplit.com/)), we can leverage Together AI's vision models to extract structured data in JSON format. This approach is particularly powerful as it combines visual understanding with structured output.

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { z } from "zod";
  import { zodToJsonSchema } from "zod-to-json-schema";
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const billUrl =
      "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/1627e746-7eda-46d3-8d08-8c8eec0d6c9c/nobu.jpg?x-id=PutObject";
    // Define the receipt schema using Zod
    const receiptSchema = z.object({
      businessName: z
        .string()
        .optional()
        .describe("Name of the business on the receipt"),
      date: z.string().optional().describe("Date when the receipt was created"),
      total: z.number().optional().describe("Total amount on the receipt"),
      tax: z.number().optional().describe("Tax amount on the receipt"),
    });

    // Convert Zod schema to JSON schema for Together AI
    const jsonSchema = zodToJsonSchema(receiptSchema, { target: "openAi" });

    const response = await together.chat.completions.create({
      model: "meta-llama/Llama-4-Scout-17B-16E-Instruct",
      messages: [
        {
          role: "system",
          content:
            "You are an expert at extracting information from receipts. Extract the relevant information and format it as JSON.",
        },
        {
          role: "user",
          content: [
            { type: "text", text: "Extract receipt information" },
            { type: "image_url", image_url: { url: billUrl } },
          ],
        },
      ],
      response_format: { type: "json_object", schema: jsonSchema },
    });

    if (response?.choices?.[0]?.message?.content) {
      const output = JSON.parse(response.choices[0].message.content);
      console.dir(output);
      return output;
    }

    throw new Error("Failed to extract receipt information");
  }

  main();
  ```

  ```python Python theme={null}
  import json
  import together
  from pydantic import BaseModel, Field
  from typing import Optional

  ## Initialize Together AI client
  client = together.Together()


  ## Define the schema for receipt data matching the Next.js example
  class Receipt(BaseModel):
      businessName: Optional[str] = Field(
          None, description="Name of the business on the receipt"
      )
      date: Optional[str] = Field(
          None, description="Date when the receipt was created"
      )
      total: Optional[float] = Field(
          None, description="Total amount on the receipt"
      )
      tax: Optional[float] = Field(None, description="Tax amount on the receipt")


  def extract_receipt_info(image_url: str) -> dict:
      """
      Extract receipt information from an image using Together AI's vision capabilities.

      Args:
          image_url: URL of the receipt image to process

      Returns:
          A dictionary containing the extracted receipt information
      """
      # Call the Together AI API with the image URL and schema
      response = client.chat.completions.create(
          model="meta-llama/Llama-4-Scout-17B-16E-Instruct",
          messages=[
              {
                  "role": "system",
                  "content": "You are an expert at extracting information from receipts. Extract the relevant information and format it as JSON.",
              },
              {
                  "role": "user",
                  "content": [
                      {"type": "text", "text": "Extract receipt information"},
                      {"type": "image_url", "image_url": {"url": image_url}},
                  ],
              },
          ],
          response_format={
              "type": "json_object",
              "schema": Receipt.model_json_schema(),
          },
      )

      # Parse and return the response
      if response and response.choices and response.choices[0].message.content:
          try:
              return json.loads(response.choices[0].message.content)
          except json.JSONDecodeError:
              return {"error": "Failed to parse response as JSON"}

      return {"error": "Failed to extract receipt information"}


  ## Example usage
  def main():
      receipt_url = "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/1627e746-7eda-46d3-8d08-8c8eec0d6c9c/nobu.jpg?x-id=PutObject"
      result = extract_receipt_info(receipt_url)
      print(json.dumps(result, indent=2))
      return result


  if __name__ == "__main__":
      main()
  ```
</CodeGroup>

In this case, we passed in a schema to the model since we want specific information out of the receipt in JSON format. Here's the response:

```json JSON theme={null}
{
  "businessName": "Noby", 
  "date": "04/16/2011", 
  "total": 5043.72, 
  "tax": 766 
}
```

## Best Practices

1. **Structured Data Definition**: Define clear schemas for your expected output, making it easier to validate and process the extracted data.
2. **Model Selection**: Choose the appropriate model based on your use case. Feel free to experiment with [our vision models](/docs/serverless-models#vision-models) to find the best one for you.
3. **Error Handling**: Always implement robust error handling for cases where the OCR might fail or return unexpected results.
4. **Validation**: Implement validation for the extracted data to ensure accuracy and completeness.

By following these patterns and leveraging Together AI's vision models, you can build powerful OCR applications that go beyond simple text extraction to provide structured, actionable data from images.


# Quickstart: Retrieval Augmented Generation (RAG)
Source: https://docs.together.ai/docs/quickstart-retrieval-augmented-generation-rag

How to build a RAG workflow in under 5 mins!

In this Quickstart you'll learn how to build a RAG workflow using Together AI in 6 quick steps that can be ran in under 5 minutes!

We will leverage the embedding, reranking and inference endpoints.

## 1. Register for an account

First, [register for an account](https://api.together.xyz/settings/api-keys) to get an API key.

Once you've registered, set your account's API key to an environment variable named `TOGETHER_API_KEY`:

```bash Shell theme={null}
export TOGETHER_API_KEY=xxxxx
```

## 2. Install your preferred library

Together provides an official library for Python:

```sh Shell theme={null}
pip install together --upgrade
```

```py Python theme={null}
from together import Together

client = Together(api_key=TOGETHER_API_KEY)
```

## 3. Data Processing and Chunking

We will RAG over Paul Grahams latest essay titled [Founder Mode](https://paulgraham.com/foundermode.html). The code below will scrape and load the essay into memory.

```py Python theme={null}
import requests
from bs4 import BeautifulSoup


def scrape_pg_essay():
    url = "https://paulgraham.com/foundermode.html"

    try:
        # Send GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Paul Graham's essays typically have the main content in a font tag
        # You might need to adjust this selector based on the actual HTML structure
        content = soup.find("font")

        if content:
            # Extract and clean the text
            text = content.get_text()
            # Remove extra whitespace and normalize line breaks
            text = " ".join(text.split())
            return text
        else:
            return "Could not find the main content of the essay."

    except requests.RequestException as e:
        return f"Error fetching the webpage: {e}"


# Scrape the essay
pg_essay = scrape_pg_essay()
```

Chunk the essay:

```py Python theme={null}
# Naive fixed sized chunking with overlaps
def create_chunks(document, chunk_size=300, overlap=50):
    return [
        document[i : i + chunk_size]
        for i in range(0, len(document), chunk_size - overlap)
    ]


chunks = create_chunks(pg_essay, chunk_size=250, overlap=30)
```

## 4. Generate Vector Index and Perform Retrieval

We will now use `bge-large-en-v1.5` to embed the augmented chunks above into a vector index.

```py Python theme={null}
from typing import List
import numpy as np


def generate_embeddings(
    input_texts: List[str],
    model_api_string: str,
) -> np.ndarray:
    """Generate embeddings from Together python library.

    Args:
        input_texts: a list of string input texts.
        model_api_string: str. An API string for a specific embedding model of your choice.

    Returns:
        embeddings_list: a list of embeddings. Each element corresponds to the each input text.
    """
    outputs = client.embeddings.create(
        input=input_texts,
        model=model_api_string,
    )
    return np.array([x.embedding for x in outputs.data])


embeddings = generate_embeddings(chunks, "BAAI/bge-large-en-v1.5")
```

The function below will help us perform vector search:

```py Python theme={null}
def vector_retreival(
    query: str,
    top_k: int = 5,
    vector_index: np.ndarray = None,
) -> List[int]:
    """
    Retrieve the top-k most similar items from an index based on a query.
    Args:
        query (str): The query string to search for.
        top_k (int, optional): The number of top similar items to retrieve. Defaults to 5.
        index (np.ndarray, optional): The index array containing embeddings to search against. Defaults to None.
    Returns:
        List[int]: A list of indices corresponding to the top-k most similar items in the index.
    """

    query_embedding = np.array(
        generate_embeddings([query], "BAAI/bge-large-en-v1.5")[0]
    )

    similarity_scores = np.dot(query_embedding, vector_index.T)

    return list(np.argsort(-similarity_scores)[:top_k])


top_k_indices = vector_retreival(
    query="What are 'skip-level' meetings?",
    top_k=5,
    vector_index=embeddings,
)
top_k_chunks = [chunks[i] for i in top_k_indices]
```

We now have a way to retrieve from the vector index given a query.

## 5. Rerank To Improve Quality

We will use a reranker model to improve retrieved chunk relevance quality:

```py Python theme={null}
def rerank(query: str, chunks: List[str], top_k=3) -> List[int]:

    response = client.rerank.create(
        model="Salesforce/Llama-Rank-V1",
        query=query,
        documents=chunks,
        top_n=top_k,
    )

    return [result.index for result in response.results]


rerank_indices = rerank(
    "What are 'skip-level' meetings?",
    chunks=top_k_chunks,
    top_k=3,
)

reranked_chunks = ""

for index in rerank_indices:
    reranked_chunks += top_k_chunks[index] + "\n\n"

print(reranked_chunks)
```

## 6. Call Generative Model - Llama 405b

We will pass the final 3 concatenated chunks into an LLM to get our final answer.

```py Python theme={null}
query = "What are 'skip-level' meetings?"

response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
    messages=[
        {"role": "system", "content": "You are a helpful chatbot."},
        {
            "role": "user",
            "content": f"Answer the question: {query}. Use only information provided here: {reranked_chunks}",
        },
    ],
)

response.choices[0].message.content
```

If you want to learn more about how to best use open models refer to our [docs](/docs) here!


# Quickstart: Using Hugging Face Inference With Together
Source: https://docs.together.ai/docs/quickstart-using-hugging-face-inference

This guide will walk you through how to use Together models with Hugging Face Inference.

This documentation provides a concise guide for developers to integrate and use Together AI inference capabilities via the Hugging Face ecosystem.

## Authentication and Billing

When using Together AI through Hugging Face, you have two options for authentication:

* Direct Requests: Use your Together AI API key in your Hugging Face user account settings. In this mode, inference requests are sent directly to Together AI, and billing is handled by your Together AI account.
* Routed Requests: If you don't configure a Together AI API key, your requests will be routed through Hugging Face. In this case, you can use a Hugging Face token for authentication. Billing for routed requests is applied to your Hugging Face account at standard provider API rates.You don’t need an account on Together AI to do this, just use your HF one!

To add a Together AI api key to your Hugging Face settings, follow these steps:

1. Go to your [Hugging Face user account settings](https://huggingface.co/settings/inference-providers).
2. Locate the "Inference Providers" section.
3. You can add your API keys for different providers, including Together AI
4. You can also set your preferred provider order, which will influence the display order in model widgets and code snippets.

<Info>
  You can search for all [Together AI models](https://huggingface.co/models?inference_provider=together\&sort=trending) on the hub and directly try out the available models via the Model Page widget too.
</Info>

## Usage Examples

The examples below demonstrate how to interact with various models using Python and JavaScript.

First, ensure you have the `huggingface_hub` library installed (version v0.29.0 or later):

<CodeGroup>
  ```sh Shell theme={null}
  pip install huggingface_hub>=0.29.0
  ```

  ```sh Shell theme={null}
  npm install @huggingface/inference
  ```
</CodeGroup>

## 1. Text Generation - LLMs

### a. Chat Completion with Hugging Face Hub library

<CodeGroup>
  ```py Python theme={null}
  from huggingface_hub import InferenceClient

  # Initialize the InferenceClient with together as the provider

  client = InferenceClient(
      provider="together",
      api_key="xxxxxxxxxxxxxxxxxxxxxxxx",  # Replace with your API key (HF or custom)
  )

  # Define the chat messages

  messages = [{"role": "user", "content": "What is the capital of France?"}]

  # Generate a chat completion

  completion = client.chat.completions.create(
      model="deepseek-ai/DeepSeek-R1",
      messages=messages,
      max_tokens=500,
  )

  # Print the response

  print(completion.choices[0].message)
  ```

  ```js TypeScript theme={null}
  import { HfInference } from "@huggingface/inference";

  // Initialize the HfInference client with your API key
  const client = new HfInference("xxxxxxxxxxxxxxxxxxxxxxxx");

  // Generate a chat completion
  const chatCompletion = await client.chatCompletion({
      model: "deepseek-ai/DeepSeek-R1",  // Replace with your desired model
      messages: [
          {
              role: "user",
              content: "What is the capital of France?"
          }
      ],
      provider: "together",  // Replace with together's provider name
      max_tokens: 500
  });

  // Log the response
  console.log(chatCompletion.choices[0].message);
  ```
</CodeGroup>

You can swap this for any compatible LLM from Together AI, here’s a handy [URL](https://huggingface.co/models?inference_provider=together\&other=text-generation-inference\&sort=trending) to find the list.

### b. OpenAI client library

You can also call inference providers via the [OpenAI python client](https://github.com/openai/openai-python). You will need to specify the `base_url` and `model` parameters in the client and call respectively.

The easiest way is to go to [a model’s page](https://huggingface.co/deepseek-ai/DeepSeek-R1?inference_api=true\&inference_provider=together\&language=python) on the hub and copy the snippet.

```py Python theme={null}
from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/together",
    api_key="hf_xxxxxxxxxxxxxxxxxxxxxxxx",  # together or Hugging Face api key
)

messages = [{"role": "user", "content": "What is the capital of France?"}]

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1",
    messages=messages,
    max_tokens=500,
)

print(completion.choices[0].message)
```

## 2. Text-to-Image Generation

<CodeGroup>
  ```py Python theme={null}
  from huggingface_hub import InferenceClient

  # Initialize the InferenceClient with together as the provider

  client = InferenceClient(
      provider="together",  # Replace with together's provider name
      api_key="xxxxxxxxxxxxxxxxxxxxxxxx",  # Replace with your API key
  )

  # Generate an image from text

  image = client.text_to_image(
      "Bob Marley in the style of a painting by Johannes Vermeer",
      model="black-forest-labs/FLUX.1-schnell",  # Replace with your desired model
  )

  # `image` is a PIL.Image object

  image.show()
  ```

  ```js TypeScript theme={null}
  import { HfInference } from "@huggingface/inference";

  // Initialize the HfInference client with your API key
  const client = new HfInference("xxxxxxxxxxxxxxxxxxxxxxxx");

  // Generate a chat completion
  const generatedImage = await client.textToImage({
      model: "black-forest-labs/FLUX.1-schnell",  // Replace with your desired model
      inputs: "Bob Marley in the style of a painting by Johannes Vermeer",
      provider: "together",  // Replace with together's provider name
      max_tokens: 500
  });
  ```
</CodeGroup>

Similar to LLMs, you can use any compatible Text to Image model from the [list here](https://huggingface.co/models?inference_provider=together\&pipeline_tag=text-to-image\&sort=trending).

You can search for all [Together AI models](https://huggingface.co/models?inference_provider=together\&sort=trending) on the hub and directly try out the available models via the Model Page widget too.

We’ll continue to increase the number of models and ways to try it out!


# Rate Limits
Source: https://docs.together.ai/docs/rate-limits

Rate limits restrict how often a user or client can access our API within a set timeframe.

Rate limiting refers to the constraints our API enforces on how frequently a user or client can access our services within a given timeframe. Rate limits are denoted as HTTP status code 429. Read more about our rate limit tiers below, and find out how you can increase them here:

* If you have a high volume of steady traffic and good payment history for this traffic, you can request a higher limit by emailing [support@together.ai](mailto:support@together.ai).
* If you are interested in our Enterprise package, with custom requests per minute (RPM) and unlimited tokens per minute (TPM), please reach out to sales [here](https://www.together.ai/contact-sales).

### What is the purpose of rate limits?

Rate limits in APIs are a standard approach, and they serve to safeguard against abuse or misuse of the API, helping to ensure equitable access to the API with consistent performance.

### How are our rate limits implemented?

Our rate limits are currently measured in requests per second (RPS) and tokens per second (TPS) for each model type. If you exceed any of the rate limits you will get a 429 error. We show you the values per minute below, as it's the industry standard.

Important: when we launch support for a brand new model, we may temporarily disable automatic increases for that given model. This ensures our service levels remain stable, as rate limits represent the maximum "up to" capacity a user is entitled to, which is ultimately driven by our available serverless capacity. We strive to enable automatic increases as soon as possible once capacity stabilizes.

### Rate limit tiers

You can view your rate limit by navigating to Settings > Billing. As your usage of the Together API and your spend on our API increases, we will automatically increase your rate limits.

**Chat, language & code models**

| Tier   | Qualification criteria      | RPM   | TPM       |
| :----- | :-------------------------- | :---- | :-------- |
| Tier 1 | Credit card added, \$5 paid | 600   | 180,000   |
| Tier 2 | \$50 paid                   | 1,800 | 250,000   |
| Tier 3 | \$100 paid                  | 3,000 | 500,000   |
| Tier 4 | \$250 paid                  | 4,500 | 1,000,000 |
| Tier 5 | \$1,000 paid                | 6,000 | 2,000,000 |

**DeepSeek R1 model-specific rate limits**

> Due to high demand on the platform, DeepSeek R1 has these special rate limits. We are actively increasing them.

| Tier   | RPM     |
| :----- | :------ |
| Tier 1 | 3       |
| Tier 2 | 60      |
| Tier 3 | \~400+  |
| Tier 4 | \~400+  |
| Tier 5 | \~1200+ |

**Embedding models**

| Tier   | Qualification criteria      | RPM    | TPM        |
| :----- | :-------------------------- | :----- | :--------- |
| Tier 1 | Credit card added, \$5 paid | 3,000  | 2,000,000  |
| Tier 2 | \$50 paid                   | 5,000  | 2,000,000  |
| Tier 3 | \$100 paid                  | 5,000  | 10,000,000 |
| Tier 4 | \$250 paid                  | 10,000 | 10,000,000 |
| Tier 5 | \$1,000 paid                | 10,000 | 20,000,000 |

**Re-rank models**

| Tier   | Qualification criteria      | RPM   | TPM       |
| :----- | :-------------------------- | :---- | :-------- |
| Tier 1 | Credit card added, \$5 paid | 2,500 | 500,000   |
| Tier 2 | \$50 paid                   | 3,500 | 1,500,000 |
| Tier 3 | \$100 paid                  | 4,000 | 2,000,000 |
| Tier 4 | \$250 paid                  | 7,500 | 3,000,000 |
| Tier 5 | \$1,000 paid                | 9,000 | 5,000,000 |

**Image models**

| Tier   | Qualification criteria      | Img/min |
| :----- | :-------------------------- | :------ |
| Tier 1 | Credit card added, \$5 paid | 240     |
| Tier 2 | \$50 paid                   | 480     |
| Tier 3 | \$100 paid                  | 600     |
| Tier 4 | \$250 paid                  | 960     |
| Tier 5 | \$1,000 paid                | 1,200   |

Note: Due to high demand:

* FLUX.1 \[schnell] Free has a model specific rate limit of 6 img/min.
* FLUX.1 Kontext \[pro] has a model specific rate limit of 57 img/min.

You may experience congestion based on traffic from other users, and may be throttled to a lower level because of that. If you want committed capacity, [contact](https://together.ai/forms/scale-ent) our sales team to inquire about our Scale and Enterprise plans, which include custom RPM and unlimited TPM.

**Rate limits in headers**

The API response includes headers that display the rate limit enforcement, current usage, and when the limit will reset. We enforce limits per second and minute for token usage and per second for request rates, but the headers display per second limits only.

| Field                  | Description                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| x-ratelimit-limit      | The maximum number of requests per sec that are permitted before exhausting the rate limit.   |
| x-ratelimit-remaining  | The remaining number of requests per sec that are permitted before exhausting the rate limit. |
| x-ratelimit-reset      | The time until the rate limit (based on requests per sec) resets to its initial state.        |
| x-tokenlimit-limit     | The maximum number of tokens per sec that are permitted before exhausting the rate limit.     |
| x-tokenlimit-remaining | The remaining number of tokens per sec that are permitted before exhausting the rate limit.   |


# Reasoning Models Guide
Source: https://docs.together.ai/docs/reasoning-models-guide

How reasoning models like DeepSeek-R1 work.

## Reasoning vs. Non-reasoning Models

Reasoning models are trained very differently from their non-reasoning counterparts, and as a result they serve different purposes. Below we'll compare both types of models, details for reasoning models, pros and cons, applications and example use-cases.

Reasoning models like `DeepSeek-R1` are specifically developed to engage in extended, deep analysis of complex challenges. Their strength lies in strategic thinking, developing comprehensive solutions to intricate problems, and processing large amounts of nuanced information to reach decisions. Their high precision and accuracy make them particularly valuable in specialized fields traditionally requiring human expertise, such as mathematics, scientific research, legal work, healthcare, financial analysis.

Non-reasoning models such as `Llama 3.3 70B` or `DeepSeek-V3` are trained for efficient, direct task execution with faster response times and better cost efficiency.

Your application can leverage both types of models: using DeepSeek-R1 to develop the strategic framework and problem-solving approach, while deploying non-reasoning models to handle specific tasks where swift execution and cost considerations outweigh the need for absolute precision.

## Reasoning models use-cases

* **Analyzing and assessing AI model outputs**\
  Reasoning models excel at evaluating responses from other systems, particularly in data validation scenarios. This becomes especially valuable in critical fields like law, where these models can apply contextual understanding rather than just following rigid validation rules.

* **Code analysis and improvement**\
  Reasoning models are great at conducting thorough code reviews and suggesting improvements across large codebases. Their ability to process extensive code makes them particularly valuable for comprehensive review processes.

* **Strategic planning and task delegation**\
  These models shine in creating detailed, multi-stage plans and determining the most suitable AI model for each phase based on specific requirements like processing speed or analytical depth needed for the task.

* **Complex document analysis and pattern recognition**\
  The models excel at processing and analyzing extensive, unstructured documents such as contract agreements, legal reports, and healthcare documentation. They're particularly good at identifying connections between different documents and making connections.

* **Precision information extraction**\
  When dealing with large volumes of unstructured data, these models excel at pinpointing and extracting exactly the relevant information needed to answer specific queries, effectively filtering out noise in search and retrieval processes. This makes them great to use in RAG or LLM augmented internet search use-cases.

* **Handling unclear instructions**\
  These models are particularly skilled at working with incomplete or ambiguous information. They can effectively interpret user intent and will proactively seek clarification rather than making assumptions when faced with information gaps.

## Pros and Cons

Reasoning models excel for tasks where you need:

* High accuracy and dependable decision-making capabilities
* Solutions to complex problems involving multiple variables and ambiguous data
* Can afford higher query latencies
* Have a higher cost/token budget per task

Non-reasoning models are optimal when you need:

* Faster processing speed (lower overall query latency) and lower operational costs
* Execution of clearly defined, straightforward tasks
* Function calling, JSON mode or other well structured tasks


# Recommended Models
Source: https://docs.together.ai/docs/recommended-models

Find the right models for your use case

We host 100+ open-source models on our serverless inference platform and even more on dedicated endpoints. This guide helps you choose the right model for your specific use case.

For a complete list of all available models with detailed specifications, visit our [Serverless](/docs/serverless-models) and [Dedicated](/docs/dedicated-models) Models pages.

## Recommended Models by Use Case

| Use Case                   | Recommended Model             | Model String                                        | Alternatives                                                                    | Learn More                                                                           |
| :------------------------- | :---------------------------- | :-------------------------------------------------- | :------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------- |
| **Chat**                   | Kimi K2 Instruct 0905         | `moonshotai/Kimi-K2-Instruct-0905`                  | `deepseek-ai/DeepSeek-V3.1`, `Qwen/Qwen3-235B-A22B-Instruct-2507-tput`          | [Chat](/docs/chat-overview)                                                          |
| **Reasoning**              | DeepSeek-R1-0528              | `deepseek-ai/DeepSeek-R1`                           | `Qwen/Qwen3-235B-A22B-Thinking-2507`, `openai/gpt-oss-120b`                     | [Reasoning Guide](/docs/reasoning-models-guide), [DeepSeek R1](/docs/deepseek-r1)    |
| **Coding Agents**          | Qwen3-Coder 480B-A35B         | `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`           | `moonshotai/Kimi-K2-Instruct-0905`, `deepseek-ai/DeepSeek-V3.1`                 | [Building Agents](/docs/how-to-build-coding-agents)                                  |
| **Small & Fast**           | GPT-OSS 20B                   | `openai/gpt-oss-20b`                                | `Qwen/Qwen2.5-7B-Instruct-Turbo`, `meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo` | -                                                                                    |
| **Medium General Purpose** | GLM 4.5 Air                   | `zai-org/GLM-4.5-Air-FP8`                           | `Qwen/Qwen3-Next-80B-A3B-Instruct`, `openai/gpt-oss-120b`                       | -                                                                                    |
| **Function Calling**       | GLM 4.5 Air                   | `zai-org/GLM-4.5-Air-FP8`                           | `Qwen/Qwen3-Next-80B-A3B-Instruct`, `moonshotai/Kimi-K2-Instruct-0905`          | [Function Calling](/docs/function-calling)                                           |
| **Vision**                 | Llama 4 Maverick              | `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | `Qwen/Qwen2.5-VL-72B-Instruct`                                                  | [Vision](/docs/vision-overview), [OCR](/docs/quickstart-how-to-do-ocr)               |
| **Image Generation**       | Qwen Image                    | `Qwen/Qwen-Image`                                   | `google/flash-image-2.5`, `ByteDance-Seed/Seedream-4.0`                         | [Images](/docs/images-overview)                                                      |
| **Image-to-Image**         | Flash Image 2.5 (Nano Banana) | `google/flash-image-2.5`                            | `black-forest-labs/FLUX.1-kontext-pro`                                          | [Flux Kontext](/docs/quickstart-flux-kontext)                                        |
| **Text-to-Video**          | Sora 2                        | `openai/sora-2-pro`                                 | `google/veo-3.0`, `ByteDance/Seedance-1.0-pro`                                  | [Video Generation](/docs/videos-overview)                                            |
| **Image-to-Video**         | Veo 3.0                       | `google/veo-3.0`                                    | `ByteDance/Seedance-1.0-pro`, `kwaivgI/kling-2.1-master`                        | [Video Generation](/docs/videos-overview)                                            |
| **Text-to-Speech**         | Cartesia Sonic 2              | `cartesia/sonic-2`                                  | `cartesia/sonic`                                                                | [Text-to-Speech](/docs/text-to-speech)                                               |
| **Speech-to-Text**         | Whisper Large v3              | `openai/whisper-large-v3`                           | -                                                                               | [Speech-to-Text](/docs/speech-to-text)                                               |
| **Embeddings**             | GTE-Modernbert-base           | `Alibaba-NLP/gte-modernbert-base`                   | `intfloat/multilingual-e5-large-instruct`                                       | [Embeddings](/reference/embeddings-2)                                                |
| **Rerank**                 | MixedBread Rerank Large       | `mixedbread-ai/Mxbai-Rerank-Large-V2`               | `Salesforce/Llama-Rank-v1`                                                      | [Rerank](/docs/rerank-overview), [Guide](/docs/how-to-improve-search-with-rerankers) |
| **Moderation**             | Virtue Guard                  | `VirtueAI/VirtueGuard-Text-Lite`                    | `meta-llama/Llama-Guard-4-12B`                                                  | -                                                                                    |

***

**Need Help Choosing?**

* Check our [Serverless Models](/docs/serverless-models) page for complete specifications
* See our [WhichLLM](https://whichllm.together.ai/) page which provides categorical benchmarks for the above usecases
* Review [Rate Limits](/docs/rate-limits) for your tier
* See [Pricing](https://together.ai/pricing) for cost information
* Visit [Inference FAQs](/docs/inference-faqs) for common questions

For high-volume production workloads, consider [Dedicated Inference](/docs/dedicated-inference) for guaranteed capacity and predictable performance.


# Rerank
Source: https://docs.together.ai/docs/rerank-overview

Learn how to improve the relevance of your search and RAG systems with reranking.

## What is a reranker?

A reranker is a specialized model that improves search relevancy by reassessing and reordering a set of retrieved documents based on their relevance to a given query. It takes a query and a set of text inputs (called 'documents'), and returns a relevancy score for each document relative to the given query. This process helps filter and prioritize the most pertinent information, enhancing the quality of search results.

In Retrieval Augmented Generation (RAG) pipelines, the reranking step sits between the initial retrieval step and the final generation phase. It acts as a quality filter, refining the selection of documents that will be used as context for language models. By ensuring that only the most relevant information is passed to the generation phase, rerankers play a crucial role in improving the accuracy of generated responses while potentially reducing processing costs.

## How does Together's Rerank API work?

Together's serverless Rerank API allows you to seamlessly integrate supported rerank models into your enterprise applications. It takes in a `query` and a number of `documents`, and outputs a relevancy score and ordering index for each document. It can also filter its response to the n most relevant documents.

Together's Rerank API is also compatible with Cohere Rerank, making it easy to try out our reranker models on your existing applications.

Key features of Together's Rerank API include:

* Flagship support for [LlamaRank](/docs/together-and-llamarank), Salesforce’s reranker model
* Support for JSON and tabular data
* Long 8K context per document
* Low latency for fast search queries
* Full compatibility with Cohere's Rerank API

[Get started building with Together Rerank today →](/docs/together-and-llamarank)

## Cohere Rerank compatibility

The Together Rerank endpoint is compatible with Cohere Rerank, making it easy to test out models like [LlamaRank](/docs/together-and-llamarank) for your existing applications. Simply switch it out by updating the `URL`, `API key` and `model`.

<CodeGroup>
  ```py Python theme={null}
  import cohere

  co = cohere.Client(
      base_url="https://api.together.xyz/v1",
      api_key=TOGETHER_API_KEY,
  )
  docs = [
      "Carson City is the capital city of the American state of Nevada.",
      "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
      "Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.",
      "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
      "Capital punishment (the death penalty) has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
  ]
  response = co.rerank(
      model="Salesforce/Llama-Rank-V1",
      query="What is the capital of the United States?",
      documents=docs,
      top_n=3,
  )
  ```

  ```ts TypeScript theme={null}
  import { CohereClient } from "cohere-ai";

  const cohere = new CohereClient({
    baseUrl: "https://api.together.xyz/",
    token: process.env.TOGETHER_API_KEY,
  });

  const docs = [
    "Carson City is the capital city of the American state of Nevada.",
    "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
    "Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.",
    "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
    "Capital punishment (the death penalty) has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
  ];

  const response = await cohere.rerank({
    model: "Salesforce/Llama-Rank-V1",
    query: "What is the capital of the United States?",
    documents: docs,
    topN: 3,
  });
  ```
</CodeGroup>

## Get Started

### Example with text

In the example below, we use the [Rerank API endpoint](/reference/rerank) to index the list of `documents` from most to least relevant to the query `What animals can I find near Peru?`.

<CodeGroup>
  ```py Python theme={null}
  from together import Together

  client = Together()

  query = "What animals can I find near Peru?"

  documents = [
      "The giant panda (Ailuropoda melanoleuca), also known as the panda bear or simply panda, is a bear species endemic to China.",
      "The llama is a domesticated South American camelid, widely used as a meat and pack animal by Andean cultures since the pre-Columbian era.",
      "The wild Bactrian camel (Camelus ferus) is an endangered species of camel endemic to Northwest China and southwestern Mongolia.",
      "The guanaco is a camelid native to South America, closely related to the llama. Guanacos are one of two wild South American camelids; the other species is the vicuña, which lives at higher elevations.",
  ]

  response = client.rerank.create(
      model="Salesforce/Llama-Rank-V1",
      query=query,
      documents=documents,
      top_n=2,
  )

  for result in response.results:
      print(f"Document Index: {result.index}")
      print(f"Document: {documents[result.index]}")
      print(f"Relevance Score: {result.relevance_score}")
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const documents = [
    "The giant panda (Ailuropoda melanoleuca), also known as the panda bear or simply panda, is a bear species endemic to China.",
    "The llama is a domesticated South American camelid, widely used as a meat and pack animal by Andean cultures since the pre-Columbian era.",
    "The wild Bactrian camel (Camelus ferus) is an endangered species of camel endemic to Northwest China and southwestern Mongolia.",
    "The guanaco is a camelid native to South America, closely related to the llama. Guanacos are one of two wild South American camelids; the other species is the vicuña, which lives at higher elevations.",
  ];

  const response = await client.rerank({
    model: "Salesforce/Llama-Rank-V1",
    query: "What animals can I find near Peru?",
    documents,
    top_n: 2,
  });

  for (const result of response.results) {
    console.log(`Document index: ${result.index}`);
    console.log(`Document: ${documents[result.index]}`);
    console.log(`Relevance score: ${result.relevance_score}`);
  }
  ```

  ```sh cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/rerank" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "Salesforce/Llama-Rank-v1",
         "query": "What animals can I find near Peru?",
         "documents": [{
            "title": "Llama",
            "text": "The llama is a domesticated South American camelid, widely used as a meat and pack animal by Andean cultures since the pre-Columbian era."
          },
          {
            "title": "Panda",
            "text": "The giant panda (Ailuropoda melanoleuca), also known as the panda bear or simply panda, is a bear species endemic to China."
          },
          {
            "title": "Guanaco",
            "text": "The guanaco is a camelid native to South America, closely related to the llama. Guanacos are one of two wild South American camelids; the other species is the vicuña, which lives at higher elevations."
          },
          {
            "title": "Wild Bactrian camel",
            "text": "The wild Bactrian camel (Camelus ferus) is an endangered species of camel endemic to Northwest China and southwestern Mongolia."
          }]
       }'
  ```
</CodeGroup>

### Example with JSON Data

Alternatively, you can pass in a JSON object and specify the fields you’d like to rank over, and the order they should be considered in. If you do not pass in any `rank_fields`, it will default to the text key.

The example below shows passing in some emails, with the query `Which pricing did we get from Oracle?`.

<CodeGroup>
  ```py Python theme={null}
  from together import Together

  client = Together()

  query = "Which pricing did we get from Oracle?"

  documents = [
      {
          "from": "Paul Doe <paul_fake_doe@oracle.com>",
          "to": ["Steve <steve@me.com>", "lisa@example.com"],
          "date": "2024-03-27",
          "subject": "Follow-up",
          "text": "We are happy to give you the following pricing for your project.",
      },
      {
          "from": "John McGill <john_fake_mcgill@microsoft.com>",
          "to": ["Steve <steve@me.com>"],
          "date": "2024-03-28",
          "subject": "Missing Information",
          "text": "Sorry, but here is the pricing you asked for for the newest line of your models.",
      },
      {
          "from": "John McGill <john_fake_mcgill@microsoft.com>",
          "to": ["Steve <steve@me.com>"],
          "date": "2024-02-15",
          "subject": "Commited Pricing Strategy",
          "text": "I know we went back and forth on this during the call but the pricing for now should follow the agreement at hand.",
      },
      {
          "from": "Generic Airline Company<no_reply@generic_airline_email.com>",
          "to": ["Steve <steve@me.com>"],
          "date": "2023-07-25",
          "subject": "Your latest flight travel plans",
          "text": "Thank you for choose to fly Generic Airline Company. Your booking status is confirmed.",
      },
      {
          "from": "Generic SaaS Company<marketing@generic_saas_email.com>",
          "to": ["Steve <steve@me.com>"],
          "date": "2024-01-26",
          "subject": "How to build generative AI applications using Generic Company Name",
          "text": "Hey Steve! Generative AI is growing so quickly and we know you want to build fast!",
      },
      {
          "from": "Paul Doe <paul_fake_doe@oracle.com>",
          "to": ["Steve <steve@me.com>", "lisa@example.com"],
          "date": "2024-04-09",
          "subject": "Price Adjustment",
          "text": "Re: our previous correspondence on 3/27 we'd like to make an amendment on our pricing proposal. We'll have to decrease the expected base price by 5%.",
      },
  ]

  response = client.rerank.create(
      model="Salesforce/Llama-Rank-V1",
      query=query,
      documents=documents,
      return_documents=True,
      rank_fields=["from", "to", "date", "subject", "text"],
  )

  print(response)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const documents = [
    {
      from: "Paul Doe <paul_fake_doe@oracle.com>",
      to: ["Steve <steve@me.com>", "lisa@example.com"],
      date: "2024-03-27",
      subject: "Follow-up",
      text: "We are happy to give you the following pricing for your project.",
    },
    {
      from: "John McGill <john_fake_mcgill@microsoft.com>",
      to: ["Steve <steve@me.com>"],
      date: "2024-03-28",
      subject: "Missing Information",
      text: "Sorry, but here is the pricing you asked for for the newest line of your models.",
    },
    {
      from: "John McGill <john_fake_mcgill@microsoft.com>",
      to: ["Steve <steve@me.com>"],
      date: "2024-02-15",
      subject: "Commited Pricing Strategy",
      text: "I know we went back and forth on this during the call but the pricing for now should follow the agreement at hand.",
    },
    {
      from: "Generic Airline Company<no_reply@generic_airline_email.com>",
      to: ["Steve <steve@me.com>"],
      date: "2023-07-25",
      subject: "Your latest flight travel plans",
      text: "Thank you for choose to fly Generic Airline Company. Your booking status is confirmed.",
    },
    {
      from: "Generic SaaS Company<marketing@generic_saas_email.com>",
      to: ["Steve <steve@me.com>"],
      date: "2024-01-26",
      subject:
        "How to build generative AI applications using Generic Company Name",
      text: "Hey Steve! Generative AI is growing so quickly and we know you want to build fast!",
    },
    {
      from: "Paul Doe <paul_fake_doe@oracle.com>",
      to: ["Steve <steve@me.com>", "lisa@example.com"],
      date: "2024-04-09",
      subject: "Price Adjustment",
      text: "Re: our previous correspondence on 3/27 we'd like to make an amendment on our pricing proposal. We'll have to decrease the expected base price by 5%.",
    },
  ];

  const response = await client.rerank({
    model: "Salesforce/Llama-Rank-V1",
    query: "Which pricing did we get from Oracle?",
    documents,
    return_documents: true,
    rank_fields: ["from", "to", "date", "subject", "text"],
  });

  console.log(response);
  ```

  ```sh cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/rerank" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "Salesforce/Llama-Rank-v1",
         "query": "Which pricing did we get from Oracle?",
         "documents": [
           {
             "from": "Paul Doe <paul_fake_doe@oracle.com>",
             "to": ["Steve <steve@me.com>", "lisa@example.com"],
             "date": "2024-03-27",
             "subject": "Follow-up",
             "text": "We are happy to give you the following pricing for your project."
           },
           {
             "from": "John McGill <john_fake_mcgill@microsoft.com>",
             "to": ["Steve <steve@me.com>"],
             "date": "2024-03-28",
             "subject": "Missing Information",
             "text": "Sorry, but here is the pricing you asked for for the newest line of your models."
           },
           {
             "from": "John McGill <john_fake_mcgill@microsoft.com>",
             "to": ["Steve <steve@me.com>"],
             "date": "2024-02-15",
             "subject": "Commited Pricing Strategy",
             "text": "I know we went back and forth on this during the call but the pricing for now should follow the agreement at hand."
           },
           {
             "from": "Generic Airline Company<no_reply@generic_airline_email.com>",
             "to": ["Steve <steve@me.com>"],
             "date": "2023-07-25",
             "subject": "Your latest flight travel plans",
             "text": "Thank you for choose to fly Generic Airline Company. Your booking status is confirmed."
           },
           {
             "from": "Generic SaaS Company<marketing@generic_saas_email.com>",
             "to": ["Steve <steve@me.com>"],
             "date": "2024-01-26",
             "subject": "How to build generative AI applications using Generic Company Name",
             "text": "Hey Steve! Generative AI is growing so quickly and we know you want to build fast!"
           },
           {
             "from": "Paul Doe <paul_fake_doe@oracle.com>",
             "to": ["Steve <steve@me.com>", "lisa@example.com"],
             "date": "2024-04-09",
             "subject": "Price Adjustment",
             "text": "Re: our previous correspondence on 3/27 we'\''d like to make an amendment on our pricing proposal. We'\''ll have to decrease the expected base price by 5%."
           }
         ],
         "return_documents": true,
         "rank_fields": ["from", "to", "date", "subject", "text"]
       }'
  ```
</CodeGroup>

In the `documents` parameter, we are passing in a list of objects which have the key values: `['from', 'to', 'date', 'subject', 'text']`. As part of the Rerank call, under `rank_fields` we are specifying which keys to rank over, as well as the order in which the key value pairs should be considered.

When the model returns rankings, we'll also receive each email in the response because the `return_documents` option is set to true.

```json JSON theme={null}
{
  "model": "Salesforce/Llama-Rank-v1",
  "choices": [
    {
      "index": 0,
      "document": {
        "text": "{\"from\":\"Paul Doe <paul_fake_doe@oracle.com>\",\"to\":[\"Steve <steve@me.com>\",\"lisa@example.com\"],\"date\":\"2024-03-27\",\"subject\":\"Follow-up\",\"text\":\"We are happy to give you the following pricing for your project.\"}"
      },
      "relevance_score": 0.606349439153678
    },
    {
      "index": 5,
      "document": {
        "text": "{\"from\":\"Paul Doe <paul_fake_doe@oracle.com>\",\"to\":[\"Steve <steve@me.com>\",\"lisa@example.com\"],\"date\":\"2024-04-09\",\"subject\":\"Price Adjustment\",\"text\":\"Re: our previous correspondence on 3/27 we'd like to make an amendment on our pricing proposal. We'll have to decrease the expected base price by 5%.\"}"
      },
      "relevance_score": 0.5059948716207964
    },
    {
      "index": 1,
      "document": {
        "text": "{\"from\":\"John McGill <john_fake_mcgill@microsoft.com>\",\"to\":[\"Steve <steve@me.com>\"],\"date\":\"2024-03-28\",\"subject\":\"Missing Information\",\"text\":\"Sorry, but here is the pricing you asked for for the newest line of your models.\"}"
      },
      "relevance_score": 0.2271930688841643
    },
    {
      "index": 2,
      "document": {
        "text": "{\"from\":\"John McGill <john_fake_mcgill@microsoft.com>\",\"to\":[\"Steve <steve@me.com>\"],\"date\":\"2024-02-15\",\"subject\":\"Commited Pricing Strategy\",\"text\":\"I know we went back and forth on this during the call but the pricing for now should follow the agreement at hand.\"}"
      },
      "relevance_score": 0.2229844295907072
    },
    {
      "index": 4,
      "document": {
        "text": "{\"from\":\"Generic SaaS Company<marketing@generic_saas_email.com>\",\"to\":[\"Steve <steve@me.com>\"],\"date\":\"2024-01-26\",\"subject\":\"How to build generative AI applications using Generic Company Name\",\"text\":\"Hey Steve! Generative AI is growing so quickly and we know you want to build fast!\"}"
      },
      "relevance_score": 0.0021253144747196517
    },
    {
      "index": 3,
      "document": {
        "text": "{\"from\":\"Generic Airline Company<no_reply@generic_airline_email.com>\",\"to\":[\"Steve <steve@me.com>\"],\"date\":\"2023-07-25\",\"subject\":\"Your latest flight travel plans\",\"text\":\"Thank you for choose to fly Generic Airline Company. Your booking status is confirmed.\"}"
      },
      "relevance_score": 0.0010322494264659
    }
  ]
}
```


# Sequential Workflow
Source: https://docs.together.ai/docs/sequential-agent-workflow

Coordinating a chain of LLM calls to solve a complex task.

A workflow where the output of one LLM call becomes the input for the next. This sequential design allows for structured reasoning and step-by-step task completion.

## Workflow Architecture

Chain multiple LLM calls sequentially to process complex tasks.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/6ba24ee6aded3b4fcbd509d1115b354ee78e414c9edd7f91f19a468c641d9e73-sequential.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=78442d4ddf22839fca77d6e13e0fbea1" alt="" data-og-width="4560" width="4560" data-og-height="1696" height="1696" data-path="images/docs/6ba24ee6aded3b4fcbd509d1115b354ee78e414c9edd7f91f19a468c641d9e73-sequential.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/6ba24ee6aded3b4fcbd509d1115b354ee78e414c9edd7f91f19a468c641d9e73-sequential.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=56dbfae0893276ec21bc44ba81ad4db6 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/6ba24ee6aded3b4fcbd509d1115b354ee78e414c9edd7f91f19a468c641d9e73-sequential.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=bcef647c7e736d88a0094777216db71e 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/6ba24ee6aded3b4fcbd509d1115b354ee78e414c9edd7f91f19a468c641d9e73-sequential.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=2476ae2ffa6857d35a293a74b97cfcbb 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/6ba24ee6aded3b4fcbd509d1115b354ee78e414c9edd7f91f19a468c641d9e73-sequential.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=552af104c83e732881245b22fc165621 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/6ba24ee6aded3b4fcbd509d1115b354ee78e414c9edd7f91f19a468c641d9e73-sequential.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=266a9a82f4e3b3b80d7151fbbd25b4ad 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/6ba24ee6aded3b4fcbd509d1115b354ee78e414c9edd7f91f19a468c641d9e73-sequential.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=842471507d90c733194478e314add630 2500w" />
</Frame>

<Info>
  ### Sequential Workflow Cookbook

  For a more detailed walk-through refer to the [notebook here](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Serial_Chain_Agent_Workflow.ipynb)
</Info>

## Setup Client

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()


  def run_llm(user_prompt: str, model: str, system_prompt: str = None):
      messages = []
      if system_prompt:
          messages.append({"role": "system", "content": system_prompt})

      messages.append({"role": "user", "content": user_prompt})

      response = client.chat.completions.create(
          model=model,
          messages=messages,
          temperature=0.7,
          max_tokens=4000,
      )

      return response.choices[0].message.content
  ```

  ```typescript TypeScript theme={null}
  import assert from "node:assert";
  import Together from "together-ai";

  const client = new Together();

  export async function runLLM(
    userPrompt: string,
    model: string,
    systemPrompt?: string,
  ) {
    const messages: { role: "system" | "user"; content: string }[] = [];
    if (systemPrompt) {
      messages.push({ role: "system", content: systemPrompt });
    }

    messages.push({ role: "user", content: userPrompt });

    const response = await client.chat.completions.create({
      model,
      messages,
      temperature: 0.7,
      max_tokens: 4000,
    });

    const content = response.choices[0].message?.content;
    assert(typeof content === "string");
    return content;
  }
  ```
</CodeGroup>

## Implement Workflow

<CodeGroup>
  ```python Python theme={null}
  from typing import List


  def serial_chain_workflow(
      input_query: str,
      prompt_chain: List[str],
  ) -> List[str]:
      """Run a serial chain of LLM calls to address the `input_query`
      using a list of prompts specified in `prompt_chain`.
      """
      response_chain = []
      response = input_query
      for i, prompt in enumerate(prompt_chain):
          print(f"Step {i+1}")
          response = run_llm(
              f"{prompt}\nInput:\n{response}",
              model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
          )
          response_chain.append(response)
          print(f"{response}\n")
      return response_chain
  ```

  ```typescript TypeScript theme={null}
  /*
    Run a serial chain of LLM calls to address the `inputQuery`
    using a list of prompts specified in `promptChain`.
  */
  async function serialChainWorkflow(inputQuery: string, promptChain: string[]) {
    const responseChain: string[] = [];
    let response = inputQuery;

    for (const prompt of promptChain) {
      console.log(`Step ${promptChain.indexOf(prompt) + 1}`);

      response = await runLLM(
        `${prompt}\nInput:\n${response}`,
        "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
      );
      console.log(`${response}\n`);
      responseChain.push(response);
    }

    return responseChain;
  }
  ```
</CodeGroup>

## Example Usage

<CodeGroup>
  ```python Python theme={null}
  question = "Sally earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?"

  prompt_chain = [
      """Given the math problem, ONLY extract any relevant numerical information and how it can be used.""",
      """Given the numberical information extracted, ONLY express the steps you would take to solve the problem.""",
      """Given the steps, express the final answer to the problem.""",
  ]

  responses = serial_chain_workflow(question, prompt_chain)

  final_answer = responses[-1]
  ```

  ```typescript TypeScript theme={null}
  const question =
    "Sally earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?";

  const promptChain = [
    "Given the math problem, ONLY extract any relevant numerical information and how it can be used.",
    "Given the numberical information extracted, ONLY express the steps you would take to solve the problem.",
    "Given the steps, express the final answer to the problem.",
  ];

  async function main() {
    await serialChainWorkflow(question, promptChain);
  }

  main();
  ```
</CodeGroup>

## Use cases

* Generating Marketing copy, then translating it into a different language.
* Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline.
* Using an LLM to clean and standardize raw data, then passing the cleaned data to another LLM for insights, summaries, or visualizations.
* Generating a set of detailed questions based on a topic with one LLM, then passing those questions to another LLM to produce well-researched answers.


# Serverless Models
Source: https://docs.together.ai/docs/serverless-models



## Chat models

> In the table below, models marked as "Turbo" are quantized to FP8 and those marked as "Lite" are INT4. All our other models are at full precision (FP16).

If you're not sure which chat model to use, we currently recommend **Llama 3.3 70B Turbo** (`meta-llama/Llama-3.3-70B-Instruct-Turbo`) to get started.

| Organization    | Model Name                              | API Model String                                  | Context length | Quantization |
| :-------------- | :-------------------------------------- | :------------------------------------------------ | :------------- | :----------- |
| Moonshot        | Kimi K2 Instruct 0905                   | moonshotai/Kimi-K2-Instruct-0905                  | 262144         | FP8          |
| DeepSeek        | DeepSeek-V3.1                           | deepseek-ai/DeepSeek-V3.1                         | 128000         | FP8          |
| OpenAI          | GPT-OSS 120B                            | openai/gpt-oss-120b                               | 128000         | MXFP4        |
| OpenAI          | GPT-OSS 20B                             | openai/gpt-oss-20b                                | 128000         | MXFP4        |
| Moonshot        | Kimi K2 Instruct                        | moonshotai/Kimi-K2-Instruct                       | 128000         | FP8          |
| Z.ai            | GLM 4.5 Air                             | zai-org/GLM-4.5-Air-FP8                           | 131072         | FP8          |
| Qwen            | Qwen3 235B-A22B Thinking 2507           | Qwen/Qwen3-235B-A22B-Thinking-2507                | 262144         | FP8          |
| Qwen            | Qwen3-Coder 480B-A35B Instruct          | Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8           | 256000         | FP8          |
| Qwen            | Qwen3 235B-A22B Instruct 2507           | Qwen/Qwen3-235B-A22B-Instruct-2507-tput           | 262144         | FP8          |
| Qwen            | Qwen3-Next-80B-A3B-Instruct             | Qwen/Qwen3-Next-80B-A3B-Instruct                  | 262144         | BF16         |
| Qwen            | Qwen3-Next-80B-A3B-Thinking             | Qwen/Qwen3-Next-80B-A3B-Thinking                  | 262144         | BF16         |
| DeepSeek        | DeepSeek-R1-0528                        | deepseek-ai/DeepSeek-R1                           | 163839         | FP8          |
| DeepSeek        | DeepSeek-R1-0528 Throughput             | deepseek-ai/DeepSeek-R1-0528-tput                 | 163839         | FP8          |
| DeepSeek        | DeepSeek-V3-0324                        | deepseek-ai/DeepSeek-V3                           | 163839         | FP8          |
| Meta            | Llama 4 Maverick<br />(17Bx128E)        | meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 | 1048576        | FP8          |
| Meta            | Llama 4 Scout<br />(17Bx16E)            | meta-llama/Llama-4-Scout-17B-16E-Instruct         | 1048576        | FP16         |
| Meta            | Llama 3.3 70B Instruct Turbo            | meta-llama/Llama-3.3-70B-Instruct-Turbo           | 131072         | FP8          |
| Deep Cogito     | Cogito v2 Preview 70B                   | deepcogito/cogito-v2-preview-llama-70B            | 32768          | BF16         |
| Deep Cogito     | Cogito v2 Preview 109B MoE              | deepcogito/cogito-v2-preview-llama-109B-MoE       | 32768          | BF16         |
| Deep Cogito     | Cogito v2 Preview 405B                  | deepcogito/cogito-v2-preview-llama-405B           | 32768          | BF16         |
| Deep Cogito     | Cogito v2 Preview 671B MoE              | deepcogito/cogito-v2-preview-deepseek-671b        | 32768          | FP8          |
| Mistral AI      | Magistral Small 2506 API                | mistralai/Magistral-Small-2506                    | 40960          | BF16         |
| DeepSeek        | DeepSeek R1 Distill Llama 70B           | deepseek-ai/DeepSeek-R1-Distill-Llama-70B         | 131072         | FP16         |
| DeepSeek        | DeepSeek R1 Distill Qwen 14B            | deepseek-ai/DeepSeek-R1-Distill-Qwen-14B          | 131072         | FP16         |
| Marin Community | Marin 8B Instruct                       | marin-community/marin-8b-instruct                 | 4096           | FP16         |
| Mistral AI      | Mistral Small 3 Instruct (24B)          | mistralai/Mistral-Small-24B-Instruct-2501         | 32768          | FP16         |
| Meta            | Llama 3.1 8B Instruct Turbo             | meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo       | 131072         | FP8          |
| Meta            | Llama 3.3 70B Instruct Turbo (Free)\*\* | meta-llama/Llama-3.3-70B-Instruct-Turbo-Free      | 8193           | FP8          |
| Qwen            | Qwen 2.5 7B Instruct Turbo              | Qwen/Qwen2.5-7B-Instruct-Turbo                    | 32768          | FP8          |
| Qwen            | Qwen 2.5 72B Instruct Turbo             | Qwen/Qwen2.5-72B-Instruct-Turbo                   | 32768          | FP8          |
| Qwen            | Qwen2.5 Vision Language 72B Instruct    | Qwen/Qwen2.5-VL-72B-Instruct                      | 32768          | FP8          |
| Qwen            | Qwen 2.5 Coder 32B Instruct             | Qwen/Qwen2.5-Coder-32B-Instruct                   | 32768          | FP16         |
| Qwen            | QwQ-32B                                 | Qwen/QwQ-32B                                      | 32768          | FP16         |
| Qwen            | Qwen3 235B A22B Throughput              | Qwen/Qwen3-235B-A22B-fp8-tput                     | 40960          | FP8          |
| Arcee           | Arcee AI Virtuoso Medium                | arcee-ai/virtuoso-medium-v2                       | 128000         | -            |
| Arcee           | Arcee AI Coder-Large                    | arcee-ai/coder-large                              | 32768          | -            |
| Arcee           | Arcee AI Virtuoso-Large                 | arcee-ai/virtuoso-large                           | 128000         | -            |
| Arcee           | Arcee AI Maestro                        | arcee-ai/maestro-reasoning                        | 128000         | -            |
| Arcee           | Arcee AI Caller                         | arcee-ai/caller                                   | 32768          | -            |
| Arcee           | Arcee AI Blitz                          | arcee-ai/arcee-blitz                              | 32768          | -            |
| Meta            | Llama 3.1 405B Instruct Turbo           | meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo     | 130815         | FP8          |
| Meta            | Llama 3.2 3B Instruct Turbo             | meta-llama/Llama-3.2-3B-Instruct-Turbo            | 131072         | FP16         |
| Meta            | Llama 3 8B Instruct Lite                | meta-llama/Meta-Llama-3-8B-Instruct-Lite          | 8192           | INT4         |
| Meta            | Llama 3 70B Instruct Reference          | meta-llama/Llama-3-70b-chat-hf                    | 8192           | FP16         |
| Google          | Gemma Instruct (2B)                     | google/gemma-2b-it\*                              | 8192           | FP16         |
| Google          | Gemma 3N E4B Instruct                   | google/gemma-3n-E4B-it                            | 32768          | FP8          |
| Gryphe          | MythoMax-L2 (13B)                       | Gryphe/MythoMax-L2-13b\*                          | 4096           | FP16         |
| Mistral AI      | Mistral (7B) Instruct                   | mistralai/Mistral-7B-Instruct-v0.1                | 8192           | FP16         |
| Mistral AI      | Mistral (7B) Instruct v0.2              | mistralai/Mistral-7B-Instruct-v0.2                | 32768          | FP16         |
| Mistral AI      | Mistral (7B) Instruct v0.3              | mistralai/Mistral-7B-Instruct-v0.3                | 32768          | FP16         |

\* The Free version of Llama 3.3 70B Instruct Turbo has a reduced rate limit of .6 requests/minute (36/hour) for users on the free tier and 3 requests/minute for any user who has added a credit card on file.

\*Deprecated model, see [Deprecations](/docs/deprecations) for more details

**Chat Model Examples**

* [PDF to Chat App](https://www.pdftochat.com/) - Chat with your PDFs (blogs, textbooks, papers)
* [Open Deep Research Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Together_Open_Deep_Research_CookBook.ipynb) - Generate long form reports using a single prompt
* [RAG with Reasoning Models Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/RAG_with_Reasoning_Models.ipynb) - RAG with DeepSeek-R1
* [Fine-tuning Chat Models Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Finetuning/Finetuning_Guide.ipynb) - Tune Language models for conversation
* [Building Agents](https://github.com/togethercomputer/together-cookbook/tree/main/Agents) - Agent workflows with language models

## Image models

Use our [Images](/reference/post-images-generations) endpoint for Image Models.

| Organization      | Model Name                     | Model String for API                     | Default steps |
| :---------------- | :----------------------------- | :--------------------------------------- | :------------ |
| Google            | Imagen 4.0 Preview             | google/imagen-4.0-preview                | -             |
| Google            | Imagen 4.0 Fast                | google/imagen-4.0-fast                   | -             |
| Google            | Imagen 4.0 Ultra               | google/imagen-4.0-ultra                  | -             |
| Google            | Flash Image 2.5 (Nano Banana)  | google/flash-image-2.5                   | -             |
| Black Forest Labs | Flux.1 \[schnell] **(free)\*** | black-forest-labs/FLUX.1-schnell-Free    | N/A           |
| Black Forest Labs | Flux.1 \[schnell] (Turbo)      | black-forest-labs/FLUX.1-schnell         | 4             |
| Black Forest Labs | Flux.1 Dev                     | black-forest-labs/FLUX.1-dev             | 28            |
| Black Forest Labs | Flux1.1 \[pro]                 | black-forest-labs/FLUX.1.1-pro           | -             |
| Black Forest Labs | Flux.1 Kontext \[pro]          | black-forest-labs/FLUX.1-kontext-pro     | 28            |
| Black Forest Labs | Flux.1 Kontext \[max]          | black-forest-labs/FLUX.1-kontext-max     | 28            |
| Black Forest Labs | Flux.1 Kontext \[dev]          | black-forest-labs/FLUX.1-kontext-dev     | 28            |
| Black Forest Labs | FLUX.1 Krea \[dev]             | black-forest-labs/FLUX.1-krea-dev        | 28            |
| ByteDance         | Seedream 3.0                   | ByteDance-Seed/Seedream-3.0              | -             |
| ByteDance         | Seedream 4.0                   | ByteDance-Seed/Seedream-4.0              | -             |
| Qwen              | Qwen Image                     | Qwen/Qwen-Image                          | -             |
| RunDiffusion      | Juggernaut Pro Flux            | RunDiffusion/Juggernaut-pro-flux         | -             |
| RunDiffusion      | Juggernaut Lightning Flux      | Rundiffusion/Juggernaut-Lightning-Flux   | -             |
| HiDream           | HiDream-I1-Full                | HiDream-ai/HiDream-I1-Full               | -             |
| HiDream           | HiDream-I1-Dev                 | HiDream-ai/HiDream-I1-Dev                | -             |
| HiDream           | HiDream-I1-Fast                | HiDream-ai/HiDream-I1-Fast               | -             |
| Ideogram          | Ideogram 3.0                   | ideogram/ideogram-3.0                    | -             |
| Lykon             | Dreamshaper                    | Lykon/DreamShaper                        | -             |
| Stability AI      | SD XL                          | stabilityai/stable-diffusion-xl-base-1.0 | -             |
| Stability AI      | Stable Diffusion 3             | stabilityai/stable-diffusion-3-medium    | -             |

Note: Due to high demand, FLUX.1 \[schnell] Free has a model specific rate limit of 10 img/min. Image models can also only be used with credits. Users are unable to call Image models with a zero or negative balance.

\*Free model has reduced rate limits and performance compared to our paid Turbo endpoint for Flux Shnell named `black-forest-labs/FLUX.1-schnell`

**Image Model Examples**

* [Blinkshot.io](https://www.blinkshot.io/) - A realtime AI image playground built with Flux Schnell
* [Logo Creator](https://www.logo-creator.io/) - An logo generator that creates professional logos in seconds using Flux Pro 1.1
* [PicMenu](https://www.picmenu.co/) - A menu visualizer that takes a restaurant menu and generates nice images for each dish.
* [Flux LoRA Inference Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Flux_LoRA_Inference.ipynb) - Using LoRA fine-tuned image generations models

**How FLUX pricing works** For FLUX models (except for pro) pricing is based on the size of generated images (in megapixels) and the number of steps used (if the number of steps exceed the default steps).

* **Default pricing:** The listed per megapixel prices are for the default number of steps.
* **Using more or fewer steps:** Costs are adjusted based on the number of steps used **only if you go above the default steps**. If you use more steps, the cost increases proportionally using the formula below. If you use fewer steps, the cost *does not* decrease and is based on the default rate.

Here’s a formula to calculate cost:

Cost = MP × Price per MP × (Steps ÷ Default Steps)

Where:

* MP = (Width × Height ÷ 1,000,000)
* Price per MP = Cost for generating one megapixel at the default steps
* Steps = The number of steps used for the image generation. This is only factored in if going above default steps.

## Vision models

If you're not sure which vision model to use, we currently recommend **Llama 4 Scout** (`meta-llama/Llama-4-Scout-17B-16E-Instruct`) to get started. For model specific rate limits, navigate [here](/docs/rate-limits).

|       |                                      |                                                   |        |
| ----- | ------------------------------------ | ------------------------------------------------- | ------ |
| Meta  | Llama 4 Maverick<br />(17Bx128E)     | meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 | 524288 |
| Meta  | Llama 4 Scout<br />(17Bx16E)         | meta-llama/Llama-4-Scout-17B-16E-Instruct         | 327680 |
| Qwen  | Qwen2.5 Vision Language 72B Instruct | Qwen/Qwen2.5-VL-72B-Instruct                      | 32768  |
| Arcee | Arcee AI Spotlight                   | arcee\_ai/arcee-spotlight                         | 128000 |

**Vision Model Examples**

* [LlamaOCR](https://llamaocr.com/) - A tool that takes documents (like receipts) and outputs markdown
* [Wireframe to Code](https://www.napkins.dev/) - A wireframe to app tool that takes in a UI mockup of a site and give you React code.
* [Extracting Structured Data from Images](https://github.com/togethercomputer/together-cookbook/blob/main/Structured_Text_Extraction_from_Images.ipynb) - Extract information from images as JSON

## Video models

| Organization | Model Name           | Model String for API        | Resolution / Duration |
| :----------- | :------------------- | :-------------------------- | :-------------------- |
| MiniMax      | MiniMax 01 Director  | minimax/video-01-director   | 720p / 5s             |
| MiniMax      | MiniMax Hailuo 02    | minimax/hailuo-02           | 768p / 10s            |
| Google       | Veo 2.0              | google/veo-2.0              | 720p / 5s             |
| Google       | Veo 3.0              | google/veo-3.0              | 720p / 8s             |
| Google       | Veo 3.0 + Audio      | google/veo-3.0-audio        | 720p / 8s             |
| Google       | Veo 3.0 Fast         | google/veo-3.0-fast         | 1080p / 8s            |
| Google       | Veo 3.0 Fast + Audio | google/veo-3.0-fast-audio   | 1080p / 8s            |
| ByteDance    | Seedance 1.0 Lite    | ByteDance/Seedance-1.0-lite | 720p / 5s             |
| ByteDance    | Seedance 1.0 Pro     | ByteDance/Seedance-1.0-pro  | 1080p / 5s            |
| PixVerse     | PixVerse v5          | pixverse/pixverse-v5        | 1080p / 5s            |
| Kuaishou     | Kling 2.1 Master     | kwaivgI/kling-2.1-master    | 1080p / 5s            |
| Kuaishou     | Kling 2.1 Standard   | kwaivgI/kling-2.1-standard  | 720p / 5s             |
| Kuaishou     | Kling 2.1 Pro        | kwaivgI/kling-2.1-pro       | 1080p / 5s            |
| Kuaishou     | Kling 2.0 Master     | kwaivgI/kling-2.0-master    | 1080p / 5s            |
| Kuaishou     | Kling 1.6 Standard   | kwaivgI/kling-1.6-standard  | 720p / 5s             |
| Kuaishou     | Kling 1.6 Pro        | kwaivgI/kling-1.6-pro       | 1080p / 5s            |
| Wan-AI       | Wan 2.2 I2V          | Wan-AI/Wan2.2-I2V-A14B      | -                     |
| Wan-AI       | Wan 2.2 T2V          | Wan-AI/Wan2.2-T2V-A14B      | -                     |
| Vidu         | Vidu 2.0             | vidu/vidu-2.0               | 720p / 8s             |
| Vidu         | Vidu Q1              | vidu/vidu-q1                | 1080p / 5s            |
| OpenAI       | Sora 2               | openai/sora-2               | 720p / 8s             |
| OpenAI       | Sora 2 Pro           | openai/sora-2-pro           | 1080p / 8s            |

## Audio models

Use our [Audio](/reference/audio-speech) endpoint for text-to-speech models. For speech-to-text models see [Transcription](/reference/audio-transcriptions) and [Translations](/reference/audio-translations)

| Organization | Modality       | Model Name       | Model String for API           |
| :----------- | :------------- | :--------------- | :----------------------------- |
| Canopy Labs  | Text-to-Speech | Orpheus 3B       | canopylabs/orpheus-3b-0.1-ft   |
| Kokoro       | Text-to-Speech | Kokoro           | hexgrad/Kokoro-82M             |
| Cartesia     | Text-to-Speech | Cartesia Sonic 2 | cartesia/sonic-2               |
| Cartesia     | Text-to-Speech | Cartesia Sonic   | cartesia/sonic                 |
| OpenAI       | Speech-to-Text | Whisper Large v3 | openai/whisper-large-v3        |
| Mistral AI   | Speech-to-Text | Voxtral Mini 3B  | mistralai/Voxtral-Mini-3B-2507 |

**Audio Model Examples**

* [PDF to Podcast Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/PDF_to_Podcast.ipynb) - Generate a NotebookLM style podcast given a PDF
* [Audio Podcast Agent Workflow](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Serial_Chain_Agent_Workflow.ipynb) - Agent workflow to generate audio files given input content

## Code models

Use our [Completions](/reference/completions-1) endpoint for Code Models.

| Organization | Model Name                  | Model String for API            | Context length |
| :----------- | :-------------------------- | :------------------------------ | :------------- |
| Qwen         | Qwen 2.5 Coder 32B Instruct | Qwen/Qwen2.5-Coder-32B-Instruct | 32768          |

**Code Model Examples**

* [LlamaCoder](https://llamacoder.together.ai) - An open source app to generate small apps with one prompt. Powered by Llama 3 405B.
* [Code Generation Agent](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Looping_Agent_Workflow.ipynb) - An agent workflow to generate and iteratively improve code.

## Embedding models

| Model Name                     | Model String for API                       | Model Size | Embedding Dimension | Context Window |
| :----------------------------- | ------------------------------------------ | :--------- | :------------------ | :------------- |
| M2-BERT-80M-32K-Retrieval      | togethercomputer/m2-bert-80M-32k-retrieval | 80M        | 768                 | 32768          |
| BGE-Large-EN-v1.5              | BAAI/bge-large-en-v1.5                     | 326M       | 1024                | 512            |
| BGE-Base-EN-v1.5               | BAAI/bge-base-en-v1.5                      | 102M       | 768                 | 512            |
| GTE-Modernbert-base            | Alibaba-NLP/gte-modernbert-base            | 149M       | 768                 | 8192           |
| Multilingual-e5-large-instruct | intfloat/multilingual-e5-large-instruct    | 560M       | 1024                | 514            |

**Embedding Model Examples**

* [Contextual RAG](https://docs.together.ai/docs/how-to-implement-contextual-rag-from-anthropic) - An open source implementation of contextual RAG by Anthropic
* [Code Generation Agent](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Looping_Agent_Workflow.ipynb) - An agent workflow to generate and iteratively improve code
* [Multimodal Search and Image Generation](https://github.com/togethercomputer/together-cookbook/blob/main/Multimodal_Search_and_Conditional_Image_Generation.ipynb) - Search for images and generate more similar ones
* [Visualizing Embeddings](https://github.com/togethercomputer/together-cookbook/blob/main/Embedding_Visualization.ipynb) - Visualizing and clustering vector embeddings

## Rerank models

Our [Rerank API](/docs/rerank-overview) has built-in support for the following models, that we host via our serverless endpoints.

| Organization | Model Name   | Model Size | Model String for API                | Max Doc Size (tokens) | Max Docs |
| ------------ | ------------ | :--------- | ----------------------------------- | --------------------- | -------- |
| Salesforce   | LlamaRank    | 8B         | Salesforce/Llama-Rank-v1            | 8192                  | 1024     |
| MixedBread   | Rerank Large | 1.6B       | mixedbread-ai/Mxbai-Rerank-Large-V2 | 32768                 | -        |

**Rerank Model Examples**

* [Search and Reranking](https://github.com/togethercomputer/together-cookbook/blob/main/Search_with_Reranking.ipynb) - Simple semantic search pipeline improved using a reranker
* [Implementing Hybrid Search Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Open_Contextual_RAG.ipynb) - Implementing semantic + lexical search along with reranking

## Language models

Use our [Completions](/reference/completions-1) endpoint for Language Models.

| Organization | Model Name           | Model String for API        | Context length |
| :----------- | :------------------- | :-------------------------- | :------------- |
| Meta         | LLaMA-2 (70B)        | meta-llama/Llama-2-70b-hf   | 4096           |
| mistralai    | Mixtral-8x7B (46.7B) | mistralai/Mixtral-8x7B-v0.1 | 32768          |

## Moderation models

Use our [Completions](/reference/completions-1) endpoint to run a moderation model as a standalone classifier, or use it alongside any of the other models above as a filter to safeguard responses from 100+ models, by specifying the parameter `"safety_model": "MODEL_API_STRING"`

| Organization | Model Name          | Model String for API             | Context length |
| :----------- | :------------------ | :------------------------------- | :------------- |
| Meta         | Llama Guard (8B)    | meta-llama/Meta-Llama-Guard-3-8B | 8192           |
| Meta         | Llama Guard 4 (12B) | meta-llama/Llama-Guard-4-12B     | 1048576        |
| Virtue AI    | Virtue Guard        | VirtueAI/VirtueGuard-Text-Lite   | 32768          |


# Slurm Management System
Source: https://docs.together.ai/docs/slurm



## Slurm

Slurm is a cluster management system that allows users to manage and schedule jobs on a cluster of computers. A Together GPU Cluster provides Slurm configured out-of-the-box for distributed training and the option to use your own scheduler. Users can submit computing jobs to the Slurm head node where the scheduler will assign the tasks to available GPU nodes based on resource availability. For more information on Slurm, see the [Slurm Quick Start User Guide](https://slurm.schedmd.com/quickstart.html).

### **Slurm Basic Concepts**

1. **Jobs**: A job is a unit of work that is submitted to the cluster. Jobs can be scripts, programs, or other types of tasks.
2. **Nodes**: A node is a computer in the cluster that can run jobs. Nodes can be physical machines or virtual machines.
3. **Head Node**: Each Together GPU Cluster cluster is configured with head node. A user will login to the head node to write jobs, submit jobs to the GPU cluster, and retrieve the results.
4. **Partitions**: A partition is a group of nodes that can be used to run jobs. Partitions can be configured to have different properties, such as the number of nodes and the amount of memory available.
5. **Priorities**: Priorities are used to determine which jobs should be run first. Jobs with higher priorities are given preference over jobs with lower priorities.

### **Using Slurm**

1. **Job Submission**: Jobs can be submitted to the cluster using the **`sbatch`** command. Jobs can be submitted in batch mode or interactively using the **`srun`** command.
2. **Job Monitoring**: Jobs can be monitored using the **`squeue`** command, which displays information about the jobs that are currently running or waiting to run.
3. **Job Control**: Jobs can be controlled using the **`scancel`** command, which allows users to cancel or interrupt jobs that are running.

### Slurm Job Arrays

You can use Slurm job arrays to partition input files into k chunks and distribute the chunks across the nodes. See this example on processing RPv1 which will need to be adapted to your processing: [arxiv-clean-slurm.batch](https://github.com/togethercomputer/RedPajama-Data/blob/rp_v1/data_prep/arxiv/scripts/arxiv-clean-slurm.sbatch)

### **Troubleshooting Slurm**

1. **Error Messages**: Slurm provides error messages that can help users diagnose and troubleshoot problems.
2. **Log Files**: Slurm provides log files that can be used to monitor the status of the cluster and diagnose problems.



---

**Navigation:** [← Previous](./06-iterative-workflow.md) | [Index](./index.md) | [Next →](./08-speech-to-text.md)
