**Navigation:** [← Previous](./05-how-to-build-coding-agents.md) | [Index](./index.md) | [Next →](./07-parallel-workflow.md)

---

# Iterative Workflow
Source: https://docs.together.ai/docs/iterative-workflow

Iteratively call LLMs to optimize task performance.

The iterative workflow ensures task requirements are fully met through iterative refinement. An LLM performs a task, followed by a second LLM evaluating whether the result satisfies all specified criteria. If not, the process repeats with adjustments, continuing until the evaluator confirms all requirements are met.

## Workflow Architecture

Build an agent that iteratively improves responses.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/16fb4a3d0976a38d9dcd7e0f4eaeebf3ccab506c4632b0cccc8f78c69d09419a-iterative.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=f8d52197b52031a0a1da679ea48a5ba4" alt="" data-og-width="4040" width="4040" data-og-height="1792" height="1792" data-path="images/16fb4a3d0976a38d9dcd7e0f4eaeebf3ccab506c4632b0cccc8f78c69d09419a-iterative.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/16fb4a3d0976a38d9dcd7e0f4eaeebf3ccab506c4632b0cccc8f78c69d09419a-iterative.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=3919659b5f3371062b30671f05950fc4 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/16fb4a3d0976a38d9dcd7e0f4eaeebf3ccab506c4632b0cccc8f78c69d09419a-iterative.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=83d793d41a8eab2cd009eb577039d4fb 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/16fb4a3d0976a38d9dcd7e0f4eaeebf3ccab506c4632b0cccc8f78c69d09419a-iterative.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=446c9bdfe0cc7f76501d4d96ec5328c1 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/16fb4a3d0976a38d9dcd7e0f4eaeebf3ccab506c4632b0cccc8f78c69d09419a-iterative.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=9ed18106822f4ae0fb0bb7075672e7ee 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/16fb4a3d0976a38d9dcd7e0f4eaeebf3ccab506c4632b0cccc8f78c69d09419a-iterative.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=3ecbda4cc2e073b6f6db1d96653ad351 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/16fb4a3d0976a38d9dcd7e0f4eaeebf3ccab506c4632b0cccc8f78c69d09419a-iterative.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=5c7f491d72a06842a16ec08c0ef33a93 2500w" />
</Frame>

## Setup Client & Helper Functions

<CodeGroup>
  ```py Python theme={null}
  import json
  from pydantic import ValidationError
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

  ```ts TypeScript theme={null}
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
  ```py Python theme={null}
  from pydantic import BaseModel
  from typing import Literal

  GENERATOR_PROMPT = """
  Your goal is to complete the task based on <user input>. If there are feedback
  from your previous generations, you should reflect on them to improve your solution

  Output your answer concisely in the following format:

  Thoughts:
  [Your understanding of the task and feedback and how you plan to improve]

  Response:
  [Your code implementation here]
  """


  def generate(
      task: str,
      generator_prompt: str,
      context: str = "",
  ) -> tuple[str, str]:
      """Generate and improve a solution based on feedback."""
      full_prompt = (
          f"{generator_prompt}\n{context}\nTask: {task}"
          if context
          else f"{generator_prompt}\nTask: {task}"
      )

      response = run_llm(
          full_prompt, model="Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8"
      )

      print("\n## Generation start")
      print(f"Output:\n{response}\n")

      return response


  EVALUATOR_PROMPT = """
  Evaluate this following code implementation for:
  1. code correctness
  2. time complexity
  3. style and best practices

  You should be evaluating only and not attempting to solve the task.

  Only output "PASS" if all criteria are met and you have no further suggestions for improvements.

  Provide detailed feedback if there are areas that need improvement. You should specify what needs improvement and why.

  Only output JSON.
  """


  def evaluate(
      task: str,
      evaluator_prompt: str,
      generated_content: str,
      schema,
  ) -> tuple[str, str]:
      """Evaluate if a solution meets requirements."""
      full_prompt = f"{evaluator_prompt}\nOriginal task: {task}\nContent to evaluate: {generated_content}"

      # Build a schema for the evaluation
      class Evaluation(BaseModel):
          evaluation: Literal["PASS", "NEEDS_IMPROVEMENT", "FAIL"]
          feedback: str

      response = JSON_llm(full_prompt, Evaluation)

      evaluation = response["evaluation"]
      feedback = response["feedback"]

      print("## Evaluation start")
      print(f"Status: {evaluation}")
      print(f"Feedback: {feedback}")

      return evaluation, feedback


  def loop_workflow(
      task: str, evaluator_prompt: str, generator_prompt: str
  ) -> tuple[str, list[dict]]:
      """Keep generating and evaluating until the evaluator passes the last generated response."""
      # Store previous responses from generator
      memory = []

      # Generate initial response
      response = generate(task, generator_prompt)
      memory.append(response)

      # While the generated response is not passing, keep generating and evaluating
      while True:
          evaluation, feedback = evaluate(task, evaluator_prompt, response)
          # Terminating condition
          if evaluation == "PASS":
              return response

          # Add current response and feedback to context and generate a new response
          context = "\n".join(
              [
                  "Previous attempts:",
                  *[f"- {m}" for m in memory],
                  f"\nFeedback: {feedback}",
              ]
          )

          response = generate(task, generator_prompt, context)
          memory.append(response)
  ```

  ```ts TypeScript theme={null}
  import dedent from "dedent";
  import { z } from "zod";

  const GENERATOR_PROMPT = dedent`
    Your goal is to complete the task based on <user input>. If there is feedback
    from your previous generations, you should reflect on them to improve your solution.

    Output your answer concisely in the following format:

    Thoughts:
    [Your understanding of the task and feedback and how you plan to improve]

    Response:
    [Your code implementation here]
  `;

  /*
    Generate and improve a solution based on feedback.
  */
  async function generate(task: string, generatorPrompt: string, context = "") {
    const fullPrompt = dedent`
      ${generatorPrompt}

      Task: ${task}

      ${context}
    `;

    const response = await runLLM(fullPrompt, "Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8");
    console.log(dedent`
      ## Generation start

      ${response}
      \n
    `);

    return response;
  }

  const EVALUATOR_PROMPT = dedent`
    Evaluate this following code implementation for:

      1. code correctness
      2. time complexity
      3. style and best practices

    You should be evaluating only and not attempting to solve the task.

    Only output "PASS" if all criteria are met and you have no further suggestions for improvements.

    Provide detailed feedback if there are areas that need improvement. You should specify what needs improvement and why. Make sure to only use a single line without newlines for the feedback.

    Only output JSON.
  `;

  /*
    Evaluate if a solution meets the requirements.
  */
  async function evaluate(
    task: string,
    evaluatorPrompt: string,
    generatedContent: string,
  ) {
    const fullPrompt = dedent`
      ${evaluatorPrompt}

      Original task: ${task}

      Content to evaluate: ${generatedContent}
    `;

    const schema = z.object({
      evaluation: z.enum(["PASS", "NEEDS_IMPROVEMENT", "FAIL"]),
      feedback: z.string(),
    });
    const { evaluation, feedback } = await jsonLLM(fullPrompt, schema);

    console.log(dedent`
      ## Evaluation start

      Status: ${evaluation}

      Feedback: ${feedback}
      \n
    `);

    return { evaluation, feedback };
  }

  /*
    Keep generating and evaluating until the evaluator passes the last generated response.
  */
  async function loopWorkflow(
    task: string,
    evaluatorPrompt: string,
    generatorPrompt: string,
  ) {
    // Store previous responses from generator
    const memory = [];

    // Generate initial response
    let response = await generate(task, generatorPrompt);
    memory.push(response);

    while (true) {
      const { evaluation, feedback } = await evaluate(
        task,
        evaluatorPrompt,
        response,
      );

      if (evaluation === "PASS") {
        break;
      }

      const context = dedent`
        Previous attempts:

        ${memory.map((m, i) => `### Attempt ${i + 1}\n\n${m}`).join("\n\n")}

        Feedback: ${feedback}
      `;

      response = await generate(task, generatorPrompt, context);
      memory.push(response);
    }
  }
  ```
</CodeGroup>

## Example Usage

<CodeGroup>
  ```py Python theme={null}
  task = """
  Implement a Stack with:
  1. push(x)
  2. pop()
  3. getMin()
  All operations should be O(1).
  """

  loop_workflow(task, EVALUATOR_PROMPT, GENERATOR_PROMPT)
  ```

  ```ts TypeScript theme={null}
  const task = dedent`
    Implement a Stack with:

      1. push(x)
      2. pop()
      3. getMin()

    All operations should be O(1).
  `;

  loopWorkflow(task, EVALUATOR_PROMPT, GENERATOR_PROMPT);
  ```
</CodeGroup>

## Use cases

* Generating code that meets specific requirements, such as ensuring runtime complexity.
* Searching for information and using an evaluator to verify that the results include all the required details.
* Writing a story or article with specific tone or style requirements and using an evaluator to ensure the output matches the desired criteria, such as adhering to a particular voice or narrative structure.
* Generating structured data from unstructured input and using an evaluator to verify that the data is properly formatted, complete, and consistent.
* Creating user interface text, like tooltips or error messages, and using an evaluator to confirm the text is concise, clear, and contextually appropriate.

