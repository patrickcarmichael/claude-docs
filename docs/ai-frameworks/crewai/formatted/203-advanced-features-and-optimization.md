---
title: "Crewai: Advanced Features and Optimization"
description: "Advanced Features and Optimization section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Advanced Features and Optimization


Learn how to get the most out of your LLM configuration:

<AccordionGroup>
  <Accordion title="Context Window Management">
    CrewAI includes smart context management features:

    ```python  theme={null}
    from crewai import LLM

    # CrewAI automatically handles:
    # 1. Token counting and tracking
    # 2. Content summarization when needed
    # 3. Task splitting for large contexts

    llm = LLM(
        model="gpt-4",
        max_tokens=4000,  # Limit response length
    )
    ```

    <Info>
      Best practices for context management:

      1. Choose models with appropriate context windows
      2. Pre-process long inputs when possible
      3. Use chunking for large documents
      4. Monitor token usage to optimize costs
    </Info>
  </Accordion>

  <Accordion title="Performance Optimization">
    <Steps>
      <Step title="Token Usage Optimization">
        Choose the right context window for your task:

        * Small tasks (up to 4K tokens): Standard models
        * Medium tasks (between 4K-32K): Enhanced models
        * Large tasks (over 32K): Large context models

        ```python  theme={null}
        # Configure model with appropriate settings
        llm = LLM(
            model="openai/gpt-4-turbo-preview",
            temperature=0.7,    # Adjust based on task
            max_tokens=4096,    # Set based on output needs
            timeout=300        # Longer timeout for complex tasks
        )
        ```

        <Tip>
          * Lower temperature (0.1 to 0.3) for factual responses
          * Higher temperature (0.7 to 0.9) for creative tasks
        </Tip>
      </Step>

      <Step title="Best Practices">
        1. Monitor token usage
        2. Implement rate limiting
        3. Use caching when possible
        4. Set appropriate max\_tokens limits
      </Step>
    </Steps>

    <Info>
      Remember to regularly monitor your token usage and adjust your configuration as needed to optimize costs and performance.
    </Info>
  </Accordion>

  <Accordion title="Drop Additional Parameters">
    CrewAI internally uses native sdks for LLM calls, which allows you to drop additional parameters that are not needed for your specific use case. This can help simplify your code and reduce the complexity of your LLM configuration.
    For example, if you don't need to send the <code>stop</code> parameter, you can simply omit it from your LLM call:

    ```python  theme={null}
    from crewai import LLM
    import os

    os.environ["OPENAI_API_KEY"] = "<api-key>"

    o3_llm = LLM(
        model="o3",
        drop_params=True,
        additional_drop_params=["stop"]
    )
    ```
  </Accordion>

  <Accordion title="Transport Interceptors">
    CrewAI provides message interceptors for several providers, allowing you to hook into request/response cycles at the transport layer.

    **Supported Providers:**

    * ✅ OpenAI
    * ✅ Anthropic

    **Basic Usage:**

    ```python  theme={null}
    import httpx
    from crewai import LLM
    from crewai.llms.hooks import BaseInterceptor

    class CustomInterceptor(BaseInterceptor[httpx.Request, httpx.Response]):
    """Custom interceptor to modify requests and responses."""

    def on_outbound(self, request: httpx.Request) -> httpx.Request:
        """Print request before sending to the LLM provider."""
        print(request)
        return request

    def on_inbound(self, response: httpx.Response) -> httpx.Response:
        """Process response after receiving from the LLM provider."""
        print(f"Status: {response.status_code}")
        print(f"Response time: {response.elapsed}")
        return response

    # Use the interceptor with an LLM
    llm = LLM(
    model="openai/gpt-4o",
    interceptor=CustomInterceptor()
    )
    ```

    **Important Notes:**

    * Both methods must return the received object or type of object.
    * Modifying received objects may result in unexpected behavior or application crashes.
    * Not all providers support interceptors - check the supported providers list above

    <Info>
      Interceptors operate at the transport layer. This is particularly useful for:

      * Message transformation and filtering
      * Debugging API interactions
    </Info>
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Output:](./202-output.md)

**Next:** [Common Issues and Solutions →](./204-common-issues-and-solutions.md)
