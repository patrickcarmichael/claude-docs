---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Creating Test Cases

When you access the Evaluation screen, you have several options to create test cases:

1. Click the '+ Add Row' button at the bottom left to manually add a case.
2. Use the 'Generate Test Case' feature to have Claude automatically generate test cases for you.
3. Import test cases from a CSV file.

To use the 'Generate Test Case' feature:

<Steps>
  <Step title="Click on 'Generate Test Case'">
    Claude will generate test cases for you, one row at a time for each time you click the button.
  </Step>

  <Step title="Edit generation logic (optional)">
    You can also edit the test case generation logic by clicking on the arrow dropdown to the right of the 'Generate Test Case' button, then on 'Show generation logic' at the top of the Variables window that pops up. You may have to click \`Generate' on the top right of this window to populate initial generation logic.

    Editing this allows you to customize and fine tune the test cases that Claude generates to greater precision and specificity.
  </Step>
</Steps>

Here's an example of a populated Evaluation screen with several test cases:

<img src="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/eval_populated.png?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=aa5f378cd1fd8bee94acbb557476f690" alt="Populated Evaluation Screen" data-og-width="1999" width="1999" data-og-height="1061" height="1061" data-path="images/eval_populated.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/eval_populated.png?w=280&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=da25331850100232004b2b4120acbc92 280w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/eval_populated.png?w=560&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=35e3ad0abb9226a616b2f2484237f012 560w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/eval_populated.png?w=840&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=42df4fd14669cf2ff21b404b74e16a97 840w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/eval_populated.png?w=1100&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=c8f77e4d68b0ef75d0d9cb18d27387f7 1100w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/eval_populated.png?w=1650&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=f8b324b1995be107795b39379818c324 1650w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/eval_populated.png?w=2500&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=77d58591d4fac46b9de9ceb24568a5fa 2500w" />

>   **📝 Note**
>
> If you update your original prompt text, you can re-run the entire eval suite against the new prompt to see how changes affect performance across all test cases.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