<Note>
  ### Iterative Workflow Cookbook

  For a more detailed walk-through refer to the [notebook here](https://togetherai.link/agent-recipes-deep-dive-evaluator) .
</Note>


# Structured Outputs
Source: https://docs.together.ai/docs/json-mode

Learn how to use JSON mode to get structured outputs from LLMs like DeepSeek V3 & Llama 3.3.

## Introduction

Standard large language models respond to user queries by generating plain text. This is great for many applications like chatbots, but if you want to programmatically access details in the response, plain text is hard to work with.

Some models have the ability to respond with structured JSON instead, making it easy to work with data from the LLM's output directly in your application code.

If you're using a supported model, you can enable structured responses by providing your desired schema details to the `response_format` key of the Chat Completions API.

## Supported models

The following newly released top models support JSON mode:

* `openai/gpt-oss-120b`
* `openai/gpt-oss-20b`
* `moonshotai/Kimi-K2-Instruct`
* `zai-org/GLM-4.5-Air-FP8`
* `Qwen/Qwen3-Next-80B-A3B-Instruct`
* `Qwen/Qwen3-Next-80B-A3B-Thinking`
* `Qwen/Qwen3-235B-A22B-Thinking-2507`
* `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`
* `Qwen/Qwen3-235B-A22B-Instruct-2507-tput`
* `deepseek-ai/DeepSeek-R1`
* `deepseek-ai/DeepSeek-R1-0528-tput`
* `deepseek-ai/DeepSeek-V3`
* `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8`
* `Qwen/Qwen2.5-72B-Instruct-Turbo`
* `Qwen/Qwen2.5-VL-72B-Instruct`

The rest of the models that support JSON mode include:

* `meta-llama/Llama-4-Scout-17B-16E-Instruct`
* `meta-llama/Llama-3.3-70B-Instruct-Turbo`
* `deepcogito/cogito-v2-preview-llama-70B`
* `deepcogito/cogito-v2-preview-llama-109B-MoE`
* `deepcogito/cogito-v2-preview-llama-405B`
* `deepcogito/cogito-v2-preview-deepseek-671b`
* `deepseek-ai/DeepSeek-R1-Distill-Llama-70B`
* `deepseek-ai/DeepSeek-R1-Distill-Qwen-14B`
* `marin-community/marin-8b-instruct`
* `meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo`
* `meta-llama/Llama-3.3-70B-Instruct-Turbo-Free`
* `Qwen/Qwen2.5-7B-Instruct-Turbo`
* `Qwen/Qwen2.5-Coder-32B-Instruct`
* `Qwen/QwQ-32B`
* `Qwen/Qwen3-235B-A22B-fp8-tput`
* `arcee-ai/coder-large`
* `meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo`
* `meta-llama/Llama-3.2-3B-Instruct-Turbo`
* `meta-llama/Meta-Llama-3-8B-Instruct-Lite`
* `meta-llama/Llama-3-70b-chat-hf`
* `google/gemma-3n-E4B-it`
* `mistralai/Mistral-7B-Instruct-v0.1`
* `mistralai/Mistral-7B-Instruct-v0.2`
* `mistralai/Mistral-7B-Instruct-v0.3`
* `arcee_ai/arcee-spotlight`

## Basic example

Let's look at a simple example, where we pass a transcript of a voice note to a model and ask it to summarize it.

We want the summary to have the following structure:

```json JSON theme={null}
{
  "title": "A title for the voice note",
  "summary": "A short one-sentence summary of the voice note",
  "actionItems": ["Action item 1", "Action item 2"]
}
```

We can tell our model to use this structure by giving it a [JSON Schema](https://json-schema.org/) definition. Since writing JSON Schema by hand is a bit tedious, we'll use a library to help – Pydantic in Python, and Zod in TypeScript.

Once we have the schema, we can include it in the system prompt and give it to our model using the `response_format` key.

Let's see what this looks like:

<CodeGroup>
  ```py Python theme={null}
  import json
  import together
  from pydantic import BaseModel, Field

  client = together.Together()


  ## Define the schema for the output
  class VoiceNote(BaseModel):
      title: str = Field(description="A title for the voice note")
      summary: str = Field(
          description="A short one sentence summary of the voice note."
      )
      actionItems: list[str] = Field(
          description="A list of action items from the voice note"
      )


  def main():
      transcript = (
          "Good morning! It's 7:00 AM, and I'm just waking up. Today is going to be a busy day, "
          "so let's get started. First, I need to make a quick breakfast. I think I'll have some "
          "scrambled eggs and toast with a cup of coffee. While I'm cooking, I'll also check my "
          "emails to see if there's anything urgent."
      )

      # Call the LLM with the JSON schema
      extract = client.chat.completions.create(
          messages=[
              {
                  "role": "system",
                  "content": f"The following is a voice message transcript. Only answer in JSON and follow this schema {json.dumps(VoiceNote.model_json_schema())}.",
              },
              {
                  "role": "user",
                  "content": transcript,
              },
          ],
          model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
          response_format={
              "type": "json_schema",
              "schema": VoiceNote.model_json_schema(),
          },
      )

      output = json.loads(extract.choices[0].message.content)
      print(json.dumps(output, indent=2))
      return output


  main()
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";
  import { z } from "zod";
  import { zodToJsonSchema } from "zod-to-json-schema";

  const together = new Together();

  // Defining the schema we want our data in
  const voiceNoteSchema = z.object({
    title: z.string().describe("A title for the voice note"),
    summary: z
      .string()
      .describe("A short one sentence summary of the voice note."),
    actionItems: z
      .array(z.string())
      .describe("A list of action items from the voice note"),
  });
  const jsonSchema = zodToJsonSchema(voiceNoteSchema, { target: "openAi" });

  async function main() {
    const transcript =
      "Good morning! It's 7:00 AM, and I'm just waking up. Today is going to be a busy day, so let's get started. First, I need to make a quick breakfast. I think I'll have some scrambled eggs and toast with a cup of coffee. While I'm cooking, I'll also check my emails to see if there's anything urgent.";
    const extract = await together.chat.completions.create({
      messages: [
        {
          role: "system",
          content: `The following is a voice message transcript. Only answer in JSON and follow this schema ${JSON.stringify(jsonSchema)}.`,
        },
        {
          role: "user",
          content: transcript,
        },
      ],
      model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      response_format: { type: "json_object", schema: jsonSchema },
    });

    if (extract?.choices?.[0]?.message?.content) {
      const output = JSON.parse(extract?.choices?.[0]?.message?.content);
      console.log(output);
      return output;
    }
    return "No output.";
  }

  main();
  ```

  ```Text curl theme={null}
  curl -X POST https://api.together.xyz/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -d '{
    "messages": [
      {
        "role": "system",
        "content": "The following is a voice message transcript. Only answer in JSON."
      },
      {
        "role": "user",
        "content": "Good morning! It'"'"'s 7:00 AM, and I'"'"'m just waking up. Today is going to be a busy day, so let'"'"'s get started. First, I need to make a quick breakfast. I think I'"'"'ll have some scrambled eggs and toast with a cup of coffee. While I'"'"'m cooking, I'"'"'ll also check my emails to see if there'"'"'s anything urgent."
      }
    ],
    "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    "response_format": {
      "type": "json_object",
      "schema": {
        "properties": {
          "title": {
            "description": "A title for the voice note",
            "title": "Title",
            "type": "string"
          },
          "summary": {
            "description": "A short one sentence summary of the voice note.",
            "title": "Summary",
            "type": "string"
          },
          "actionItems": {
            "description": "A list of action items from the voice note",
            "items": { "type": "string" },
            "title": "Actionitems",
            "type": "array"
          }
        },
        "required": ["title", "summary", "actionItems"],
        "title": "VoiceNote",
        "type": "object"
      }
    }
  }'
  ```
</CodeGroup>

If we try it out, our model responds with the following:

```json JSON theme={null}
{
  "title": "Morning Routine",
  "summary": "Starting the day with a quick breakfast and checking emails",
  "actionItems": [
    "Cook scrambled eggs and toast",
    "Brew a cup of coffee",
    "Check emails for urgent messages"
  ]
}
```

Pretty neat!

Our model has generated a summary of the user's transcript using the schema we gave it.

### Prompting the model

It's important to always tell the model to respond **only in JSON** and include a plain‑text copy of the schema in the prompt (either as a system prompt or a user message). This instruction must be given *in addition* to passing the schema via the `response_format` parameter.

By giving an explicit "respond in JSON" direction and showing the schema text, the model will generate output that matches the structure you defined. This combination of a textual schema and the `response_format` setting ensures consistent, valid JSON responses every time.

## Regex example

All the models supported for JSON mode also support regex mode. Here's an example using it to constrain the classification.

<CodeGroup>
  ```py Python theme={null}
  import together

  client = together.Together()

  completion = client.chat.completions.create(
      model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
      messages=[
          {
              "role": "system",
              "content": "You are an AI-powered expert specializing in classifying sentiment. You will be provided with a text, and your task is to classify its sentiment as positive, neutral, or negative.",
          },
          {"role": "user", "content": "Wow. I loved the movie!"},
      ],
      response_format={
          "type": "regex",
          "pattern": "(positive|neutral|negative)",
      },
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";
  const together = new Together();

  async function main() {
    const completion = await together.chat.completions.create({
      model: "meta-llama/Llama-3.3-70B-Instruct-Turbo",
      temperature: 0.2,
      max_tokens: 10,
      messages: [
        {
          role: "system",
          content:
            "You are an AI-powered expert specializing in classifying sentiment. You will be provided with a text, and your task is to classify its sentiment as positive, neutral, or negative.",
        },
        {
          role: "user",
          content: "Wow. I loved the movie!",
        },
      ],
      response_format: {
        type: "regex",
        // @ts-ignore
        pattern: "(positive|neutral|negative)",
      },
    });

    console.log(completion?.choices[0]?.message?.content);
  }

  main();
  ```

  ```curl cURL theme={null}
  curl https://api.together.xyz/v1/chat/completions \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
      "messages": [
        {
          "role": "user",
          "content": "Return only an email address for Alan Turing at Enigma. End with .com and newline."
        }
      ],
      "stop": ["\n"],
      "response_format": {
        "type": "regex",
        "pattern": "\\w+@\\w+\\.com\\n"
      },
      "temperature": 0.0,
      "max_tokens": 50
    }'
  ```
</CodeGroup>

## Reasoning model example

You can also extract structured outputs from some reasoning models such as `DeepSeek-R1-0528`.

Below we ask the model to solve a math problem step-by-step showing its work:

```py Python theme={null}
import json
import together
from pydantic import BaseModel, Field

client = together.Together()


class Step(BaseModel):
    explanation: str
    output: str


class MathReasoning(BaseModel):
    steps: list[Step]
    final_answer: str


completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful math tutor. Guide the user through the solution step by step.",
        },
        {"role": "user", "content": "how can I solve 8x + 7 = -23"},
    ],
    response_format={
        "type": "json_schema",
        "schema": MathReasoning.model_json_schema(),
    },
)

math_reasoning = json.loads(completion.choices[0].message.content)

print(json.dumps(math_reasoning, indent=2))
```

Example output:

```json JSON theme={null}
{
  "steps": [
    {
      "explanation": "To solve the equation 8x + 7 = -23, I need to isolate the variable x on one side of the equation. That means I'll have to get rid of the constant term and the coefficient of x.",
      "output": ""
    },
    {
      "explanation": "First, I'll eliminate the constant term on the left side. Since it's +7, I can subtract 7 from both sides of the equation. This keeps the equation balanced.",
      "output": "8x + 7 - 7 = -23 - 7"
    },
    {
      "explanation": "Now, simplifying both sides: on the left, 7 - 7 is 0, so I'm left with 8x. On the right, -23 - 7 is -30.",
      "output": "8x = -30"
    },
    {
      "explanation": "Next, I need to solve for x. Since x is multiplied by 8, I should divide both sides by 8 to isolate x.",
      "output": "8x / 8 = -30 / 8"
    },
    {
      "explanation": "Simplifying that, 8x divided by 8 is just x. And -30 divided by 8 is -30/8.",
      "output": "x = -30/8"
    },
    {
      "explanation": "I can simplify this fraction. Both 30 and 8 are divisible by 2. So, -30 divided by 2 is -15, and 8 divided by 2 is 4.",
      "output": "x = -15/4"
    },
    {
      "explanation": "I can also write this as a mixed number or decimal, but the fraction is already simplified. -15/4 is -3.75, but I'll keep it as a fraction since it's exact.",
      "output": "x = -15/4"
    }
  ],
  "final_answer": "x = -\\frac{15}{4}"
}
```

## Vision model example

Let's look at another example, this time using a vision model.

We want our LLM to extract text from the following screenshot of a Trello board:

![Trello board](https://files.readme.io/4512824ce58b18d946c8a8c786a21a5346e18e8b1860fc03de07d69a0145450e-image.png)

In particular, we want to know the name of the project (Project A), and the number of columns in the board (4).

Let's try it out:

<CodeGroup>
  ```py Python theme={null}
  import json
  import together
  from pydantic import BaseModel, Field

  client = together.Together()


  ## Define the schema for the output
  class ImageDescription(BaseModel):
      project_name: str = Field(
          description="The name of the project shown in the image"
      )
      col_num: int = Field(description="The number of columns in the board")


  def main():
      imageUrl = "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/d96a3145-472d-423a-8b79-bca3ad7978dd/trello-board.png"

      # Call the LLM with the JSON schema
      extract = client.chat.completions.create(
          messages=[
              {
                  "role": "user",
                  "content": [
                      {
                          "type": "text",
                          "text": "Extract a JSON object from the image.",
                      },
                      {
                          "type": "image_url",
                          "image_url": {
                              "url": imageUrl,
                          },
                      },
                  ],
              },
          ],
          model="Qwen/Qwen2.5-VL-72B-Instruct",
          response_format={
              "type": "json_schema",
              "schema": ImageDescription.model_json_schema(),
          },
      )

      output = json.loads(extract.choices[0].message.content)
      print(json.dumps(output, indent=2))
      return output


  main()
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";
  import { z } from "zod";
  import { zodToJsonSchema } from "zod-to-json-schema";

  const together = new Together();

  // Define the shape of our data
  const schema = z.object({
    projectName: z
      .string()
      .describe("The name of the project shown in the image"),
    columnCount: z.number().describe("The number of columns in the board"),
  });
  const jsonSchema = zodToJsonSchema(schema, { target: "openAi" });

  const imageUrl =
    "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/d96a3145-472d-423a-8b79-bca3ad7978dd/trello-board.png";

  async function main() {
    const extract = await together.chat.completions.create({
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: "Extract a JSON object from the image." },
            {
              type: "image_url",
              image_url: { url: imageUrl },
            },
          ],
        },
      ],
      model: "Qwen/Qwen2.5-VL-72B-Instruct",
      response_format: {
        type: "json_object",
        schema: jsonSchema,
      },
    });

    if (extract?.choices?.[0]?.message?.content) {
      const output = JSON.parse(extract?.choices?.[0]?.message?.content);
      console.log(output);
      return output;
    }
    return "No output.";
  }

  main();
  ```
</CodeGroup>

If we run it, we get the following output:

```json JSON theme={null}
{
  "projectName": "Project A",
  "columnCount": 4
}
```

JSON mode has worked perfectly alongside Qwen's vision model to help us extract structured text from an image!

## Try out your code in the Together Playground

You can try out JSON Mode in the [Together Playground](https://api.together.ai/playground/v2/chat/Qwen/Qwen2.5-VL-72B-Instruct?) to test out variations on your schema and prompt:

![Playground](https://files.readme.io/464405525305919beed6d35a6e85b48cf5a3149891c4eefcee4d17b79773940c-Screenshot_2025-04-24_at_5.07.55_PM.png)

Just click the RESPONSE FORMAT dropdown in the right-hand sidebar, choose JSON, and upload your schema!


# Kimi K2 QuickStart
Source: https://docs.together.ai/docs/kimi-k2-quickstart

How to get the most out of models like Kimi K2.

Kimi K2 is a state-of-the-art mixture-of-experts (MoE) language model developed by Moonshot AI. It's a 1 trillion total parameter model (32B activated) that is currently the best non-reasoning open source model out there.

It was trained on 15.5 trillion tokens, supports a 256k context window, and excels in agentic tasks, coding, reasoning, and tool use. Even though it's a 1T model, at inference time, the fact that only 32 B parameters are active gives it near‑frontier quality at a fraction of the compute of dense peers.

In this quick guide, we'll go over the main use cases for Kimi K2, how to get started with it, when to use it, and prompting tips for getting the most out of this incredible model.

## How to use Kimi K2

Get started with this model in 10 lines of code! The model ID is `moonshotai/Kimi-K2-Instruct-0905` and the pricing is \$1.00 per 1M input tokens and \$3.00 per 1M output tokens.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()
  resp = client.chat.completions.create(
      model="moonshotai/Kimi-K2-Instruct-0905",
      messages=[{"role": "user", "content": "Code a hacker news clone"}],
      stream=True,
  )
  for tok in resp:
      print(tok.choices[0].delta.content, end="", flush=True)
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';
  const together = new Together();

  const stream = await together.chat.completions.create({
    model: 'moonshotai/Kimi-K2-Instruct-0905',
    messages: [{ role: 'user', content: 'Code a hackernews clone' }],
    stream: true,
  });

  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || '');
  }
  ```
</CodeGroup>

## Use cases

Kimi K2 shines in scenarios requiring autonomous problem-solving – specifically with coding & tool use:

* **Agentic Workflows**: Automate multi-step tasks like booking flights, research, or data analysis using tools/APIs
* **Coding & Debugging**: Solve software engineering tasks (e.g., SWE-bench), generate patches, or debug code
* **Research & Report Generation**: Summarize technical documents, analyze trends, or draft reports using long-context capabilities
* **STEM Problem-Solving**: Tackle advanced math (AIME, MATH), logic puzzles (ZebraLogic), or scientific reasoning
* **Tool Integration**: Build AI agents that interact with APIs (e.g., weather data, databases).

## Prompting tips

| Tip                                                                                                                       | Rationale                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Keep the system prompt simple** - `"You are Kimi, an AI assistant created by Moonshot AI."` is the recommended default. | Matches the prompt used during instruction tuning.                                                                                       |
| **Temperature ≈ 0.6**                                                                                                     | Calibrated to Kimi-K2-Instruct's RLHF alignment curve; higher values yield verbosity.                                                    |
| **Leverage native tool calling**                                                                                          | Pass a JSON schema in `tools=[...]`; set `tool_choice="auto"`. Kimi decides when/what to call.                                           |
| **Think in goals, not steps**                                                                                             | Because the model is "agentic", give a *high-level objective* ("Analyse this CSV and write a report"), letting it orchestrate sub-tasks. |
| **Chunk very long contexts**                                                                                              | 256 K is huge, but response speed drops on >100 K inputs; supply a short executive summary in the final user message to focus the model. |

Many of this information was found in the [Kimi GitHub repo](https://github.com/MoonshotAI/Kimi-K2).

## General Limitations of Kimi K2

We've outlined various use cases for when to use Kimi K2, but it also has a few situations where it currently isn't the best. The main ones are for latency specific applications like real-time voice agents, it's not the best solution currently due to its speed.

Similarly, if you wanted a quick summary for a long PDF, even though it can handle a good amount of context (256k tokens), its speed is a bit prohibitive if you want to show text quickly to your user as it can get even slower when it is given a lot of context. However, if you're summarizing PDFs async for example or in another scenario where latency isn't a concern, this could be a good model to try.


# LangGraph
Source: https://docs.together.ai/docs/langgraph

Using LangGraph with Together AI

LangGraph is an OSS library for building stateful, multi-actor applications with LLMs, specifically designed for agent and multi-agent workflows. The framework supports critical agent architecture features including persistent memory across conversations and human-in-the-loop capabilities through checkpointed states.

## Installing Libraries

<CodeGroup>
  ```shell Python theme={null}
    pip install -U langgraph langchain-together
  ```

  ```shell Typescript theme={null}
    pnpm add @langchain/langgraph @langchain/core  @langchain/community
  ```
</CodeGroup>

Set your Together AI API key:

<CodeGroup>
  ```shell Shell theme={null}
  export TOGETHER_API_KEY=***
  ```
</CodeGroup>

## Example

In this simple example we augment an LLM with a calculator tool!

<CodeGroup>
  ```python Python theme={null}
  import os
  from langchain_together import ChatTogether

  llm = ChatTogether(
      model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
      api_key=os.getenv("TOGETHER_API_KEY"),
  )


  # Define a tool
  def multiply(a: int, b: int) -> int:
      return a * b


  # Augment the LLM with tools
  llm_with_tools = llm.bind_tools([multiply])

  # Invoke the LLM with input that triggers the tool call
  msg = llm_with_tools.invoke("What is 2 times 3?")

  # Get the tool call
  msg.tool_calls
  ```

  ```typescript Typescript theme={null}
  import { ChatTogetherAI } from "@langchain/community/chat_models/togetherai";

  const llm = new ChatTogetherAI({
      model: "meta-llama/Llama-3.3-70B-Instruct-Turbo",
      apiKey: process.env.TOGETHER_API_KEY,
  });

  // Define a tool
  const multiply = {
      name: "multiply",
      description: "Multiply two numbers",
      schema: {
          type: "function",
          function: {
              name: "multiply",
              description: "Multiply two numbers",
              parameters: {
                  type: "object",
                  properties: {
                      a: { type: "number" },
                      b: { type: "number" },
                  },
                  required: ["a", "b"],
              },
          },
      },
  };

  // Augment the LLM with tools
  const llmWithTools = llm.bindTools([multiply]);

  // Invoke the LLM with input that triggers the tool call
  const msg = await llmWithTools.invoke("What is 2 times 3?");

  // Get the tool call
  console.log(msg.tool_calls);
  ```
</CodeGroup>

## Next Steps

<Info>
  ### LangGraph - Together AI Notebook

  Learn more about building agents using LangGraph with Together AI in our:

  * [Agentic RAG Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/LangGraph/Agentic_RAG_LangGraph.ipynb)
  * [Planning Agent Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/LangGraph/LangGraph_Planning_Agent.ipynb)
</Info>


# Code/Language
Source: https://docs.together.ai/docs/language-overview

Learn how to create completions from language and code models.

## Creating a completion

Use `client.completions.create` to create a completion for a code or language models:

<CodeGroup>
  ```py Python theme={null}
  import os
  from together import Together

  client = Together()

  response = client.completions.create(
      model="meta-llama/Llama-2-70b-hf",
      prompt="def fibonacci(n): ",
      stream=True,
  )

  for chunk in response:
      print(chunk.choices[0].text or "", end="", flush=True)
  ```

  ```ts TypeScript theme={null}
  import Together from 'together-ai';

  const together = new Together();

  const response = await together.completions.create({
    model: "meta-llama/Llama-2-70b-hf",
    prompt: 'def bubbleSort(): ',
    stream: true
  });

  for chunk in response:
      console.log(chunk.choices[0].text)
  ```
</CodeGroup>


# Llama 4 Quickstart
Source: https://docs.together.ai/docs/llama4-quickstart

How to get the most out of the new Llama 4 models.

Together AI offers day 1 support for the new Llama 4 multilingual vision models that can analyze multiple images and respond to queries about them.

Register for a [Together AI account](https://api.together.xyz/) to get an API key. New accounts come with free credits to start. Install the Together AI library for your preferred language.

## How to use Llama 4 Models

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()  # API key via api_key param or TOGETHER_API_KEY env var

  # Query image with Llama 4 Maverick model
  response = client.chat.completions.create(
      model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "What can you see in this image?"},
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png"
                      },
                  },
              ],
          }
      ],
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();  // API key via apiKey param or TOGETHER_API_KEY env var

  async function main() {
   const response = await together.chat.completions.create({
     model: "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
     messages: [{
       role: "user",
       content: [
         { type: "text", text: "What can you see in this image?" },
         { type: "image_url", image_url: { url: "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png" }}
       ]
     }]
   });

   console.log(response.choices[0].message.content);
  }

  main();
  ```
</CodeGroup>

### Output

```
The image depicts a serene landscape of Yosemite National Park, featuring a river flowing through a valley surrounded by towering cliffs and lush greenery.

*   **River:**
    *   The river is calm and peaceful, with clear water that reflects the surrounding scenery.
    *   It flows gently from the bottom-left corner to the center-right of the image.
    *   The riverbank is lined with rocks and grasses, adding to the natural beauty of the scene.
*   **Cliffs:**
    *   The cliffs are massive and imposing, rising steeply from the valley floor.
    *   They are composed of light-colored rock, possibly granite, and feature vertical striations.
    *   The cliffs are covered in trees and shrubs, which adds to their rugged charm.
*   **Trees and Vegetation:**
    *   The valley is densely forested, with tall trees growing along the riverbanks and on the cliffsides.
    *   The trees are a mix of evergreen and deciduous species, with some displaying vibrant green foliage.
    *   Grasses and shrubs grow in the foreground, adding texture and color to the scene.
*   **Sky:**
    *   The sky is a brilliant blue, with only a few white clouds scattered across it.
    *   The sun appears to be shining from the right side of the image, casting a warm glow over the scene.

In summary, the image presents a breathtaking view of Yosemite National Park, showcasing the natural beauty of the valley and its surroundings. The calm river, towering cliffs, and lush vegetation all contribute to a sense of serenity and wonder.
```

<Info>
  ### Llama4 Notebook

  If you'd like to see common use-cases in code see our [notebook here](https://github.com/togethercomputer/together-cookbook/blob/main/Getting_started_with_Llama4.ipynb) .
</Info>

## Llama 4 Model Details

### Llama 4 Maverick

* **Model String**: *meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8*

* **Specs**:

  * 17B active parameters (400B total)
  * 128-expert MoE architecture
  * 524,288 context length (will be increased to 1M)
  * Support for 12 languages: Arabic, English, French, German, Hindi, Indonesian, Italian, Portuguese, Spanish, Tagalog, Thai, and Vietnamese
  * Multimodal capabilities (text + images)
  * Support Function Calling

* **Best for**: Enterprise applications, multilingual support, advanced document intelligence

* **Knowledge Cutoff**: August 2024

### Llama 4 Scout

* **Model String**: *meta-llama/Llama-4-Scout-17B-16E-Instruct*

* **Specs**:

  * 17B active parameters (109B total)
  * 16-expert MoE architecture
  * 327,680 context length (will be increased to 10M)
  * Support for 12 languages: Arabic, English, French, German, Hindi, Indonesian, Italian, Portuguese, Spanish, Tagalog, Thai, and Vietnamese
  * Multimodal capabilities (text + images)
  * Support Function Calling

* **Best for**: Multi-document analysis, codebase reasoning, and personalized tasks

* **Knowledge Cutoff**: August 2024

## Function Calling

<CodeGroup>
  ```python Python theme={null}
  import os
  import json
  import openai

  client = openai.OpenAI(
      base_url="https://api.together.xyz/v1",
      api_key=os.environ["TOGETHER_API_KEY"],
  )

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
      }
  ]

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

  response = client.chat.completions.create(
      model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
      messages=messages,
      tools=tools,
      tool_choice="auto",
  )

  print(
      json.dumps(
          response.choices[0].message.model_dump()["tool_calls"],
          indent=2,
      )
  )
  ```
</CodeGroup>

### Output

<CodeGroup>
  ```json JSON theme={null}
  [
    {
      "id": "call_1p75qwks0etzfy1g6noxvsgs",
      "function": {
        "arguments": "{\"location\":\"New York, NY\",\"unit\":\"fahrenheit\"}",
        "name": "get_current_weather"
      },
      "type": "function"
    },
    {
      "id": "call_aqjfgn65d0c280fjd3pbzpc6",
      "function": {
        "arguments": "{\"location\":\"San Francisco, CA\",\"unit\":\"fahrenheit\"}",
        "name": "get_current_weather"
      },
      "type": "function"
    },
    {
      "id": "call_rsg8muko8hymb4brkycu3dm5",
      "function": {
        "arguments": "{\"location\":\"Chicago, IL\",\"unit\":\"fahrenheit\"}",
        "name": "get_current_weather"
      },
      "type": "function"
    }
  ]
  ```
</CodeGroup>

## Query models with multiple images

Currently this model supports **5 images** as input.

<CodeGroup>
  ```python Python theme={null}
  # Multi-modal message with multiple images
  response = client.chat.completions.create(
      model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "Compare these two images."},
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png"
                      },
                  },
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/slack.png"
                      },
                  },
              ],
          }
      ],
  )
  print(response.choices[0].message.content)
  ```
</CodeGroup>

### Output

```
The first image is a collage of multiple identical landscape photos showing a natural scene with rocks, trees, and a stream under a blue sky. The second image is a screenshot of a mobile app interface, specifically the navigation menu of the Canva app, which includes icons for Home, DMs (Direct Messages), Activity, Later, Canvases, and More.

### Comparison:
1. **Content**:
   - The first image focuses on a natural landscape.
   - The second image shows a digital interface from an app.

2. **Purpose**:
   - The first image could be used for showcasing nature, design elements in graphic work, or as a background.
   - The second image represents the functionality and layout of the Canva app's navigation system.

3. **Visual Style**:
   - The first image has vibrant colors and realistic textures typical of outdoor photography.
   - The second image uses flat design icons with a simple color palette suited for user interface design.

4. **Context**:
   - The first image is likely intended for artistic or environmental contexts.
   - The second image is relevant to digital design and app usability discussions.
```

## Llama 4 Use-cases

### Llama 4 Maverick:

* **Instruction following and Long context ICL**: Very consistent in following precise instructions with in-context learning across very long contexts
* **Multilingual customer support**: Process support tickets with screenshots in 12 languages to quickly diagnose technical issues
* **Multimodal capabilities**: Particularly strong at OCR and chart/graph interpretation
* **Agent/tool calling work**: Designed for agentic workflows with consistent tool calling capabilities

### Llama 4 Scout:

* **Summarization**: Excels at condensing information effectively
* **Function calling**: Performs well in executing predefined functions
* **Long context ICL recall**: Shows strong ability to recall information from long contexts using in-context learning
* **Long Context RAG**: Serves as a workhorse model for coding flows and RAG (Retrieval-Augmented Generation) applications
* **Cost-efficient**: Provides good performance as an affordable long-context model


# Getting Started with Logprobs
Source: https://docs.together.ai/docs/logprobs

Learn how to return log probabilities for your output tokens & build better classifiers.

Logprobs, short for log probabilities, are logarithms of probabilities that indicate the likelihood of each token occurring based on the previous tokens in the context. They allow users to gauge a model's confidence in its outputs and explore alternative responses considered by the model and are beneficial for various applications such as classification tasks, retrieval evaluations, and autocomplete suggestions.

One big use case of using logprobs is to assess how confident a model is in its answer. For example, if you were building a classifier to categorize emails into 5 categories, with logprobs, you can get back the category and the confidence of the model in that token. For example, the LLM can categorize an email as "Spam" with 87% confidence. You can then make decisions based on this probability like if it's too low, having a larger LLM classify a specific email.

## Returning logprobs

To return logprobs from our API, simply add `logprobs: 1` to your API call as seen below.

<CodeGroup>
  ```python Python theme={null}
  from together import Together
  import json

  client = Together()

  completion = client.chat.completions.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      messages=[
          {
              "role": "system",
              "content": "What are the top 3 things to do in New York?",
          }
      ],
      max_tokens=10,
      logprobs=1,
  )

  print(json.dumps(completion.model_dump(), indent=1))
  ```
</CodeGroup>

### Response of returning logprobs

Here's the response you can expect. You'll notice both the tokens and the log probability of every token is shown.

```json  theme={null}
{
  "id": "nrFCEVD-2j9zxn-934d8c409a0f43fd",
  "object": "chat.completion",
  "created": 1745413268,
  "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
  "choices": [
    {
      "index": 0,
      "logprobs": {
        "tokens": [
          "New",
          " York",
          " City",
          " is",
          " a",
          " vibrant",
          " and",
          " diverse",
          " destination",
          " with"
        ],
        "token_logprobs": [
          -0.39648438, -2.026558e-6, -0.3515625, -0.609375, -0.023803711,
          -0.53125, -0.03149414, -0.43359375, -0.38085938, -0.74609375
        ],
        "token_ids": [3648, 4356, 4409, 374, 264, 34076, 323, 17226, 9284, 449],
        "top_logprobs": [
          { "New": -0.39648438 },
          { " York": -2.026558e-6 },
          { " City": -0.3515625 },
          { " is": -0.609375 },
          { " a": -0.023803711 },
          { " vibrant": -0.53125 },
          { " and": -0.03149414 },
          { " diverse": -0.43359375 },
          { " destination": -0.38085938 },
          { " with": -0.74609375 }
        ]
      },
      "seed": 15158565520978651000,
      "finish_reason": "length",
      "message": {
        "role": "assistant",
        "content": "New York City is a vibrant and diverse destination with",
        "tool_calls": []
      }
    }
  ],
  "prompt": [],
  "usage": {
    "prompt_tokens": 48,
    "completion_tokens": 10,
    "total_tokens": 58,
    "cached_tokens": 0
  }
}
```

## Converting logprobs to probabilities

Let's take the first token from the previous example: `{ "New": -0.39648438 }`. The "New" token has a logprob of -0.39648438, but this isn't very helpful by itself. However, we can quickly convert it to a probability by taking the exponential of it.

<CodeGroup>
  ```python Python theme={null}
  import math


  def get_probability(logprob: float) -> float:
      return round(math.exp(logprob) * 100, 2)


  print(get_probability(-0.39648438))
  # 67.02%
  ```
</CodeGroup>

This tells us that the model's confidence in starting with "New" was 67%. Let's now look at a practical example where this would be useful.

## A practical example for logprobs: Classification

In this example, we're building an email classifier and we want to know how confident the model is in its answer. We give the LLM 4 categories in the system prompt then pass in an example email.

<CodeGroup>
  ```python Python theme={null}
  from together import Together
  import json

  client = Together()

  completion = client.chat.completions.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      messages=[
          {
              "role": "system",
              "content": "You are a helpful email categorizer. Given an email, please classify it as one of the following categories: 'work', 'personal', 'spam', or 'other'. ONLY respond with the category name.",
          },
          {
              "role": "user",
              "content": "I hope this message finds you well. I am writing to request a meeting next week to discuss the progress of Project X. We have reached several key milestones, and I believe it would be beneficial to review our current status and plan the next steps together.Could we schedule a time that works best for you? Please let me know your availability between Tuesday and Thursday next week. Also, lmk if you still wanna grab dinner on Friday!.",
          },
      ],
      logprobs=1,
  )

  print(completion.choices[0].logprobs.top_logprobs)
  ```
</CodeGroup>

The output is the following:

```json  theme={null}
[{'work': -0.012512207}, {'<|eot_id|>': -0.005706787}]
```

This means that the model chose "work" as the answer, which is correct, and the logprob for work was `-0.012512207`. After taking the exponential of this, we get a probability of 98.7%. We're using a small and fast LLM here (llama 3.1 8B) which is great, but using logprobs, we can also tell when the model is unsure of its answer and see if we need to route it to a bigger LLM.

## Conclusion

We were able to use `logprobs` to show how to build a more robust classifier (and a cheaper classifier, using a smaller model for most queries but selectively using bigger models when needed). There are many other use cases for `logprobs` around autocompletion, keyword selection, and moderation.


# Serverless LoRA Inference
Source: https://docs.together.ai/docs/lora-inference

Deploy a fine-tuned or uploaded LoRA model on serverless for inference

LoRA (Low-Rank Adaptation of LLMs) is a popular and lightweight training technique that significantly reduces the number of trainable parameters. It works by inserting a smaller number of new weights into the model and only these are trained. During inference these updated weights are added to the frozen original model weights. This makes training with LoRA much faster, memory-efficient, and produces smaller model weights (a few hundred MBs), which are easier to store and share.

## Running LoRA Inference on Together

The Together API now supports LoRA inference on select base models, allowing you to either:

1. Do LoRA fine-tuning on the many available models through Together AI, then run inference right away
2. Bring Your Own Adapters: If you have custom LoRA adapters, that you've trained or obtained from HuggingFace, you can upload them and run inference

You can follow the instructions provided in the [Fine-Tuning Overview](/docs/fine-tuning-quickstart) to get started with LoRA Fine-tuning. Otherwise, follow the instructions below.

Adapters trained previous to 12/17 will not be available for LoRA serverless at the moment. We will be migrating your previous adapters to work with LoRA Serverless. A workaround is to download the adapter and re-upload it using Option 2 below.

## Supported Base Models

Currently, LoRA inference is supported for adapters based on the following base models in Together API. Whether using pre-fine-tuned models or bringing your own adapters, these are the only compatible models:

| Organization | Base Model Name           | Base Model String                                | Quantization |
| :----------- | :------------------------ | :----------------------------------------------- | :----------- |
| Meta         | Llama 4 Maverick Instruct | meta-llama/Llama-4-Maverick-17B-128E-Instruct    | FP8          |
| Meta         | Llama 3.1 8B Instruct     | meta-llama/Meta-Llama-3.1-8B-Instruct-Reference  | BF16         |
| Meta         | Llama 3.1 70B Instruct    | meta-llama/Meta-Llama-3.1-70B-Instruct-Reference | BF16         |
| Alibaba      | Qwen2.5 14B Instruct      | Qwen/Qwen2.5-14B-Instruct\*                      | FP8          |
| Alibaba      | Qwen2.5 72B Instruct      | Qwen/Qwen2.5-72B-Instruct                        | FP8          |

## Option 1: Fine-tune your LoRA model and run inference on it on Together

The Together API supports both LoRA and full fine-tuning. For serverless LoRA inference, follow these steps:

**Step 1: Fine-Tune with LoRA on Together API:** To start a Fine-tuning job with LoRA, follow the detailed instructions in the [Fine-Tuning Overview,](/docs/fine-tuning-overview) or follow the below snippets as a quick start:

<CodeGroup>
  ```curl CLI theme={null}
  together files upload "your-datafile.jsonl"
  ```

  ```python Python theme={null}
  import os
  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

  resp = client.files.upload(file="your-datafile.jsonl")

  print(resp.model_dump())
  ```
</CodeGroup>

<CodeGroup>
  ```curl CLI theme={null}
  together fine-tuning create \
    --training-file "file-629e58b4-ff73-438c-b2cc-f69542b27980" \
    --model "meta-llama/Meta-Llama-3.1-8B-Instruct-Reference" \
    --lora
  ```

  ```python Python theme={null}
  import os
  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

  response = client.fine_tuning.create(
      training_file=file_resp.id,
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
      lora=True,
  )

  print(response)
  ```
</CodeGroup>

If you plan to use a validation set, make sure to set the `--validation-file` and `--n-evals` (the number of evaluations over the entire job) parameters. `--n-evals` needs to be set as a number above 0 in order for your validation set to be used.

**Step 2: Run LoRA Inference**:

Once you submit the fine-tuning job you should be able to see the model name in the response:

<CodeGroup>
  ```json Json theme={null}
  {
    "id": "ft-44129430-ac08-4136-9774-aed81e0164a4",
    "training_file": "file-629e58b4-ff73-438c-b2cc-f69542b27980",
    "validation_file": "",
    "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
    "output_name": "zainhas/Meta-Llama-3.1-8B-Instruct-Reference-my-demo-finetune-4224205a",
    ...
  }
  ```
</CodeGroup>

You can also see the status of the job and get the model name if you navigate to your fine-tuned model in the 'Model' or 'Jobs' tab in the Together dashboard. You'll see a model string – use it through the Together API.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7e332c714e184d6d4d9554b761a6e350" alt="" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=cc3d85962dac161d2842617ce37f0b45 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=2081ba31e7cb4fa4d9cacb96d4a08976 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=db9915d04970709baaa0ee97c53d3235 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a051712d1d8408ba70701d81dc41aef3 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=6677dee05d46a3641aa28021bb3ddcf5 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7a83d855bf5a9d4dd8f4fc26497cdb19 2500w" />
</Frame>

<CodeGroup>
  ```curl cURL theme={null}
  MODEL_NAME_FOR_INFERENCE="zainhas/Meta-Llama-3.1-8B-Instruct-Reference-my-demo-finetune-4224205a"

  curl -X POST https://api.together.xyz/v1/completions \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "'$MODEL_NAME_FOR_INFERENCE'",
      "messages": [
        {
          "role": "user",
          "content": "debate the pros and cons of AI",
        },
      ],
      "max_tokens": 128
    }'
  ```

  ```python Python theme={null}
  import os
  from together import Together

  client = Together(api_key=TOGETHERAI_API_KEY)

  user_prompt = "debate the pros and cons of AI"

  response = client.chat.completions.create(
      model="zainhas/Meta-Llama-3.1-8B-Instruct-Reference-my-demo-finetune-4224205a",
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
    model: 'zainhas/Meta-Llama-3.1-8B-Instruct-Reference-my-demo-finetune-4224205a',
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

Expected Response:

<CodeGroup>
  ```json JSON theme={null}
  {
    "id": "8f2cb236c80ea20e-YYZ",
    "object": "text.completion",
    "created": 1734331375,
    "model": "zainhas/Meta-Llama-3.1-8B-Instruct-Reference-my-demo-finetune-4224205a",
    "prompt": [],
    "choices": [
      {
        "text": "Here's a debate on the pros and cons of AI:\n\n**Moderator:** Welcome to today's debate on the pros and cons of AI. We have two debaters, Alex and Ben, who will present their arguments on the topic. Alex will argue in favor of AI, while Ben will argue against it. Let's begin with opening statements.\n\n**Alex (In Favor of AI):** Thank you, Moderator. AI has revolutionized the way we live and work. It has improved efficiency, productivity, and accuracy in various industries, such as healthcare, finance, and transportation. AI-powered systems can analyze vast amounts of data, identify",
        "finish_reason": "length",
        "seed": 5626645655383684000,
        "logprobs": null,
        "index": 0
      }
    ],
    "usage": {
      "prompt_tokens": 18,
      "completion_tokens": 128,
      "total_tokens": 146,
      "cache_hit_rate": 0
    }
  }
  ```
</CodeGroup>

Your first couple queries may have slow TTFT (up to 10 seconds) but subsequent queries should be fast!

## Option 2: Upload a Custom Adapter & run inference on it on Together

The Together API also allows you to upload your own private LoRA adapter files for inference. To upload a custom adapter:

### **Step 1: Prepare Adapter File:**

Ensure your adapter file is compatible with the above supported base models.

If you are getting the adapter from HuggingFace you can find information about the base model there as well.

You need to make sure that the adapter you are trying to upload has an `adapter_config.json` and `adapter_model.safetensors` files.

### **Step 2: Upload Adapter Using Together API:**

**Source 1: Source the adapter from an AWS s3 bucket:**

<CodeGroup>
  ```curl cURL theme={null}
  #!/bin/bash
  # uploadadapter.sh

  # Generate presigned adapter url
  ADAPTER_URL="s3://test-s3-presigned-adapter/my-70B-lora-1.zip"
  PRESIGNED_ADAPTER_URL=$(aws s3 presign ${ADAPTER_URL})

  # Specify additional params
  MODEL_TYPE="adapter"
  ADAPTER_MODEL_NAME="test-lora-model-70B-1"
  BASE_MODEL="meta-llama/Meta-Llama-3.1-70B-Instruct"
  DESCRIPTION="test_70b_lora_description" # Lazy curl replace below, don't put spaces here.

  # Upload
  curl -v https://api.together.xyz/v0/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -d '{
    "model_name": "'${ADAPTER_MODEL_NAME}'",
    "model_source": "'${PRESIGNED_ADAPTER_URL}'",
    "model_type": "'${MODEL_TYPE}'",
    "base_model": "'${BASE_MODEL}'",
    "description": "'${DESCRIPTION}'"
  }'
  ```
</CodeGroup>

**Source 2: Source the adapter from HuggingFace:**

Make sure that the adapter contains `adapter_config.json` and `adapter_model.safetensors` files in Files and versions tab on HuggingFace.

<CodeGroup>
  ```curl cURL theme={null}
  # From HuggingFace
  HF_URL="https://huggingface.co/reissbaker/llama-3.1-8b-abliterated-lora"

  MODEL_TYPE="adapter"
  BASE_MODEL="meta-llama/Meta-Llama-3.1-8B-Instruct-Reference"
  DESCRIPTION="test_lora_8B"
  ADAPTER_MODEL_NAME=test-lora-model-creation-8b
  HF_TOKEN=hf_token
  TOGETHER_API_KEY=together-api-key

  # Upload
  curl -v https://api.together.xyz/v0/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -d '{
    "model_name": "'${ADAPTER_MODEL_NAME}'",
    "model_source": "'${HF_URL}'",
    "model_type": "'${MODEL_TYPE}'",
    "description": "'${DESCRIPTION}'",
    "hf_token": "'${HF_TOKEN}'"
  }'
  ```
</CodeGroup>

For both Option 1 and 2 the output contains the "job\_id" and "model\_name". The model name must be unique, if you attempt to upload a model name that previously was uploaded you will receive a "Model name already exists" error.

<CodeGroup>
  ```json JSON theme={null}
  {
    "data": {
      "job_id": "job-b641db51-38e8-40f2-90a0-5353aeda6f21",   <------- Job ID
      "model_name": "devuser/test-lora-model-creation-8b",
      "model_source": "remote_archive"
    },
    "message": "job created"
  }
  ```
</CodeGroup>

You can poll our API using the "job\_id" until the adapter has finished uploading.

<CodeGroup>
  ```curl cURL theme={null}
  curl https://api.together.xyz/v1/jobs/job-b641db51-38e8-40f2-90a0-5353aeda6f21 \
    -H "Authorization: Bearer $TOGETHER_API_KEY" | jq .
  ```
</CodeGroup>

The output contains a "status" field. When the "status" is "Complete", your adapter is ready!

<CodeGroup>
  ```json JSON theme={null}
  {
    "type": "adapter_upload",
    "job_id": "job-b641db51-38e8-40f2-90a0-5353aeda6f21",
    "status": "Complete",
    "status_updates": []
  }
  ```
</CodeGroup>

### **Step 3: Run LoRA Inference**:

Take the model\_name string you get from the adapter upload output below, then use it through the Together API.

<CodeGroup>
  ```json JSON theme={null}
  {
    "data": {
      "job_id": "job-b641db51-38e8-40f2-90a0-5353aeda6f21",
      "model_name": "devuser/test-lora-model-creation-8b",      <------ Model Name
      "model_source": "remote_archive"
    },
    "message": "job created"
  }
  ```
</CodeGroup>

Make Together API call to the model:

<CodeGroup>
  ```curl cURL theme={null}
  MODEL_NAME_FOR_INFERENCE="devuser/test-lora-model-creation-8b"

   curl -X POST https://api.together.xyz/v1/completions \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "'$MODEL_NAME_FOR_INFERENCE'",
      "prompt": "Q: The capital of France is?\nA:",
      "temperature": 0.8,
      "max_tokens": 128
    }'
  ```
</CodeGroup>

Expected Response:

<CodeGroup>
  ```json JSON theme={null}
  {
    "id": "8f3317dd3c3a39ef-YYZ",
    "object": "text.completion",
    "created": 1734398453,
    "model": "devuser/test-lora-model-creation-8b",
    "prompt": [],
    "choices": [
      {
        "text": " Paris\nB: Berlin\nC: Warsaw\nD: London\nAnswer: A",
        "finish_reason": "eos",
        "seed": 13424880326038300000,
        "logprobs": null,
        "index": 0
      }
    ],
    "usage": {
      "prompt_tokens": 10,
      "completion_tokens": 18,
      "total_tokens": 28,
      "cache_hit_rate": 0
    }
  }
  ```
</CodeGroup>

## LoRA Adapter Limits

You are limited to the following number of LoRA adapters hosted based on build tier:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/bc98169540fb29568558f6882c1a1ac8d2fb988269c49742b26a91afa1241094-image.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=f27e607b8a55dfa1016c1954168ed2cd" alt="" data-og-width="1210" width="1210" data-og-height="800" height="800" data-path="images/docs/bc98169540fb29568558f6882c1a1ac8d2fb988269c49742b26a91afa1241094-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/bc98169540fb29568558f6882c1a1ac8d2fb988269c49742b26a91afa1241094-image.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5a87885e453221fd1c1916bffa8fa683 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/bc98169540fb29568558f6882c1a1ac8d2fb988269c49742b26a91afa1241094-image.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d9b1785fa2d5bb1ff45b88abd4ba4d31 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/bc98169540fb29568558f6882c1a1ac8d2fb988269c49742b26a91afa1241094-image.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c3bd41e1355239974123600a03114b7c 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/bc98169540fb29568558f6882c1a1ac8d2fb988269c49742b26a91afa1241094-image.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d96222e04affc12d32d58c64c4b2cd71 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/bc98169540fb29568558f6882c1a1ac8d2fb988269c49742b26a91afa1241094-image.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=72eeecb9e1a069c700ce19539a7ab5c8 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/bc98169540fb29568558f6882c1a1ac8d2fb988269c49742b26a91afa1241094-image.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a188a9c10919e3006d5adfb866bb5a0e 2500w" />
</Frame>


# Together Mixture Of Agents (MoA)
Source: https://docs.together.ai/docs/mixture-of-agents



<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/1.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=02766bf41d0316857249b3c6f9ec2018" alt="" data-og-width="2588" width="2588" data-og-height="1350" height="1350" data-path="images/guides/1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/1.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c6c27dc0c366ca8b2a755e260b272a6e 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/1.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=0c4d554476f94c2fcaad2cddcd17bfec 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/1.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=29bad505a1c5776526b4d46f5eb8440a 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/1.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=f4d742f2d7f2ed140ba87b4636a6c7a2 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/1.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7d0814be47799eb4a50e5cb73945f115 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/1.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a430e65b511573b35350a1202c43ba2a 2500w" />
</Frame>

## What is Together MoA?

Mixture of Agents (MoA) is a novel approach that leverages the collective strengths of multiple LLMs to enhance performance, achieving state-of-the-art results. By employing a layered architecture where each layer comprises several LLM agents, **MoA significantly outperforms** GPT-4 Omni’s 57.5% on AlpacaEval 2.0 with a score of 65.1%, using only open-source models!

The way Together MoA works is that given a prompt, like `tell me the best things to do in SF`, it sends it to 4 different OSS LLMs. It then combines results from all 4, sends it to a final LLM, and asks it to combine all 4 responses into an ideal response. That’s it! It’s just the idea of combining the results of 4 different LLMs to produce a better final output. It’s obviously slower than using a single LLM but it can be great for use cases where latency doesn't matter as much like synthetic data generation.

For a quick summary and 3-minute demo on how to implement MoA with code, watch the video below:

<Frame>
  <iframe class="embedly-embed" src="//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FTvGjgdNC0P8%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DTvGjgdNC0P8&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FTvGjgdNC0P8%2Fhqdefault.jpg&key=7788cb384c9f4d5dbbdbeffd9fe4b92f&type=text%2Fhtml&schema=youtube" width="854" height="480" scrolling="no" title="YouTube embed" frameborder="0" allow="autoplay; fullscreen; encrypted-media; picture-in-picture;" allowfullscreen="true" />
</Frame>

## Together MoA in 50 lines of code

To get to get started with using MoA in your own apps, you'll need to install the Together python library, get your Together API key, and run the code below which uses our chat completions API to interact with OSS models.

1. Install the Together Python library

```bash Shell theme={null}
pip install together
```

2. Get your [Together API key](https://api.together.xyz/settings/api-keys) & export it

```bash Shell theme={null}
export TOGETHER_API_KEY='xxxx'
```

3. Run the code below, which interacts with our chat completions API.

This implementation of MoA uses 2 layers and 4 LLMs. We’ll define our 4 initial LLMs and our aggregator LLM, along with our prompt. We’ll also add in a prompt to send to the aggregator to combine responses effectively. Now that we have this, we’ll simply send the prompt to the 4 LLMs and compute all results simultaneously. Finally, we'll send the results from the four LLMs to our final LLM, along with a system prompt instructing it to combine them into a final answer, and we’ll stream results back.

```py Python theme={null}
# Mixture-of-Agents in 50 lines of code
import asyncio
import os
from together import AsyncTogether, Together

