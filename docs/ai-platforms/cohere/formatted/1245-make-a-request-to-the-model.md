---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Make a request to the model

response = co.chat(
    message=PROMPT,
    model="command-r",
    temperature=0.3,
    documents=documents,
    prompt_truncation="AUTO"
)

print(response.text)
```
```txt title="Output"
Here are the overall revenue numbers for the years 2021, 2022, and 2023 as bullet points:
- 2021: $5,992 million
- 2022: $8,399 million
- 2023: $9,917 million

Revenue increased by 18% in 2023 compared to 2022, primarily due to a 14% increase in Nights and Experiences Booked, which reached 54.5 million. This, combined with higher average daily rates, resulted in a 16% increase in Gross Booking Value, which reached $10.0 billion.

The revenue growth trend demonstrates sustained strong travel demand. On a constant-currency basis, revenue increased by 17% in 2023 compared to the previous year.

Other factors influencing the company's financial performance are described outside of the revenue growth trends.
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
