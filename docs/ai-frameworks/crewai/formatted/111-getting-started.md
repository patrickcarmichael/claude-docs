---
title: "Crewai: Getting Started"
description: "Getting Started section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Getting Started


Let's create a simple Flow where you will use OpenAI to generate a random city in one task and then use that city to generate a fun fact in another task.

```python Code theme={null}

from crewai.flow.flow import Flow, listen, start
from dotenv import load_dotenv
from litellm import completion

class ExampleFlow(Flow):
    model = "gpt-4o-mini"

    @start()
    def generate_city(self):
        print("Starting flow")
        # Each flow state automatically gets a unique ID
        print(f"Flow State ID: {self.state['id']}")

        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": "Return the name of a random city in the world.",
                },
            ],
        )

        random_city = response["choices"][0]["message"]["content"]
        # Store the city in our state
        self.state["city"] = random_city
        print(f"Random City: {random_city}")

        return random_city

    @listen(generate_city)
    def generate_fun_fact(self, random_city):
        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Tell me a fun fact about {random_city}",
                },
            ],
        )

        fun_fact = response["choices"][0]["message"]["content"]
        # Store the fun fact in our state
        self.state["fun_fact"] = fun_fact
        return fun_fact

flow = ExampleFlow()
flow.plot()
result = flow.kickoff()

print(f"Generated fun fact: {result}")
```

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=18b381277b7b017abf7cb19bc5e03923" alt="Flow Visual image" data-og-width="1913" width="1913" data-og-height="989" height="989" data-path="images/crewai-flow-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=78864d97e0fc7f225a5313c9fb650900 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3d87938c680e7aa201798075fe19dcf8 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=36448790f7ca45e69ffdd3ceb2b2e713 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4d10a3f4f9ea1c9b0428fbb66f0fca17 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=928a75232235b73e9308d4d9cfeaf0e8 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-1.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=fa7022034285d0022ff07f97f6b675f7 2500w" />
In the above example, we have created a simple Flow that generates a random city using OpenAI and then generates a fun fact about that city. The Flow consists of two tasks: `generate_city` and `generate_fun_fact`. The `generate_city` task is the starting point of the Flow, and the `generate_fun_fact` task listens for the output of the `generate_city` task.

Each Flow instance automatically receives a unique identifier (UUID) in its state, which helps track and manage flow executions. The state can also store additional data (like the generated city and fun fact) that persists throughout the flow's execution.

When you run the Flow, it will:

1. Generate a unique ID for the flow state
2. Generate a random city and store it in the state
3. Generate a fun fact about that city and store it in the state
4. Print the results to the console

The state's unique ID and stored data can be useful for tracking flow executions and maintaining context between tasks.

**Note:** Ensure you have set up your `.env` file to store your `OPENAI_API_KEY`. This key is necessary for authenticating requests to the OpenAI API.

### @start()

The `@start()` decorator marks entry points for a Flow. You can:

* Declare multiple unconditional starts: `@start()`
* Gate a start on a prior method or router label: `@start("method_or_label")`
* Provide a callable condition to control when a start should fire

All satisfied `@start()` methods will execute (often in parallel) when the Flow begins or resumes.

### @listen()

The `@listen()` decorator is used to mark a method as a listener for the output of another task in the Flow. The method decorated with `@listen()` will be executed when the specified task emits an output. The method can access the output of the task it is listening to as an argument.

#### Usage

The `@listen()` decorator can be used in several ways:

1. **Listening to a Method by Name**: You can pass the name of the method you want to listen to as a string. When that method completes, the listener method will be triggered.

   ```python Code theme={null}
   @listen("generate_city")
   def generate_fun_fact(self, random_city):
       # Implementation
   ```

2. **Listening to a Method Directly**: You can pass the method itself. When that method completes, the listener method will be triggered.
   ```python Code theme={null}
   @listen(generate_city)
   def generate_fun_fact(self, random_city):
       # Implementation
   ```

### Flow Output

