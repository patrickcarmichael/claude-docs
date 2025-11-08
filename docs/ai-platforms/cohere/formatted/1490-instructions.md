---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## instructions

Your task is to assist a user in writing a short biography for social media.
The length of the text should be no more than 100 words.
Write the summary in first person.
```
Command-R returns with the following:
```python PYTHON
upgraded_prompt = co.chat(
    message=meta_prompt,
    model='command-r',
)
```
```python PYTHON
print(upgraded_prompt.text)
```
````txt title="Output"
Here is the task delved into a JSON object as requested:
```json JSON
{
    "context": [
    {
        "Work Experience": "Over 15 years of AI and machine learning engineering experience. Proficient in Python, C++, and Java, with expertise in developing algorithms for natural language processing, computer vision, and recommendation systems."
    },
    {
        "Education": "B.Sc. in Physics (Trent University, 2004) and Ph.D. in Statistics (HEC Paris, 2010)."
    },
    {
        "Personal Life": "I’m a married senior software engineer with 4 children and 3 grandchildren. I enjoy hiking, free diving, and vintage watch restoration."
    },
    {
        "Current Position": "I work at GlobalSolTech in the AI Research and Development department as a senior software engineer."
    }
    ],
    "instructions": "Using the provided information, write a concise, first-person social media biography of no more than 100 words."
}
```
````

To extract the returned information, we will write two simple functions to post-process out the JSON and then parse it.
````python PYTHON
def get_json(text: str) -> str:
    matches = [m.group(1) for m in re.finditer("```([\w\W]*?)```", text)]
    if len(matches):
        postproced = matches[0]
        if postproced[:4] == 'json':
            return postproced[4:]
        return postproced
    return text
````
```python PYTHON
def get_prompt_and_docs(text: str) -> tuple:
    json_obj = json.loads(get_json(text))
    prompt = json_obj['instructions']
    docs = []
    for item in json_obj['context']:
        for k,v in item.items():
            docs.append({"title": k, "snippet": v})
    return prompt, docs
```
```python PYTHON
new_prompt, docs = get_prompt_and_docs(upgraded_prompt.text)
```
```python PYTHON
new_prompt, docs
```
```txt title="Output"
('Using the provided information, write a concise, first-person social media biography of no more than 100 words.',
    [{'title': 'Work Experience',
    'snippet': 'Over 15 years of AI and machine learning engineering experience. Proficient in Python, C++, and Java, with expertise in developing algorithms for natural language processing, computer vision, and recommendation systems.'},
    {'title': 'Education',
    'snippet': 'B.Sc. in Physics (Trent University, 2004) and Ph.D. in Statistics (HEC Paris, 2010).'},
    {'title': 'Personal Life',
    'snippet': 'I’m a married senior software engineer with 4 children and 3 grandchildren. I enjoy hiking, free diving, and vintage watch restoration.'},
    {'title': 'Current Position',
    'snippet': 'I work at GlobalSolTech in the AI Research and Development department as a senior software engineer.'}])
```
As we can see above, the new prompt is much more concise and gets right to the point. The context has been split into 4 "documents" that Command-R can ground the information to. Now let's run the same task with the new prompt while leveraging the `documents=` parameter. Note that the `docs` variable is a list of dict objects with `title` describing the contents of a text and `snippet` containing the text itself:
```python PYTHON
response = co.chat(
    message=new_prompt,
    model='command-r',
    documents=docs,
)
```
```python PYTHON
print(response.text)
```
```txt title="Output"
I'm a senior software engineer with a Ph.D. in Statistics and over 15 years of AI and machine learning engineering experience. My current focus at GlobalSolTech's AI R&amp;D department is developing algorithms for natural language processing, computer vision, and recommendation systems. In my free time, I enjoy hiking, freediving, and restoring vintage watches, and I'm a married father of four with three grandchildren.
```
The response is concise. More importantly, we can ensure that there is no hallucination because the text is automatically grounded in the input documents. Using the simple function below, we can add this grounding information to the text as citations:
```python PYTHON
def insert_citations(text: str, citations: list[dict], add_one: bool=False):
    """
    A helper function to pretty print citations.
    """
    offset = 0
    # Process citations in the order they were provided

    for citation in citations:
        # Adjust start/end with offset

        start, end = citation.start + offset, citation.end + offset
        if add_one:
            cited_docs = [str(int(doc[4:]) + 1) for doc in citation.document_ids]
        else:
            cited_docs = [doc[4:] for doc in citation.document_ids]
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
```
```python PYTHON
print(insert_citations(response.text, response.citations, True))
```
```txt title="Output"
I'm a senior software engineer [3, 4] with a Ph.D. in Statistics [2] and over 15 years of AI and machine learning engineering experience. [1] My current focus at GlobalSolTech's AI R&amp;D department [4] is developing algorithms for natural language processing, computer vision, and recommendation systems. [1] In my free time, I enjoy hiking, freediving, and restoring vintage watches [3], and I'm a married father of four with three grandchildren. [3]
```
Now let's move on to an arguably more difficult problem.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
