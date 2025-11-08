---
title: "Crewai: Flow Control"
description: "Flow Control section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Flow Control


### Conditional Logic: `or`

The `or_` function in Flows allows you to listen to multiple methods and trigger the listener method when any of the specified methods emit an output.

<CodeGroup>
  ```python Code theme={null}
  from crewai.flow.flow import Flow, listen, or_, start

  class OrExampleFlow(Flow):

      @start()
      def start_method(self):
          return "Hello from the start method"

      @listen(start_method)
      def second_method(self):
          return "Hello from the second method"

      @listen(or_(start_method, second_method))
      def logger(self, result):
          print(f"Logger: {result}")

  flow = OrExampleFlow()
  flow.plot("my_flow_plot")
  flow.kickoff()
  ```

  ```text Output theme={null}
  Logger: Hello from the start method
  Logger: Hello from the second method
  ```
</CodeGroup>

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=88ce9c9f10781b835f170847bc541a13" alt="Flow Visual image" data-og-width="2026" width="2026" data-og-height="1016" height="1016" data-path="images/crewai-flow-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=796ce622251faa461b481eb5d7cdcf70 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=260fcd89a5b3a6a42a25dd4f41e7c5c6 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=b9268adb3abef93c7cce693a424a78ba 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=75f3ad392bfd6b72bd29d701675899d6 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=dd771250338648e1f22c1463cb8e2ff0 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-4.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=b8e6fd63ec2ba23d9fa4f1dc2fd87143 2500w" />

When you run this Flow, the `logger` method will be triggered by the output of either the `start_method` or the `second_method`.
The `or_` function is used to listen to multiple methods and trigger the listener method when any of the specified methods emit an output.

### Conditional Logic: `and`

The `and_` function in Flows allows you to listen to multiple methods and trigger the listener method only when all the specified methods emit an output.

<CodeGroup>
  ```python Code theme={null}
  from crewai.flow.flow import Flow, and_, listen, start

  class AndExampleFlow(Flow):

      @start()
      def start_method(self):
          self.state["greeting"] = "Hello from the start method"

      @listen(start_method)
      def second_method(self):
          self.state["joke"] = "What do computers eat? Microchips."

      @listen(and_(start_method, second_method))
      def logger(self):
          print("---- Logger ----")
          print(self.state)

  flow = AndExampleFlow()
  flow.plot()
  flow.kickoff()
  ```

  ```text Output theme={null}
  ---- Logger ----
  {'greeting': 'Hello from the start method', 'joke': 'What do computers eat? Microchips.'}
  ```
</CodeGroup>

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=104318219be9d3502ac57ebb513aded7" alt="Flow Visual image" data-og-width="2062" width="2062" data-og-height="987" height="987" data-path="images/crewai-flow-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=6e9cb9d2b1ec2cb2aee2df008d3696c9 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=07cbcc6de6e8c8ae5da6c02a6fe4b457 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=afc6aad8f7276be4918527e553b5aa81 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=e026919d9dff7ce0b0e592f4f2c0c4fd 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=03ea50c8681de2b8ea8cada6c0150e2c 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-5.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=61f9c7b0aceb69df6346ab2af321b779 2500w" />

When you run this Flow, the `logger` method will be triggered only when both the `start_method` and the `second_method` emit an output.
The `and_` function is used to listen to multiple methods and trigger the listener method only when all the specified methods emit an output.

### Router

The `@router()` decorator in Flows allows you to define conditional routing logic based on the output of a method.
You can specify different routes based on the output of the method, allowing you to control the flow of execution dynamically.

<CodeGroup>
  ```python Code theme={null}
  import random
  from crewai.flow.flow import Flow, listen, router, start
  from pydantic import BaseModel

  class ExampleState(BaseModel):
      success_flag: bool = False

  class RouterFlow(Flow[ExampleState]):

      @start()
      def start_method(self):
          print("Starting the structured flow")
          random_boolean = random.choice([True, False])
          self.state.success_flag = random_boolean

      @router(start_method)
      def second_method(self):
          if self.state.success_flag:
              return "success"
          else:
              return "failed"

      @listen("success")
      def third_method(self):
          print("Third method running")

      @listen("failed")
      def fourth_method(self):
          print("Fourth method running")

  flow = RouterFlow()
  flow.plot("my_flow_plot")
  flow.kickoff()
  ```

  ```text Output theme={null}
  Starting the structured flow
  Third method running
  Fourth method running
  ```
</CodeGroup>

<img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f8cad73f073b4e936ef68d88545f1777" alt="Flow Visual image" data-og-width="1951" width="1951" data-og-height="1101" height="1101" data-path="images/crewai-flow-6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=9a8462f42a9d9e14748d35312553ec6c 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=78e66eabae15099e2ef1d0c314d3cb04 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=a144377de810ed24f1d1aed1ba54d2d7 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=2b17ebb2dd4eee4d086a8d0126a36c0d 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4536b83aa7ff7e897f1193709ace944f 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crewai-flow-6.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3b89cff817f7b4d05338f4a3a028f974 2500w" />

In the above example, the `start_method` generates a random boolean value and sets it in the state.
The `second_method` uses the `@router()` decorator to define conditional routing logic based on the value of the boolean.
If the boolean is `True`, the method returns `"success"`, and if it is `False`, the method returns `"failed"`.
The `third_method` and `fourth_method` listen to the output of the `second_method` and execute based on the returned value.

When you run this Flow, the output will change based on the random boolean value generated by the `start_method`.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Flow Persistence](./113-flow-persistence.md)

**Next:** [Adding Agents to Flows →](./115-adding-agents-to-flows.md)