client = Together()
async_client = AsyncTogether()

user_prompt = "What are some fun things to do in SF?"
reference_models = [
    "Qwen/Qwen2-72B-Instruct",
    "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "mistralai/Mixtral-8x22B-Instruct-v0.1",
    "databricks/dbrx-instruct",
]
aggregator_model = "mistralai/Mixtral-8x22B-Instruct-v0.1"
aggreagator_system_prompt = """You have been provided with a set of responses from various open-source models to the latest user query. Your task is to synthesize these responses into a single, high-quality response. It is crucial to critically evaluate the information provided in these responses, recognizing that some of it may be biased or incorrect. Your response should not simply replicate the given answers but should offer a refined, accurate, and comprehensive reply to the instruction. Ensure your response is well-structured, coherent, and adheres to the highest standards of accuracy and reliability.

Responses from models:"""


async def run_llm(model):
    """Run a single LLM call with a reference model."""
    response = await async_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": user_prompt}],
        temperature=0.7,
        max_tokens=512,
    )
    print(model)
    return response.choices[0].message.content


async def main():
    results = await asyncio.gather(
        *[run_llm(model) for model in reference_models]
    )

    finalStream = client.chat.completions.create(
        model=aggregator_model,
        messages=[
            {"role": "system", "content": aggreagator_system_prompt},
            {
                "role": "user",
                "content": ",".join(str(element) for element in results),
            },
        ],
        stream=True,
    )

    for chunk in finalStream:
        print(chunk.choices[0].delta.content or "", end="", flush=True)


