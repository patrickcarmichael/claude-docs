---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Code consultant

Source: https://docs.claude.com/en/resources/prompt-library/code-consultant

Suggest improvements to optimize Python code performance.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | Your task is to analyze the provided Python code snippet and suggest improvements to optimize its performance. Identify areas where the code can be made more efficient, faster, or less resource-intensive. Provide specific suggestions for optimization, along with explanations of how these changes can enhance the code's performance. The optimized code should maintain the same functionality as the original code while demonstrating improved efficiency. |
| User   | def fibonacci(n): <br /> if n \<= 0: <br /> return \[] <br /> elif n == 1: <br /> return \[0] <br /> elif n == 2: <br /> return \[0, 1] <br /> else: <br /> fib = \[0, 1] <br /> for i in range(2, n): <br /> fib.append(fib\[i-1] + fib\[i-2]) <br /> return fib                                                                                                                                                                                                    |

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
