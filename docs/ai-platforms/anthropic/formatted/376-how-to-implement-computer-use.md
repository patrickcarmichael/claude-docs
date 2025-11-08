---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How to implement computer use

### Start with our reference implementation

We have built a [reference implementation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo) that includes everything you need to get started quickly with computer use:

* A [containerized environment](https://github.com/anthropics/anthropic-quickstarts/blob/main/computer-use-demo/Dockerfile) suitable for computer use with Claude
* Implementations of [the computer use tools](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo/computer_use_demo/tools)
* An [agent loop](https://github.com/anthropics/anthropic-quickstarts/blob/main/computer-use-demo/computer_use_demo/loop.py) that interacts with the Claude API and executes the computer use tools
* A web interface to interact with the container, agent loop, and tools.

### Understanding the multi-agent loop

The core of computer use is the "agent loop" - a cycle where Claude requests tool actions, your application executes them, and returns results to Claude. Here's a simplified example:
```python
async def sampling_loop(
    *,
    model: str,
    messages: list[dict],
    api_key: str,
    max_tokens: int = 4096,
    tool_version: str,
    thinking_budget: int | None = None,
    max_iterations: int = 10,  # Add iteration limit to prevent infinite loops

):
    """
    A simple agent loop for Claude computer use interactions.

    This function handles the back-and-forth between:
    1. Sending user messages to Claude
    2. Claude requesting to use tools
    3. Your app executing those tools
    4. Sending tool results back to Claude
    """
    # Set up tools and API parameters

    client = Anthropic(api_key=api_key)
    beta_flag = "computer-use-2025-01-24" if "20250124" in tool_version else "computer-use-2024-10-22"

    # Configure tools - you should already have these initialized elsewhere

    tools = [
        {"type": f"computer_{tool_version}", "name": "computer", "display_width_px": 1024, "display_height_px": 768},
        {"type": f"text_editor_{tool_version}", "name": "str_replace_editor"},
        {"type": f"bash_{tool_version}", "name": "bash"}
    ]

    # Main agent loop (with iteration limit to prevent runaway API costs)

    iterations = 0
    while True and iterations < max_iterations:
        iterations += 1
        # Set up optional thinking parameter (for Claude Sonnet 3.7)

        thinking = None
        if thinking_budget:
            thinking = {"type": "enabled", "budget_tokens": thinking_budget}

        # Call the Claude API

        response = client.beta.messages.create(
            model=model,
            max_tokens=max_tokens,
            messages=messages,
            tools=tools,
            betas=[beta_flag],
            thinking=thinking
        )

        # Add Claude's response to the conversation history

        response_content = response.content
        messages.append({"role": "assistant", "content": response_content})

        # Check if Claude used any tools

        tool_results = []
        for block in response_content:
            if block.type == "tool_use":
                # In a real app, you would execute the tool here

                # For example: result = run_tool(block.name, block.input)

                result = {"result": "Tool executed successfully"}

                # Format the result for Claude

                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result
                })

        # If no tools were used, Claude is done - return the final messages

        if not tool_results:
            return messages

        # Add tool results to messages for the next iteration with Claude

        messages.append({"role": "user", "content": tool_results})
```
The loop continues until either Claude responds without requesting any tools (task completion) or the maximum iteration limit is reached. This safeguard prevents potential infinite loops that could result in unexpected API costs.

>   **⚠️ Warning**
>
> When using the computer use tool, you must include the appropriate beta flag for your model version:

  <AccordionGroup>
    <Accordion title="Claude 4 models">
      When using `computer_20250124`, include this beta flag:
```
      "betas": ["computer-use-2025-01-24"]
```
    </Accordion>

    <Accordion title="Claude Sonnet 3.7">
      When using `computer_20250124`, include this beta flag:
```
      "betas": ["computer-use-2025-01-24"]
```
    </Accordion>
  </AccordionGroup>

We recommend trying the reference implementation out before reading the rest of this documentation.

### Optimize model performance with prompting

Here are some tips on how to get the best quality outputs:

1. Specify simple, well-defined tasks and provide explicit instructions for each step.
2. Claude sometimes assumes outcomes of its actions without explicitly checking their results. To prevent this you can prompt Claude with `After each step, take a screenshot and carefully evaluate if you have achieved the right outcome. Explicitly show your thinking: "I have evaluated step X..." If not correct, try again. Only when you confirm a step was executed correctly should you move on to the next one.`
3. Some UI elements (like dropdowns and scrollbars) might be tricky for Claude to manipulate using mouse movements. If you experience this, try prompting the model to use keyboard shortcuts.
4. For repeatable tasks or UI interactions, include example screenshots and tool calls of successful outcomes in your prompt.
5. If you need the model to log in, provide it with the username and password in your prompt inside xml tags like `<robot_credentials>`. Using computer use within applications that require login increases the risk of bad outcomes as a result of prompt injection. Please review our [guide on mitigating prompt injections](/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) before providing the model with login credentials.

<Tip>
  If you repeatedly encounter a clear set of issues or know in advance the tasks
  Claude will need to complete, use the system prompt to provide Claude with
  explicit tips or instructions on how to do the tasks successfully.
</Tip>

### System prompts

When one of the Anthropic-defined tools is requested via the Claude API, a computer use-specific system prompt is generated. It's similar to the [tool use system prompt](/en/docs/agents-and-tools/tool-use/implement-tool-use#tool-use-system-prompt) but starts with:

> You have access to a set of functions you can use to answer the user's question. This includes access to a sandboxed computing environment. You do NOT currently have the ability to inspect files or interact with external resources, except by invoking the below functions.

As with regular tool use, the user-provided `system_prompt` field is still respected and used in the construction of the combined system prompt.

### Available actions

The computer use tool supports these actions:

**Basic actions (all versions)**

* **screenshot** - Capture the current display
* **left\_click** - Click at coordinates `[x, y]`
* **type** - Type text string
* **key** - Press key or key combination (e.g., "ctrl+s")
* **mouse\_move** - Move cursor to coordinates

**Enhanced actions (`computer_20250124`)**
Available in Claude 4 models and Claude Sonnet 3.7:

* **scroll** - Scroll in any direction with amount control
* **left\_click\_drag** - Click and drag between coordinates
* **right\_click**, **middle\_click** - Additional mouse buttons
* **double\_click**, **triple\_click** - Multiple clicks
* **left\_mouse\_down**, **left\_mouse\_up** - Fine-grained click control
* **hold\_key** - Hold a key while performing other actions
* **wait** - Pause between actions

<Accordion title="Example actions">
```json
  // Take a screenshot
  {
    "action": "screenshot"
  }

  // Click at position
  {
    "action": "left_click",
    "coordinate": [500, 300]
  }

  // Type text
  {
    "action": "type",
    "text": "Hello, world!"
  }

  // Scroll down (Claude 4/3.7)
  {
    "action": "scroll",
    "coordinate": [500, 400],
    "scroll_direction": "down",
    "scroll_amount": 3
  }
```
</Accordion>

### Tool parameters

| Parameter           | Required | Description                                               |
| ------------------- | -------- | --------------------------------------------------------- |
| `type`              | Yes      | Tool version (`computer_20250124` or `computer_20241022`) |
| `name`              | Yes      | Must be "computer"                                        |
| `display_width_px`  | Yes      | Display width in pixels                                   |
| `display_height_px` | Yes      | Display height in pixels                                  |
| `display_number`    | No       | Display number for X11 environments                       |

>   **⚠️ Warning**
>
> Keep display resolution at or below 1280x800 (WXGA) for best performance. Higher resolutions may cause accuracy issues due to [image resizing](/en/docs/build-with-claude/vision#evaluate-image-size).

>   **📝 Note**
>
>   **Important**: The computer use tool must be explicitly executed by your application - Claude cannot execute it directly. You are responsible for implementing the screenshot capture, mouse movements, keyboard inputs, and other actions based on Claude's requests.

### Enable thinking capability in Claude 4 models and Claude Sonnet 3.7

Claude Sonnet 3.7 introduced a new "thinking" capability that allows you to see the model's reasoning process as it works through complex tasks. This feature helps you understand how Claude is approaching a problem and can be particularly valuable for debugging or educational purposes.

To enable thinking, add a `thinking` parameter to your API request:
```json
"thinking": {
  "type": "enabled",
  "budget_tokens": 1024
}
```
The `budget_tokens` parameter specifies how many tokens Claude can use for thinking. This is subtracted from your overall `max_tokens` budget.

When thinking is enabled, Claude will return its reasoning process as part of the response, which can help you:

1. Understand the model's decision-making process
2. Identify potential issues or misconceptions
3. Learn from Claude's approach to problem-solving
4. Get more visibility into complex multi-step operations

Here's an example of what thinking output might look like:
```
[Thinking]
I need to save a picture of a cat to the desktop. Let me break this down into steps:

1. First, I'll take a screenshot to see what's on the desktop
2. Then I'll look for a web browser to search for cat images
3. After finding a suitable image, I'll need to save it to the desktop

Let me start by taking a screenshot to see what's available...
```

### Augmenting computer use with other tools

The computer use tool can be combined with other tools to create more powerful automation workflows. This is particularly useful when you need to:

* Execute system commands ([bash tool](/en/docs/agents-and-tools/tool-use/bash-tool))
* Edit configuration files or scripts ([text editor tool](/en/docs/agents-and-tools/tool-use/text-editor-tool))
* Integrate with custom APIs or services (custom tools)
```bash
  curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: computer-use-2025-01-24" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 2000,
      "tools": [
        {
          "type": "computer_20250124",
          "name": "computer",
          "display_width_px": 1024,
          "display_height_px": 768,
          "display_number": 1
        },
        {
          "type": "text_editor_20250124",
          "name": "str_replace_editor"
        },
        {
          "type": "bash_20250124",
          "name": "bash"
        },
        {
          "name": "get_weather",
          "description": "Get the current weather in a given location",
          "input_schema": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA"
              },
              "unit": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"],
                "description": "The unit of temperature, either 'celsius' or 'fahrenheit'"
              }
            },
            "required": ["location"]
          }
        }
      ],
      "messages": [
        {
          "role": "user",
          "content": "Find flights from San Francisco to a place with warmer weather."
        }
      ],
      "thinking": {
        "type": "enabled",
        "budget_tokens": 1024
      }
    }'
```
```Python
  import anthropic

  client = anthropic.Anthropic()

  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      tools=[
          {
            "type": "computer_20250124",
            "name": "computer",
            "display_width_px": 1024,
            "display_height_px": 768,
            "display_number": 1,
          },
          {
            "type": "text_editor_20250124",
            "name": "str_replace_editor"
          },
          {
            "type": "bash_20250124",
            "name": "bash"
          },
          {
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "input_schema": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
                },
                "unit": {
                  "type": "string",
                  "enum": ["celsius", "fahrenheit"],
                  "description": "The unit of temperature, either 'celsius' or 'fahrenheit'"
                }
              },
              "required": ["location"]
            }
          },
      ],
      messages=[{"role": "user", "content": "Find flights from San Francisco to a place with warmer weather."}],
      betas=["computer-use-2025-01-24"],
      thinking={"type": "enabled", "budget_tokens": 1024},
  )
  print(response)
```
```TypeScript
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  const message = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 1024,
    tools: [
        {
          type: "computer_20250124",
          name: "computer",
          display_width_px: 1024,
          display_height_px: 768,
          display_number: 1,
        },
        {
          type: "text_editor_20250124",
          name: "str_replace_editor"
        },
        {
          type: "bash_20250124",
          name: "bash"
        },
        {
          name: "get_weather",
          description: "Get the current weather in a given location",
          input_schema: {
            type: "object",
            properties: {
              location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
              },
              unit: {
                type: "string",
                enum: ["celsius", "fahrenheit"],
                description: "The unit of temperature, either 'celsius' or 'fahrenheit'"
              }
            },
            required: ["location"]
          }
        },
    ],
    messages: [{ role: "user", content: "Find flights from San Francisco to a place with warmer weather." }],
    betas: ["computer-use-2025-01-24"],
    thinking: { type: "enabled", budget_tokens: 1024 },
  });
  console.log(message);
```
```java
  import java.util.List;
  import java.util.Map;

  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.core.JsonValue;
  import com.anthropic.models.beta.messages.BetaMessage;
  import com.anthropic.models.beta.messages.MessageCreateParams;
  import com.anthropic.models.beta.messages.BetaToolBash20250124;
  import com.anthropic.models.beta.messages.BetaToolComputerUse20250124;
  import com.anthropic.models.beta.messages.BetaToolTextEditor20250124;
  import com.anthropic.models.beta.messages.BetaThinkingConfigEnabled;
  import com.anthropic.models.beta.messages.BetaThinkingConfigParam;
  import com.anthropic.models.beta.messages.BetaTool;

  public class MultipleToolsExample {

      public static void main(String[] args) {
          AnthropicClient client = AnthropicOkHttpClient.fromEnv();

          MessageCreateParams params = MessageCreateParams.builder()
                  .model("claude-sonnet-4-5")
                  .maxTokens(1024)
                  .addTool(BetaToolComputerUse20250124.builder()
                          .displayWidthPx(1024)
                          .displayHeightPx(768)
                          .displayNumber(1)
                          .build())
                  .addTool(BetaToolTextEditor20250124.builder()
                          .build())
                  .addTool(BetaToolBash20250124.builder()
                          .build())
                  .addTool(BetaTool.builder()
                          .name("get_weather")
                          .description("Get the current weather in a given location")
                          .inputSchema(BetaTool.InputSchema.builder()
                                  .properties(
                                          JsonValue.from(
                                                  Map.of(
                                                          "location", Map.of(
                                                                  "type", "string",
                                                                  "description", "The city and state, e.g. San Francisco, CA"
                                                          ),
                                                          "unit", Map.of(
                                                                  "type", "string",
                                                                  "enum", List.of("celsius", "fahrenheit"),
                                                                  "description", "The unit of temperature, either 'celsius' or 'fahrenheit'"
                                                          )
                                                  )
                                          ))
                                  .build()
                          )
                          .build())
                  .thinking(BetaThinkingConfigParam.ofEnabled(
                          BetaThinkingConfigEnabled.builder()
                                  .budgetTokens(1024)
                                  .build()
                  ))
                  .addUserMessage("Find flights from San Francisco to a place with warmer weather.")
                  .addBeta("computer-use-2025-01-24")
                  .build();

          BetaMessage message = client.beta().messages().create(params);
          System.out.println(message);
      }
  }
```

### Build a custom computer use environment

The [reference implementation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo) is meant to help you get started with computer use. It includes all of the components needed have Claude use a computer. However, you can build your own environment for computer use to suit your needs. You'll need:

* A virtualized or containerized environment suitable for computer use with Claude
* An implementation of at least one of the Anthropic-defined computer use tools
* An agent loop that interacts with the Claude API and executes the `tool_use` results using your tool implementations
* An API or UI that allows user input to start the agent loop

#### Implement the computer use tool

The computer use tool is implemented as a schema-less tool. When using this tool, you don't need to provide an input schema as with other tools; the schema is built into Claude's model and can't be modified.

<Steps>
  <Step title="Set up your computing environment">
    Create a virtual display or connect to an existing display that Claude will interact with. This typically involves setting up Xvfb (X Virtual Framebuffer) or similar technology.
  </Step>

  <Step title="Implement action handlers">
    Create functions to handle each action type that Claude might request:
```python
    def handle_computer_action(action_type, params):
        if action_type == "screenshot":
            return capture_screenshot()
        elif action_type == "left_click":
            x, y = params["coordinate"]
            return click_at(x, y)
        elif action_type == "type":
            return type_text(params["text"])
        # ... handle other actions

```
  </Step>

  <Step title="Process Claude's tool calls">
    Extract and execute tool calls from Claude's responses:
```python
    for content in response.content:
        if content.type == "tool_use":
            action = content.input["action"]
            result = handle_computer_action(action, content.input)
            
            # Return result to Claude

            tool_result = {
                "type": "tool_result",
                "tool_use_id": content.id,
                "content": result
            }
```
  </Step>

  <Step title="Implement the agent loop">
    Create a loop that continues until Claude completes the task:
```python
    while True:
        response = client.beta.messages.create(...)
        
        # Check if Claude used any tools

        tool_results = process_tool_calls(response)
        
        if not tool_results:
            # No more tool use, task complete

            break
            
        # Continue conversation with tool results

        messages.append({"role": "user", "content": tool_results})
```
  </Step>
</Steps>

#### Handle errors

When implementing the computer use tool, various errors may occur. Here's how to handle them:

<AccordionGroup>
  <Accordion title="Screenshot capture failure">
    If screenshot capture fails, return an appropriate error message:
```json
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: Failed to capture screenshot. Display may be locked or unavailable.",
          "is_error": true
        }
      ]
    }
```
  </Accordion>

  <Accordion title="Invalid coordinates">
    If Claude provides coordinates outside the display bounds:
```json
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: Coordinates (1200, 900) are outside display bounds (1024x768).",
          "is_error": true
        }
      ]
    }
```
  </Accordion>

  <Accordion title="Action execution failure">
    If an action fails to execute:
```json
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: Failed to perform click action. The application may be unresponsive.",
          "is_error": true
        }
      ]
    }
```
  </Accordion>
</AccordionGroup>

#### Follow implementation best practices

<AccordionGroup>
  <Accordion title="Use appropriate display resolution">
    Set display dimensions that match your use case while staying within recommended limits:

    * For general desktop tasks: 1024x768 or 1280x720
    * For web applications: 1280x800 or 1366x768
    * Avoid resolutions above 1920x1080 to prevent performance issues
  </Accordion>

  <Accordion title="Implement proper screenshot handling">
    When returning screenshots to Claude:

    * Encode screenshots as base64 PNG or JPEG
    * Consider compressing large screenshots to improve performance
    * Include relevant metadata like timestamp or display state
  </Accordion>

  <Accordion title="Add action delays">
    Some applications need time to respond to actions:
```python
    def click_and_wait(x, y, wait_time=0.5):
        click_at(x, y)
        time.sleep(wait_time)  # Allow UI to update

```
  </Accordion>

  <Accordion title="Validate actions before execution">
    Check that requested actions are safe and valid:
```python
    def validate_action(action_type, params):
        if action_type == "left_click":
            x, y = params.get("coordinate", (0, 0))
            if not (0 <= x < display_width and 0 <= y < display_height):
                return False, "Coordinates out of bounds"
        return True, None
```
  </Accordion>

  <Accordion title="Log actions for debugging">
    Keep a log of all actions for troubleshooting:
```python
    import logging

    def log_action(action_type, params, result):
        logging.info(f"Action: {action_type}, Params: {params}, Result: {result}")
```
  </Accordion>
</AccordionGroup>

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