asyncio.run(main())
```

## Advanced MoA example

In the previous example, we went over how to implement MoA with 2 layers (4 LLMs answering and one LLM aggregating). However, one strength of MoA is being able to go through several layers to get an even better response. In this example, we'll go through how to run MoA with 3+ layers.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/2.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=0d8b3ab35cd1c934702082358f0aea7f" alt="" data-og-width="2036" width="2036" data-og-height="926" height="926" data-path="images/guides/2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/2.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d5d56bcaa112033fd024a43c6873ffd4 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/2.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=476fbdc4c0e77ab6e281d11535799e85 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/2.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=838eb9b5f26594a63dab6c57effc376e 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/2.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=436b698543fd544c09b24ac4a0b4aec8 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/2.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=8f99043f81c6b16b8581441f3ad2205e 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/2.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=19b41287a5693e2863443f3becfa36dd 2500w" />
</Frame>

```py Python theme={null}
# Advanced Mixture-of-Agents example – 3 layers
import asyncio
import os
import together
from together import AsyncTogether, Together

client = Together()
async_client = AsyncTogether()

user_prompt = "What are 3 fun things to do in SF?"
reference_models = [
    "Qwen/Qwen2-72B-Instruct",
    "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "mistralai/Mixtral-8x22B-Instruct-v0.1",
    "databricks/dbrx-instruct",
]
aggregator_model = "mistralai/Mixtral-8x22B-Instruct-v0.1"
aggreagator_system_prompt = """You have been provided with a set of responses from various open-source models to the latest user query. Your task is to synthesize these responses into a single, high-quality response. It is crucial to critically evaluate the information provided in these responses, recognizing that some of it may be biased or incorrect. Your response should not simply replicate the given answers but should offer a refined, accurate, and comprehensive reply to the instruction. Ensure your response is well-structured, coherent, and adheres to the highest standards of accuracy and reliability.

Responses from models:"""
layers = 3


