---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## we look at the first page as a sanity check:

plt.imshow(pages[0])
plt.axis('off')
plt.show()
```
Now, we can process the image of each page with `pytesseract` and concatenate the results to get our parsed document.
```python PYTHON
label_ocr_pytesseract = "".join([pytesseract.image_to_string(page) for page in pages])
```
```python PYTHON
print(label_ocr_pytesseract[:200])
```
```txt title="Output"
HIGHLIGHTS OF PRESCRIBING INFORMATION

These highlights do not include all the information needed to use
IWILFIN™ safely and effectively. See full prescribing information for
IWILFIN.

IWILFIN™ (eflor
```
```python PYTHON
label_ocr_pytesseract = "".join([pytesseract.image_to_string(page) for page in pages])

with open(f"pytesseract-parsed-{source_filename}.txt", "w") as f:
  f.write(label_ocr_pytesseract)
```

#### Visualize the parsed document

```python PYTHON
filename = "pytesseract-parsed-{}.txt".format(source_filename)
with open("{}/{}".format(data_dir, filename), "r") as doc:
    parsed_document = doc.read()

print(parsed_document[:1000])
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
