---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Helper function for displaying response WITH citations

def insert_citations(text: str, citations: list[dict]):
    """
    A helper function to pretty print citations.
    """
    offset = 0
    # Process citations in the order they were provided

    for citation in citations:
        # Adjust start/end with offset

        start, end = citation['start'] + offset, citation['end'] + offset
        cited_docs = [doc[4:] for doc in citation["document_ids"]]
        # Shorten citations if they're too long for convenience

        if len(cited_docs) > 3:
            placeholder = "[" + ", ".join(cited_docs[:3]) + "...]"
        else:
            placeholder = "[" + ", ".join(cited_docs) + "]"
        # ^ doc[4:] removes the 'doc_' prefix, and leaves the quoted document

        modification = f'{text[start:end]} {placeholder}'
        # Replace the cited text with its bolded version + placeholder

        text = text[:start] + modification + text[end:]
        # Update the offset for subsequent replacements

        offset += len(modification) - (end - start)

    return text

print(insert_citations(response.text, response.citations))
```
```txt title="Output"
Here are the overall revenue numbers for the years 2021, 2022, and 2023 as bullet points:
- 2021: $5,992 million [13]
- 2022: $8,399 million [13]
- 2023: $9,917 million [13]

Revenue increased by 18% in 2023 [11] compared to 2022, primarily due to a 14% increase in Nights and Experiences Booked [11], which reached 54.5 million. [11] This, combined with higher average daily rates [11], resulted in a 16% increase in Gross Booking Value [11], which reached $10.0 billion. [11]

The revenue growth trend demonstrates sustained strong travel demand. [11] On a constant-currency basis [11], revenue increased by 17% in 2023 [11] compared to the previous year.

Other factors [8, 14] influencing the company's financial performance are described outside of the revenue growth trends. [8, 14]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