def getFinalSystemPrompt(system_prompt, results):
    """Construct a system prompt for layers 2+ that includes the previous responses to synthesize."""
    return (
        system_prompt
        + "\n"
        + "\n".join(
            [f"{i+1}. {str(element)}" for i, element in enumerate(results)]
        )
    )


async def run_llm(model, prev_response=None):
    """Run a single LLM call with a model while accounting for previous responses + rate limits."""
    for sleep_time in [1, 2, 4]:
        try:
            messages = (
                [
                    {
                        "role": "system",
                        "content": getFinalSystemPrompt(
                            aggreagator_system_prompt, prev_response
                        ),
                    },
                    {"role": "user", "content": user_prompt},
                ]
                if prev_response
                else [{"role": "user", "content": user_prompt}]
            )
            response = await async_client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.7,
                max_tokens=512,
            )
            print("Model: ", model)
            break
        except together.error.RateLimitError as e:
            print(e)
            await asyncio.sleep(sleep_time)
    return response.choices[0].message.content


async def main():
    """Run the main loop of the MOA process."""
    results = await asyncio.gather(
        *[run_llm(model) for model in reference_models]
    )

    for _ in range(1, layers - 1):
        results = await asyncio.gather(
            *[
                run_llm(model, prev_response=results)
                for model in reference_models
            ]
        )

    finalStream = client.chat.completions.create(
        model=aggregator_model,
        messages=[
            {
                "role": "system",
                "content": getFinalSystemPrompt(
                    aggreagator_system_prompt, results
                ),
            },
            {"role": "user", "content": user_prompt},
        ],
        stream=True,
    )
    for chunk in finalStream:
        print(chunk.choices[0].delta.content or "", end="", flush=True)