Accessing and handling the output of a Flow is essential for integrating your AI workflows into larger applications or systems. CrewAI Flows provide straightforward mechanisms to retrieve the final output, access intermediate results, and manage the overall state of your Flow.

#### Retrieving the Final Output

When you run a Flow, the final output is determined by the last method that completes. The `kickoff()` method returns the output of this final method.

Here's how you can access the final output:

<CodeGroup>
  ```python Code theme={null}
  from crewai.flow.flow import Flow, listen, start

  class OutputExampleFlow(Flow):
      @start()
      def first_method(self):
          return "Output from first_method"

      @listen(first_method)
      def second_method(self, first_output):
          return f"Second method received: {first_output}"

  flow = OutputExampleFlow()
  flow.plot("my_flow_plot")
  final_output = flow.kickoff()

  print("---- Final Output ----")
  print(final_output)
  ```

  ```text Output theme={null}
  ---- Final Output ----
  Second method received: Output from first_method
  ```
</CodeGroup>

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3d987994d2c99a06a3cf149c71831fd5" alt="Flow Visual image" data-og-width="2015" width="2015" data-og-height="1040" height="1040" data-path="images/crewai-flow-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=e6b4e913cd2d4bf4dc67bdcb2e59cceb 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=245303e4f6e5bc30819aa9357561e7b3 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=32155410f336267e29c64407e22ae57e 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=5dc414bc338e0475ae40aa3eedea0bd8 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=cfdf47937eb1f0a1f7e9ffdaab866e5a 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ef7d71c39b8ea4ad865c514420df28d1 2500w" />

In this example, the `second_method` is the last method to complete, so its output will be the final output of the Flow.
The `kickoff()` method will return the final output, which is then printed to the console. The `plot()` method will generate the HTML file, which will help you understand the flow.

#### Accessing and Updating State

In addition to retrieving the final output, you can also access and update the state within your Flow. The state can be used to store and share data between different methods in the Flow. After the Flow has run, you can access the state to retrieve any information that was added or updated during the execution.

Here's an example of how to update and access the state:

<CodeGroup>
  ```python Code theme={null}
  from crewai.flow.flow import Flow, listen, start
  from pydantic import BaseModel

  class ExampleState(BaseModel):
      counter: int = 0
      message: str = ""

  class StateExampleFlow(Flow[ExampleState]):

      @start()
      def first_method(self):
          self.state.message = "Hello from first_method"
          self.state.counter += 1

      @listen(first_method)
      def second_method(self):
          self.state.message += " - updated by second_method"
          self.state.counter += 1
          return self.state.message

  flow = StateExampleFlow()
  flow.plot("my_flow_plot")
  final_output = flow.kickoff()
  print(f"Final Output: {final_output}")
  print("Final State:")
  print(flow.state)
  ```

  ```text Output theme={null}
  Final Output: Hello from first_method - updated by second_method
  Final State:
  counter=2 message='Hello from first_method - updated by second_method'
  ```
</CodeGroup>

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3d987994d2c99a06a3cf149c71831fd5" alt="Flow Visual image" data-og-width="2015" width="2015" data-og-height="1040" height="1040" data-path="images/crewai-flow-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=e6b4e913cd2d4bf4dc67bdcb2e59cceb 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=245303e4f6e5bc30819aa9357561e7b3 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=32155410f336267e29c64407e22ae57e 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=5dc414bc338e0475ae40aa3eedea0bd8 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=cfdf47937eb1f0a1f7e9ffdaab866e5a 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-2.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ef7d71c39b8ea4ad865c514420df28d1 2500w" />

In this example, the state is updated by both `first_method` and `second_method`.
After the Flow has run, you can access the final state to see the updates made by these methods.

By ensuring that the final method's output is returned and providing access to the state, CrewAI Flows make it easy to integrate the results of your AI workflows into larger applications or systems,
while also maintaining and accessing the state throughout the Flow's execution.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Overview](./110-overview.md)

**Next:** [Flow State Management →](./112-flow-state-management.md)
