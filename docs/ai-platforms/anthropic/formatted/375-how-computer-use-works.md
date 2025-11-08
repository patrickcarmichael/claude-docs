---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How computer use works

<Steps>
  <Step title="1. Provide Claude with the computer use tool and a user prompt" icon="toolbox">
    * Add the computer use tool (and optionally other tools) to your API request.
    * Include a user prompt that requires desktop interaction, e.g., "Save a picture of a cat to my desktop."
  </Step>

  <Step title="2. Claude decides to use the computer use tool" icon="screwdriver-wrench">
    * Claude assesses if the computer use tool can help with the user's query.
    * If yes, Claude constructs a properly formatted tool use request.
    * The API response has a `stop_reason` of `tool_use`, signaling Claude's intent.
  </Step>

  <Step title="3. Extract tool input, evaluate the tool on a computer, and return results" icon="computer">
    * On your end, extract the tool name and input from Claude's request.
    * Use the tool on a container or Virtual Machine.
    * Continue the conversation with a new `user` message containing a `tool_result` content block.
  </Step>

  <Step title="4. Claude continues calling computer use tools until it's completed the task" icon="arrows-spin">
    * Claude analyzes the tool results to determine if more tool use is needed or the task has been completed.
    * If Claude decides it needs another tool, it responds with another `tool_use` `stop_reason` and you should return to step 3.
    * Otherwise, it crafts a text response to the user.
  </Step>
</Steps>

We refer to the repetition of steps 3 and 4 without user input as the "agent loop" - i.e., Claude responding with a tool use request and your application responding to Claude with the results of evaluating that request.

### The computing environment

Computer use requires a sandboxed computing environment where Claude can safely interact with applications and the web. This environment includes:

1. **Virtual display**: A virtual X11 display server (using Xvfb) that renders the desktop interface Claude will see through screenshots and control with mouse/keyboard actions.

2. **Desktop environment**: A lightweight UI with window manager (Mutter) and panel (Tint2) running on Linux, which provides a consistent graphical interface for Claude to interact with.

3. **Applications**: Pre-installed Linux applications like Firefox, LibreOffice, text editors, and file managers that Claude can use to complete tasks.

4. **Tool implementations**: Integration code that translates Claude's abstract tool requests (like "move mouse" or "take screenshot") into actual operations in the virtual environment.

5. **Agent loop**: A program that handles communication between Claude and the environment, sending Claude's actions to the environment and returning the results (screenshots, command outputs) back to Claude.

When you use computer use, Claude doesn't directly connect to this environment. Instead, your application:

1. Receives Claude's tool use requests
2. Translates them into actions in your computing environment
3. Captures the results (screenshots, command outputs, etc.)
4. Returns these results to Claude

For security and isolation, the reference implementation runs all of this inside a Docker container with appropriate port mappings for viewing and interacting with the environment.

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