asyncio.run(main())
```

## Resources

* [Together MoA GitHub Repo](https://github.com/togethercomputer/MoA) (includes an interactive demo)
* [Together MoA blog post](https://www.together.ai/blog/together-moa)
* [MoA Technical Paper](https://arxiv.org/abs/2406.04692)


# Multiple API Keys
Source: https://docs.together.ai/docs/multiple-api-keys



## Can I create multiple API keys?

Under [Settings](https://api.together.ai/settings/api-keys) you will find a list of all the API keys associated with the account. Here, you can create a new API key, set an API key name and optionally set an expiration date.

<Note>
  Note: new API keys will not be available to copy after creation. Make sure to copy the API key and save it in a secure location.
</Note>

## What is the Together.ai user key?

Every account has a default API key. You can find and copy this key under Manage Account on the dashboard. For the time being, this first API key cannot be revoked. If it is compromised, it can be regenerated. If this happens, no further work is required on your end, all the Together systems will recognize the regenerated API key as the new default API key.

## Can I set limits on a specific API key?

At this point in time, it is not possible to limit usage of a given API key

## How does the playground work with API keys?

The playground recognizes all of the API keys associated with the account. In the playground, the list of My online models will show the models online across all API keys.

## Can I copy my API key after creating it?

New API keys will be shown only after it is created. Be sure to secure your new API key as soon as it is created. User keys, however, will always be available to copy.


# How to run nanochat on Instant Clusters⚡️
Source: https://docs.together.ai/docs/nanochat-on-instant-clusters

Learn how to train Andrej Karpathy's end-to-end ChatGPT clone on Together's on-demand GPU clusters

## Overview

[nanochat](https://github.com/karpathy/nanochat) is Andrej Karpathy's end-to-end ChatGPT clone that demonstrates how a full conversational AI stack, from tokenizer to web UI—can, be trained and deployed for \$100 on 8×H100 hardware. In this guide, you'll learn how to train and deploy nanochat using Together's [Instant Clusters](https://api.together.ai/clusters).

The entire process takes approximately 4 hours on an 8×H100 cluster and includes:

* Training a BPE tokenizer on [FineWeb-Edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu)
* Pretraining a base transformer model
* Midtraining on curated tasks
* Supervised fine-tuning for conversational alignment
* Deploying a FastAPI web server with a chat interface

## Prerequisites

Before you begin, make sure you have:

* A Together AI account with access to [Instant Clusters](https://api.together.ai/clusters)
* Basic familiarity with SSH and command line operations
* `kubectl` installed on your local machine ([installation guide](https://kubernetes.io/docs/tasks/tools/))

# Training nanochat

## Step 1: Create an Instant Cluster

First, let's create an 8×H100 cluster to train nanochat.

1. Log into [api.together.ai](https://api.together.ai)
2. Click **GPU Clusters** in the top navigation menu
3. Click **Create Cluster**
4. Select **On-demand** capacity
5. Choose **8xH100** as your cluster size
6. Enter a cluster name (e.g., `nanochat-training`)
7. Select **Slurm on Kubernetes** as the cluster type
8. Choose your preferred region
9. Create a shared volume, min 1 TB storage
10. Click **Preview CLuster** and then "Confirm & Create"
    <Frame><img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/1.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=bb1efef1417b404fd8b8aaa50e74eb4c" alt="" data-og-width="3136" width="3136" data-og-height="2598" height="2598" data-path="images/guides/nanochat/1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/1.png?w=280&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=81d379b89146ce7d7fe4706758bca46e 280w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/1.png?w=560&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=756f70fad503cc742dbde7f1e3079ceb 560w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/1.png?w=840&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=714ef6e20e08911c160c80246027cff0 840w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/1.png?w=1100&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=8c9aba3aa3e0feed200d2153f0bdb63b 1100w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/1.png?w=1650&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=1f6ecc3ccba91861d4ddb2e0fe1e342d 1650w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/1.png?w=2500&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=e31df18d9275bcaf0e4b878794cd3353 2500w" /></Frame>

Your cluster will be ready in a few minutes. Once the status shows **Ready**, you can proceed to the next step.

<Info>
  For detailed information about Instant Clusters features and options, see the [Instant Clusters documentation](/docs/instant-clusters).
</Info>

## Step 2: SSH into Your Cluster

From the Instant Clusters UI, you'll find SSH access details for your cluster.

A command like the one below can be copied from the instant clusters dashboard.
<Frame><img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/2.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=4a050ff646ed47e2170097444194b3f3" alt="" data-og-width="3136" width="3136" data-og-height="2598" height="2598" data-path="images/guides/nanochat/2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/2.png?w=280&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=1471b86739a04513ac1e78c1afa1801a 280w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/2.png?w=560&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=dc8482f041ce00798f581a62db347b4f 560w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/2.png?w=840&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=33db19c5345c30d7151f222c1a170842 840w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/2.png?w=1100&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=a7805b729ed28bd5de76e61e9451bd63 1100w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/2.png?w=1650&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=574c4f780ef4f2a828cad63a719d87dd 1650w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/2.png?w=2500&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=398b359f5aa96fbf55a545a64b0f913e 2500w" /></Frame>

<CodeGroup>
  ```bash Shell theme={null}
  ssh <username>@<cluster-hostname>
  ```
</CodeGroup>

You can also use `ssh -o ServerAliveInterval=60` - it sends a ping to the ssh server every 60s, so it keeps the TCP ssh session alive, even if there's no terminal input/output for a long time during training.

Once connected, you'll be in the login node of your Slurm cluster.

## Step 3: Clone nanochat and Set Up Environment

Let's clone the nanochat repository and set up the required dependencies.

<CodeGroup>
  ```bash Shell theme={null}
  # Clone the repository
  git clone https://github.com/karpathy/nanochat.git
  cd nanochat

  # Add ~/.local/bin to your PATH
  export PATH="$HOME/.local/bin:$PATH"

  # Source the Cargo environment
  source "$HOME/.cargo/env"
  ```
</CodeGroup>

**Install System Dependencies**

nanochat requires Python 3.10 and development headers:

<CodeGroup>
  ```bash Shell theme={null}
  # Update package manager and install Python dependencies
  sudo apt-get update
  sudo apt-get install -y python3.10-dev

  # Verify Python installation
  python3 -c "import sysconfig; print(sysconfig.get_path('include'))"
  ```
</CodeGroup>

## Step 4: Access GPU Resources

Use Slurm's `srun` command to allocate 8 GPUs for your training job:

<CodeGroup>
  ```bash Shell theme={null}
  srun --gres=gpu:8 --pty bash
  ```
</CodeGroup>

This command requests 8 GPUs and gives you an interactive bash session on a compute node. Once you're on the compute node, verify GPU access:

<CodeGroup>
  ```bash Shell theme={null}
  nvidia-smi
  ```
</CodeGroup>

You should see all 8 H100 GPUs listed with their memory and utilization stats like below.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/3.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=93378a3fae8db4f27c53c61d4f3c86aa" alt="" data-og-width="2222" width="2222" data-og-height="2196" height="2196" data-path="images/guides/nanochat/3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/3.png?w=280&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=2bf0af7074878754f2b74d8aa0685fee 280w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/3.png?w=560&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=8768e758fced8fb71b506e8ca55b058a 560w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/3.png?w=840&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=3d7cec0dac1089bfd6f4969c5270d341 840w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/3.png?w=1100&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=ce3754eeb833e577bb88c111534c5271 1100w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/3.png?w=1650&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=1bb8b8a7adaf39b46db4a7d3124d58f3 1650w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/3.png?w=2500&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=abab57e1deafde093756bdaa520ee6d0 2500w" />
</Frame>

## Step 5: Configure Cache Directory

To optimize data loading performance, set the nanochat cache directory to the `/scratch` volume, which is optimized for high-throughput I/O:

<CodeGroup>
  ```bash Shell theme={null}
  export NANOCHAT_BASE_DIR="/scratch/$USER/nanochat/.cache/nanochat"
  ```
</CodeGroup>

This needs to be changed inside the `speedrun.sh` file and ensures that dataset streaming, checkpoints, and intermediate artifacts don't bottleneck your training.

<Info>
  This step is critical and without it, during training, you'll notice that your FLOP utilization is only \~13% instead of \~50%. This is due to dataloading bottlenecks.
</Info>

## Step 6: Run the Training Pipeline

Now you're ready to kick off the full training pipeline! nanochat includes a `speedrun.sh` script that orchestrates all training phases:

<CodeGroup>
  ```bash Shell theme={null}
  bash speedrun.sh

  # or you can use screen

  screen -L -Logfile speedrun.log -S speedrun bash speedrun.sh
  ```
</CodeGroup>

This script will execute the following stages:

1. **Tokenizer Training** - Trains a GPT-4 style BPE tokenizer on FineWeb-Edu data
2. **Base Model Pretraining** - Trains the base transformer model with rotary embeddings and Muon optimizer
3. **Midtraining** - Fine-tunes on a curated mixture of SmolTalk, MMLU, and GSM8K tasks
4. **Supervised Fine-Tuning (SFT)** - Aligns the model for conversational interactions
5. **Evaluation** - Runs CORE benchmarks and generates a comprehensive report

The entire training process takes approximately **4 hours** on 8×H100 GPUs.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/4.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=d77d394dee60ff4576f461932ba317df" alt="" data-og-width="2606" width="2606" data-og-height="2212" height="2212" data-path="images/guides/nanochat/4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/4.png?w=280&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=b2832b8925d4f7f4970400ff91a15ec2 280w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/4.png?w=560&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=aad30fd3ce919b479e3dc0281cad59a9 560w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/4.png?w=840&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=ef3fbc34fdbc444163f2e26fb9ebe7c7 840w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/4.png?w=1100&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=3cc7cc6b28114b7ea531358c75b2e509 1100w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/4.png?w=1650&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=f67b83d0e53dcf9fdf7a081fcaf8316a 1650w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/4.png?w=2500&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=a70b3e9c60091511189a4fd0b7d233c5 2500w" />
</Frame>

**Monitor Training Progress**

During training, you can monitor several key metrics:

* **Model Flops Utilization (MFU)**: Should be around 50% for optimal performance
* **tok/sec**: Tracks tokens processed per second of training
* **Step timing**: Each step should complete in a few seconds

The scripts automatically log progress and save checkpoints under `$NANOCHAT_BASE_DIR`.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/5.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=82bdc348257581badd6ef22c819dcd10" alt="" data-og-width="2606" width="2606" data-og-height="2212" height="2212" data-path="images/guides/nanochat/5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/5.png?w=280&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=4e696d8c87ad41292392fb66fc94140a 280w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/5.png?w=560&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=ebb08f3efee42a3c74b55b7fe0a89181 560w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/5.png?w=840&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=4b4512ce3929c97609967e1f2cb39f16 840w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/5.png?w=1100&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=770f79729d0154ba5f5c275e6921eb95 1100w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/5.png?w=1650&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=4ea8ea07ebf4844d562e75036e8858c3 1650w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/5.png?w=2500&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=889ec5da7ce8c3b69d42a1fbe6a2fbdb 2500w" />
</Frame>

# nanochat Inference

## Step 1: Download Your Cluster's Kubeconfig

While training is running (or after it completes), download your cluster's kubeconfig from the Together AI dashboard. This will allow you to access the cluster using kubectl.

1. Go to your cluster in the Together AI dashboard
2. Click on the **View Kubeconfig** button
3. Copy and save the kubeconfig file to your local machine (e.g., `~/.kube/nanochat-cluster-config`)

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/6.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=c879f73961de55cfb06f4dd83602260b" alt="" data-og-width="3136" width="3136" data-og-height="2598" height="2598" data-path="images/guides/nanochat/6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/6.png?w=280&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=0d621d1a52843df9bd39fa7496395be1 280w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/6.png?w=560&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=e89097fbb4bec1503def8ed8abec5507 560w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/6.png?w=840&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=fbafafb52a1b45a98b7f5f97acd50fc3 840w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/6.png?w=1100&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=44fb0683eee383a3cf484fc2ab48a175 1100w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/6.png?w=1650&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=4306e9cd6c86e38925364df871826827 1650w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/6.png?w=2500&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=37e57273e371c246aa1a3572b836270f 2500w" />
</Frame>

## Step 2: Access the Compute Pod via kubectl

From your **local machine**, set up kubectl access to your cluster:

<CodeGroup>
  ```bash Shell theme={null}
  # Set the KUBECONFIG environment variable
  export KUBECONFIG=/path/to/nanochat-cluster-config

  # List pods in the slurm namespace
  kubectl -n slurm get pods
  ```
</CodeGroup>

You should see your Slurm compute pods listed. Identify the production pod where your training ran:

<CodeGroup>
  ```bash Shell theme={null}
  # Example output:
  # NAME                              READY   STATUS    RESTARTS   AGE
  # slurm-compute-production-abc123   1/1     Running   0          2h

  # Exec into the pod
  kubectl -n slurm exec -it <your-slurm-compute-production-pod> -- /bin/bash
  ```
</CodeGroup>

Once inside the pod, navigate to the nanochat directory:

<CodeGroup>
  ```bash Shell theme={null}
  cd /path/to/nanochat
  ```
</CodeGroup>

**Set Up Python Virtual Environment**

Inside the compute pod, set up the Python virtual environment using `uv`:

<CodeGroup>
  ```bash Shell theme={null}
  # Install uv (if not already installed)
  command -v uv &> /dev/null || curl -LsSf https://astral.sh/uv/install.sh | sh

  # Create a local virtual environment
  [ -d ".venv" ] || uv venv

  # Install the repo dependencies with GPU support
  uv sync --extra gpu

  # Activate the virtual environment
  source .venv/bin/activate
  ```
</CodeGroup>

## Step 3: Launch the nanochat Web Server

Now that training is complete and your environment is set up, launch the FastAPI web server:

<CodeGroup>
  ```bash Shell theme={null}
  python -m scripts.chat_web
  ```
</CodeGroup>

The server will start on port 8000 inside the pod. You should see output indicating the server is running:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/7.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=7fec3be4e92c726b1f9490dfae41c6bc" alt="" data-og-width="2422" width="2422" data-og-height="1666" height="1666" data-path="images/guides/nanochat/7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/7.png?w=280&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=7e471e282c932da0fa60e5e9a3c45f84 280w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/7.png?w=560&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=d0efb8d3243e4392c55caf0aea48a53a 560w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/7.png?w=840&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=7823882aa7a3181970cd30615803b4a9 840w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/7.png?w=1100&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=f05fe5c85150fe82d76b28f95cae20ee 1100w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/7.png?w=1650&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=348caa3402aef818bcaf9549322a4914 1650w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/7.png?w=2500&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=c24d88d65056db9f59331b46e49c01f9 2500w" />
</Frame>

## Step 4: Port Forward to Access the UI

In a **new terminal window on your local machine**, set up port forwarding to access the web UI:

<CodeGroup>
  ```bash Shell theme={null}
  # Set the KUBECONFIG (if not already set in this terminal)
  export KUBECONFIG=/path/to/nanochat-cluster-config

  # Forward port 8000 from the pod to local port 6818
  kubectl -n slurm port-forward <your-slurm-compute-production-pod> 6818:8000
  ```
</CodeGroup>

The port forwarding will remain active as long as this terminal session is open.

## Step 5: Chat with nanochat!

Open your web browser and navigate to:

```
http://localhost:6818/
```

You should see the nanochat web interface! You can now have conversations with your trained model. Go ahead and ask it its favorite question and see what reaction you get!

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/8.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=3d5b642098e9f0a713cd231187bde974" alt="" data-og-width="2134" width="2134" data-og-height="2172" height="2172" data-path="images/guides/nanochat/8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/8.png?w=280&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=8c9b0916560ef613ab4adcc2585f7e15 280w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/8.png?w=560&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=bc3ec9d7d49a2d1afb5010681a0b097a 560w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/8.png?w=840&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=916119eaedfe29c7615b81faa6fa58c8 840w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/8.png?w=1100&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=cea3f75b1aaff02e0540ee692cbc48d1 1100w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/8.png?w=1650&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=3959f1939236dced81f19cf22de59298 1650w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/8.png?w=2500&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=64992aa0315a9d71114a83ee5d1e3c64 2500w" />
</Frame>

## Understanding Training Costs and Performance

The nanochat training pipeline on 8×H100 Instant Clusters typically:

* **Training time**: \~4 hours for the full speedrun pipeline
* **Model Flops Utilization**: \~50% (indicating efficient GPU utilization)
* **Cost**: Approximately \$100 depending on your selected hardware and duration
* **Final model**: A fully functional conversational AI

After training completes, check the generated report `report.md` for detailed metrics.

## Troubleshooting

**GPU Not Available**

If `nvidia-smi` doesn't show GPUs after `srun`:

<CodeGroup>
  ```bash Shell theme={null}
  # Try requesting GPUs explicitly
  srun --gres=gpu:8 --nodes=1 --pty bash
  ```
</CodeGroup>

**Out of Memory Errors**

If you encounter OOM errors during training:

1. Check that `NANOCHAT_BASE_DIR` is set to `/scratch`
2. Ensure no other processes are using GPU memory
3. The default batch sizes should work on H100 80GB

**Port Forwarding Connection Issues**

If you can't connect to the web UI:

1. Verify the pod name matches exactly: `kubectl -n slurm get pods`
2. Ensure the web server is running: check logs in the pod terminal
3. Try a different local port if 6818 is in use

## Next Steps

Now that you have nanochat running, you can:

1. **Experiment with different prompts** - Test the model's conversational abilities and domain knowledge
2. **Fine-tune further** - Modify the SFT data or run additional RL training for specific behaviors
3. **Deploy to production** - Extend `chat_web.py` with authentication and persistence layers
4. **Scale the model** - Try the `run1000.sh` script for a larger model with better performance
5. **Integrate with other tools** - Use the inference API to build custom applications

For more details on the nanochat architecture and training process, visit the [nanochat GitHub repository](https://github.com/karpathy/nanochat).

## Additional Resources

* [Instant Clusters Documentation](/docs/instant-clusters)
* [Instant Clusters API Reference](/api-reference/gpuclusterservice/create-gpu-cluster)
* [nanochat Repository](https://github.com/karpathy/nanochat)
* [Together AI Models](/docs/serverless-models)

***


# Quickstart: Next.Js
Source: https://docs.together.ai/docs/nextjs-chat-quickstart

Build an app that can ask a single question or chat with an LLM using Next.js and Together AI.

In this guide you'll learn how to use Together AI and Next.js to build two common AI features:

* Ask a question and getting a response
* Have a long-running chat with a bot

We'll first build these features using the Together AI SDK directly, then show how to build a chat app using popular frameworks like Vercel AI SDK and Mastra.

[Here's the live demo](https://together-nextjs-chat.vercel.app/), and [here's the source on GitHub](https://github.com/samselikoff/together-nextjs-chat) .

Let's get started!

## Installation

After [creating a new Next.js app](https://nextjs.org/docs/app/getting-started/installation) , install the [Together AI TypeScript SDK](https://www.npmjs.com/package/together-ai) :

```
npm i together-ai
```

## Ask a single question

To ask a question with Together AI, we'll need an API route, and a page with a form that lets the user submit their question.

**1. Create the API route**

Make a new POST route that takes in a `question` and returns a chat completion as a stream:

```js TypeScript theme={null}
// app/api/answer/route.ts
import Together from "together-ai";

const together = new Together();

export async function POST(request: Request) {
  const { question } = await request.json();

  const res = await together.chat.completions.create({
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages: [{ role: "user", content: question }],
    stream: true,
  });

  return new Response(res.toReadableStream());
}
```

**2. Create the page**

Add a form that sends a POST request to your new API route, and use the `ChatCompletionStream` helper to read the stream and update some React state to display the answer:

```js TypeScript theme={null}
// app/page.tsx
"use client";

import { FormEvent, useState } from "react";
import { ChatCompletionStream } from "together-ai/lib/ChatCompletionStream";

export default function Chat() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  async function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();

    setIsLoading(true);
    setAnswer("");

    const res = await fetch("/api/answer", {
      method: "POST",
      body: JSON.stringify({ question }),
    });

    if (!res.body) return;

    ChatCompletionStream.fromReadableStream(res.body)
      .on("content", (delta) => setAnswer((text) => text + delta))
      .on("end", () => setIsLoading(false));
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask me a question"
          required
        />

        <button disabled={isLoading} type="submit">
          Submit
        </button>
      </form>

      <p>{answer}</p>
    </div>
  );
}
```

That's it! Submitting the form will update the page with the LLM's response. You can now use the `isLoading` state to add additional styling, or a Reset button if you want to reset the page.

## Have a long-running chat

To build a chatbot with Together AI, we'll need an API route that accepts an array of messages, and a page with a form that lets the user submit new messages. The page will also need to store the entire history of messages between the user and the AI assistant.

**1. Create an API route**

Make a new POST route that takes in a `messages` array and returns a chat completion as a stream:

```js TypeScript theme={null}
// app/api/chat/route.ts
import Together from "together-ai";

