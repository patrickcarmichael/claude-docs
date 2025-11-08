---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Legal Question Answering

On March 21st, the DOJ announced that it is [suing Apple](https://www.theverge.com/2024/3/21/24107659/apple-doj-lawsuit-antitrust-documents-suing) for anti-competitive practices. The [complaint](https://www.justice.gov/opa/media/1344546/dl) is 88 pages long and consists of about 230 paragraphs of text. To understand what the suit alleges, a common use case would be to ask for a summary. Because Command-R has a context window of 128K, even an 88-page legal complaint fits comfortably within the window.
```python PYTHON
apple = open('data/apple_mod.txt').read()
```
```python PYTHON
tokens = co.tokenize(text=apple, model='command-r')
len(tokens.tokens)
```
```txt title="Output"
29697
```
We can set up a prompt template that allows us to ask questions on the original text.
```python PYTHON
prompt_template = '''
{legal_text}

{question}
'''
```
```python PYTHON
question = '''Please summarize the attached legal complaint succinctly. Focus on answering the question: what does the complaint allege?'''
rendered_prompt = prompt_template.format(legal_text=apple, question=question)
```
```python PYTHON
response = co.chat(
    message=rendered_prompt,
    model='command-r',
    temperature=0.3,
)
```
```python PYTHON
print(response.text)
```
```txt title="Output"
The complaint alleges that Apple has violated antitrust laws by engaging in a pattern of anticompetitive conduct to maintain its monopoly power over the U.S. markets for smartphones and performance smartphones. Apple is accused of using its control over app distribution and access to its operating system to impede competition and innovation. Specifically, the company is said to have restricted developers' ability to create certain apps and limited the functionality of others, making it harder for consumers to switch away from iPhones to rival smartphones. This conduct is alleged to have harmed consumers and developers by reducing choice, increasing prices, and stifling innovation. The plaintiffs seek injunctive relief and potential monetary awards to remedy these illegal practices.
```
The summary seems clear enough. But we are interested in the specific allegations that the DOJ makes. For example, skimming the full complaint, it looks like the DOJ is alleging that Apple could encrypt text messages sent to Android phones if it wanted to do so. We can amend the rendered prompt and ask:
```python PYTHON
question = '''Does the DOJ allege that Apple could encrypt text messages sent to Android phones?'''
rendered_prompt = prompt_template.format(legal_text=apple, question=question)
```
```python PYTHON
response = co.chat(
    message=rendered_prompt,
    model='command-r',
)
```
```python PYTHON
print(response.text)
```
```txt title="Output"
Yes, the DOJ alleges that Apple could allow iPhone users to send encrypted messages to Android users while still using iMessage on their iPhones but chooses not to do so. According to the DOJ, this would instantly improve the privacy and security of iPhones and other smartphones.
```
This is a very interesting allegation that at first glance suggests that the model could be hallucinating. Because RAG has been shown to help reduce hallucinations and grounds its responses in the input text, we should convert this prompt to the RAG style paradigm to gain confidence in its response.

While previously we asked Command-R to chunk the text for us, the legal complaint is highly structured with numbered paragraphs so we can use the following function to break the complaint into input docs ready for RAG:
```python PYTHON
def chunk_doc(input_doc: str) -> list:
    chunks = []
    current_para = 'Preamble'
    current_chunk = ''
    # pattern to find an integer number followed by a dot (finding the explicitly numbered paragraph numbers)

    pattern = r'^\d+\.$'

    for line in input_doc.splitlines():
        if re.match(pattern, line):
            chunks.append((current_para.replace('.', ''), current_chunk))
            current_chunk = ''
            current_para = line
        else:
            current_chunk += line + '\n'

    docs = []
    for chunk in chunks:
        docs.append({"title": chunk[0], "snippet": chunk[1]})

    return docs
```
```python PYTHON
chunks = chunk_doc(apple)
```
```python PYTHON
print(chunks[18])
```
```python title="Output"
    {'title': '18', 'snippet': '\nProtecting competition and the innovation that competition inevitably ushers in\nfor consumers, developers, publishers, content creators, and device manufacturers is why\nPlaintiffs bring this lawsuit under Section 2 of the Sherman Act to challenge Apple’s\nmaintenance of its monopoly over smartphone markets, which affect hundreds of millions of\nAmericans every day. Plaintiffs bring this case to rid smartphone markets of Apple’s\nmonopolization and exclusionary conduct and to ensure that the next generation of innovators\ncan upend the technological world as we know it with new and transformative technologies.\n\n\nII.\n\nDefendant Apple\n\n'}
```
We can now try the same question but ask it directly to Command-R with the chunks as grounding information.
```python PYTHON
response = co.chat(
    message='''Does the DOJ allege that Apple could encrypt text messages sent to Android phones?''',
    model='command-r',
    documents=chunks,
)
```
```python PYTHON
print(response.text)
```
```txt title="Output"
Yes, according to the DOJ, Apple could encrypt text messages sent from iPhones to Android phones. The DOJ claims that Apple degrades the security and privacy of its users by impeding cross-platform encryption and preventing developers from fixing the broken cross-platform messaging experience. Apple's conduct makes it harder to switch from iPhone to Android, as messages sent from iPhones to Android phones are unencrypted.
```
The responses seem similar, but we should add citations and check the citation to get confidence in the response.
```python PYTHON
print(insert_citations(response.text, response.citations))
```
```txt title="Output"
Yes, according to the DOJ, Apple could encrypt text messages sent from iPhones to Android phones. [144] The DOJ claims that Apple degrades the security and privacy [144] of its users by impeding cross-platform encryption [144] and preventing developers from fixing the broken cross-platform messaging experience. [93] Apple's conduct makes it harder to switch from iPhone to Android [144], as messages sent from iPhones to Android phones are unencrypted. [144]
```
The most important passage seems to be paragraph 144. Paragraph 93 is also cited. Let's check what they contain.
```python PYTHON
print(chunks[144]['snippet'])
```
```txt title="Output"
Apple is also willing to make the iPhone less secure and less private if that helps
maintain its monopoly power. For example, text messages sent from iPhones to Android phones
are unencrypted as a result of Apple’s conduct. If Apple wanted to, Apple could allow iPhone
users to send encrypted messages to Android users while still using iMessage on their iPhone,
which would instantly improve the privacy and security of iPhone and other smartphone users.
```
```python PYTHON
print(chunks[93]['snippet'])
```
```txt title="Output"
Recently, Apple blocked a third-party developer from fixing the broken cross-
platform messaging experience in Apple Messages and providing end-to-end encryption for
messages between Apple Messages and Android users. By rejecting solutions that would allow
for cross-platform encryption, Apple continues to make iPhone users’ less secure than they could
otherwise be.

ii.
```typescript
Paragraph 144 indeed contains the important allegation: **If Apple wanted to, Apple could allow iPhone users to send encrypted messages to Android users**.

In this cookbook we have shown how one can easily take an existing monolithic prompt and migrate it to the RAG paradigm to get less hallucination, grounded information, and in-line citations. We also demonstrated Command-R's ability to re-write an instruction prompt in a single shot to make it more concise and potentially lead to higher quality completions.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
