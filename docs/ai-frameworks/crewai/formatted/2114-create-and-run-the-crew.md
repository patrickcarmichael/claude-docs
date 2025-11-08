---
title: "Crewai: Create and run the crew"
description: "Create and run the crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create and run the crew

crew = Crew(
    agents=[expert_analyst],
    tasks=[inspection_task]
)

result = crew.kickoff()
```

### Tool Details

When working with multimodal agents, the `AddImageTool` is automatically configured with the following schema:

```python  theme={null}
class AddImageToolSchema:
    image_url: str  # Required: The URL or path of the image to process
    action: Optional[str] = None  # Optional: Additional context or specific questions about the image
```

The multimodal agent will automatically handle the image processing through its built-in tools, allowing it to:

* Access images via URLs or local file paths
* Process image content with optional context or specific questions
* Provide analysis and insights based on the visual information and task requirements

### Best Practices

When working with multimodal agents, keep these best practices in mind:

1. **Image Access**
   * Ensure your images are accessible via URLs that the agent can reach
   * For local images, consider hosting them temporarily or using absolute file paths
   * Verify that image URLs are valid and accessible before running tasks

2. **Task Description**
   * Be specific about what aspects of the image you want the agent to analyze
   * Include clear questions or requirements in the task description
   * Consider using the optional `action` parameter for focused analysis

3. **Resource Management**
   * Image processing may require more computational resources than text-only tasks
   * Some language models may require base64 encoding for image data
   * Consider batch processing for multiple images to optimize performance

4. **Environment Setup**
   * Verify that your environment has the necessary dependencies for image processing
   * Ensure your language model supports multimodal capabilities
   * Test with small images first to validate your setup

5. **Error Handling**
   * Implement proper error handling for image loading failures
   * Have fallback strategies for when image processing fails
   * Monitor and log image processing operations for debugging

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create a task with specific analysis requirements](./2113-create-a-task-with-specific-analysis-requirements.md)

**Next:** [Overview →](./2115-overview.md)