const together = new Together();

export async function POST(request: Request) {
  const { messages } = await request.json();

  const res = await together.chat.completions.create({
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages,
    stream: true,
  });

  return new Response(res.toReadableStream());
}
```

**2. Create a page**

Create a form to submit a new message, and some React state to stores the `messages` for the session. In the form's submit handler, send over the new array of messages, and use the `ChatCompletionStream` helper to read the stream and update the last message with the LLM's response.

```js TypeScript theme={null}
// app/page.tsx
"use client";

import { FormEvent, useState } from "react";
import Together from "together-ai";
import { ChatCompletionStream } from "together-ai/lib/ChatCompletionStream";

export default function Chat() {
  const [prompt, setPrompt] = useState("");
  const [messages, setMessages] = useState<
    Together.Chat.Completions.CompletionCreateParams.Message[]
  >([]);
  const [isPending, setIsPending] = useState(false);

  async function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();

    setPrompt("");
    setIsPending(true);
    setMessages((messages) => [...messages, { role: "user", content: prompt }]);

    const res = await fetch("/api/chat", {
      method: "POST",
      body: JSON.stringify({
        messages: [...messages, { role: "user", content: prompt }],
      }),
    });

    if (!res.body) return;

    ChatCompletionStream.fromReadableStream(res.body)
      .on("content", (delta, content) => {
        setMessages((messages) => {
          const lastMessage = messages.at(-1);

          if (lastMessage?.role !== "assistant") {
            return [...messages, { role: "assistant", content }];
          } else {
            return [...messages.slice(0, -1), { ...lastMessage, content }];
          }
        });
      })
      .on("end", () => {
        setIsPending(false);
      });
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <fieldset>
          <input
            placeholder="Send a message"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
          />
          <button type="submit" disabled={isPending}>
            Submit
          </button>
        </fieldset>
      </form>

      {messages.map((message, i) => (
        <p key={i}>
          {message.role}: {message.content}
        </p>
      ))}
    </div>
  );
}
```

You've just built a simple chatbot with Together AI!

***

## Using Vercel AI SDK

The Vercel AI SDK provides React hooks that simplify streaming and state management. Install it with:

```bash  theme={null}
npm i ai @ai-sdk/togetherai
```

The API route uses `streamText` instead of the Together SDK directly:

```js TypeScript theme={null}
// app/api/chat/route.ts
import { streamText, convertToModelMessages } from "ai";
import { createTogetherAI } from "@ai-sdk/togetherai";

const togetherAI = createTogetherAI({
  apiKey: process.env.TOGETHER_API_KEY,
});

export async function POST(req: Request) {
  const { messages } = await req.json();

  const result = streamText({
    model: togetherAI("meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"),
    messages: convertToModelMessages(messages),
  });

  return result.toUIMessageStreamResponse();
}
```

The page uses the `useChat` hook which handles all message state and streaming automatically:

```js TypeScript theme={null}
// app/page.tsx
"use client";

import { useChat } from "@ai-sdk/react";
import { useState } from "react";

export default function Chat() {
  const [input, setInput] = useState("");
  const { messages, sendMessage } = useChat();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (input.trim()) {
      sendMessage({
        role: "user",
        parts: [{ type: "text", text: input }],
      });
      setInput("");
    }
  };

  return (
    <div>
      {messages.map((message) => (
        <div key={message.id}>
          <strong>{message.role}:</strong>
          {message.parts.map((part, i) =>
            part.type === "text" ? <span key={i}> {part.text}</span> : null
          )}
        </div>
      ))}

      <form onSubmit={handleSubmit}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Send a message"
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}
```

***

## Using Mastra

Mastra is an AI framework that provides built-in integrations and abstractions for building AI applications. Install it with:

```bash  theme={null}
npm i @mastra/core
```

The API route uses Mastra's Together AI integration:

```js TypeScript theme={null}
// app/api/chat/route.ts
import { Agent } from "@mastra/core/agent";
import { NextRequest } from "next/server";

const agent = new Agent({
  name: "my-agent",
  instructions: "You are a helpful assistant",
  model: "togetherai/meta-llama/Llama-3.3-70B-Instruct-Turbo"
});

export async function POST(request: NextRequest) {
  const { messages } = await request.json();

  const conversationHistory = messages
    .map((msg: { role: string; content: string }) => `${msg.role}: ${msg.content}`)
    .join('\n');

  const streamResponse = await agent.stream(conversationHistory);
  
  const encoder = new TextEncoder();
  const readableStream = new ReadableStream({
    async start(controller) {
      for await (const chunk of streamResponse.textStream) {
        controller.enqueue(encoder.encode(`data: ${JSON.stringify(chunk)}\n\n`));
      }
      controller.close();
    },
  });

  return new Response(readableStream, {
    headers: {
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
    },
  });
}
```

The page uses Mastra's chat hooks to manage conversation state:

```js TypeScript theme={null}
// app/page.tsx
"use client";

import { useState } from "react";

export default function Chat() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState<Array<{ role: string; content: string }>>([]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;

    const newMessages = [...messages, { role: "user", content: input }];
    setMessages([...newMessages, { role: "assistant", content: "" }]);
    setInput("");

    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ messages: newMessages }),
    });

    const reader = res.body?.getReader();
    const decoder = new TextDecoder();
    let assistantMessage = "";

    if (reader) {
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const lines = decoder.decode(value).split("\n");
        for (const line of lines) {
          if (line.startsWith("data: ")) {
            const chunk = JSON.parse(line.slice(6));
            assistantMessage += typeof chunk === "string" ? chunk : "";
            setMessages((prev) => [
              ...prev.slice(0, -1),
              { role: "assistant", content: assistantMessage }
            ]);
          }
        }
      }
    }
  };

  return (
    <div>
      {messages.map((m, i) => (
        <div key={i}>
          <strong>{m.role}:</strong> {m.content}
        </div>
      ))}
      <form onSubmit={handleSubmit}>
        <input value={input} onChange={(e) => setInput(e.target.value)} placeholder="Send a message" />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}
```

***


# How To Build An Open Source NotebookLM: PDF To Podcast
Source: https://docs.together.ai/docs/open-notebooklm-pdf-to-podcast

In this guide we will see how to create a podcast like the one below from a PDF input!

Inspired by [NotebookLM's podcast generation](https://notebooklm.google/) feature and a recent open source implementation of [Open Notebook LM](https://github.com/gabrielchua/open-notebooklm). In this guide we will implement a walkthrough of how you can build a PDF to podcast pipeline.

Given any PDF we will generate a conversation between a host and a guest discussing and explaining the contents of the PDF.

In doing so we will learn the following:

1. How we can use JSON mode and structured generation with open models like Llama 3 70b to extract a script for the Podcast given text from the PDF.
2. How we can use TTS models to bring this script to life as a conversation.

## Define Dialogue Schema with Pydantic

We need a way of telling the LLM what the structure of the podcast script between the guest and host will look like. We will do this using `pydantic` models.

Below we define the required classes:

* The overall conversation consists of lines said by either the host or the guest. The `DialogueItem` class specifies the structure of these lines.
* The full script is a combination of multiple lines performed by the speakers, here we also include a `scratchpad` field to allow the LLM to ideate and brainstorm the overall flow of the script prior to actually generating the lines. The `Dialogue` class specifies this.

```py Python theme={null}
from pydantic import BaseModel
from typing import List, Literal, Tuple, Optional


class LineItem(BaseModel):
    """A single line in the script."""

    speaker: Literal["Host (Jane)", "Guest"]
    text: str


class Script(BaseModel):
    """The script between the host and guest."""

    scratchpad: str
    name_of_guest: str
    script: List[LineItem]
```

The inclusion of a scratchpad field is very important - it allows the LLM compute and tokens to generate an unstructured overview of the script prior to generating a structured line by line enactment.

## System Prompt for Script Generation

Next we need to define a detailed prompt template engineered to guide the LLM through the generation of the script. Feel free to modify and update the prompt below.

```py Python theme={null}
# Adapted and modified from https://github.com/gabrielchua/open-notebooklm
SYSTEM_PROMPT = """
You are a world-class podcast producer tasked with transforming the provided input text into an engaging and informative podcast script. The input may be unstructured or messy, sourced from PDFs or web pages. Your goal is to extract the most interesting and insightful content for a compelling podcast discussion.

# Steps to Follow:

1. **Analyze the Input:**
   Carefully examine the text, identifying key topics, points, and interesting facts or anecdotes that could drive an engaging podcast conversation. Disregard irrelevant information or formatting issues.

2. **Brainstorm Ideas:**
   In the `<scratchpad>`, creatively brainstorm ways to present the key points engagingly. Consider:
   - Analogies, storytelling techniques, or hypothetical scenarios to make content relatable
   - Ways to make complex topics accessible to a general audience
   - Thought-provoking questions to explore during the podcast
   - Creative approaches to fill any gaps in the information

3. **Craft the Dialogue:**
   Develop a natural, conversational flow between the host (Jane) and the guest speaker (the author or an expert on the topic). Incorporate:
   - The best ideas from your brainstorming session
   - Clear explanations of complex topics
   - An engaging and lively tone to captivate listeners
   - A balance of information and entertainment

   Rules for the dialogue:
   - The host (Jane) always initiates the conversation and interviews the guest
   - Include thoughtful questions from the host to guide the discussion
   - Incorporate natural speech patterns, including occasional verbal fillers (e.g., "Uhh", "Hmmm", "um," "well," "you know")
   - Allow for natural interruptions and back-and-forth between host and guest - this is very important to make the conversation feel authentic
   - Ensure the guest's responses are substantiated by the input text, avoiding unsupported claims
   - Maintain a PG-rated conversation appropriate for all audiences
   - Avoid any marketing or self-promotional content from the guest
   - The host concludes the conversation

4. **Summarize Key Insights:**
   Naturally weave a summary of key points into the closing part of the dialogue. This should feel like a casual conversation rather than a formal recap, reinforcing the main takeaways before signing off.

5. **Maintain Authenticity:**
   Throughout the script, strive for authenticity in the conversation. Include:
   - Moments of genuine curiosity or surprise from the host
   - Instances where the guest might briefly struggle to articulate a complex idea
   - Light-hearted moments or humor when appropriate
   - Brief personal anecdotes or examples that relate to the topic (within the bounds of the input text)

6. **Consider Pacing and Structure:**
   Ensure the dialogue has a natural ebb and flow:
   - Start with a strong hook to grab the listener's attention
   - Gradually build complexity as the conversation progresses
   - Include brief "breather" moments for listeners to absorb complex information
   - For complicated concepts, reasking similar questions framed from a different perspective is recommended
   - End on a high note, perhaps with a thought-provoking question or a call-to-action for listeners

IMPORTANT RULE: Each line of dialogue should be no more than 100 characters (e.g., can finish within 5-8 seconds)

Remember: Always reply in valid JSON format, without code blocks. Begin directly with the JSON output.
"""
```

## Download PDF and Extract Contents

Here we will load in an academic paper that proposes the use of many open source language models in a collaborative manner together to outperform proprietary models that are much larger!

We will use the text in the PDF as content to generate the podcast with!

<Frame><img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/24.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=caffab5ada2f163e753291e76586bb05" alt="" data-og-width="1410" width="1410" data-og-height="1150" height="1150" data-path="images/guides/24.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/24.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=97c884d170b731472a20dff0e619f660 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/24.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=82d39461d40964d6377072712a316fba 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/24.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=95bf71e40b9f039606cca195de30e816 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/24.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=267eeb92db3688b931fa1e881c30cf9b 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/24.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=882994d0c0996005ad598c15a0a1785f 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/24.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7cb93cda496d12c431cd9599ca35d143 2500w" /></Frame>

Download the PDF file and then extract text contents using the function below.

```bash Shell theme={null}
!wget https://arxiv.org/pdf/2406.04692
!mv 2406.04692 MoA.pdf
```

```py Python theme={null}
from pypdf import PdfReader


def get_PDF_text(file: str):
    text = ""

    # Read the PDF file and extract text
    try:
        with Path(file).open("rb") as f:
            reader = PdfReader(f)
            text = "\n\n".join([page.extract_text() for page in reader.pages])
    except Exception as e:
        raise f"Error reading the PDF file: {str(e)}"

        # Check if the PDF has more than ~400,000 characters
        # The context lenght limit of the model is 131,072 tokens and thus the text should be less than this limit
        # Assumes that 1 token is approximately 4 characters
    if len(text) > 400000:
        raise "The PDF is too long. Please upload a PDF with fewer than ~131072 tokens."

    return text


text = get_PDF_text("MoA.pdf")
```

## Generate Podcast Script using JSON Mode

Below we call Llama3.1 70B with JSON mode to generate a script for our podcast. JSON mode makes it so that the LLM will only generate responses in the format specified by the `Script` class. We will also be able to read it's scratchpad and see how it structured the overall conversation.

```py Python theme={null}
from together import Together
from pydantic import ValidationError

client_together = Together(api_key="TOGETHER_API_KEY")


def call_llm(system_prompt: str, text: str, dialogue_format):
    """Call the LLM with the given prompt and dialogue format."""
    response = client_together.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text},
        ],
        model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
        response_format={
            "type": "json_object",
            "schema": dialogue_format.model_json_schema(),
        },
    )
    return response


def generate_script(system_prompt: str, input_text: str, output_model):
    """Get the script from the LLM."""
    # Load as python object
    try:
        response = call_llm(system_prompt, input_text, output_model)
        dialogue = output_model.model_validate_json(
            response.choices[0].message.content
        )
    except ValidationError as e:
        error_message = f"Failed to parse dialogue JSON: {e}"
        system_prompt_with_error = f"{system_prompt}\n\nPlease return a VALID JSON object. This was the earlier error: {error_message}"
        response = call_llm(system_prompt_with_error, input_text, output_model)
        dialogue = output_model.model_validate_json(
            response.choices[0].message.content
        )
    return dialogue


# Generate the podcast script

