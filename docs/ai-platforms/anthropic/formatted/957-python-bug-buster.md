---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Python bug buster

Source: https://docs.claude.com/en/resources/prompt-library/python-bug-buster

Detect and fix bugs in Python code.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                                                             |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | Your task is to analyze the provided Python code snippet, identify any bugs or errors present, and provide a corrected version of the code that resolves these issues. Explain the problems you found in the original code and how your fixes address them. The corrected code should be functional, efficient, and adhere to best practices in Python programming. |
| User   | def calculate\_average(nums): <br /> sum = 0 <br /> for num in nums: <br /> sum += num <br /> average = sum / len(nums) <br /> return average <br /><br /> numbers = \[10, 20, 30, 40, 50] <br /> result = calculate\_average(numbers) <br /> print("The average is:", results)                                                                                     |

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
