---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Fit the linear regression model

X = data["GDP per capita (current US$)"].values.reshape(-1, 1)
y = data["Life expectancy at birth, total (years)"].values.reshape(-1, 1)
model = LinearRegression().fit(X, y)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
