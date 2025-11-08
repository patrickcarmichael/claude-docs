---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Iterate over the retrieved objects and print their details

for obj in response.objects:
    title = obj.properties.get("title")
    description = obj.properties.get("description")
    distance = (
        obj.metadata.distance
    )  # Get the distance metadata (A lower value for a distance means that two vectors are closer to one another than a higher value)

    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"Distance: {distance}")
    print("-" * 50)
```
The output will look something like this (NOTE: a lower value for a `Distance` means that two vectors are closer to one another than those with a higher value):
```
Title: Pharmacy Regulations
Description: Overview of state and federal regulations governing pharmacy practices, including prescription drug monitoring, compounding, and controlled substances.
Distance: 0.5904817581176758
--------------------------------------------------
Title: FDA Drug Approval Process
Description: Detailed explanation of the FDA's drug approval process, covering clinical trials, safety reviews, and post-market surveillance.
Distance: 0.6262975931167603
--------------------------------------------------
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
