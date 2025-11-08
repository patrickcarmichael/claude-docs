---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 3. Introduce citations to the summary for grounding \[#introduce-citations-to-the-summary-for-grounding]

When summarizing long documents, introducing citations is one simple method for checking the factuality of the summary without needing to read the full document.

We've trained Command-R to introduce citations whenever prompted by our grounded generations instructions. Triggering this grounded mode is straightforward. Starting from the previous snippet, we only need to make two changes:

1. Pass our text to the `documents` argument
2. Pass our instructions to the `message` argument

For more information on how to enable grounded generation via our `co.chat` API, please refer to our [documentation](https://docs.cohere.com/reference/chat).

Finally, note that we chunk the IMF report into multiple documents before passing them to `co.chat`. This isn't necessary (`co.chat` annotates citations at the character level), but allows for more human-readable citations.
```python PYTHON
summarize_preamble = """\
You will receive a series of text fragments from an article that are presented in chronological order. \
As the assistant, you must generate responses to user's requests based on the information given in the fragments. \
Ensure that your responses are accurate and truthful, and that you reference your sources where appropriate to answer \
the queries, regardless of their complexity.\
"""

instructions = """\

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
