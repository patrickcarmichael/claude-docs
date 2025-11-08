---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create tools

The pre-requisite, before we can run a tool use workflow, is to set up the tools. Let's create three tools:

* `search_faqs`: A tool for searching the FAQs of a company. For simplicity, we'll not implement any retrieval logic, but we'll simply pass a list of three predefined documents. In practice, we would set up a retrieval system as we did in Chapters 4, 5, and 6.
* `search_emails`: A tool for searching the emails. Same as above, we'll simply pass a list of predefined emails.
* `create_calendar_event`: A tool for creating new calendar events. Again, for simplicity, we'll only return mock successful event creations without actual implementation. In practice, we can connect to a calendar service API and implement all the necessary logic here.

Here, we are defining a Python function for each tool, but more broadly, the tool can be any function or service that can receive and send objects.
```python PYTHON
def search_faqs(query):
    faqs = [
        {
            "text": "Submitting Travel Expenses:\nSubmit your expenses through our user-friendly finance tool."
        },
        {
            "text": "Side Projects Policy:\nWe encourage you to explore your passions! Just ensure there's no conflict of interest with our business."
        },
        {
            "text": "Wellness Benefits:\nTo promote a healthy lifestyle, we provide gym memberships, on-site yoga classes, and health insurance."
        },
    ]
    return faqs


def search_emails(query):
    emails = [
        {
            "from": "hr@co1t.com",
            "to": "david@co1t.com",
            "date": "2024-06-24",
            "subject": "A Warm Welcome to Co1t, David!",
            "text": "We are delighted to have you on board. Please find attached your first week's agenda.",
        },
        {
            "from": "it@co1t.com",
            "to": "david@co1t.com",
            "date": "2024-06-24",
            "subject": "Instructions for IT Setup",
            "text": "Welcome, David! To get you started, please follow the attached guide to set up your work accounts.",
        },
        {
            "from": "john@co1t.com",
            "to": "david@co1t.com",
            "date": "2024-06-24",
            "subject": "First Week Check-In",
            "text": "Hi David, let's chat briefly tomorrow to discuss your first week. Also, come join us for lunch this Thursday at noon to meet everyone!",
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

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
