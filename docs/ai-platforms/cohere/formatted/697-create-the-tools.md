---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create the tools

def search_faqs(query):
    faqs = [
        {
            "text": "Reimbursing Travel Expenses: Easily manage your travel expenses by submitting them through our finance tool. Approvals are prompt and straightforward."
        },
        {
            "text": "Working from Abroad: Working remotely from another country is possible. Simply coordinate with your manager and ensure your availability during core hours."
        },
    ]
    return faqs


def search_emails(query):
    emails = [
        {
            "from": "it@co1t.com",
            "to": "david@co1t.com",
            "date": "2024-06-24",
            "subject": "Setting Up Your IT Needs",
            "text": "Greetings! To ensure a seamless start, please refer to the attached comprehensive guide, which will assist you in setting up all your work accounts.",
        },
        {
            "from": "john@co1t.com",
            "to": "david@co1t.com",
            "date": "2024-06-24",
            "subject": "First Week Check-In",
            "text": "Hello! I hope you're settling in well. Let's connect briefly tomorrow to discuss how your first week has been going. Also, make sure to join us for a welcoming lunch this Thursday at noon—it's a great opportunity to get to know your colleagues!",
        },
    ]
    return emails


def create_calendar_event(date: str, time: str, duration: int):
    # You can implement any logic here

    return {
        "is_success": True,
        "message": f"Created a {duration} hour long event at {time} on {date}",
    }


functions_map = {
    "search_faqs": search_faqs,
    "search_emails": search_emails,
    "create_calendar_event": create_calendar_event,
}
```
The second and final setup step is to define the tool schemas in a format that can be passed to the Chat endpoint. The schema must contain the following fields: `name`, `description`, and `parameters` in the format shown below.

This schema informs the LLM about what the tool does, and the LLM decides whether to use a particular tool based on it. Therefore, the more descriptive and specific the schema, the more likely the LLM will make the right tool call decisions.

Further reading:

* [Documentation on parameter types in tool use](https://docs.cohere.com/v2/docs/parameter-types-in-tool-use)
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
