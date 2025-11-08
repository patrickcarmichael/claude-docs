---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Data to be written to the CSV file

data = [
    ["movie", "name", "num_tickets"],
    ["The Shawshank Redemption", "John", 2],
    ["The Shawshank Redemption", "Jerry", 2],
    ["The Shawshank Redemption", "Jack", 4],
    ["The Shawshank Redemption", "Jeremy", 2],
    ["Finding Nemo", "Darren", 3],
    ["Finding Nemo", "Jones", 2],
    ["Finding Nemo", "King", 1],
    ["Finding Nemo", "Penelope", 5],
]

file_path = "movies_tickets.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file created successfully at {file_path}.")
```
CSV file created successfully at movies\_tickets.csv.

Let's use our CSV Agent to interact with the CSV file
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