script = generate_script(SYSTEM_PROMPT, text, Script)
```

Above we are also handling the erroneous case which will let us know if the script was not generated following the `Script` class.

Now we can have a look at the script that is generated:

```
[DialogueItem(speaker='Host (Jane)', text='Welcome to today’s podcast. I’m your host, Jane. Joining me is Junlin Wang, a researcher from Duke University and Together AI. Junlin, welcome to the show!'),
 DialogueItem(speaker='Guest', text='Thanks for having me, Jane. I’m excited to be here.'),
 DialogueItem(speaker='Host (Jane)', text='Junlin, your recent paper proposes a new approach to enhancing large language models (LLMs) by leveraging the collective strengths of multiple models. Can you tell us more about this?'),
 DialogueItem(speaker='Guest', text='Our approach is called Mixture-of-Agents (MoA). We found that LLMs exhibit a phenomenon we call collaborativeness, where they generate better responses when presented with outputs from other models, even if those outputs are of lower quality.'),
 DialogueItem(speaker='Host (Jane)', text='That’s fascinating. Can you walk us through how MoA works?'),
 DialogueItem(speaker='Guest', text='MoA consists of multiple layers, each comprising multiple LLM agents. Each agent takes all the outputs from agents in the previous layer as auxiliary information in generating its response. This process is repeated for several cycles until a more robust and comprehensive response is obtained.'),
 DialogueItem(speaker='Host (Jane)', text='I see. And what kind of results have you seen with MoA?'),
 DialogueItem(speaker='Guest', text='We evaluated MoA on several benchmarks, including AlpacaEval 2.0, MT-Bench, and FLASK. Our results show substantial improvements in response quality, with MoA achieving state-of-the-art performance on these benchmarks.'),
 DialogueItem(speaker='Host (Jane)', text='Wow, that’s impressive. What about the cost-effectiveness of MoA?'),
 DialogueItem(speaker='Guest', text='We found that MoA can deliver performance comparable to GPT-4 Turbo while being 2x more cost-effective. This is because MoA can leverage the strengths of multiple models, reducing the need for expensive and computationally intensive training.'),
 DialogueItem(speaker='Host (Jane)', text='That’s great to hear. Junlin, what do you think is the potential impact of MoA on the field of natural language processing?'),
 DialogueItem(speaker='Guest', text='I believe MoA has the potential to significantly enhance the effectiveness of LLM-driven chat assistants, making AI more accessible to a wider range of people. Additionally, MoA can improve the interpretability of models, facilitating better alignment with human reasoning.'),
 DialogueItem(speaker='Host (Jane)', text='That’s a great point. Junlin, thank you for sharing your insights with us today.'),
 DialogueItem(speaker='Guest', text='Thanks for having me, Jane. It was a pleasure discussing MoA with you.')]
```

## Generate Podcast Using TTS

Below we read through the script and parse choose the TTS voice depending on the speaker. We define a speaker and guest voice id.

```py Python theme={null}
import subprocess
import ffmpeg
from cartesia import Cartesia

client_cartesia = Cartesia(api_key="CARTESIA_API_KEY")

host_id = "694f9389-aac1-45b6-b726-9d9369183238"  # Jane - host voice
guest_id = "a0e99841-438c-4a64-b679-ae501e7d6091"  # Guest voice

model_id = "sonic-english"  # The Sonic Cartesia model for English TTS

output_format = {
    "container": "raw",
    "encoding": "pcm_f32le",
    "sample_rate": 44100,
}

# Set up a WebSocket connection.
ws = client_cartesia.tts.websocket()
```

We can loop through the lines in the script and generate them by a call to the TTS model with specific voice and lines configurations. The lines all appended to the same buffer and once the script finishes we write this out to a wav file, ready to be played.

```py Python theme={null}
# Open a file to write the raw PCM audio bytes to.
f = open("podcast.pcm", "wb")

# Generate and stream audio.
for line in script.dialogue:
    if line.speaker == "Guest":
        voice_id = guest_id
    else:
        voice_id = host_id

    for output in ws.send(
        model_id=model_id,
        transcript="-"
        + line.text,  # the "-"" is to add a pause between speakers
        voice_id=voice_id,
        stream=True,
        output_format=output_format,
    ):
        buffer = output["audio"]  # buffer contains raw PCM audio bytes
        f.write(buffer)

# Close the connection to release resources
ws.close()
f.close()

# Convert the raw PCM bytes to a WAV file.
ffmpeg.input("podcast.pcm", format="f32le").output("podcast.wav").run()

# Play the file
subprocess.run(["ffplay", "-autoexit", "-nodisp", "podcast.wav"])
```

Once this code executes you will have a `podcast.wav` file saved on disk that can be played!

If you're ready to create your own PDF to podcast app like above [sign up for Together AI today](https://www.together.ai/) and make your first query in minutes!


# OpenAI Compatibility
Source: https://docs.together.ai/docs/openai-api-compatibility

Together's API is compatible with OpenAI's libraries, making it easy to try out our open-source models on existing applications.

Together's API endpoints for chat, vision, images, embeddings, speech are fully compatible with OpenAI's API.

If you have an application that uses one of OpenAI's client libraries, you can easily configure it to point to Together's API servers, and start running your existing applications using our open-source models.

## Configuring OpenAI to use Together's API

To start using Together with OpenAI's client libraries, pass in your Together API key to the `api_key` option, and change the `base_url` to `https://api.together.xyz/v1`:

<CodeGroup>
  ```python Python theme={null}
  import os
  import openai

  client = openai.OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )
  ```

  ```typescript TypeScript theme={null}
  import OpenAI from "openai";

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: "https://api.together.xyz/v1",
  });
  ```
</CodeGroup>

You can find your API key in [your settings page](https://api.together.xyz/settings/api-keys). If you don't have an account, you can [register for free](https://api.together.ai/).

## Querying a chat model

Now that your OpenAI client is configured to point to Together, you can start using one of our open-source models for your inference queries.

For example, you can query one of our [chat models](/docs/serverless-models#chat-models), like Llama 3.1 8B:

<CodeGroup>
  ```python Python theme={null}
  import os
  import openai

  client = openai.OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  response = client.chat.completions.create(
      model="openai/gpt-oss-20b",
      messages=[
          {
              "role": "system",
              "content": "You are a travel agent. Be descriptive and helpful.",
          },
          {
              "role": "user",
              "content": "Tell me the top 3 things to do in San Francisco",
          },
      ],
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: 'https://api.together.xyz/v1',
  });

  const response = await client.chat.completions.create({
    model: 'openai/gpt-oss-20b',
    messages: [
      { role: 'user', content: 'What are some fun things to do in New York?' },
    ],
  });

  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

## Streaming a response

You can also use OpenAI's streaming capabilities to stream back your response:

<CodeGroup>
  ```python Python theme={null}
  import os
  import openai

  client = openai.OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  stream = client.chat.completions.create(
      model="Qwen/Qwen3-Next-80B-A3B-Instruct",
      messages=[
          {
              "role": "system",
              "content": "You are a travel agent. Be descriptive and helpful.",
          },
          {"role": "user", "content": "Tell me about San Francisco"},
      ],
      stream=True,
  )

  for chunk in stream:
      print(chunk.choices[0].delta.content or "", end="", flush=True)
  ```

  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: 'https://api.together.xyz/v1',
  });

  async function run() {
    const stream = await client.chat.completions.create({
      model: 'Qwen/Qwen3-Next-80B-A3B-Instruct',
      messages: [
        { role: 'system', content: 'You are an AI assistant' },
        { role: 'user', content: 'Who won the world series in 2020?' },
      ],
      stream: true,
    });

    for await (const chunk of stream) {
      // use process.stdout.write instead of console.log to avoid newlines
      process.stdout.write(chunk.choices[0]?.delta?.content || '');
    }
  }

  run();
  ```
</CodeGroup>

## Using Vision Models

<CodeGroup>
  ```python Python theme={null}
  import os
  import openai

  client = openai.OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  response = client.chat.completions.create(
      model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "What's in this image?"},
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                      },
                  },
              ],
          }
      ],
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: 'https://api.together.xyz/v1',
  });

  const response = await openai.chat.completions.create({
      model: "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
      messages: [{
          role: "user",
          content: [
              { type: "text", text: "What is in this image?" },
              {
                  type: "image_url",
                  image_url: {
                      url: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                  },
              },
          ],
      }],
  });

  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

Output:

```text Text theme={null}
The image depicts a serene and idyllic scene of a wooden boardwalk winding through a lush, green field on a sunny day.

*   **Sky:**
    *   The sky is a brilliant blue with wispy white clouds scattered across it.
    *   The clouds are thin and feathery, adding to the overall sense of tranquility.
*   **Boardwalk:**
    *   The boardwalk is made of weathered wooden planks, worn smooth by time and use.
    *   It stretches out into the distance, disappearing into the horizon.
    *   The boardwalk is flanked by tall grasses and reeds that reach up to the knees.
*   **Field:**
    *   The field is filled with tall, green grasses and reeds that sway gently in the breeze.
    *   The grasses are so tall that they almost obscure the boardwalk, creating a sense of mystery and adventure.
    *   In the distance, trees and bushes can be seen, adding depth and texture to the scene.
*   **Atmosphere:**
    *   The overall atmosphere is one of peace and serenity, inviting the viewer to step into the tranquil world depicted in the image.
    *   The warm sunlight and gentle breeze create a sense of comfort and relaxation.

In summary, the image presents a picturesque scene of a wooden boardwalk meandering through a lush, green field on a sunny day, evoking feelings of peace and serenity.
```

## Image Generation

<CodeGroup>
  ```python Python theme={null}
  from openai import OpenAI
  import os

  client = OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  prompt = """
  A children's book drawing of a veterinarian using a stethoscope to 
  listen to the heartbeat of a baby otter.
  """

  result = client.images.generate(
      model="black-forest-labs/FLUX.1-dev", prompt=prompt
  )

  print(result.data[0].url)
  ```

  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: 'https://api.together.xyz/v1',
  });

  const prompt = `
  A children's book drawing of a veterinarian using a stethoscope to 
  listen to the heartbeat of a baby otter.
  `;

  async function main() {
    const response = await client.images.create({
      model: "black-forest-labs/FLUX.1-dev",
      prompt: prompt,
    });

    console.log(response.data[0].url);
  }

  main();
  ```
</CodeGroup>

Output:

<div style={{textAlign: 'center'}}>
  <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=840c30380735f6bad166e6fda2c0375b" style={{width: '300px'}} data-og-width="1024" width="1024" data-og-height="768" height="768" data-path="images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=12e0c9ecdac254c9a57ef97fe5136ad1 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=95e37cf0394bbb531d4ed1123e2df599 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=e3fcdaaa3da32ab990a7af7fa98228a0 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=23629c234356a16d96096fabb9a5f89f 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=f1d11281b1809e98b6c28e64139c550c 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c1cf869e56065ef72ed5d1fd432a9c37 2500w" />
</div>

## Text-to-Speech

<CodeGroup>
  ```python Python theme={null}
  from openai import OpenAI
  import os

  client = OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  speech_file_path = "speech.mp3"

  response = client.audio.speech.create(
      model="hexgrad/Kokoro-82M",
      input="Today is a wonderful day to build something people love!",
      voice="helpful woman",
  )

  response.stream_to_file(speech_file_path)
  ```

  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';
  import { createWriteStream } from 'fs';
  import { pipeline } from 'stream/promises';

  const client = new OpenAI({
      apiKey: process.env.TOGETHER_API_KEY,
      baseURL: 'https://api.together.xyz/v1',
    });

  const speechFilePath = 'speech.mp3';

  async function main() {
      const response = await client.audio.speech.create({
        model: 'hexgrad/Kokoro-82M',
        input: 'Today is a wonderful day to build!',
        voice: 'helpful woman',
      });

      const buffer = Buffer.from(await response.arrayBuffer());
      await require('fs').promises.writeFile(speechFilePath, buffer);
    }

  main();
  ```
</CodeGroup>

Output:

<iframe src="https://drive.google.com/file/d/1zpUdy_UlCeveGJP1z4ddj_Uh3uKnSovT/preview" />

## Generating vector embeddings

Use our [embedding models](/docs/serverless-models#embedding-models) to generate an embedding for some text input:

<CodeGroup>
  ```python Python theme={null}
  import os
  import openai

  client = openai.OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  response = client.embeddings.create(
      model="togethercomputer/m2-bert-80M-8k-retrieval",
      input="Our solar system orbits the Milky Way galaxy at about 515,000 mph",
  )

  print(response.data[0].embedding)
  ```

  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: 'https://api.together.xyz/v1',
  });

  const response = await client.embeddings.create({
    model: 'togethercomputer/m2-bert-80M-32k-retrieval',
    input: 'Our solar system orbits the Milky Way galaxy at about 515,000 mph',
  });

  console.log(response.data[0].embedding);
  ```
</CodeGroup>

Output

```text Text theme={null}
[0.2633975, 0.13856211, 0.14047204,... ]
```

## Structured Outputs

```python Python theme={null}
from pydantic import BaseModel
from openai import OpenAI
import os, json

client = OpenAI(
    api_key=os.environ.get("TOGETHER_API_KEY"),
    base_url="https://api.together.xyz/v1",
)


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {
            "role": "user",
            "content": "Alice and Bob are going to a science fair on Friday. Answer in JSON",
        },
    ],
    response_format={
        "type": "json_schema",
        "schema": CalendarEvent.model_json_schema(),
    },
)

output = json.loads(completion.choices[0].message.content)
print(json.dumps(output, indent=2))
```

Output:

```text Text theme={null}
{
  "name": "Alice and Bob",
  "date": "Friday",
  "participants": [
    "Alice",
    "Bob"
  ]
}
```

## Function Calling

<CodeGroup>
  ```python Python theme={null}
  from openai import OpenAI
  import os, json

  client = OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

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

  completion = client.chat.completions.create(
      model="zai-org/GLM-4.5-Air-FP8",
      messages=[
          {"role": "user", "content": "What is the weather like in Paris today?"}
      ],
      tools=tools,
      tool_choice="auto",
  )

  print(
      json.dumps(
          completion.choices[0].message.model_dump()["tool_calls"], indent=2
      )
  )
  ```

  ```typescript TypeScript theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: 'https://api.together.xyz/v1',
  });

  const tools = [{
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
              "required": [
                  "location"
              ],
              "additionalProperties": false
          },
          "strict": true
      }
  }];

  const completion = await openai.chat.completions.create({
      model: "zai-org/GLM-4.5-Air-FP8",
      messages: [{ role: "user", content: "What is the weather like in Paris today?" }],
      tools,
      store: true,
  });

  console.log(completion.choices[0].message.tool_calls);
  ```
</CodeGroup>

Output:

```text Text theme={null}
[
  {
    "id": "call_nu2ifnvqz083p5kngs3a3aqz",
    "function": {
      "arguments": "{\"location\":\"Paris, France\"}",
      "name": "get_weather"
    },
    "type": "function",
    "index": 0
  }
]
```

## Community libraries

The Together API is also supported by most [OpenAI libraries built by the community](https://platform.openai.com/docs/libraries/community-libraries).

Feel free to [reach out to support](https://www.together.ai/contact) if you come across some unexpected behavior when using our API.



---

**Navigation:** [← Previous](./05-how-to-build-coding-agents.md) | [Index](./index.md) | [Next →](./07-parallel-workflow.md)
