---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Head-to-head Comparisons

Run the code cells below to make head to head comparisons of the different parsing techniques across different questions.
```python PYTHON
import pandas as pd
results = pd.read_csv("{}/results-table.csv".format(data_dir))
```
```python PYTHON
question = input("""
Question 1: What are the most common adverse reactions of Iwilfin?
Question 2: What is the recommended dosage of Iwilfin on body surface area between 0.5 m2 and 0.75 m2?
Question 3: I need a succinct summary of the compound name, indication, route of administration, and mechanism of action of Iwilfin.

Pick which question you want to see (1,2,3):  """)
references = input("Do you want to see the references as well? References are long and noisy (y/n): ")
print("\n\n")

index = {"1": 0, "2": 3, "3": 6}[question]

for src in ["gcp", "aws", "unstructured-io", "llamaparse-text", "llamaparse-markdown", "pytesseract"]:
  print("| {} |".format(src))
  print("\n")
  print(results[src][index])
  if references == "y":
    print("\n")
    print("References:")
    print(results[src][index+1])
  print("\n")
```
```txt title="Output"
Question 1: What are the most common adverse reactions of Iwilfin?
Question 2: What is the recommended dosage of Iwilfin on body surface area between 0.5 m2 and 0.75 m2?
Question 3: I need a succinct summary of the compound name, indication, route of administration, and mechanism of action of Iwilfin.

Pick which question you want to see (1,2,3):  3
Do you want to see the references as well? References are long and noisy (y/n): n


| gcp |


Compound Name: eflornithine hydrochloride ([0], [1], [2]) (IWILFIN ([1])™)

Indication: used to reduce the risk of relapse in adult and paediatric patients with high-risk neuroblastoma (HRNB) ([1], [3]), who have responded at least partially to prior multiagent, multimodality therapy. ([1], [3], [4])

Route of Administration: IWILFIN™ tablets ([1], [3], [4]) are taken orally twice daily ([3], [4]), with doses ranging from 192 to 768 mg based on body surface area. ([3], [4])

Mechanism of Action: IWILFIN™ is an ornithine decarboxylase inhibitor. ([0], [2])


| aws |


Compound Name: eflornithine ([0], [1], [2], [3]) (IWILFIN ([0])™)

Indication: used to reduce the risk of relapse ([0], [3]) in adults ([0], [3]) and paediatric patients ([0], [3]) with high-risk neuroblastoma (HRNB) ([0], [3]) who have responded to prior therapies. ([0], [3], [4])

Route of Administration: Oral ([2], [4])

Mechanism of Action: IWILFIN is an ornithine decarboxylase inhibitor. ([1])


| unstructured-io |


Compound Name: Iwilfin ([1], [2], [3], [4]) (eflornithine) ([0], [2], [3], [4])

Indication: Iwilfin is indicated to reduce the risk of relapse ([1], [3]) in adult and paediatric patients ([1], [3]) with high-risk neuroblastoma (HRNB) ([1], [3]), who have responded to prior anti-GD2 ([1]) immunotherapy ([1], [4]) and multi-modality therapy. ([1])

Route of Administration: Oral ([0], [3])

Mechanism of Action: Iwilfin is an ornithine decarboxylase inhibitor. ([1], [2], [3], [4])


| llamaparse-text |


Compound Name: IWILFIN ([2], [3]) (eflornithine) ([3])

Indication: IWILFIN is used to reduce the risk of relapse ([1], [2], [3]) in adult and paediatric patients ([1], [2], [3]) with high-risk neuroblastoma (HRNB) ([1], [2], [3]), who have responded at least partially to certain prior therapies. ([2], [3])

Route of Administration: IWILFIN is administered as a tablet. ([2])

Mechanism of Action: IWILFIN is an ornithine decarboxylase inhibitor. ([0], [1], [4])


| llamaparse-markdown |


Compound Name: IWILFIN ([1], [2]) (eflornithine) ([1])

Indication: IWILFIN is indicated to reduce the risk of relapse ([1], [2]) in adult and paediatric patients ([1], [2]) with high-risk neuroblastoma (HRNB) ([1], [2]), who have responded at least partially ([1], [2], [3]) to prior anti-GD2 immunotherapy ([1], [2]) and multiagent, multimodality therapy. ([1], [2], [3])

Route of Administration: Oral ([0], [1], [3], [4])

Mechanism of Action: IWILFIN acts as an ornithine decarboxylase inhibitor. ([1])


| pytesseract |


Compound Name: IWILFIN™ ([0], [2]) (eflornithine) ([0], [2])

Indication: IWILFIN is indicated to reduce the risk of relapse ([0], [2]) in adult and paediatric patients ([0], [2]) with high-risk neuroblastoma (HRNB) ([0], [2]), who have responded positively to prior anti-GD2 immunotherapy and multiagent, multimodality therapy. ([0], [2], [4])

Route of Administration: IWILFIN is administered orally ([0], [1], [3], [4]), in the form of a tablet. ([1])

Mechanism of Action: IWILFIN acts as an ornithine decarboxylase inhibitor. ([0])
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
