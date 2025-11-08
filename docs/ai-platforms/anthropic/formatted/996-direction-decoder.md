---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Direction decoder

Source: https://docs.claude.com/en/resources/prompt-library/direction-decoder

Transform natural language into step-by-step directions.

> Copy this prompt into our developer [Console](https://console.anthropic.com/login?selectAccount=true\&returnTo=%2Fdashboard%3F) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | Your task is to take the provided natural language description of a process or task and transform it into clear, concise step-by-step directions that are logical, sequential, and easy to follow. Use imperative language and begin each step with an action verb. Provide necessary details and explanations to ensure the reader can complete the task successfully. If the original description is unclear, ambiguous, or lacks sufficient information, ask for clarification or additional details. |
| User   | To make a cup of tea, start by boiling some water in a kettle. While the water is heating up, get a mug and put a tea bag in it. Once the water is boiling, carefully pour it into the mug, over the tea bag. Let the tea steep for a few minutes, depending on how strong you like it. After steeping, remove the tea bag and add milk and sugar to taste. Stir everything together and enjoy your hot cup of tea.                                                                                      |

### Example output

> 1. Fill a kettle with water and place it on the stove to boil.
> 2. While waiting for the water to boil, select a mug and place a tea bag inside it.
> 3. Once the water reaches a boil, carefully pour the hot water into the mug, over the tea bag.
> 4. Allow the tea to steep in the hot water for the desired amount of time, typically 2-5 minutes, depending on the preferred strength.
> 5. After the steeping time has elapsed, remove the tea bag from the mug and discard it.
> 6. Add milk and sugar to the tea, according to your taste preferences.
> 7. Using a spoon, stir the tea, milk, and sugar together until well combined.
> 8. Your cup of tea is now ready to enjoy. Drink it while it's still hot.

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
