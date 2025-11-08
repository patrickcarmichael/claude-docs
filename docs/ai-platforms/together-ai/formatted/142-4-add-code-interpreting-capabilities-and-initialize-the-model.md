---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 4. Add code interpreting capabilities and initialize the model

Now we define the function that will use the E2B code interpreter. Every time the LLM assistant decides that it needs to execute code, this function will be used. Read more about the Code Interpreter SDK [here](https://e2b.dev/docs/code-interpreter/installation).

We also initialize the Together AI client. The function for matching code blocks is important because we need to pick the right part of the output that contains the code produced by the LLM. The chat function takes care of the interaction with the LLM. It calls the E2B code interpreter anytime there is a code to be run.
````py
def code_interpret(e2b_code_interpreter, code):
    print("Running code interpreter...")
    exec = e2b_code_interpreter.notebook.exec_cell(
        code,
        on_stderr=lambda stderr: print("[Code Interpreter]", stderr),
        on_stdout=lambda stdout: print("[Code Interpreter]", stdout),
        # You can also stream code execution results

        # on_result=...

    )

    if exec.error:
        print("[Code Interpreter ERROR]", exec.error)
    else:
        return exec.results


client = Together()

pattern = re.compile(
    r"```python\n(.*?)\n```", re.DOTALL
)  # Match everything in between ```python and ```python

def match_code_blocks(llm_response):
    match = pattern.search(llm_response)
    if match:
        code = match.group(1)
        print(code)
        return code
    return ""


def chat_with_llm(e2b_code_interpreter, user_message):
    print(f"\n{'='*50}\nUser message: {user_message}\n{'='*50}")

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message},
    ]

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
    )

    response_message = response.choices[0].message
    python_code = match_code_blocks(response_message.content)
    if python_code != "":
        code_interpreter_results = code_interpret(
            e2b_code_interpreter, python_code
        )
        return code_interpreter_results
    else:
        print(
            f"Failed to match any Python code in model's response {response_message}"
        )
        return []
````

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
