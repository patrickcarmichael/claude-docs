---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Response Format

The API returns:

* `session_id`: Identifier for the current session
* `outputs`: Array of execution outputs, which can include:
  * Execution output (the return value of your snippet)
  * Standard output (`stdout`)
  * Standard error (`stderr`)
  * Error messages
  * Rich display data (images, HTML, etc.)
    Example
```json
{
  "data": {
    "outputs": [
      {
        "data": "Hello, world!\n",
        "type": "stdout"
      },
      {
        "data": {
          "image/png": "iVBORw0KGgoAAAANSUhEUgAAA...",
          "text/plain": "<Figure size 640x480 with 1 Axes>"
        },
        "type": "display_data"
      }
    ],
    "session_id": "ses_CM42NfvvzCab123"
  },
  "errors": null
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
