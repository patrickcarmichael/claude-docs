---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Bonus: Citations come for free with Cohere! 🎉

At Cohere, all RAG calls come with... precise citations! 🎉
The model cites which groups of words, in the RAG chunks, were used to generate the final answer.
These citations make it easy to check where the model’s generated response claims are coming from.
They help users gain visibility into the model reasoning, and sanity check the final model generation.
These citations are optional — you can decide to ignore them.
```python PYTHON
print("Citations that support the final answer:")
for cite in response.citations:
  print(cite)
```
```txt title="Output"
Citations that support the final answer:
{'start': 63, 'end': 79, 'text': 'Denis Villeneuve', 'document_ids': ['doc_0']}
{'start': 81, 'end': 102, 'text': 'director and producer', 'document_ids': ['doc_0']}
{'start': 105, 'end': 116, 'text': 'Jon Spaihts', 'document_ids': ['doc_0']}
{'start': 118, 'end': 145, 'text': 'co-writer of the screenplay', 'document_ids': ['doc_0']}
{'start': 148, 'end': 159, 'text': 'Mary Parent', 'document_ids': ['doc_1']}
{'start': 164, 'end': 175, 'text': 'Cale Boyter', 'document_ids': ['doc_1']}
{'start': 177, 'end': 186, 'text': 'producers', 'document_ids': ['doc_1']}
{'start': 190, 'end': 204, 'text': 'Tanya Lapointe', 'document_ids': ['doc_1']}
{'start': 206, 'end': 219, 'text': 'Brian Herbert', 'document_ids': ['doc_1']}
{'start': 221, 'end': 234, 'text': 'Byron Merritt', 'document_ids': ['doc_1']}
{'start': 236, 'end': 247, 'text': 'Kim Herbert', 'document_ids': ['doc_1']}
{'start': 249, 'end': 260, 'text': 'Thomas Tull', 'document_ids': ['doc_1']}
{'start': 262, 'end': 283, 'text': 'Richard P. Rubinstein', 'document_ids': ['doc_1']}
{'start': 285, 'end': 298, 'text': 'John Harrison', 'document_ids': ['doc_1']}
{'start': 300, 'end': 315, 'text': 'Herbert W. Gain', 'document_ids': ['doc_1']}
{'start': 320, 'end': 337, 'text': 'Kevin J. Anderson', 'document_ids': ['doc_1']}
{'start': 339, 'end': 358, 'text': 'executive producers', 'document_ids': ['doc_1']}
{'start': 362, 'end': 372, 'text': 'Joe Walker', 'document_ids': ['doc_2']}
{'start': 374, 'end': 380, 'text': 'editor', 'document_ids': ['doc_2']}
{'start': 383, 'end': 393, 'text': 'Brad Riker', 'document_ids': ['doc_2']}
{'start': 395, 'end': 419, 'text': 'supervising art director', 'document_ids': ['doc_2']}
{'start': 422, 'end': 438, 'text': 'Patrice Vermette', 'document_ids': ['doc_2']}
{'start': 440, 'end': 459, 'text': 'production designer', 'document_ids': ['doc_2']}
{'start': 462, 'end': 474, 'text': 'Paul Lambert', 'document_ids': ['doc_2']}
{'start': 476, 'end': 501, 'text': 'visual effects supervisor', 'document_ids': ['doc_2']}
{'start': 504, 'end': 515, 'text': 'Gerd Nefzer', 'document_ids': ['doc_2']}
{'start': 517, 'end': 543, 'text': 'special effects supervisor', 'document_ids': ['doc_2']}
{'start': 546, 'end': 562, 'text': 'Thomas Struthers', 'document_ids': ['doc_2']}
{'start': 564, 'end': 582, 'text': 'stunt coordinator.', 'document_ids': ['doc_2']}
{'start': 686, 'end': 691, 'text': '2024.', 'document_ids': ['doc_0']}
```
```python PYTHON
def insert_citations_in_order(text, citations):
    """
    A helper function to pretty print citations.
    """
    offset = 0
    document_id_to_number = {}
    citation_number = 0
    modified_citations = []

    # Process citations, assigning numbers based on unique document_ids

    for citation in citations:
        citation_numbers = []
        for document_id in sorted(citation["document_ids"]):
            if document_id not in document_id_to_number:
                citation_number += 1  # Increment for a new document_id

                document_id_to_number[document_id] = citation_number
            citation_numbers.append(document_id_to_number[document_id])

        # Adjust start/end with offset

        start, end = citation['start'] + offset, citation['end'] + offset
        placeholder = ''.join([f'[{number}]' for number in citation_numbers])
        # Bold the cited text and append the placeholder

        modification = f'**{text[start:end]}**{placeholder}'
        # Replace the cited text with its bolded version + placeholder

        text = text[:start] + modification + text[end:]
        # Update the offset for subsequent replacements

        offset += len(modification) - (end - start)

    # Prepare citations for listing at the bottom, ensuring unique document_ids are listed once

    unique_citations = {number: doc_id for doc_id, number in document_id_to_number.items()}
    citation_list = '\n'.join([f'[{doc_id}] source: "{documents[doc_id - 1]["snippet"]}"' for doc_id, number in sorted(unique_citations.items(), key=lambda item: item[1])])
    text_with_citations = f'{text}\n\n{citation_list}'

    return text_with_citations


print(insert_citations_in_order(response.text, response.citations))
```
```markdown title="Output"
Here are the key crew members involved in 'Dune: Part Two':

- **Denis Villeneuve**[1]: **director and producer**[1]
- **Jon Spaihts**[1]: **co-writer of the screenplay**[1]
- **Mary Parent**[2] and **Cale Boyter**[2]: **producers**[2]
- **Tanya Lapointe**[2], **Brian Herbert**[2], **Byron Merritt**[2], **Kim Herbert**[2], **Thomas Tull**[2], **Richard P. Rubinstein**[2], **John Harrison**[2], **Herbert W. Gain**[2] and **Kevin J. Anderson**[2]: **executive producers**[2]
- **Joe Walker**[3]: **editor**[3]
- **Brad Riker**[3]: **supervising art director**[3]
- **Patrice Vermette**[3]: **production designer**[3]
- **Paul Lambert**[3]: **visual effects supervisor**[3]
- **Gerd Nefzer**[3]: **special effects supervisor**[3]
- **Thomas Struthers**[3]: **stunt coordinator.**[3]

A number of crew members from the first film returned for the sequel, which is set to be released in **2024.**[1]

[1] source: "Dune: Part Two is a 2024 American epic science fiction film directed and produced by Denis Villeneuve, who co-wrote the screenplay with Jon Spaihts. The sequel to Dune (2021) adapts the 1965 novel Dune by Frank Herbert and follows Paul Atreides as he unites with the Fremen people of the desert planet Arrakis to wage war against House Harkonnen. Timothée Chalamet, Rebecca Ferguson, Josh Brolin, Stellan Skarsgård, Dave Bautista, Zendaya, Charlotte Rampling, and Javier Bardem reprise their roles from the first"
[2] source: "stunt coordinator. Dune: Part Two was produced by Villeneuve, Mary Parent, and Cale Boyter, with Tanya Lapointe, Brian Herbert, Byron Merritt, Kim Herbert, Thomas Tull, Jon Spaihts, Richard P. Rubinstein, John Harrison, and Herbert W. Gain serving as executive producers and Kevin J. Anderson as creative consultant. Legendary CEO Joshua Grode confirmed in April 2019 that they plan to make a sequel, adding that "there's a logical place to stop the [first] movie before the book is over".In December 2020,"
[3] source: "series. Villeneuve ultimately secured a two-film deal with Warner Bros. Pictures, in the same style as the two-part adaption of Stephen King's It in 2017 and 2019. In January 2019, Joe Walker was confirmed to be serving as the film's editor. Other crew included Brad Riker as supervising art director, Patrice Vermette as production designer, Paul Lambert as visual effects supervisor, Gerd Nefzer as special effects supervisor, and Thomas Struthers as stunt coordinator. Dune: Part Two was produced by"
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
