---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Clean the data

data = data.dropna(
    subset=[
        "GDP per capita (current US$)",
        "Life expectancy at birth, total (years)",
    ]
)
data["GDP per capita (current US$)"] = pd.to_numeric(
    data["GDP per capita (current US$)"],
    errors="coerce",
)
data["Life expectancy at birth, total (years)"] = pd.to_numeric(
    data["Life expectancy at birth, total (years)"],
    errors="coerce",
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
