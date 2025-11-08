**Navigation:** [← Previous](./17-credentials-file-populate-if-you-are-running-in-a-.md) | [Index](./index.md) | [Next →](./19-instantiate-the-react-agent.md)

---

# Employing a smaller context window also has the additional benefit of reducing the cost per request, especially if billed by the number of tokens.

MAX_TOKENS = 40000

def truncate(long: str, max_tokens: int) -> str:
    """
    Shortens `long` by brutally truncating it to the first `max_tokens` tokens.
    This can break up sentences, passages, etc.
    """

    tokenized = co.tokenize(text=long, model=co_model).token_strings
    truncated = tokenized[:max_tokens]
    short = "".join(truncated)
    return short
```

```python PYTHON
short_text = truncate(long_text, MAX_TOKENS)

prompt = prompt_template.format(document=short_text)
print(generate_response(message=prompt))
```

The document discusses the impact of a specific protein, p53, on the process of angiogenesis, which is the growth of new blood vessels. Angiogenesis plays a critical role in various physiological processes, including wound healing and embryonic development. The presence of the p53 protein can inhibit angiogenesis by regulating the expression of certain genes and proteins. This inhibition can have significant implications for tumor growth, as angiogenesis is essential for tumor progression. Therefore, understanding the role of p53 in angiogenesis can contribute to our knowledge of tumor suppression and potential therapeutic interventions.

Additionally, the document mentions that the regulation of angiogenesis by p53 occurs independently of the protein's role in cell cycle arrest and apoptosis, which are other key functions of p53 in tumor suppression. This suggests that p53 has a complex and multifaceted impact on cellular processes.

## Approach 2: Query Based Retrieval \[#appoach-2]

In this section we present how we can leverage a query retriereval based approach to generate an answer to the following question: `Based on the document, are there any risks related to Elon Musk?`.

The solution is outlined below and can be broken down into four functional steps.

1. Chunk the text into units

   * Here we employ a simple chunking algorithm. More information about different chunking strategies can be found \[here]\(TODO: link to chunking post).

2. Use a ranking algorithm to rank chunks against the query

   * We leverage another Cohere endpoint, `co.rerank` ([docs link](https://docs.cohere.com/reference/rerank-1)), to rank each chunk against the query.

3. Keep the most-relevant chunks until context limit is reached

   * `co.rerank` returns a relevance score, facilitating the selection of the most pertinent chunks. We can choose the most relevant chunks based on this score.

4. Put condensed text back in original order
   * Finally, we arrange the chosen chunks in their original sequence as they appear in the document.

See `query_based_retrieval` function for the starting point.

### Query based retrieval implementation

```python PYTHON
def split_text_into_sentences(text) -> List[str]:
    """
    Split the input text into a list of sentences.
    """
    sentences = sent_tokenize(text)

    return sentences

def group_sentences_into_passages(sentence_list, n_sentences_per_passage=5):
    """
    Group sentences into passages of n_sentences sentences.
    """
    passages = []
    passage = ""
    for i, sentence in enumerate(sentence_list):
        passage += sentence + " "
        if (i + 1) % n_sentences_per_passage == 0:
            passages.append(passage)
            passage = ""
    return passages

def build_simple_chunks(text, n_sentences=5):
    """
    Build chunks of text from the input text.
    """
    sentences = split_text_into_sentences(text)
    chunks = group_sentences_into_passages(sentences, n_sentences_per_passage=n_sentences)
    return chunks
```

```python PYTHON
sentences = split_text_into_sentences(long_text)
passages = group_sentences_into_passages(sentences, n_sentences_per_passage=5)
print('Example sentence:', np.random.choice(np.asarray(sentences), size=1, replace=False))
print()
print('Example passage:', np.random.choice(np.asarray(passages), size=1, replace=False))
```

```txt title="Output"
Example sentence: ['4.']

Example passage: ['T echnical robustness and safety means that AI systems are developed  and used in a way that allows robustness in case of problems and resilience against  attempts to alter the use or performance of the AI system so as to allow unlawful use by  third parties, a nd minimise unintended harm. Privacy and data governance means that AI  systems are developed and used in compliance with existing privacy and data protection  rules, while processing data that meets high standards in terms of quality and integrity. Transpar ency means that AI systems are developed and used in a way that allows  appropriate traceability and explainability, while making humans aware that they  communicate or interact with an AI system, as well as duly informing deployers of the  capabilities and l imitations of that AI system and affected persons about their rights. Diversity, non - discrimination and fairness means that AI systems are developed and used  in a way that includes diverse actors and promotes equal access, gender equality and  cultural dive rsity, while avoiding discriminatory impacts and unfair biases that are  prohibited by Union or national law. Social and environmental well - being means that AI  systems are developed and used in a sustainable and environmentally friendly manner as  well as in   a way to benefit all human beings, while monitoring and assessing the long - term  impacts on the individual, society and democracy. ']
```

```python PYTHON
def _add_chunks_by_priority(
    chunks: List[str],
    idcs_sorted_by_priority: List[int],
    max_tokens: int,
) -> List[Tuple[int, str]]:
    """
    Given chunks of text and their indices sorted by priority (highest priority first), this function
    fills the model context window with as many highest-priority chunks as possible.

    The output is a list of (index, chunk) pairs, ordered by priority. To stitch back the chunks into
    a cohesive text that preserves chronological order, sort the output on its index.
    """

    selected = []
    num_tokens = 0
    idcs_queue = deque(idcs_sorted_by_priority)

    while num_tokens < max_tokens and len(idcs_queue) > 0:
        next_idx = idcs_queue.popleft()
        num_tokens += len(co.tokenize(text=chunks[next_idx], model=co_model).tokens)
        # keep index and chunk, to reorder chronologically
        selected.append((next_idx, chunks[next_idx]))
    if num_tokens > max_tokens:
        selected.pop()

    return selected

def query_based_retrieval(
    long: str,
    max_tokens: int,
    query: str,
    n_setences_per_passage: int = 5,
) -> str:
    """
    Performs query-based retrieval on a long text document.
    """
    # 1. Chunk text into units
    chunks = build_simple_chunks(long, n_setences_per_passage)

    # 2. Use co.rerank to rank chunks vs. query
    chunks_reranked = co.rerank(query=query, documents=chunks, model="rerank-english-v3.0")
    idcs_sorted_by_relevance = [
        chunk.index for chunk in sorted(chunks_reranked.results, key=lambda c: c.relevance_score, reverse=True)
    ]

    # 3. Add chunks back in order of relevance
    selected = _add_chunks_by_priority(chunks, idcs_sorted_by_relevance, max_tokens)

    # 4. Put condensed text back in original order
    separator = " "
    short = separator.join([chunk for index, chunk in sorted(selected, key=lambda item: item[0], reverse=False)])
    return short
```

```python PYTHON
# Example prompt
prompt_template = """
## Instruction
{query}

## Document
{document}

## Answer
""".strip()
```

```python PYTHON
query = "What does the report say about biometric identification? Answer only based on the document."
short_text = query_based_retrieval(long_text, MAX_TOKENS, query)
prompt = prompt_template.format(query=query, document=short_text)
print(generate_response(message=prompt, max_tokens=300))
```

```txt title="Output"
The report discusses the restrictions on the use of biometric identification by law enforcement in publicly accessible spaces. According to the document, real-time biometric identification is prohibited unless in exceptional cases where its use is strictly necessary and proportionate to achieving a substantial public interest. The use of post-remote biometric identification systems is also mentioned, noting the requirements for authorization and limitations on its use.

The report also highlights the classification of certain AI systems as high-risk, including biometric identification systems, emotion recognition systems, and biometric categorisation systems, with the exception of systems used for biometric verification. High-risk AI systems are subject to specific requirements and obligations.
```

## Approach 3: Text rank \[#approach-3]

In the final section we will show how we leverage graph theory to select chunks based on their centrality. Centrality is a graph-theoretic measure of how connected a node is; the higher the centrality, the more connected the node is to surrounding nodes (with fewer connections among those neighbors).

The solution presented in this document can be broken down into five functional steps:

1. Break the document into chunks.

   * This mirrors the first step in [Approach 2](#approach-2).

2. Embed each chunk using an embedding model and construct a similarity matrix.

   * We utilize `co.embed` [documentation link](https://docs.cohere.com/reference/embed).

3. Compute the centrality of each chunk.

   * We employ a package called [`NetworkX`](https://networkx.org/documentation/networkx-1.10/overview.html). It constructs a graph where the chunks are nodes, and the similarity score between them serves as the weight of the edges. Then, we calculate the centrality of each chunk as the sum of the edge weights adjacent to the node representing that chunk.

4. Retain the highest-centrality chunks until the context limit is reached.

   * This step follows a similar approach to [Approach 2](#approach-2).

5. Reassemble the shortened text by reordering chunks in their original order.
   * This step mirrors the last step in [Approach 2](#approach-2).

See `text_rank` as the starting point.

### Text rank implementation

```python PYTHON
def text_rank(text: str, max_tokens: int, n_setences_per_passage: int) -> str:
    """
    Shortens text by extracting key units of text from it based on their centrality.
    The output is the concatenation of those key units, in their original order.
    """

    # 1. Chunk text into units
    chunks = build_simple_chunks(text, n_setences_per_passage)

    # 2. Embed and construct similarity matrix
    embeddings = np.array(
        co.embed(
            texts=chunks,
            model="embed-v4.0",
            input_type="clustering",
        ).embeddings
    )
    similarities = np.dot(embeddings, embeddings.T)

    # 3. Compute centrality and sort sentences by centrality
    # Easiest to use networkx's `degree` function with similarity as weight
    g = nx.from_numpy_array(similarities, edge_attr="weight")
    centralities = g.degree(weight="weight")
    idcs_sorted_by_centrality = [node for node, degree in sorted(centralities, key=lambda item: item[1], reverse=True)]

    # 4. Add chunks back in order of centrality
    selected = _add_chunks_by_priority(chunks, idcs_sorted_by_centrality, max_tokens)

    # 5. Put condensed text back in original order
    short = " ".join([chunk for index, chunk in sorted(selected, key=lambda item: item[0], reverse=False)])

    return short
```

```python PYTHON
# Example summary prompt.
prompt_template = """
## Instruction
Summarize the following Document in 3-5 sentences. Only answer based on the information provided in the document.

## Document
{document}

## Summary
""".strip()
```

```python PYTHON
short_text = text_rank(long_text, MAX_TOKENS, 5)
prompt = prompt_template.format(document=short_text)
print(generate_response(message=prompt, max_tokens=600))
```

```txt title="Output"
The document outlines the requirements and obligations for developing and deploying AI systems in the European Union. It aims to establish a regulatory framework to foster innovation while ensuring the protection of fundamental rights and public interests. The regulation applies to providers and deployers of AI systems, including those established outside the EU. High-risk AI systems are subject to specific requirements, such as risk management, data governance, and transparency. Providers must ensure compliance and keep records, and deployers must use AI systems responsibly. The regulation also establishes an AI Office, advisory bodies, and a database for high-risk AI systems. Additionally, it addresses issues like testing, codes of conduct, and cooperation with third countries. Fines and penalties are proposed for non-compliance.
```

## Summary

In this notebook we present three useful methods to over come the limitations of context window size. In the following [blog post](https://docs.cohere.com/page/chunking-strategies), we talk more about how these methods can be evaluated.


# Migrating Monolithic Prompts to Command-R with RAG

> This page contains a discussion of how to automatically migrating monolothic prompts.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Migrating_Monolithic_Prompts_to_Command_R_with_RAG.ipynb" />

Command-R is a powerful LLM optimized for long context tasks such as retrieval augmented generation (RAG). Migrating a monolithic task such as question-answering or query-focused summarization to RAG can improve the quality of responses due to reduced hallucination and improved conciseness through grounding.

Previously, migrating an existing use case to RAG involved a lot of manual work around indexing documents, implementing at least a basic search strategy, extensive post-processing to introduce proper grounding through citations, and of course fine-tuning an LLM to work well in the RAG paradigm.

This cookbook demonstrates automatic migration of monolithic prompts through two diverse use cases where an original prompt is broken down into two parts: (1) context; and (2) instructions. The former can be done automatically or through simple chunking, while the latter is done automatically by Command-R through single shot prompt optimization.

The two use cases demonstrated here are:

1. Autobiography Assistant; and
2. Legal Question Answering

```python PYTHON
#!pip install cohere
```

```python PYTHON
import json
import os
import re

import cohere
import getpass
```

```python PYTHON
CO_API_KEY = getpass.getpass('cohere API key:')
```

```txt title="Output"
cohere API key:··········
```

```python PYTHON
co = cohere.Client(CO_API_KEY)
```

## Autobiography Assistant

This application scenario is a common LLM-as-assistant use case: given some context, help the user to complete a task. In this case, the task is to write a concise autobiographical summary.

```python PYTHON
original_prompt = '''## information
Current Job Title: Senior Software Engineer
Current Company Name: GlobalSolTech
Work Experience: Over 15 years of experience in software engineering, specializing in AI and machine learning. Proficient in Python, C++, and Java, with expertise in developing algorithms for natural language processing, computer vision, and recommendation systems.
Current Department Name: AI Research and Development
Education: B.Sc. in Physics from Trent University (2004), Ph.D. in Statistics from HEC in Paris (2010)
Hobbies: I love hiking in the mountains, free diving, and collecting and restoring vintage world war one mechanical watches.
Family: Married with 4 children and 3 grandchildren.

## instructions
Your task is to assist a user in writing a short biography for social media.
The length of the text should be no more than 100 words.
Write the summary in first person.'''
```

```python PYTHON
response = co.chat(
    message=original_prompt,
    model='command-r',
)
```

```python PYTHON
print(response.text)
```

```txt
    I'm a Senior Software Engineer at GlobalSolTech, with over 15 years of experience in AI and machine learning. My expertise lies in developing innovative algorithms for natural language processing, computer vision, and recommendation systems. I hold a B.Sc. in Physics and a Ph.D. in Statistics and enjoy hiking, free diving, and collecting vintage watches in my spare time. I'm passionate about using my skills to contribute to cutting-edge AI research and development. At GlobalSolTech, I'm proud to be part of a dynamic team driving technological advancement.
```

Using Command-R, we can automatically upgrade the original prompt to a RAG-style prompt to get more faithful adherence to the instructions, a clearer and more concise prompt, and in-line citations for free. Consider the following meta-prompt:

```python PYTHON
meta_prompt = f'''Below is a task for an LLM delimited with ## Original Task. Your task is to split that task into two parts: (1) the context; and (2) the instructions.
The context should be split into several separate parts and returned as a JSON object where each part has a name describing its contents and the value is the contents itself.
Make sure to include all of the context contained in the original task description and do not change its meaning.
The instructions should be re-written so that they are very clear and concise. Do not change the meaning of the instructions or task, just make sure they are very direct and clear.
Return everything in a JSON object with the following structure:

{{
  "context": [{{"<description 1="" of="" part="">": "<content 1="" of="" part="">"}}, ...],
  "instructions": "<the instructions="" re-written="">"
}}

## Original Task
{original_prompt}
'''
```

```python PYTHON
print(meta_prompt)
```

```txt title="Output"
Below is a task for an LLM delimited with ## Original Task. Your task is to split that task into two parts: (1) the context; and (2) the instructions.
The context should be split into several separate parts and returned as a JSON object where each part has a name describing its contents and the value is the contents itself.
Make sure to include all of the context contained in the original task description and do not change its meaning.
The instructions should be re-written so that they are very clear and concise. Do not change the meaning of the instructions or task, just make sure they are very direct and clear.
Return everything in a JSON object with the following structure:

{
    "context": [{"<description 1="" of="" part="">": "<content 1="" of="" part="">"}, ...],
    "instructions": "<the instructions="" re-written="">"
}

## Original Task
## information
Current Job Title: Senior Software Engineer
Current Company Name: GlobalSolTech
Work Experience: Over 15 years of experience in software engineering, specializing in AI and machine learning. Proficient in Python, C++, and Java, with expertise in developing algorithms for natural language processing, computer vision, and recommendation systems.
Current Department Name: AI Research and Development
Education: B.Sc. in Physics from Trent University (2004), Ph.D. in Statistics from HEC in Paris (2010)
Hobbies: I love hiking in the mountains, free diving, and collecting and restoring vintage world war one mechanical watches.
Family: Married with 4 children and 3 grandchildren.

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
```

Paragraph 144 indeed contains the important allegation: **If Apple wanted to, Apple could allow iPhone users to send encrypted messages to Android users**.

In this cookbook we have shown how one can easily take an existing monolithic prompt and migrate it to the RAG paradigm to get less hallucination, grounded information, and in-line citations. We also demonstrated Command-R's ability to re-write an instruction prompt in a single shot to make it more concise and potentially lead to higher quality completions.


# Multilingual Search with Cohere and Langchain

> This page contains a basic tutorial on how to do search across different languages with Cohere's LLM platform.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Multilingual_Search_with_Cohere_and_Langchain.ipynb" />

***Read the accompanying [blog post here](https://cohere.com/blog/search-cohere-langchain/).***

This notebook contains two examples for performing multilingual search using Cohere and Langchain. Langchain is a library that assists the development of applications built on top of large language models (LLMs), such as Cohere's models.

In short, Cohere makes it easy for developers to leverage LLMs and Langchain makes it easy to build applications with these models.

We'll go through the following examples:

* **Example 1 - Basic Multilingual Search**

  This is a simple example of multilingual search over a list of documents.

  The steps in summary:

  * Import a list of documents
  * Embed the documents and store them in an index
  * Enter a query
  * Return the document most similar to the query

* **Example 2 - Search-Based Question Answering**

  This example shows a more involved example where search is combined with text generation to answer questions about long-form documents.

  The steps in summary:

  * Add an article and chunk it into smaller passages
  * Embed the passages and store them in an index
  * Enter a question
  * Answer the question based on the most relevant documents

```python PYTHON
from langchain.embeddings.cohere import CohereEmbeddings
from langchain.llms import Cohere
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import RetrievalQA
from langchain.vectorstores import Qdrant
from langchain.document_loaders import TextLoader
import textwrap as tr
import random
import dotenv
import os

dotenv.load_dotenv(".env") # Upload an '.env' file containing an environment variable named 'COHERE_API_KEY' using your Cohere API Key
```

```txt title="Output"
True
```

### Import a list of documents

```python PYTHON
import tensorflow_datasets as tfds
dataset = tfds.load('trec', split='train')
texts = [item['text'].decode('utf-8') for item in tfds.as_numpy(dataset)]
print(f"Number of documents: {len(texts)}")
```

```txt title="Output"
Downloading and preparing dataset 350.79 KiB (download: 350.79 KiB, generated: 636.90 KiB, total: 987.69 KiB) to /root/tensorflow_datasets/trec/1.0.0...



Dl Completed...: 0 url [00:00, ? url/s]



Dl Size...: 0 MiB [00:00, ? MiB/s]



Extraction completed...: 0 file [00:00, ? file/s]



Generating splits...:   0%|          | 0/2 [00:00<?, ? splits/s]



Generating train examples...:   0%|          | 0/5452 [00:00<?, ? examples/s]



Shuffling /root/tensorflow_datasets/trec/1.0.0.incompleteWOR5EP/trec-train.tfrecord*...:   0%|          | 0/54…



Generating test examples...:   0%|          | 0/500 [00:00<?, ? examples/s]



Shuffling /root/tensorflow_datasets/trec/1.0.0.incompleteWOR5EP/trec-test.tfrecord*...:   0%|          | 0/500…


Dataset trec downloaded and prepared to /root/tensorflow_datasets/trec/1.0.0. Subsequent calls will reuse this data.
Number of documents: 5452
```

```python PYTHON
random.seed(11)
for item in random.sample(texts, 5):
  print(item)
```

```txt title="Output"
What is the starting salary for beginning lawyers ?
Where did Bill Gates go to college ?
What task does the Bouvier breed of dog perform ?
What are the top boy names in the U.S. ?
What is a female rabbit called ?
```

### Embed the documents and store them in an index

```python PYTHON
embeddings = CohereEmbeddings(model = "multilingual-22-12")

db = Qdrant.from_texts(texts, embeddings, location=":memory:", collection_name="my_documents", distance_func="Dot")
```

### Enter a query

```python PYTHON
queries = ["How to get in touch with Bill Gates",
           "Comment entrer en contact avec Bill Gates",
           "Cara menghubungi Bill Gates"]

queries_lang = ["English", "French", "Indonesian"]
```

### Return the document most similar to the query

```python PYTHON
answers = []
for query in queries:
  docs = db.similarity_search(query)
  answers.append(docs[0].page_content)
```

```python PYTHON
for idx,query in enumerate(queries):
  print(f"Query language: {queries_lang[idx]}")
  print(f"Query: {query}")
  print(f"Most similar existing question: {answers[idx]}")
  print("-"*20,"\n")
```

```txt title="Output"
Query language: English
Query: How to get in touch with Bill Gates
Most similar existing question: What is Bill Gates of Microsoft E-mail address ?
--------------------

Query language: French
Query: Comment entrer en contact avec Bill Gates
Most similar existing question: What is Bill Gates of Microsoft E-mail address ?
--------------------

Query language: Indonesian
Query: Cara menghubungi Bill Gates
Most similar existing question: What is Bill Gates of Microsoft E-mail address ?
--------------------
```

## Add an article and chunk it into smaller passages

```python PYTHON

!wget 'https://docs.google.com/uc?export=download&amp;id=1f1INWOfJrHTFmbyF_0be5b4u_moz3a4F' -O steve-jobs-commencement.txt
```

```txt title="Output"
--2023-06-08 06:11:19--  https://docs.google.com/uc?export=download&amp;id=1f1INWOfJrHTFmbyF_0be5b4u_moz3a4F
Resolving docs.google.com (docs.google.com)... 74.125.200.101, 74.125.200.138, 74.125.200.102, ...
Connecting to docs.google.com (docs.google.com)|74.125.200.101|:443... connected.
HTTP request sent, awaiting response... 303 See Other
Location: https://doc-0g-84-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/84t4moii9dmg08hmrh6rfpp8ecrjh6jq/1686204675000/12721472133292131824/*/1f1INWOfJrHTFmbyF_0be5b4u_moz3a4F?e=download&amp;uuid=a26288c7-ad0c-4707-ae0b-72cb94c224dc [following]
Warning: wildcards not supported in HTTP.
--2023-06-08 06:11:19--  https://doc-0g-84-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/84t4moii9dmg08hmrh6rfpp8ecrjh6jq/1686204675000/12721472133292131824/*/1f1INWOfJrHTFmbyF_0be5b4u_moz3a4F?e=download&amp;uuid=a26288c7-ad0c-4707-ae0b-72cb94c224dc
Resolving doc-0g-84-docs.googleusercontent.com (doc-0g-84-docs.googleusercontent.com)... 74.125.130.132, 2404:6800:4003:c01::84
Connecting to doc-0g-84-docs.googleusercontent.com (doc-0g-84-docs.googleusercontent.com)|74.125.130.132|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 11993 (12K) [text/plain]
Saving to: ‘steve-jobs-commencement.txt’

steve-jobs-commence 100%[===================>]  11.71K  --.-KB/s    in 0s

2023-06-08 06:11:20 (115 MB/s) - ‘steve-jobs-commencement.txt’ saved [11993/11993]
```

```python PYTHON
loader = TextLoader("steve-jobs-commencement.txt")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
```

## Embed the passages and store them in an index

```python PYTHON
embeddings = CohereEmbeddings(model = "multilingual-22-12")
db = Qdrant.from_documents(texts, embeddings, location=":memory:", collection_name="my_documents", distance_func="Dot")
```

## Enter a question

```python PYTHON
questions = [
           "What did the author liken The Whole Earth Catalog to?",
           "What was Reed College great at?",
           "What was the author diagnosed with?",
           "What is the key lesson from this article?",
           "What did the article say about Michael Jackson?",
           ]
```

## Answer the question based on the most relevant documents

```python PYTHON

prompt_template = """Text: {context}

Question: {question}

Answer the question based on the text provided. If the text doesn't contain the answer, reply that the answer is not available."""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)
```

```python PYTHON
chain_type_kwargs = {"prompt": PROMPT}

qa = RetrievalQA.from_chain_type(llm=Cohere(model="command", temperature=0),
                                 chain_type="stuff",
                                 retriever=db.as_retriever(),
                                 chain_type_kwargs=chain_type_kwargs,
                                 return_source_documents=True)

for question in questions:
  answer = qa({"query": question})
  result = answer["result"].replace("\n","").replace("Answer:","")
  sources = answer['source_documents']
  print("-"*150,"\n")
  print(f"Question: {question}")
  print(f"Answer: {result}")

  ### COMMENT OUT THE 4 LINES BELOW TO HIDE THE SOURCES
  print(f"\nSources:")
  for idx, source in enumerate(sources):
    source_wrapped = tr.fill(str(source.page_content), width=150)
    print(f"{idx+1}: {source_wrapped}")
```

```txt title="Output"
------------------------------------------------------------------------------------------------------------------------------------------------------

Question: What did the author liken The Whole Earth Catalog to?
Answer: It was sort of like Google in paperback form, 35 years before Google came along

Sources:
1: When I was young, there was an amazing publication called The Whole Earth Catalog, which was one of the bibles of my generation. It was created by a
fellow named Stewart Brand not far from here in Menlo Park, and he brought it to life with his poetic touch. This was in the late 1960s, before
personal computers and desktop publishing, so it was all made with typewriters, scissors and Polaroid cameras. It was sort of like Google in paperback
form, 35 years before Google came along: It was
2: Stewart and his team put out several issues of The Whole Earth Catalog, and then when it had run its course, they put out a final issue. It was the
mid-1970s, and I was your age. On the back cover of their final issue was a photograph of an early morning country road, the kind you might find
yourself hitchhiking on if you were so adventurous. Beneath it were the words: “Stay Hungry. Stay Foolish.” It was their farewell message as they
signed off. Stay Hungry. Stay Foolish. And I have always
3: idealistic, and overflowing with neat tools and great notions.
4: beautiful, historical, artistically subtle in a way that science can’t capture, and I found it fascinating.
------------------------------------------------------------------------------------------------------------------------------------------------------

Question: What was Reed College great at?
Answer: Reed College was great at calligraphy instruction.

Sources:
1: Reed College at that time offered perhaps the best calligraphy instruction in the country. Throughout the campus every poster, every label on every
drawer, was beautifully hand calligraphed. Because I had dropped out and didn’t have to take the normal classes, I decided to take a calligraphy class
to learn how to do this. I learned about serif and sans serif typefaces, about varying the amount of space between different letter combinations,
about what makes great typography great. It was
2: I dropped out of Reed College after the first 6 months, but then stayed around as a drop-in for another 18 months or so before I really quit. So why
did I drop out?
3: never dropped out, I would have never dropped in on this calligraphy class, and personal computers might not have the wonderful typography that they
do. Of course it was impossible to connect the dots looking forward when I was in college. But it was very, very clear looking backward 10 years
later.
4: OK. It was pretty scary at the time, but looking back it was one of the best decisions I ever made. The minute I dropped out I could stop taking the
required classes that didn’t interest me, and begin dropping in on the ones that looked interesting.
------------------------------------------------------------------------------------------------------------------------------------------------------

Question: What was the author diagnosed with?
Answer: The author was diagnosed with cancer.

Sources:
1: I lived with that diagnosis all day. Later that evening I had a biopsy, where they stuck an endoscope down my throat, through my stomach and into my
intestines, put a needle into my pancreas and got a few cells from the tumor. I was sedated, but my wife, who was there, told me that when they viewed
the cells under a microscope the doctors started crying because it turned out to be a very rare form of pancreatic cancer that is curable with
surgery. I had the surgery and I’m fine now.
2: About a year ago I was diagnosed with cancer. I had a scan at 7:30 in the morning, and it clearly showed a tumor on my pancreas. I didn’t even know
what a pancreas was. The doctors told me this was almost certainly a type of cancer that is incurable, and that I should expect to live no longer than
three to six months. My doctor advised me to go home and get my affairs in order, which is doctor’s code for prepare to die. It means to try to tell
your kids everything you thought you’d have the
3: Stewart and his team put out several issues of The Whole Earth Catalog, and then when it had run its course, they put out a final issue. It was the
mid-1970s, and I was your age. On the back cover of their final issue was a photograph of an early morning country road, the kind you might find
yourself hitchhiking on if you were so adventurous. Beneath it were the words: “Stay Hungry. Stay Foolish.” It was their farewell message as they
signed off. Stay Hungry. Stay Foolish. And I have always
4: beautiful, historical, artistically subtle in a way that science can’t capture, and I found it fascinating.
------------------------------------------------------------------------------------------------------------------------------------------------------

Question: What is the key lesson from this article?
Answer: The key lesson from this article is that you have to trust that the dots will somehow connect in your future. You have to trust in something -- your gut, destiny, life, karma, whatever. This approach has never let me down, and it has made all the difference in my life.

Sources:
1: Again, you can’t connect the dots looking forward; you can only connect them looking backward. So you have to trust that the dots will somehow connect
in your future. You have to trust in something — your gut, destiny, life, karma, whatever. This approach has never let me down, and it has made all
the difference in my life.  My second story is about love and loss.
2: Remembering that I’ll be dead soon is the most important tool I’ve ever encountered to help me make the big choices in life. Because almost everything
— all external expectations, all pride, all fear of embarrassment or failure — these things just fall away in the face of death, leaving only what is
truly important. Remembering that you are going to die is the best way I know to avoid the trap of thinking you have something to lose. You are
already naked. There is no reason not to follow your
3: Your time is limited, so don’t waste it living someone else’s life. Don’t be trapped by dogma — which is living with the results of other people’s
thinking. Don’t let the noise of others’ opinions drown out your own inner voice. And most important, have the courage to follow your heart and
intuition. They somehow already know what you truly want to become. Everything else is secondary.
4: I really didn’t know what to do for a few months. I felt that I had let the previous generation of entrepreneurs down — that I had dropped the baton
as it was being passed to me. I met with David Packard and Bob Noyce and tried to apologize for screwing up so badly. I was a very public failure, and
I even thought about running away from the valley. But something slowly began to dawn on me — I still loved what I did. The turn of events at Apple
had not changed that one bit. I had been rejected,
------------------------------------------------------------------------------------------------------------------------------------------------------

Question: What did the article say about Michael Jackson?
Answer: The text did not provide information about Michael Jackson.

Sources:
1: baby boy; do you want him?” They said: “Of course.” My biological mother later found out that my mother had never graduated from college and that my
father had never graduated from high school. She refused to sign the final adoption papers. She only relented a few months later when my parents
promised that I would someday go to college.
2: beautiful, historical, artistically subtle in a way that science can’t capture, and I found it fascinating.
3: I really didn’t know what to do for a few months. I felt that I had let the previous generation of entrepreneurs down — that I had dropped the baton
as it was being passed to me. I met with David Packard and Bob Noyce and tried to apologize for screwing up so badly. I was a very public failure, and
I even thought about running away from the valley. But something slowly began to dawn on me — I still loved what I did. The turn of events at Apple
had not changed that one bit. I had been rejected,
4: This was the closest I’ve been to facing death, and I hope it’s the closest I get for a few more decades. Having lived through it, I can now say this
to you with a bit more certainty than when death was a useful but purely intellectual concept:
```

## Questions in French

```python PYTHON
questions_fr = [
           "À quoi se compare The Whole Earth Catalog ?",
           "Dans quoi Reed College était-il excellent ?",
           "De quoi l'auteur a-t-il été diagnostiqué ?",
           "Quelle est la leçon clé de cet article ?",
           "Que disait l'article sur Michael Jackson ?",
           ]
```

```python PYTHON
```

```python PYTHON

chain_type_kwargs = {"prompt": PROMPT}

qa = RetrievalQA.from_chain_type(llm=Cohere(model="command", temperature=0),
                                 chain_type="stuff",
                                 retriever=db.as_retriever(),
                                 chain_type_kwargs=chain_type_kwargs,
                                 return_source_documents=True)

for question in questions_fr:
  answer = qa({"query": question})
  result = answer["result"].replace("\n","").replace("Answer:","")
  sources = answer['source_documents']
  print("-"*20,"\n")
  print(f"Question: {question}")
  print(f"Answer: {result}")
```

```txt title="Output"
--------------------

Question: À quoi se compare The Whole Earth Catalog ?
Answer: The Whole Earth Catalog was like Google in paperback form, 35 years before Google came along.
--------------------

Question: Dans quoi Reed College était-il excellent ?
Answer: Reed College offered the best calligraphy instruction in the country.
--------------------

Question: De quoi l'auteur a-t-il été diagnostiqué ?
Answer: The author was diagnosed with a very rare form of pancreatic cancer that is curable with surgery.
--------------------

Question: Quelle est la leçon clé de cet article ?
Answer: The key lesson of this article is that remembering that you will die soon is the most important tool to help one make the big choices in life.
--------------------

Question: Que disait l'article sur Michael Jackson ?
Answer: The text does not contain the answer to the question.
```


# PDF Extractor with Native Multi Step Tool Use

> This page describes how to create an AI agent able to extract information from PDFs.

<AuthorsContainer
  authors={[
    {
      name: "Jason Jung",
      imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/0803e3d-Jason_Jung.jpg",
    },
  ]}
/>

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/agents/pdf-extractor/pdf_extractor.ipynb" />

## Objective

Generally, users are limited to text inputs when using large language models (LLMs), but agents enable the model to do more than ingest or output text information. Using tools, LLMs can call other APIs, save data, and much more. In this notebook, we will explore how we can leverage agents to extract information from PDFs. We will mimic an application where the user uploads PDF files and the agent extracts useful information. This can be useful when the text information has varying formats and you need to extract various types of information.

In the directory, we have a simple\_invoice.pdf file. Everytime a user uploads the document, the agent will extract key information total\_amount and invoice\_number and then save it as CSV which then can be used in another application. We only extract two pieces of information in this demo, but users can extend the example and extract a lot more information.

## Steps

1. extract\_pdf() function extracts text data from the PDF using [unstructured](https://unstructured.io/) package. You can use other packages like PyPDF2 as well.
2. This extracted text is added to the prompt so the model can "see" the document.
3. The agent summarizes the document and passes that information to convert\_to\_json() function. This function makes another call to command model to convert the summary to json output. This separation of tasks is useful when the text document is complicated and long. Therefore, we first distill the information and ask another model to convert the text into json object. This is useful so each model or agent focuses on its own task without suffering from long context.
4. Then the json object goes through a check to make sure all keys are present and gets saved as a csv file. When the document is too long or the task is too complex, the model may fail to extract all information. These checks are then very useful because they give feedback to the model so it can adjust it's parameters to retry.

```python PYTHON
import os

import cohere
import pandas as pd
import json
from unstructured.partition.pdf import partition_pdf
```

```python PYTHON
# uncomment to install dependencies
# !pip install cohere unstructured
```

```python PYTHON
# versions
print('cohere version:', cohere.__version__)
```

```txt title="Output"
cohere version: 5.5.1
```

## Setup

```python PYTHON
COHERE_API_KEY = os.environ.get("CO_API_KEY")
COHERE_MODEL = 'command-a-03-2025'
co = cohere.Client(api_key=COHERE_API_KEY)
```

## Data

The sample invoice data is from [https://unidoc.io/media/simple-invoices/simple\_invoice.pdf](https://unidoc.io/media/simple-invoices/simple_invoice.pdf).

## Tool

Here we define the tool which converts summary of the pdf into json object. Then, it checks to make sure all necessary keys are present and saves it as csv.

```python PYTHON
def convert_to_json(text: str) -> dict:
    """
    Given text files, convert to json object and saves to csv.

    Args:
        text (str): The text to extract information from.

    Returns:
        dict: A dictionary containing the result of the conversion process.
    """

    MANDATORY_FIELDS = [
        "total_amount",
        "invoice_number",
    ]

    message = """# Instruction
    Given the text, convert to json object with the following keys:
    total_amount, invoice_number

    # Output format json:
    {{
        "total_amount": "<extracted amount="" invoice="" total="">",
        "invoice_number": "<extracted invoice="" number="">",
    }}

    Do not output code blocks.

    # Extracted PDF
    {text}
    """

    result = co.chat(
        message=message.format(text=text), model=COHERE_MODEL, preamble=None
    ).text

    try:
        result = json.loads(result)
        # check if all keys are present
        if not all(i in result.keys() for i in MANDATORY_FIELDS):
            return {"result": f"ERROR: Keys are missing. Please check your result {result}"}

        df = pd.DataFrame(result, index=[0])
        df.to_csv("output.csv", index=False)
        return {"result": "SUCCESS. All steps have been completed."}

    except Exception as e:
        return {"result": f"ERROR: Could not load the result as json. Please check the result: {result} and ERROR: {e}"}

```

### Cohere Agent

Below is a cohere agent that leverages multi-step API. It is equipped with convert\_to\_json tool.

```python PYTHON
def cohere_agent(
    message: str,
    preamble: str,
    verbose: bool = False,
) -> str:
    """
    Function to handle multi-step tool use api.

    Args:
        message (str): The message to send to the Cohere AI model.
        preamble (str): The preamble or context for the conversation.
        verbose (bool, optional): Whether to print verbose output. Defaults to False.

    Returns:
        str: The final response from the call.
    """

    functions_map = {
        "convert_to_json": convert_to_json,
    }

    tools = [
        {
            "name": "convert_to_json",
            "description": "Given a text, convert it to json object.",
            "parameter_definitions": {
                "text": {
                    "description": "text to be converted into json",
                    "type": "str",
                    "required": True,
                },
            },
        }
    ]

    counter = 1

    response = co.chat(
        model=COHERE_MODEL,
        message=message,
        preamble=preamble,
        tools=tools,
    )

    if verbose:
        print(f"\nrunning step 0")
        print(response.text)

    while response.tool_calls:
        tool_results = []

        if verbose:
            print(f"\nrunning step {counter}")
        for tool_call in response.tool_calls:
            print("tool_call.parameters:", tool_call.parameters)
            if tool_call.parameters:
                output = functions_map[tool_call.name](**tool_call.parameters)
            else:
                output = functions_map[tool_call.name]()

            outputs = [output]
            tool_results.append({"call": tool_call, "outputs": outputs})

            if verbose:
                print(
                    f"= running tool {tool_call.name}, with parameters: {tool_call.parameters}"
                )
                print(f"== tool results: {outputs}")

        response = co.chat(
            model=COHERE_MODEL,
            message="",
            chat_history=response.chat_history,
            preamble=preamble,
            tools=tools,
            tool_results=tool_results,
        )

        if verbose:
            print(response.text)
            counter += 1

    return response.text
```

### main

```python PYTHON
def extract_pdf(path):
    """
    Function to extract text from a PDF file.
    """
    elements = partition_pdf(path)
    return "\n".join([str(el) for el in elements])


def pdf_extractor(pdf_path):
    """
    Main function that extracts pdf and calls the cohere agent.
    """
    pdf_text = extract_pdf(pdf_path)

    prompt = f"""
    # Instruction
    You are expert at extracting invoices from PDF. The text of the PDF file is given below.

    You must follow the steps below:
    1. Summarize the text and extract only the most information: total amount billed and invoice number.
    2. Using the summary above, call convert_to_json tool, which uses the summary from step 1.
    If you run into issues. Identifiy the issue and retry.
    You are not done unless you see SUCCESS in the tool output.

    # File Name:
    {pdf_path}

    # Extracted Text:
    {pdf_text}
    """
    output = cohere_agent(prompt, None, verbose=True)
    print(f"Finished extracting: {pdf_path}")

    print('Please check the output below')
    print(pd.read_csv('output.csv'))


pdf_extractor('simple_invoice.pdf')

```

```txt title="Output"
running step 0
I will summarise the text and then use the convert_to_json tool to format the summary.

running step 1
tool_call.parameters: {'text': 'Total amount billed: $115.00\nInvoice number: 0852'}
= running tool convert_to_json, with parameters: {'text': 'Total amount billed: $115.00\nInvoice number: 0852'}
== tool results: [{'result': 'SUCCESS. All steps have been completed.'}]
SUCCESS.
Finished extracting: simple_invoice.pdf
Please check the output below
    total_amount  invoice_number
0      $115.00             852
```

As shown above, the model first summarized the extracted pdf as `Total amount: $115.00\nInvoice number: 0852` and sent this to `conver_to_json()` function.
`conver_to_json()` then converts it to json format and saves it into a csv file.


# Pondr, Fostering Connection through Good Conversation

> This page contains a basic tutorial on how tplay an AI-powered version of the icebreaking game 'Pondr'.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Pondr_Question_Generation.ipynb" />

We tend to chat all the time with friends new and olds, but often it feels like we’re just scratching at the surface, or defaulting to predictable, mundane conversations. Really good conversations — ones that introduce an element of vulnerability, spur a moment of fun, or create a deep sense of closeness — are few and far between. And when we have those types of conversations, we remember them.

Pondr is a game that turns strangers into friends, and friends into besties, by fostering connection and closeness through really good conversations. Using Cohere, Pondr generates question prompts on command that are uniquely tailored to the players’ setting. Whether you’re looking to deepen a connection with someone you’ve known forever, or you’re just hoping to become more familiar with a new friend, Pondr will help you drive the right sort of conversation.

You can build your own version of Pondr by following these simple steps:

1. Generate potential conversation questions
2. Rank the generated questions
3. Put the generation and classification behind an interface

In this notebook we will walk through the first two steps.

### Setup

Install and import the tools we will need as well as initializing the Cohere model.

```python PYTHON
import cohere
from cohere.responses.classify import Example
import pandas as pd
```

```python PYTHON
co=cohere.Client('YOUR_API_KEY')
```

### 1. Generate Potential Conversation Questions

Generate a list of potential conversation questions and retain the first 10.

```python PYTHON
#user_input is hardcoded for this example
user_input='I am meeting up with a coworker. We are meeting at a fancy restaurant. I wanna ask some interesting questions. These questions should be deep.'
prompt=user_input+'\nHere are 10 interesting questions to ask:\n1)'
response=co.generate(model='xlarge', prompt=prompt, max_tokens=200, temperature=5).generations[0].text
response
```

```python PYTHON
def generation_to_df(generation):
    generation=response.split('\n')
    clean_questions=[]
    for i in range(10):
        curr_q=generation[i]
        clean_questions.append(curr_q[curr_q.find(')')+1:])
    clean_q_df=pd.DataFrame(clean_questions, columns=['questions'])
    return clean_q_df
```

```python PYTHON
clean_q_df = generation_to_df(response)
pd.options.display.max_colwidth=150
clean_q_df
```

### 2. Classify Questions

Rank and sort the questions based on interestingness and specificity.

```python PYTHON
interestingness=[
    Example("What do you think is the hardest part of what I do for a living?", "Not Interesting"),
    Example("What\'s the first thing you noticed about me?", "Interesting"),
    Example("Do you think plants thrive or die in my care?", "Interesting"),
    Example("Do I seem like more of a creative or analytical type?", "Interesting"),
    Example("What subject do you think I thrived at in school?", "Not Interesting"),
    Example("What\'s been your happiest memory this past year?", "Interesting"),
    Example("What lesson took you the longest to un-learn?", "Not Interesting"),
    Example("How can you become a better person?", "Not Interesting"),
    Example("Do you think I intimidate others? Why or why not?", "Interesting"),
    Example("What\'s the most embarrassing thing that happened to you on a date?", "Not Interesting"),
    Example("How would you describe what you think my type is in three words?", "Interesting"),
    Example("What do you think I\'m most likely to splurge on?", "Interesting"),
    Example("As a child what do you think I wanted to be when I grow up?", "Interesting"),
    Example("Do you think you are usually early, on time, or late to events?", "Not Interesting"),
    Example("Do you think I was popular at school?", "Interesting"),
    Example("What questions are you trying to answer most in your life right now?", "Not Interesting")]
specificity=[
    Example("What\'s the first thing you noticed about me?", "Specific"),
    Example("Do you think plants thrive or die in my care?", "Specific"),
    Example("Do I seem like more of a creative or analytical type?", "Not Specific"),
    Example("How would you describe what you think my type is in three words?", "Not Specific"),
    Example("What do you think I\'m most likely to splurge on?", "Specific"),
    Example("What subject do you think I thrived at in school?", "Not Specific"),
    Example("As a child what do you think I wanted to be when I grow up?", "Specific"),
    Example("Do you think I was popular at school?", "Specific"),
    Example("Do you think you\'re usually early, on time, or late to events?", "Specific"),
    Example("Do you think I intimidate others? Why or why not?", "Specific"),
    Example("What\'s been your happiest memory this past year?", "Not Specific"),
    Example("What subject do you think I thrived at in school?", "Specific"),
    Example("What\'s the biggest mistake that you think you needed to make to become who you are now?", "Specific"),
    Example("Is there anything you\'ve done recently that you\'re incredibly proud of?", "Not Specific"),
    Example("How are you and your siblings similar?", "Not Specific"),
    Example("What\'s the worst pain you have ever been in that wasn\'t physical?", "Specific"),
    Example("Has a stranger ever changed your life?", "Specific"),
    Example("Do you think the image you have of yourself matches the image other people see you as?", "Specific"),
    Example("What would your younger self not believe about your life today?", "Specific")]
```

```python PYTHON
def add_attribute(df, attribute, name, target):

  response = co.classify(
    model='medium',
    inputs=list(df['questions']),
    examples=attribute)

  q_conf=[]
  for q in response.classifications:
    q_conf.append(q.labels[target].confidence)

  df[name]=q_conf
```

```python PYTHON
add_attribute(clean_q_df, interestingness, 'interestingness', 'Interesting')
add_attribute(clean_q_df, specificity, 'specificity', 'Specific')
clean_q_df['average']= clean_q_df.iloc[:,1:].mean(axis=1)
clean_q_df.sort_values(by='average', ascending=False)
```


# Deep Dive Into Evaluating RAG Outputs

> This page contains information on evaluating the output of RAG systems.

<AuthorsContainer
  authors={[
    {
      name: "Marco Del Tredici",
      imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/f103c96-Marco.jpg",
    },
  ]}
/>

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Deep_dive_into_RAG_evaluation.ipynb" />

In this notebook, we'll show you how to evaluate the output of a RAG system. The high-level RAG flow is depicted in the diagram below.

We will focus on the evaluation of **Retrieve** and **Response** (or **Generation**), and present a set of metrics for each phase. We will deep dive into each metric, to give you a full understanding of how we evaluate models and why we do it this way, and provide code so you can repdroduce on your own data.

To demonstrate the metrics, we will use data from the [Docugami's KG-RAG](https://github.com/docugami/KG-RAG-datasets/tree/main/sec-10-q/data/v1) dataset, a RAG dataset for financial 10Q filing reports. We will focus only on evaluation, without performing the actual Retrieval and response Generation steps.

# Table of content

1. [Getting started](#getting-started)
2. [Retrieval Evaluation](#retrieval-evaluation)
3. [Generation Evaluation](#generation-evaluation)
4. [Final Comments](#final-comments)

## Getting Started \[#getting-started]

Let's start by setting the environment and downloading the dataset.

```python PYTHON
%%capture
!pip install llama-index cohere openai
!pip install mistralai
```

```python PYTHON
# required imports
from getpass import getpass
import os
import re
import numpy as np
from llama_index.core import SimpleDirectoryReader
from llama_index.core.llama_dataset import download_llama_dataset, LabelledRagDataset
from openai import Client
from mistralai.client import MistralClient
```

For Response evaluation, we will use an LLM as a judge.
Any LLM can be used for this goal, but because evaluation is a very challenging task, we recommend using powerful LLMs, possibly as an ensemble of models. In [previous work](https://arxiv.org/pdf/2303.16634.pdf), it has been shown that models tend to assign higher scores to their own output. Since we generated the answers in this notebook using `command-r`, we will not use it for evaluation. We will provide two alternatives, `gpt-4` and `mistral`. We set `gpt-4` as the default model because, as mentioned above, evaluation is challenging, and `gpt-4` is powerful enough to efficiently perform the task.

```python PYTHON
# Get keys
openai_api_key = getpass("Enter your OpenAI API Key: ")
# uncomment if you want to use mistral
#mistral_api_key = getpass["Enter your Mistral API Key: "]

# Define the model you want to use - you can replace gpt-4 with any other gpt version
model = "gpt-4"
# uncomment if you want to use mistral
#model = "mistral-large-latest"

```

```python PYTHON
if model == "gpt-4":
  client = Client(api_key=openai_api_key)
else:
  client = MistralClient(api_key=mistral_api_key)
```

```python PYTHON
# let's define a function to get the model's response for a given input
def get_response(model, client, prompt):
  response = client.chat.completions.create(
      model=model,
      messages=[{"role": "user", "content": prompt}],
      temperature=0)
  return response.choices[0].message.content
```

```python PYTHON
# load the DocugamiKgRagSec10Q dataset
if os.path.exists("./data/source_files") and os.path.exists("./data/rag_dataset.json"):
        rag_dataset = LabelledRagDataset.from_json("./data/rag_dataset.json")
        documents = SimpleDirectoryReader(input_dir="./data/source_files").load_data(show_progress=True)
else:
    rag_dataset, documents = download_llama_dataset("DocugamiKgRagSec10Q", "./data")
```

## Retrieval Evaluation \[#retrieval-evaluation]

In the Retrieval phase, we evaluate the set of **retrieved documents** against the **golden documents** set.

We use three standard metrics to evaluate retrieval:

* **Precision**: the proportion of returned documents that are relevant, according to the gold annotation
* **Recall**: the proportion of relevant documents in the gold data found in the retrieved documents
* **Mean Average Precision** (**MAP**): measures the capability of the retriever to return relevant documents at the top of the list

We implement these three metrics in the class below:

```python PYTHON
class RetrievalEvaluator:

    def compute_precision(self, retrieved_documents, golden_documents):
      # compute the percentage of retrieved documents found in the golden docs
      return len(set(retrieved_documents).intersection(golden_documents)) / len(retrieved_documents)

    def compute_recall(self, retrieved_documents, golden_documents):
      # compute the percentage of golden documents found in the retrieved docs
      return len(set(retrieved_documents).intersection(golden_documents)) / len(golden_documents)

    def compute_mean_average_precision(self, retrieved_documents, golden_documents):
      # check which among the retrieved docs is found in the gold, keeping the order
      correct_retrieved_documents = [1 if x in golden_documents else 0 for x in retrieved_documents]
      # compute map
      map = np.mean([sum(correct_retrieved_documents[: i + 1]) / (i + 1) for i, v in enumerate(correct_retrieved_documents) if v == 1])
      return map

    def run_evals(self, retrieved_documents, golden_documents):
      precision = round(self.compute_precision(retrieved_documents, golden_documents),2)
      recall = round(self.compute_recall(retrieved_documents, golden_documents),2)
      map = round(self.compute_mean_average_precision(retrieved_documents, golden_documents),2)
      results = {'precision': [precision],
                 'recall': [recall],
                 'map': [map]}
      for k,v in results.items():
          print(f"{k}: {v[0]}")

```

Let's now see how to use the class above to compute the results on a single datapoint.

```python PYTHON
# select the index of a single datapoint - the first one in the dataset
idx = 0

# select the query
query = rag_dataset[idx].query

# and the golden docs
golden_docs = rag_dataset[idx].reference_answer.split('SOURCE(S): ')[1].split(', ')

# let's assume we have the following set of retrieved docs
retrieved_docs = ['2022 Q3 AAPL.pdf', '2023 Q1 MSFT.pdf', '2023 Q1 AAPL.pdf']

print(f'Query: {query}')
print(f'Golden docs: {golden_docs}')
print(f'Retrieved docs: {retrieved_docs}')
```

```txt title="Output"
Query: How has Apple's total net sales changed over time?
Golden docs: ['2022 Q3 AAPL.pdf', '2023 Q1 AAPL.pdf', '2023 Q2 AAPL.pdf', '2023 Q3 AAPL.pdf']
Retrieved docs: ['2022 Q3 AAPL.pdf', '2023 Q1 MSFT.pdf', '2023 Q1 AAPL.pdf']
```

```python PYTHON
# we can now instantiate the evaluator
evaluate_retrieval = RetrievalEvaluator()

# and run the evaluation
evaluate_retrieval.run_evals(retrieved_docs,golden_docs)

```

```txt title="Output"
precision: 0.67
recall: 0.5
map: 0.83
```

What are the figures above telling us?

* Precision (0.67) tells us that 2 out of 3 of the retrieved docs are correct
* Recall (0.5) means that 2 out of 4 relevant docs have been retrieved
* MAP (0.83) is computed as the average of 1/1 (the highest ranked doc is correct) and 2/3 (the 2nd ranked doc is wrong, the 3rd is correct).

While the example here focuses on a single datapoint, you can easily apply the same metrics to all your dataset and get the overall performance of your Retrieve phase.

## Generation Evaluation \[#generation-evaluation]

Evaluating grounded generation (the second step of RAG) is notoriously difficult, because generations are usually complex and rich of information, and simply labelling an answer as "good" or "bad" is not enough.
To overcome this issue, we first decompose complex answers into a set of basic *claims*, where a claim is any sentence or part of a sentence in the answer that expresses a verifiable fact. Subsequently, we check the validity of each claim independently, defining the overall quality of the answer based on the correctness of the claims it includes.

We use claims to compute three metrics:

* **Faithfulness**, which measures how many of the claims in the generated response are supported by the retrieved documents. This is a fundamental metric, as it tells us how *grounded* in the documents the response is, and, contextually, it allows us to spot hallucinations

* **Correctness**, which checks which claims in the response also occur in the gold answer

* And **Coverage**, by which we assess how many of the claims in the gold answer are included in the generated response.

Note that Faithfulness and Correctness share the exact same approach, the difference being that the former checks the claims against the supporting docs, while the latter against the golden answer.
Also, while Correctness is measuring the precision of the claims in the response, Coverage can be seen as complementary, as it measures recall.

### Claim Extraction

Let's now see how we implement the evaluation described above using LLMs. Let's start with **claim extraction**.

```python PYTHON
# first, let's define a function which extracts the claims from a response
def extract_claims(query, response, model, client):

  # define the instructions on how to extract the claims
  preamble = "You are shown a prompt and a completion. You have to identify the main claims stated in the completion. A claim is any sentence or part of a sentence that expresses a verifiable fact. Please return a bullet list, in which every line includes one of the claims you identified. Do not add any further explanation to the bullet points."

  # build the prompt
  prompt = f"{preamble}\n\nPROMPT: {query}\n\nCOMPLETION: {response}"

  # get the claims
  claims = get_response(model, client, prompt)

  return claims

```

```python PYTHON
# now, let's consider this answer, which we previously generated with command-r
response = "Apple's total net sales experienced a decline over the last year. The three-month period ended July 1, 2023, saw a total net sale of $81,797 million, which was a 1% decrease from the same period in 2022. The nine-month period ended July 1, 2023, fared slightly better, with a 3% decrease in net sales compared to the first nine months of 2022.\nThis downward trend continued into the three and six-month periods ending April 1, 2023. Apple's total net sales decreased by 3% and 4% respectively, compared to the same periods in 2022."

# let's extract the claims
claims = extract_claims(query, response, model, client)

# and see what the model returns
print(f"List of claims extracted from the model's response:\n\n{claims}")
```

```txt title="Output"
List of claims extracted from the model's response:

- Apple's total net sales experienced a decline over the last year.
- The three-month period ended July 1, 2023, saw a total net sale of $81,797 million.
- This was a 1% decrease from the same period in 2022.
- The nine-month period ended July 1, 2023, had a 3% decrease in net sales compared to the first nine months of 2022.
- The downward trend continued into the three and six-month periods ending April 1, 2023.
- Apple's total net sales decreased by 3% and 4% respectively, compared to the same periods in 2022.
```

### Claim Assessment

Nice! now that we have the list of claims, we can go ahead and **assess the validity** of each claim.

```python PYTHON
# Let's create a function that checks each claim against a reference text,
# which here we will call "context". As you will see, we will use different contexts,
# depending on the metric we want to compute.

def assess_claims(query, claims, context, model, client):

  # define the instructions on how to perform the assessment.
  # the model has to append to each row a binary SUPPORTED tag
  preamble = "You are shown a prompt, a context and a list of claims. You have to check which of the claims in the list are supported by the context. Please return the list of claims exactly as is it, just append to each row “SUPPORTED=1” if the claim is supported by the context, or “SUPPORTED=0” if the claim is not supported by the context. Do not add any further explanation to the bullet points."

  # turn list into string
  context = '\n'.join(context)

  # build the prompt
  prompt = f"{preamble}\n\nPROMPT: {query}\n\nCONTEXT:\n{context}\n\nCLAIMS:\n{claims}"

  # get the response
  assessment = get_response(model, client, prompt)

  return assessment
```

### Faithfulness

```python PYTHON
# Let's start with Faithfulness: in this case, we want to assess the claims
# in the response against the retrieved documents (i.e., context = retrieved documents)

# for the sake of clarity, we report the actual text of the retrieved documents
retrieved_documents = ['Products and Services Performance\nThe following table shows net sales by category for the three- and six-month periods ended April 1, 2023 and March 26, 2022 (dollars in millions):\nThree Months Ended Six Months Ended\nApril 1,\n2023March 26,\n2022 ChangeApril 1,\n2023March 26,\n2022 Change\nNet sales by category:\niPhone $ 51,334 $ 50,570 2 %$ 117,109 $ 122,198 (4)%\nMac 7,168 10,435 (31)% 14,903 21,287 (30)%\niPad 6,670 7,646 (13)% 16,066 14,894 8 %\nWearables, Home and Accessories 8,757 8,806 (1)% 22,239 23,507 (5)%\nServices 20,907 19,821 5 % 41,673 39,337 6 %\nTotal net sales $ 94,836 $ 97,278 (3)%$ 211,990 $ 221,223 (4)%\niPhone\niPhone net sales were relatively flat during the second quarter of 2023 compared to the secon d quarter of 2022. Year-over-year iPhone net sales decreased\nduring the first six months of 2023 due primarily to lower net sales from the Company’ s new iPhone models launched in the fourth quarter of 2022.\nMac\nMac net sales decreased during the second quarter and first six months of 2023 compared to the same periods in 2022 due primarily to lower net sales of\nMacBook Pro.\niPad\niPad net sales decreased during the second quarter of 2023 compared to the second quarter of 2022 due primarily to lower net sales of iPad Pro  and iPad Air.\nYear-over-year iPad net sales increased during the first six months of 2023 due primarily to higher net sales of iPad, partially offset by lower net sales of iPad\nmini .\nWearables, Home and Accessories\nWearables, Home and Accessories net sales were relatively flat during the second quarter of 2023 compared to the second quarter of 2022. Year-over-year\nWearables, Home and Accessories net sales decreased during the first six months of 2023 due primarily to lower net sales of AirPods .\nServices\nServices net sales increased during the second quarter and first six months of 2023 compared to the same periods in 2022 due primarily to higher net sales from\ncloud services, music and advertising.® ®\n®\n®\nApple Inc. | Q2 2023 Form 10-Q | 16', 'Products and Services Performance\nThe following table shows net sales by category for the three- and nine-month periods ended July 1, 2023 and June 25, 2022 (dollars in millions):\nThree Months Ended Nine Months Ended\nJuly 1,\n2023June 25,\n2022 ChangeJuly 1,\n2023June 25,\n2022 Change\nNet sales by category:\niPhone $ 39,669 $ 40,665 (2)%$ 156,778 $ 162,863 (4)%\nMac 6,840 7,382 (7)% 21,743 28,669 (24)%\niPad 5,791 7,224 (20)% 21,857 22,118 (1)%\nWearables, Home and Accessories 8,284 8,084 2 % 30,523 31,591 (3)%\nServices 21,213 19,604 8 % 62,886 58,941 7 %\nTotal net sales $ 81,797 $ 82,959 (1)%$ 293,787 $ 304,182 (3)%\niPhone\niPhone net sales decreased during the third quarter and first nine months of 2023 compared to the same periods in 2022 due primarily to lower net sales from\ncertain iPhone models, partially of fset by higher net sales of iPhone 14 Pro models.\nMac\nMac net sales decreased during the third quarter and first nine months of 2023 compared to the same periods in 2022 due primarily to lower net sales of laptops.\niPad\niPad net sales decreased during the third quarter of 2023 compared to the third quarter of 2022 due primarily to lower net sales across most iPad models. Year-\nover-year iPad net sales were relatively flat during the first nine months of 2023.\nWearables, Home and Accessories\nWearables, Home and Accessories net sales increased during the third quarter of 2023 compare d to the third quarter of 2022 due primarily to higher net sales of\nWearables, which includes AirPods , Apple Watch  and Beats  products, partially offset by lower net sales of accessories. Year-over-year Wearables, Home\nand Accessories net sales decreased during the first nine months of 2023 due primarily to lower net sales of W earables and accessories.\nServices\nServices net sales increased during the third quarter of 2023 compared to the third quarter of 2022 due primarily to higher net sales from advertising, cloud\nservices and the App Store . Year-over-year Services net sales increased during the first nine months of 2023 due primarily to higher net sales from cloud\nservices, advertising and music.® ® ®\n®\nApple Inc. | Q3 2023 Form 10-Q | 16']

# get the Faithfulness assessment for each claim
assessed_claims_faithfulness = assess_claims(query=query,
                                             claims=claims,
                                             context=retrieved_documents,
                                             model=model,
                                             client=client)

print(f"Assessment of the claims extracted from the model's response:\n\n{assessed_claims_faithfulness}")
```

```txt title="Output"
Assessment of the claims extracted from the model's response:

- Apple's total net sales experienced a decline over the last year. SUPPORTED=1
- The three-month period ended July 1, 2023, saw a total net sale of $81,797 million. SUPPORTED=1
- This was a 1% decrease from the same period in 2022. SUPPORTED=1
- The nine-month period ended July 1, 2023, had a 3% decrease in net sales compared to the first nine months of 2022. SUPPORTED=1
- The downward trend continued into the three and six-month periods ending April 1, 2023. SUPPORTED=1
- Apple's total net sales decreased by 3% and 4% respectively, compared to the same periods in 2022. SUPPORTED=1
```

Great, we now have an assessment for each of the claims: in the last step, we just need to use these assessments to define the final score.

```python PYTHON
# given the list of claims and their label, compute the final score
# as the proportion of correct claims over the full list of claims
def get_final_score(claims_list):
  supported = len(re.findall("SUPPORTED=1", claims_list))
  non_supported = len(re.findall("SUPPORTED=0", claims_list))
  score = supported / (supported+non_supported)
  return round(score, 2)
```

```python PYTHON
score_faithfulness = get_final_score(assessed_claims_faithfulness)
print(f'Faithfulness: {score_faithfulness}')
```

```txt title="Output"
Faithfulness: 1.0
```

The final Faithfulness score is 1, which means that the model's response is fully grounded in the retrieved documents: that's a very good news :)

Before moving on, let's modify the model's response by adding a piece of information which is **not** grounded in any document, and re-compute Faithfulness.

```python PYTHON
# let's mess up the century, changing 2022 to 1922
modified_response = response.replace('2022', '1922')

# extract the claims from the modified response
modified_claims = extract_claims(query, modified_response, model, client)

# and get assess the modified claims
assessed_modified_claims = assess_claims(query=query,
                                         claims=modified_claims,
                                         context=retrieved_documents,
                                         model=model,
                                         client=client)

print(f"Assessment of the modified claims:\n\n{assessed_modified_claims}\n")

score_faithfulness_modified_claims = get_final_score(assessed_modified_claims)
print(f'Faithfulness: {score_faithfulness_modified_claims}')
```

```txt title="Output"
Assessment of the modified claims:

- Apple's total net sales experienced a decline over the last year. SUPPORTED=1
- The three-month period ended July 1, 2023, saw a total net sale of $81,797 million. SUPPORTED=1
- This was a 1% decrease from the same period in 1922. SUPPORTED=0
- The nine-month period ended July 1, 2023, had a 3% decrease in net sales compared to the first nine months of 1922. SUPPORTED=0
- The downward trend continued into the three and six-month periods ending April 1, 2023. SUPPORTED=1
- Apple's total net sales decreased by 3% and 4% respectively, compared to the same periods in 1922. SUPPORTED=0

Faithfulness: 0.5
```

As you can see, by assessing claims one by one, we are able to spot **hallucinations**, that is, the (corrupted) cases in which the information provided by the model is not grounded in any of the retrieved documents.

### Correctness

As said, Faithfulness and Correctness share the same logic, the only difference being that we will check the claims against the gold answer. We can therefore repeat the process above, and just substitute the `context`.

```python PYTHON
# let's get the gold answer from the dataset
golden_answer = rag_dataset[idx].reference_answer

# and check the claims in the response against the gold.
# note that assess_claims takes exactly the same args as with Faithfulness
# except for the context, that now is the golden_answer
assessed_claims_correctness = assess_claims(query=query,
                                            claims=claims,
                                            context=golden_answer, # note the different context
                                            model=model,
                                            client=client)


print(f"Assess the claims extracted from the model's response against the golden answer:\n\n{assessed_claims_correctness}")
```

```txt title="Output"
Assess the claims extracted from the model's response against the golden answer:

- Apple's total net sales experienced a decline over the last year. SUPPORTED=1
- The three-month period ended July 1, 2023, saw a total net sale of $81,797 million. SUPPORTED=1
- This was a 1% decrease from the same period in 2022. SUPPORTED=0
- The nine-month period ended July 1, 2023, had a 3% decrease in net sales compared to the first nine months of 2022. SUPPORTED=0
- The downward trend continued into the three and six-month periods ending April 1, 2023. SUPPORTED=1
- Apple's total net sales decreased by 3% and 4% respectively, compared to the same periods in 2022. SUPPORTED=0
```

As mentioned above, automatic evaluation is a hard task, and even when using powerful models, claim assessment can present problems: for example, the third claim is labelled as 0, even if it might be inferred from the information in the gold answer.

```python PYTHON
# we can now compute the final Correctness score
score_correctness = get_final_score(assessed_claims_correctness)
print(f'Correctness: {score_correctness}')
```

```txt title="Output"
Correctness: 0.5
```

For Correctness, we found that only half of the claims in the generated response are found in the gold answer. Note that this is not necessarily an issue: reference answers are often non-exhaustive, especially in dataset including open-ended questions, like the one we are considering in this post, and *both* the generated and golden answer can include relevant information.

### Coverage

We finally move to Coverage. Remember that, in this case, we want to check how many of the claims *in the gold answer* are included in the generated response. To do it, we first need to extract the claims from the gold answer.

```python PYTHON
# let's extract the golden claims
gold_claims = extract_claims(query, golden_answer, model, client)

print(f"List of claims extracted from the gold answer:\n\n{gold_claims}")
```

```txt title="Output"
List of claims extracted from the gold answer:

- For the quarterly period ended June 25, 2022, the total net sales were $82,959 million.
- For the quarterly period ended December 31, 2022, the total net sales were $117,154 million.
- For the quarterly period ended April 1, 2023, the total net sales were $94,836 million.
- For the quarterly period ended July 1, 2023, the total net sales were $81,797 million.
- There was an increase in total net sales from the quarter ended June 25, 2022, to the quarter ended December 31, 2022.
- There was a decrease in total net sales in the quarters ended April 1, 2023, and July 1, 2023.
```

Then, we check which of these claims is present in the response generated by the model.

```python PYTHON
# note that in, this case, the context is the model's response
assessed_claims_coverage = assess_claims(query=query,
                                         claims=gold_claims,
                                         context=response,
                                         model=model,
                                         client=client)


print(f"Assess which of the gold claims is in the model's response:\n\n{assessed_claims_coverage}")
```

```txt title="Output"
Assess which of the gold claims is in the model's response:

- For the quarterly period ended June 25, 2022, the total net sales were $82,959 million. SUPPORTED=0
- For the quarterly period ended December 31, 2022, the total net sales were $117,154 million. SUPPORTED=0
- For the quarterly period ended April 1, 2023, the total net sales were $94,836 million. SUPPORTED=0
- For the quarterly period ended July 1, 2023, the total net sales were $81,797 million. SUPPORTED=1
- There was an increase in total net sales from the quarter ended June 25, 2022, to the quarter ended December 31, 2022. SUPPORTED=0
- There was a decrease in total net sales in the quarters ended April 1, 2023, and July 1, 2023. SUPPORTED=1
```

```python PYTHON
# we compute the final Coverage score
score_coverage = get_final_score(assessed_claims_coverage)
print(f'Coverage: {score_coverage}')
```

```txt title="Output"
Coverage: 0.33
```

The Coverage score is telling us that 1/3 of the information in the gold answer is present in the generated answer. This is a useful information, that, similarly to what said above regarding Correctness, can raise further questions, such as: is it acceptable to have diverging information in the generated answer? Is any crucial piece of information missing in the generated answer?

The answer to these questions is use case-specific, and has to be made by the end user: The claim-based approach implemented here supports the user by providing a clear and detailed view on what the model is assessing and how.

## Final Comments \[#final-comments]

RAG evaluation is a hard task, especially the evaluation of the generated response. In this notebook we offer a clear, robust and replicable approach to evaluation, on which you can build on to build your evaluation pipeline.


# RAG With Chat Embed and Rerank via Pinecone

> This page contains a basic tutorial on how to build a RAG-powered chatbot.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/RAG_with_Chat_Embed_and_Rerank_via_Pinecone.ipynb" />

This notebook shows how to build a RAG-powered chatbot with Cohere's Chat endpoint. The chatbot can extract relevant information from external documents and produce verifiable, inline citations in its responses.

This application will use several Cohere API endpoints:

* Chat: For handling the main logic of the chatbot, including turning a user message into queries, generating responses, and producing citations
* Embed: For turning textual documents into their embeddings representation, later to be used in retrieval (we’ll use the latest, state-of-the-art Embed v4 model)
* Rerank: For reranking the retrieved documents according to their relevance to a query

The diagram below provides an overview of what we’ll build.

Here is a summary of the steps involved.

Initial phase:

* **Step 0**: Ingest the documents – get documents, chunk, embed, and index.

For each user-chatbot interaction:

* **Step 1**: Get the user message
* **Step 2**: Call the Chat endpoint in query-generation mode
* If at least one query is generated
  * **Step 3**: Retrieve and rerank relevant documents
  * **Step 4**: Call the Chat endpoint in document mode to generate a grounded response with citations
* If no query is generated
  * **Step 4**: Call the Chat endpoint in normal mode to generate a response

```python PYTHON
! pip install cohere hnswlib unstructured python-dotenv -q
```

```python PYTHON
import cohere
from pinecone import Pinecone, PodSpec
import uuid
import hnswlib
from typing import List, Dict
from unstructured.partition.html import partition_html
from unstructured.chunking.title import chunk_by_title

co = cohere.Client("COHERE_API_KEY") # Get your API key here: https://dashboard.cohere.com/api-keys
pc = Pinecone(api_key="PINECONE_API_KEY") # (get API key at app.pinecone.io)
```

```python PYTHON
import cohere
import os
import dotenv

dotenv.load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))
pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)

```

First, we define the list of documents we want to ingest and make available for retrieval. As an example, we'll use the contents from the first module of Cohere's *LLM University: What are Large Language Models?*.

```python PYTHON
raw_documents = [
    {
        "title": "Text Embeddings",
        "url": "https://docs.cohere.com/docs/text-embeddings"},
    {
        "title": "Similarity Between Words and Sentences",
        "url": "https://docs.cohere.com/docs/similarity-between-words-and-sentences"},
    {
        "title": "The Attention Mechanism",
        "url": "https://docs.cohere.com/docs/the-attention-mechanism"},
    {
        "title": "Transformer Models",
        "url": "https://docs.cohere.com/docs/transformer-models"}
]
```

Usually the number of documents for practical applications is vast, and so we'll need to be able to search documents efficiently. This involves breaking the documents into chunks, generating embeddings, and indexing the embeddings, as shown in the image below.

We implement this in the `Vectorstore` class below, which takes the `raw_documents` list as input. Three methods are immediately called when creating an object of the `Vectorstore` class:

`load_and_chunk()`\
This method uses the `partition_html()` method from the `unstructured` library to load the documents from URL and break them into smaller chunks. Each chunk is turned into a dictionary object with three fields:

* `title` - the web page’s title,
* `text` - the textual content of the chunk, and
* `url` - the web page’s URL.

`embed()`\
This method uses Cohere's `embed-v4.0` model to generate embeddings of the chunked documents. Since our documents will be used for retrieval, we set `input_type="search_document"`. We send the documents to the Embed endpoint in batches, because the endpoint has a limit of 96 documents per call.

`index()`\
This method uses the `hsnwlib` package to index the document chunk embeddings. This will ensure efficient similarity search during retrieval. Note that `hnswlib` uses a vector library, and we have chosen it for its simplicity.

```python PYTHON
class Vectorstore:
    """
    A class representing a collection of documents indexed into a vectorstore.

    Parameters:
    raw_documents (list): A list of dictionaries representing the sources of the raw documents. Each dictionary should have 'title' and 'url' keys.

    Attributes:
    raw_documents (list): A list of dictionaries representing the raw documents.
    docs (list): A list of dictionaries representing the chunked documents, with 'title', 'text', and 'url' keys.
    docs_embs (list): A list of the associated embeddings for the document chunks.
    docs_len (int): The number of document chunks in the collection.
    idx (hnswlib.Index): The index used for document retrieval.

    Methods:
    load_and_chunk(): Loads the data from the sources and partitions the HTML content into chunks.
    embed(): Embeds the document chunks using the Cohere API.
    index(): Indexes the document chunks for efficient retrieval.
    retrieve(): Retrieves document chunks based on the given query.
    """

    def __init__(self, raw_documents: List[Dict[str, str]]):
        self.raw_documents = raw_documents
        self.docs = []
        self.docs_embs = []
        self.retrieve_top_k = 10
        self.rerank_top_k = 3
        self.load_and_chunk()
        self.embed()
        self.index()


    def load_and_chunk(self) -> None:
        """
        Loads the text from the sources and chunks the HTML content.
        """
        print("Loading documents...")

        for raw_document in self.raw_documents:
            elements = partition_html(url=raw_document["url"])
            chunks = chunk_by_title(elements)
            for chunk in chunks:
                self.docs.append(
                    {
                        "title": raw_document["title"],
                        "text": str(chunk),
                        "url": raw_document["url"],
                    }
                )

    def embed(self) -> None:
        """
        Embeds the document chunks using the Cohere API.
        """
        print("Embedding document chunks...")

        batch_size = 90
        self.docs_len = len(self.docs)
        for i in range(0, self.docs_len, batch_size):
            batch = self.docs[i : min(i + batch_size, self.docs_len)]
            texts = [item["text"] for item in batch]
            docs_embs_batch = co.embed(
                texts=texts, model="embed-v4.0", input_type="search_document"
            ).embeddings
            self.docs_embs.extend(docs_embs_batch)

    def index(self) -> None:
        """
        Indexes the documents for efficient retrieval.
        """
        print("Indexing documents...")

        index_name = 'rag-01'

        # If the index does not exist, we create it
        if index_name not in pc.list_indexes().names():
            pc.create_index(
                name=index_name,
                dimension=len(self.docs_embs[0]),
                metric="cosine",
                spec=PodSpec(
                    environment="gcp-starter"
                )
                )

        # connect to index
        self.idx = pc.Index(index_name)

        batch_size = 128

        ids = [str(i) for i in range(len(self.docs))]
        # create list of metadata dictionaries
        meta = self.docs

        # create list of (id, vector, metadata) tuples to be upserted
        to_upsert = list(zip(ids, self.docs_embs, meta))

        for i in range(0, len(self.docs), batch_size):
            i_end = min(i+batch_size, len(self.docs))
            self.idx.upsert(vectors=to_upsert[i:i_end])

        # let's view the index statistics
        print("Indexing complete")


    def retrieve(self, query: str) -> List[Dict[str, str]]:
        """
        Retrieves document chunks based on the given query.

        Parameters:
        query (str): The query to retrieve document chunks for.

        Returns:
        List[Dict[str, str]]: A list of dictionaries representing the retrieved document chunks, with 'title', 'text', and 'url' keys.
        """

        docs_retrieved = []
        query_emb = co.embed(
            texts=[query], model="embed-v4.0", input_type="search_query"
        ).embeddings


        res = self.idx.query(vector=query_emb, top_k=self.retrieve_top_k, include_metadata=True)
        docs_to_rerank = [match['metadata']['text'] for match in res['matches']]

        rerank_results = co.rerank(
            query=query,
            documents=docs_to_rerank,
            top_n=self.rerank_top_k,
            model="rerank-english-v2.0",
        )

        docs_reranked = [res['matches'][result.index] for result in rerank_results.results]

        for doc in docs_reranked:
            docs_retrieved.append(doc['metadata'])

        return docs_retrieved
```

In the code cell below, we initialize an instance of the `Vectorstore` class and pass in the `raw_documents` list as input.

```python PYTHON
vectorstore = Vectorstore(raw_documents)
```

```
Loading documents...
Embedding document chunks...
Indexing documents...
Indexing complete
```

The `Vectorstore` class also has a `retrieve()` method, which we'll use to retrieve relevant document chunks given a query (as in Step 3 in the diagram shared at the beginning of this notebook). This method has two components: (1) dense retrieval, and (2) reranking.

### Dense retrieval

First, we embed the query using the same `embed-v4.0` model we used to embed the document chunks, but this time we set `input_type="search_query"`.

Search is performed by the `knn_query()` method from the `hnswlib` library. Given a query, it returns the document chunks most similar to the query. We can define the number of document chunks to return using the attribute `self.retrieve_top_k=10`.

### Reranking

After semantic search, we implement a reranking step. While our semantic search component is already highly capable of retrieving relevant sources, the [Rerank endpoint](https://cohere.com/rerank) provides an additional boost to the quality of the search results, especially for complex and domain-specific queries. It takes the search results and sorts them according to their relevance to the query.

We call the Rerank endpoint with the `co.rerank()` method and define the number of top reranked document chunks to retrieve using the attribute `self.rerank_top_k=3`. The model we use is `rerank-english-v2.0`.

This method returns the top retrieved document chunks `chunks_retrieved` so that they can be passed to the chatbot.

In the code cell below, we check the document chunks that are retrieved for the query `"multi-head attention definition"`.

## Test Retrieval

```python PYTHON
vectorstore.retrieve("multi-head attention definition")
```

```
[{'text': 'The attention step used in transformer models is actually much more powerful, and it’s called multi-head attention. In multi-head attention, several different embeddings are used to modify the vectors and add context to them. Multi-head attention has helped language models reach much higher levels of efficacy when processing and generating text.',
  'title': 'Transformer Models',
  'url': 'https://docs.cohere.com/docs/transformer-models'},
 {'text': "What you learned in this chapter is simple self-attention. However, we can do much better than that. There is a method called multi-head attention, in which one doesn't only consider one embedding, but several different ones. These are all obtained from the original by transforming it in different ways. Multi-head attention has been very successful at the task of adding context to text. If you'd like to learn more about the self and multi-head attention, you can check out the following two",
  'title': 'The Attention Mechanism',
  'url': 'https://docs.cohere.com/docs/the-attention-mechanism'},
 {'text': 'Attention helps give context to each word, based on the other words in the sentence (or text).',
  'title': 'Transformer Models',
  'url': 'https://docs.cohere.com/docs/transformer-models'}]
```

Next, we implement a class to handle the interaction between the user and the chatbot. It takes an instance of the `Vectorstore` class as input.

The `run()` method will be used to run the chatbot application. It begins with the logic for getting the user message, along with a way for the user to end the conversation.

Based on the user message, the chatbot needs to decide if it needs to consult external information before responding. If so, the chatbot determines an optimal set of search queries to use for retrieval. When we call `co.chat()` with `search_queries_only=True`, the Chat endpoint handles this for us automatically.

The generated queries can be accessed from the `search_queries` field of the object that is returned. Then, what happens next depends on how many queries are returned.

* If queries are returned, we call the `retrieve()` method of the Vectorstore object for the retrieval step. The retrieved document chunks are then passed to the Chat endpoint by adding a `documents` parameter when we call `co.chat()` again.
* Otherwise, if no queries are returned, we call the Chat endpoint another time, passing the user message and without needing to add any documents to the call.

In either case, we also pass the `conversation_id` parameter, which retains the interactions between the user and the chatbot in the same conversation thread. We also enable the `stream` parameter so we can stream the chatbot response.

We then print the chatbot's response. In the case that the external information was used to generate a response, we also display citations.

```python PYTHON
class Chatbot:
    def __init__(self, vectorstore: Vectorstore):
        """
        Initializes an instance of the Chatbot class.

        Parameters:
        vectorstore (Vectorstore): An instance of the Vectorstore class.

        """
        self.vectorstore = vectorstore
        self.conversation_id = str(uuid.uuid4())

    def run(self):
        """
        Runs the chatbot application.

        """
        while True:
            # Get the user message
            message = input("User: ")

            # Typing "quit" ends the conversation
            if message.lower() == "quit":
              print("Ending chat.")
              break
            # else:                       # Uncomment for Google Colab to avoid printing the same thing twice
              # print(f"User: {message}") # Uncomment for Google Colab to avoid printing the same thing twice

            # Generate search queries (if any)
            response = co.chat(message=message,
                               model="command-r",
                               search_queries_only=True)

            # If there are search queries, retrieve document chunks and respond
            if response.search_queries:
                print("Retrieving information...", end="")

                # Retrieve document chunks for each query
                documents = []
                for query in response.search_queries:
                    documents.extend(self.vectorstore.retrieve(query.text))

                # Use document chunks to respond
                response = co.chat_stream(
                    message=message,
                    model="command-r",
                    documents=documents,
                    conversation_id=self.conversation_id,
                )

            # If there is no search query, directly respond
            else:
                response = co.chat_stream(
                    message=message,
                    model="command-r",
                    conversation_id=self.conversation_id,
                )

            # Print the chatbot response, citations, and documents
            print("\nChatbot:")
            citations = []
            cited_documents = []

            # Display response
            for event in response:
                if event.event_type == "text-generation":
                    print(event.text, end="")
                elif event.event_type == "citation-generation":
                    citations.extend(event.citations)
                elif event.event_type == "search-results":
                    cited_documents = event.documents

            # Display citations and source documents
            if citations:
              print("\n\nCITATIONS:")
              for citation in citations:
                print(citation)

              print("\nDOCUMENTS:")
              for document in cited_documents:
                print(document)

            print(f"\n{'-'*100}\n")
```

We can now run the chatbot. For this, we create the instance of `Chatbot` and run the chatbot by invoking the `run()` method.

The format of each citation is:

* `start`: The starting point of a span where one or more documents are referenced
* `end`: The ending point of a span where one or more documents are referenced
* `text`: The text representing this span
* `document_ids`: The IDs of the documents being referenced (`doc_0` being the ID of the first document passed to the `documents` creating parameter in the endpoint call, and so on)

```python PYTHON
chatbot = Chatbot(vectorstore)

chatbot.run()
```

```
Chatbot:
Hello! What's your question? I'm here to help you in any way I can.
----------------------------------------------------------------------------------------------------

Retrieving information...
Chatbot:
Word embeddings associate words with lists of numbers, so that similar words are close to each other and dissimilar words are further away.
Sentence embeddings do the same thing, but for sentences. Each sentence is associated with a vector of numbers in a coherent way, so that similar sentences are assigned similar vectors, and different sentences are given different vectors.

CITATIONS:
start=0 end=15 text='Word embeddings' document_ids=['doc_0']
start=16 end=53 text='associate words with lists of numbers' document_ids=['doc_0']
start=63 end=100 text='similar words are close to each other' document_ids=['doc_0']
start=105 end=139 text='dissimilar words are further away.' document_ids=['doc_0']
start=140 end=159 text='Sentence embeddings' document_ids=['doc_0', 'doc_2']
start=160 end=177 text='do the same thing' document_ids=['doc_0', 'doc_2']
start=198 end=211 text='Each sentence' document_ids=['doc_0', 'doc_2']
start=215 end=250 text='associated with a vector of numbers' document_ids=['doc_0', 'doc_2']
start=256 end=264 text='coherent' document_ids=['doc_2']
start=278 end=295 text='similar sentences' document_ids=['doc_0', 'doc_2']
start=300 end=324 text='assigned similar vectors' document_ids=['doc_0', 'doc_2']
start=330 end=349 text='different sentences' document_ids=['doc_0', 'doc_2']
start=354 end=378 text='given different vectors.' document_ids=['doc_0', 'doc_2']

DOCUMENTS:
{'id': 'doc_0', 'text': 'In the previous chapters, you learned about word and sentence embeddings and similarity between words and sentences. In short, a word embedding is a way to associate words with lists of numbers (vectors) in such a way that similar words are associated with numbers that are close by, and dissimilar words with numbers that are far away from each other. A sentence embedding does the same thing, but associating a vector to every sentence. Similarity is a way to measure how similar two words (or', 'title': 'The Attention Mechanism', 'url': 'https://docs.cohere.com/docs/the-attention-mechanism'}
{'id': 'doc_1', 'text': 'Sentence embeddings\n\nSo word embeddings seem to be pretty useful, but in reality, human language is much more complicated than simply a bunch of words put together. Human language has structure, sentences, etc. How would one be able to represent, for instance, a sentence? Well, here’s an idea. How about the sums of scores of all the words? For example, say we have a word embedding that assigns the following scores to these words:\n\nNo: [1,0,0,0]\n\nI: [0,2,0,0]\n\nAm: [-1,0,1,0]\n\nGood: [0,0,1,3]', 'title': 'Text Embeddings', 'url': 'https://docs.cohere.com/docs/text-embeddings'}
{'id': 'doc_2', 'text': 'This is where sentence embeddings come into play. A sentence embedding is just like a word embedding, except it associates every sentence with a vector full of numbers, in a coherent way. By coherent, I mean that it satisfies similar properties as a word embedding. For instance, similar sentences are assigned to similar vectors, different sentences are assigned to different vectors, and most importantly, each of the coordinates of the vector identifies some (whether clear or obscure) property of', 'title': 'Text Embeddings', 'url': 'https://docs.cohere.com/docs/text-embeddings'}

----------------------------------------------------------------------------------------------------

Retrieving information...
Chatbot:
The similarities between words and sentences are both quantitative measures of how close the two given items are. There are two types of similarities that can be defined: dot product similarity, and cosine similarity. These methods can determine how similar two words, or sentences, are.

CITATIONS:
start=54 end=75 text='quantitative measures' document_ids=['doc_0']
start=79 end=88 text='how close' document_ids=['doc_0']
start=124 end=133 text='two types' document_ids=['doc_0', 'doc_4']
start=171 end=193 text='dot product similarity' document_ids=['doc_0', 'doc_4']
start=199 end=217 text='cosine similarity.' document_ids=['doc_0', 'doc_4']
start=236 end=257 text='determine how similar' document_ids=['doc_0', 'doc_4']

DOCUMENTS:
{'id': 'doc_0', 'text': 'Now that we know embeddings quite well, let’s move on to using them to find similarities. There are two types of similarities we’ll define in this post: dot product similarity and cosine similarity. Both are very similar and very useful to determine if two words (or sentences) are similar.', 'title': 'Similarity Between Words and Sentences', 'url': 'https://docs.cohere.com/docs/similarity-between-words-and-sentences'}
{'id': 'doc_1', 'text': 'But let me add some numbers to this reasoning to make it more clear. Imagine that we calculate similarities for the words in each sentence, and we get the following:\n\nThis similarity makes sense in the following ways:\n\nThe similarity between each word and itself is 1.\n\nThe similarity between any irrelevant word (“the”, “of”, etc.) and any other word is 0.\n\nThe similarity between “bank” and “river” is 0.11.\n\nThe similarity between “bank” and “money” is 0.25.', 'title': 'The Attention Mechanism', 'url': 'https://docs.cohere.com/docs/the-attention-mechanism'}
{'id': 'doc_2', 'text': 'And the results are:\n\nThe similarity between sentences 1 and 2: 6738.2858668486715\n\nThe similarity between sentences 1 and 3: -122.22666955510499\n\nThe similarity between sentences 2 and 3: -3.494608113647928\n\nThese results certainly confirm our predictions. The similarity between sentences 1 and 2 is 6738, which is high. The similarities between sentences 1 and 3, and 2 and 3, are -122 and -3.5 (dot products are allowed to be negative too!), which are much lower.', 'title': 'Similarity Between Words and Sentences', 'url': 'https://docs.cohere.com/docs/similarity-between-words-and-sentences'}
{'id': 'doc_3', 'text': 'But let me add some numbers to this reasoning to make it more clear. Imagine that we calculate similarities for the words in each sentence, and we get the following:\n\nThis similarity makes sense in the following ways:\n\nThe similarity between each word and itself is 1.\n\nThe similarity between any irrelevant word (“the”, “of”, etc.) and any other word is 0.\n\nThe similarity between “bank” and “river” is 0.11.\n\nThe similarity between “bank” and “money” is 0.25.', 'title': 'The Attention Mechanism', 'url': 'https://docs.cohere.com/docs/the-attention-mechanism'}
{'id': 'doc_4', 'text': 'Now that we know embeddings quite well, let’s move on to using them to find similarities. There are two types of similarities we’ll define in this post: dot product similarity and cosine similarity. Both are very similar and very useful to determine if two words (or sentences) are similar.', 'title': 'Similarity Between Words and Sentences', 'url': 'https://docs.cohere.com/docs/similarity-between-words-and-sentences'}
{'id': 'doc_5', 'text': 'And the results are:\n\nThe similarity between sentences 1 and 2: 6738.2858668486715\n\nThe similarity between sentences 1 and 3: -122.22666955510499\n\nThe similarity between sentences 2 and 3: -3.494608113647928\n\nThese results certainly confirm our predictions. The similarity between sentences 1 and 2 is 6738, which is high. The similarities between sentences 1 and 3, and 2 and 3, are -122 and -3.5 (dot products are allowed to be negative too!), which are much lower.', 'title': 'Similarity Between Words and Sentences', 'url': 'https://docs.cohere.com/docs/similarity-between-words-and-sentences'}

----------------------------------------------------------------------------------------------------

Ending chat.
```


# Learn How Cohere's Rerank Models Work

> This page contains a basic tutorial on how Cohere's ReRank models work and how to use them.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/rerank-demo.ipynb" />

In the past months, we engineered a novel relevance endpoint that takes a query and a list of documents and predicts the relevance between the query and each document.

It can be used in a two-stage retrieval setup: First you take the user question, and retrieve the top-100 documents from your collection by either using lexical search or semantic search.

You then pass the question and these top-100 documents to our relevance-endpoint to get a score for each document. You can then rank these documents based on these scores.

In our benchmarks across 20 datasets, we **saw significant improvements compared to lexical and semantic search**, especially for use-cases where no training data is available.

We will demonstrate the rerank endpoint in this notebook.

```python PYTHON
!pip install "cohere<5"
```

```txt title="Output"
[33mDEPRECATION: Configuring installation scheme with distutils config files is deprecated and will no longer work in the near future. If you are using a Homebrew or Linuxbrew Python, please see discussion at https://github.com/Homebrew/homebrew-core/issues/76621[0m[33m
[0mRequirement already satisfied: cohere<5 in /opt/homebrew/lib/python3.9/site-packages (4.45)
Requirement already satisfied: aiohttp<4.0,>=3.0 in /opt/homebrew/lib/python3.9/site-packages (from cohere<5) (3.8.1)
Requirement already satisfied: backoff<3.0,>=2.0 in /opt/homebrew/lib/python3.9/site-packages (from cohere<5) (2.2.1)
Requirement already satisfied: fastavro<2.0,>=1.8 in /opt/homebrew/lib/python3.9/site-packages (from cohere<5) (1.9.3)
Requirement already satisfied: importlib_metadata<7.0,>=6.0 in /opt/homebrew/lib/python3.9/site-packages (from cohere<5) (6.6.0)
Requirement already satisfied: requests<3.0.0,>=2.25.0 in /Users/elliottchoi/Library/Python/3.9/lib/python/site-packages (from cohere<5) (2.28.2)
Requirement already satisfied: urllib3<3,>=1.26 in /Users/elliottchoi/Library/Python/3.9/lib/python/site-packages (from cohere<5) (1.26.14)
Requirement already satisfied: attrs>=17.3.0 in /opt/homebrew/lib/python3.9/site-packages (from aiohttp<4.0,>=3.0->cohere<5) (22.1.0)
Requirement already satisfied: charset-normalizer<3.0,>=2.0 in /opt/homebrew/lib/python3.9/site-packages (from aiohttp<4.0,>=3.0->cohere<5) (2.0.12)
Requirement already satisfied: multidict<7.0,>=4.5 in /opt/homebrew/lib/python3.9/site-packages (from aiohttp<4.0,>=3.0->cohere<5) (6.0.2)
Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /opt/homebrew/lib/python3.9/site-packages (from aiohttp<4.0,>=3.0->cohere<5) (4.0.2)
Requirement already satisfied: yarl<2.0,>=1.0 in /opt/homebrew/lib/python3.9/site-packages (from aiohttp<4.0,>=3.0->cohere<5) (1.8.1)
Requirement already satisfied: frozenlist>=1.1.1 in /opt/homebrew/lib/python3.9/site-packages (from aiohttp<4.0,>=3.0->cohere<5) (1.3.1)
Requirement already satisfied: aiosignal>=1.1.2 in /opt/homebrew/lib/python3.9/site-packages (from aiohttp<4.0,>=3.0->cohere<5) (1.2.0)
Requirement already satisfied: zipp>=0.5 in /opt/homebrew/lib/python3.9/site-packages (from importlib_metadata<7.0,>=6.0->cohere<5) (3.15.0)
Requirement already satisfied: idna<4,>=2.5 in /Users/elliottchoi/Library/Python/3.9/lib/python/site-packages (from requests<3.0.0,>=2.25.0->cohere<5) (3.4)
Requirement already satisfied: certifi>=2017.4.17 in /Users/elliottchoi/Library/Python/3.9/lib/python/site-packages (from requests<3.0.0,>=2.25.0->cohere<5) (2022.12.7)
[33mDEPRECATION: Configuring installation scheme with distutils config files is deprecated and will no longer work in the near future. If you are using a Homebrew or Linuxbrew Python, please see discussion at https://github.com/Homebrew/homebrew-core/issues/76621[0m[33m
[0m
```

```python PYTHON
import cohere
import requests
import numpy as np
from time import time
from typing import List
from pprint import pprint
```

```python PYTHON
API_KEY = "<insert api="" key="" your="">"
co = cohere.Client(API_KEY)
MODEL_NAME = "rerank-english-v3.0" # another option is rerank-multilingual-02

query = "What is the capital of the United States?"
docs = [
    "Carson City is the capital city of the American state of Nevada. At the 2010 United States Census, Carson City had a population of 55,274.",
    "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean that are a political division controlled by the United States. Its capital is Saipan.",
    "Charlotte Amalie is the capital and largest city of the United States Virgin Islands. It has about 20,000 people. The city is on the island of Saint Thomas.",
    "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district. The President of the USA and many major national government offices are in the territory. This makes it the political center of the United States of America.",
    "West Virginia is a state in the Appalachian region of the United States. Its capital and largest city is Charleston. It is often abbreviated W. Va. or simply WV.",
    "Capital punishment has existed in the United States since before the United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states. The federal government (including the United States military) also uses capital punishment.",
    "North Dakota is a state in the United States. 672,591 people lived in North Dakota in the year 2010. The capital and seat of government is Bismarck.",
    "Kentucky is a state in the United States. Its capital is Frankfort. It touches the states of Missouri (by the Mississippi River), Illinois, Indiana, Ohio, West Virginia (by the Ohio River), Tennessee and Virginia. There are many rivers in Kentucky",
    "Micronesia, officially the Federated States of Micronesia, is an island nation in the Pacific Ocean, northeast of Papua New Guinea. The country is a sovereign state in free association with the United States. The capital city of Federated States of Micronesia is Palikir.",
    "Utah is a state in the west United States. The capital and largest city is Salt Lake City. Utah became a state in the U.S. on January 4, 1896."]
```

## Using the Endpoint

In the following cell we will call rerank to rank `docs` based on how relevant they are with `query`.

```python PYTHON
results = co.rerank(query=query, model=MODEL_NAME, documents=docs, top_n=3) # Change top_n to change the number of results returned. If top_n is not passed, all results will be returned.
for idx, r in enumerate(results):
  print(f"Document Rank: {idx + 1}, Document Index: {r.index}")
  print(f"Document: {r.document['text']}")
  print(f"Relevance Score: {r.relevance_score:.2f}")
  print("\n")
```

```txt title="Output"
Document Rank: 1, Document Index: 3
Document: Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district. The President of the USA and many major national government offices are in the territory. This makes it the political center of the United States of America.
Relevance Score: 1.00


Document Rank: 2, Document Index: 5
Document: Capital punishment has existed in the United States since before the United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states. The federal government (including the United States military) also uses capital punishment.
Relevance Score: 0.75


Document Rank: 3, Document Index: 1
Document: The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean that are a political division controlled by the United States. Its capital is Saipan.
Relevance Score: 0.09
```

## Search on Wikipedia - End2end demo

The following is an example how to use this model end-to-end to search over the Simple English Wikipedia, which consists of about 500k passages.

We use BM25 lexical search to retrieve the top-100 passages matching the query and then send these 100 passages and the query to our rerank endpoint to get a re-ranked list. We output the top-3 hits according to BM25 lexical search (as used by e.g. Elasticsearch) and the re-ranked list from our endpoint.

```python PYTHON
!pip install -U  rank_bm25
```

```txt title="Output"
[33mDEPRECATION: Configuring installation scheme with distutils config files is deprecated and will no longer work in the near future. If you are using a Homebrew or Linuxbrew Python, please see discussion at https://github.com/Homebrew/homebrew-core/issues/76621[0m[33m
[0mCollecting rank_bm25
    Downloading rank_bm25-0.2.2-py3-none-any.whl.metadata (3.2 kB)
Requirement already satisfied: numpy in /opt/homebrew/lib/python3.9/site-packages (from rank_bm25) (1.23.5)
Downloading rank_bm25-0.2.2-py3-none-any.whl (8.6 kB)
Installing collected packages: rank_bm25
[33m  DEPRECATION: Configuring installation scheme with distutils config files is deprecated and will no longer work in the near future. If you are using a Homebrew or Linuxbrew Python, please see discussion at https://github.com/Homebrew/homebrew-core/issues/76621[0m[33m
[0m[33mDEPRECATION: Configuring installation scheme with distutils config files is deprecated and will no longer work in the near future. If you are using a Homebrew or Linuxbrew Python, please see discussion at https://github.com/Homebrew/homebrew-core/issues/76621[0m[33m
[0mSuccessfully installed rank_bm25-0.2.2
```

```python PYTHON
import json
import gzip
import os
from rank_bm25 import BM25Okapi
from sklearn.feature_extraction import _stop_words
import string
from tqdm.autonotebook import tqdm
```

```txt title="Output"
/var/folders/ww/ht8qwj2s7s799qnktblg6qhm0000gp/T/ipykernel_31832/1066443236.py:7: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html
    from tqdm.autonotebook import tqdm
```

```python PYTHON
!wget http://sbert.net/datasets/simplewiki-2020-11-01.jsonl.gz
```

```txt title="Output"
--2024-04-08 14:28:00--  http://sbert.net/datasets/simplewiki-2020-11-01.jsonl.gz
Resolving sbert.net (sbert.net)... 172.64.80.1, 2606:4700:130:436c:6f75:6466:6c61:7265
Connecting to sbert.net (sbert.net)|172.64.80.1|:80... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://sbert.net/datasets/simplewiki-2020-11-01.jsonl.gz [following]
--2024-04-08 14:28:01--  https://sbert.net/datasets/simplewiki-2020-11-01.jsonl.gz
Connecting to sbert.net (sbert.net)|172.64.80.1|:443... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://public.ukp.informatik.tu-darmstadt.de/reimers/sentence-transformers/datasets/simplewiki-2020-11-01.jsonl.gz [following]
--2024-04-08 14:28:01--  https://public.ukp.informatik.tu-darmstadt.de/reimers/sentence-transformers/datasets/simplewiki-2020-11-01.jsonl.gz
Resolving public.ukp.informatik.tu-darmstadt.de (public.ukp.informatik.tu-darmstadt.de)... 130.83.167.186
Connecting to public.ukp.informatik.tu-darmstadt.de (public.ukp.informatik.tu-darmstadt.de)|130.83.167.186|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 50223724 (48M) [application/octet-stream]
Saving to: ‘simplewiki-2020-11-01.jsonl.gz’

simplewiki-2020-11- 100%[===================>]  47.90M  5.78MB/s    in 8.9s

2024-04-08 14:28:11 (5.37 MB/s) - ‘simplewiki-2020-11-01.jsonl.gz’ saved [50223724/50223724]
```

```python PYTHON
wikipedia_filepath = 'simplewiki-2020-11-01.jsonl.gz'

passages = []
with gzip.open(wikipedia_filepath, 'rt', encoding='utf8') as fIn:
    for line in fIn:
        data = json.loads(line.strip())
        passages.extend(data['paragraphs'])

print("Passages:", len(passages))
```

```txt title="Output"
Passages: 509663
```

```python PYTHON
print(passages[0], passages[1])
```

Ted Cassidy (July 31, 1932 - January 16, 1979) was an American actor. He was best known for his roles as Lurch and Thing on "The Addams Family". Aileen Carol Wuornos Pralle (born Aileen Carol Pittman; February 29, 1956 – October 9, 2002) was an American serial killer. She was born in Rochester, Michigan. She confessed to killing six men in Florida and was executed in Florida State Prison by lethal injection for the murders. Wuornos said that the men she killed had raped her or tried to rape her while she was working as a prostitute.

```python PYTHON

def bm25_tokenizer(text):
    tokenized_doc = []
    for token in text.lower().split():
        token = token.strip(string.punctuation)

        if len(token) > 0 and token not in _stop_words.ENGLISH_STOP_WORDS:
            tokenized_doc.append(token)
    return tokenized_doc


tokenized_corpus = []
for passage in tqdm(passages):
    tokenized_corpus.append(bm25_tokenizer(passage))

bm25 = BM25Okapi(tokenized_corpus)
```

```
100%|██████████| 509663/509663 [00:09<00:00, 51180.82it/s]
```

```python PYTHON

def search(query, top_k=3, num_candidates=100):
    print("Input question:", query)

    ##### BM25 search (lexical search) #####
    bm25_scores = bm25.get_scores(bm25_tokenizer(query))
    top_n = np.argpartition(bm25_scores, -num_candidates)[-num_candidates:]
    bm25_hits = [{'corpus_id': idx, 'score': bm25_scores[idx]} for idx in top_n]
    bm25_hits = sorted(bm25_hits, key=lambda x: x['score'], reverse=True)

    print(f"Top-3 lexical search (BM25) hits")
    for hit in bm25_hits[0:top_k]:
        print("\t{:.3f}\t{}".format(hit['score'], passages[hit['corpus_id']].replace("\n", " ")))


    #Add re-ranking
    docs = [passages[hit['corpus_id']] for hit in bm25_hits]

    print(f"\nTop-3 hits by rank-API ({len(bm25_hits)} BM25 hits re-ranked)")
    results = co.rerank(query=query, model=MODEL_NAME, documents=docs, top_n=top_k)
    for hit in results:
        print("\t{:.3f}\t{}".format(hit.relevance_score, hit.document["text"].replace("\n", " ")))
```

```python PYTHON
search(query = "What is the capital of the United States?")
```

```txt title="Output"
Input question: What is the capital of the United States?
Top-3 lexical search (BM25) hits
    16.264	Capital punishment has existed in the United States since before the United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states. The federal government (including the United States military) also uses capital punishment.
    15.124	In 1783, it was the capital of the United States for a few months.
    14.476	New York was the capital of the United States under the Articles of Confederation from 1785 to 1788. When the US Constitution was made, it stayed as the capital from 1789 until 1790. In 1789, the first President of the United States, George Washington, was inaugurated; the first United States Congress and the Supreme Court of the United States each met for the first time, and the United States Bill of Rights was written, all at Federal Hall on Wall Street. By 1790, New York grew bigger than Philadelphia, so it become the biggest city in the United States. By the end of 1790, because of the Residence Act, Philadelphia became the new capital.

Top-3 hits by rank-API (100 BM25 hits re-ranked)
    0.999	Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district. The President of the USA and many major national government offices are in the territory. This makes it the political center of the United States of America.
    0.994	New York was the capital of the United States under the Articles of Confederation from 1785 to 1788. When the US Constitution was made, it stayed as the capital from 1789 until 1790. In 1789, the first President of the United States, George Washington, was inaugurated; the first United States Congress and the Supreme Court of the United States each met for the first time, and the United States Bill of Rights was written, all at Federal Hall on Wall Street. By 1790, New York grew bigger than Philadelphia, so it become the biggest city in the United States. By the end of 1790, because of the Residence Act, Philadelphia became the new capital.
    0.993	As the national capital of the United States, Washington, D.C. has numerous media outlets in various mediums. Some of these media are known throughout the United States, including "The Washington Post" and various broadcasting networks headquartered in D.C.
```

```python PYTHON
search(query = "Number countries Europe")
```

```txt title="Output"
Input question: Number countries Europe
Top-3 lexical search (BM25) hits
    16.963	ECoHR' has a number of judges. The number of judges is seven normally but at the case of dealing a great issue, the number will be 21 and the judges are equally from member countries of the Council of Europe. At present, there are forty seven member countries of the Council of Europe. Each country may have one judge in the ECoHR. But, judges work independently for the ECoHR, and not for their country.
    14.560	Most countries in Europe, and a few countries in Asia, have made some or all synthetic cannabinoids illegal.
    14.165	Many of these countries were members of the Western European Union. Many, such as Norway, are also in Northern Europe or in Central Europe or Southern Europe.

Top-3 hits by rank-API (100 BM25 hits re-ranked)
    0.997	There are at least 43 countries in Europe (the European identities of 5 transcontinental countries:Cyprus, Georgia, Kazakhstan, Russia and Turkey are disputed). Most of these countries are members of the European Union.
    0.987	Within these regions, there are up to 48 independent European countries (with the identities of 5 transcontinental countries being disputed). The largest is the Russian Federation, which covers 39% of Europe.
    0.981	Europe, the planet's 6th largest continent, includes 47 countries and assorted dependencies, islands and territories.
```

```python PYTHON
search(query = "Elon Musk year birth")
```

```txt title="Output"
Input question: Elon Musk year birth
Top-3 lexical search (BM25) hits
    22.568	Tesla, Inc. is a company based in Palo Alto, California which makes electric cars. It was started in 2003 by Martin Eberhard, Dylan Stott, and Elon Musk (who also co-founded PayPal and SpaceX and is the CEO of SpaceX). Eberhard no longer works there. Today, Elon Musk is the Chief Executive Officer (CEO). It started selling its first car, the Roadster in 2008.
    20.492	Elon Musk complained via Twitter about Los Angeles traffic and the same day, December 17, 2016, founded the company. It built a short test tunnel in Los Angeles.
    20.448	At the end of 2016, Musk founded The Boring Company which focuses on tunnelling and infrastructure. He mentioned Los Angeles traffic as the reason for starting this company. In March 2017 Elon Musk announced he has started another company which aims to merge human brains and computers, it is called Neuralink.

Top-3 hits by rank-API (100 BM25 hits re-ranked)
    0.994	Elon Reeve Musk (born June 28, 1971) is a businessman and philanthropist. He was born in South Africa. He moved to Canada and later became an American citizen. Musk is the current CEO &amp; Chief Product Architect of Tesla Motors, a company that makes electric vehicles. He is also the CEO of Solar City, a company that makes solar panels, and the CEO &amp; CTO of SpaceX, an aerospace company. In August 2020, Bloomberg ranked Musk third among the richest people on the planet with net worth to be $115.4 billion.
    0.602	Elon Musk and his brother started Zip2, a software company, in 1995. In 1999 he sold it and became a millionaire. He then started X.com, which merged with the company to make PayPal. X.com was then renamed to PayPal, and he focused on growing that part of the company. He then started SpaceX and became the CEO of Tesla.
    0.474	In early 2002, Musk was seeking workers for his new space company, soon to be named SpaceX. Musk found a rocket engineer Tom Mueller (later SpaceX's CTO of Propulsion). He agreed to work for Musk. That was how SpaceX was born. The first headquarters of SpaceX was in a warehouse in El Segundo, California. The company has grown rapidly since it was founded in 2002, growing from 160 workers in November 2005 to 1,100 in 2010, 3,800 workers and contractors by October 2013, nearly 5,000 by late 2015, and about 6,000 in April 2017.
```

```python PYTHON
search(query = "Which US president was killed?")
```

```txt title="Output"
Input question: Which US president was killed?
Top-3 lexical search (BM25) hits
    11.966	He came into office when the previous president, Cyprien Ntaryamira, was killed in a plane crash. It was an assassination in which the Rwandan president Juvénal Habyarimana was also killed. Ntibantunganya left office when he was deposed by Pierre Buyoya in a military coup of 1996.
    11.697	Burr killed Alexander Hamilton in a duel in 1804, when Burr was still Vice President.
    11.482	After President James A. Garfield died, vice-president Chester Arthur replaced him. The man who killed him expected the new President to pardon him. This did not happen.

Top-3 hits by rank-API (100 BM25 hits re-ranked)
    0.984	James Abram Garfield (November 19, 1831 - September 19, 1881) was the 20th (1881) President of the United States and the 2nd President to be assassinated (killed while in office). President Garfield was in office from March to September of 1881. He was in office for a total of six months and fifteen days. For almost half that time he was bedridden as a result of an attempt to kill him. He was shot on July 2 and finally died in September the same year he got into office.
    0.976	President William McKinley was killed by anarchist Leon Czolgosz because Czolgosz believed president McKinley was against good working people, he considered McKinley responsible for falsifying the reasons for the war, and approving and waging an illegal, devastating Philippines war.
    0.916	On the night that President Abraham Lincoln was killed, someone also tried to kill Seward. For the rest of his life, Seward had scars on his face from the attack. Later, the man who attacked him was caught and put to death.
```

```python PYTHON
search(query="When is Chinese New Year")
```

```txt title="Output"
Input question: When is Chinese New Year
Top-3 lexical search (BM25) hits
    18.606	Today in China the Gregorian calendar is used for most activities. At the same time, the Chinese calendar is still used for traditional Chinese holidays like Chinese New Year or Lunar New Year.
    18.151	Before that, the holiday was usually just called the "NewYear". Because the traditional Chinese calendar is mostly based on the changes in the moon, the Chinese New Year is also known in English as the "Lunar New Year" or "Chinese Lunar New Year". This name comes from "Luna", an old Latin name for the moon. The Indonesian name for the holiday is Imlek, which comes from the Hokkien word for the old Chinese calendar and is therefore also like saying "Lunar New Year".
    18.011	Spring Festival is the Chinese New Year.

Top-3 hits by rank-API (100 BM25 hits re-ranked)
    0.999	Chinese New Year, known in China as the SpringFestival and in Singapore as the LunarNewYear, is a holiday on and around the new moon on the first day of the year in the traditional Chinese calendar. This calendar is based on the changes in the moon and is only sometimes changed to fit the seasons of the year based on how the Earth moves around the sun. Because of this, Chinese New Year is never on January1. It moves around between January21 and February20.
    0.997	Chinese New Year always starts on a new moon, when the Moon is between the Earth and Sun and it looks all dark in the night sky. Because new moons happen about every 29.53 days but the year set by Pope GregoryXIII is 365.2425 days long, the Chinese holiday moves to different days each year. The Chinese calendar adds a 13th month every so often to keep the seasons in the right place, so the first day of the new year always happens between January21 and February20 on the 2nd or 3rd new moon after the 1st day of winter. The chart on the right gives the day of each Chinese New Year from 1996 to 2031.
    0.996	Chinese New Year lasts fifteen days, including one week as a national holiday. It starts with the first day of the Chinese lunar year and ends with the full moon fifteen days later. It is always in the middle of winter, but is called the Spring Festival in Chinese because Chinese seasons are a little different from English ones. On the first day of the Chinese New Year, people call on friends and relatives. Because most people watch the special performances on CCTV all the night on New Year's Eve and don't go to bed until 12:00 AM, they usually get up later in the next day. The fifth day of the Chinese New Year is the day to welcome the god of Wealth (Chinese:财神爷), many people make and eat dumplings (Chinese:饺子. Pinyin: Jaozi). They believe that dumplings can hold the god of Wealth and bring luck. The last day of the Chinese New Year is the Lantern Festival. On this day, the moon becomes the full moon. People go out and watch the lantern festivals everywhere. After that, they eat sweet dumpling (Chinese:汤圆,元宵), a kind of dumpling which is round and looks like the full moon.
```

```python PYTHON
search(query="How many people live in Paris")
```

```txt title="Output"
Input question: How many people live in Paris
Top-3 lexical search (BM25) hits
    16.277	Live à Paris (English: "Live in Paris") is a live album by Canadian singer Céline Dion.
    15.173	Île-de-France is a region of France. The capital city is Paris. It is also the capital city of France. In 2013 about 12 million people lived in the region. About 2.1 million people live in the city of Paris.
    14.666	Gennevilliers is a town in France near Paris. It is in the region Île-de-France and the department of Hauts-de-Seine. About 41,000 people live there.

Top-3 hits by rank-API (100 BM25 hits re-ranked)
    0.999	Paris (nicknamed the ""City of light"") is the capital city of France, and the largest city in France. The area is , and around 2.15 million people live there. If suburbs are counted, the population of the Paris area rises to 12 million people.
    0.987	Île-de-France is a region of France. The capital city is Paris. It is also the capital city of France. In 2013 about 12 million people lived in the region. About 2.1 million people live in the city of Paris.
    0.602	Essonne is a department to the south of Paris in the Île-de-France region. Its prefecture is Évry. About 1,172,000 people live there (2006 estimation).
```

```python PYTHON
search(query="Who is the director of The Matrix?")
```

```txt title="Output"
Input question: Who is the director of The Matrix?
Top-3 lexical search (BM25) hits
    16.253	An inverse matrix is a matrix that, when multiplied by another matrix, equals the identity matrix. For example:
    16.072	is an identity matrix. There is exactly one identity matrix for each square dimension set. An identity matrix is special because when multiplying any matrix by the identity matrix, the result is always the original matrix with no change.
    15.353	First, the system needs to be turned into an augmented matrix. In an augmented matrix, each linear equation becomes a row. On one side of the augmented matrix, the coefficients of each term in the linear equation become numbers in the matrix. On the other side of the augmented matrix are the constant terms each linear equation is equal to. For this system, the augmented matrix is:

Top-3 hits by rank-API (100 BM25 hits re-ranked)
    0.995	The Matrix is a science fiction action movie that was made in 1999. It was written and directed by the Wachowski Brothers. The main actors in the movie are Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, and Hugo Weaving. "The Matrix" was followed by two sequels: "The Matrix Reloaded" and "The Matrix Revolutions".
    0.992	Helmut Bakaitis (born 26 September 1944) is a German-born Australian director, actor and screenwriter. He is known for his role as The Architect in "The Matrix" movie series. Bakaitis was born in Lauban, Lower Silesia, Germany (now Lubań, Poland). Bakaitis started teaching directing at Australian Academy of Dramatic Art (AADA).
    0.804	The Matrix Revolutions is a 2003 movie that was written and directed by the Wachowski brothers. It is the sequel to "The Matrix Reloaded".

```


# Build a SQL Agent with Cohere's LLM Platform

> This page contains a tutorial on how to build a SQL agent with Cohere's LLM platform.

<AuthorsContainer
  authors={[
    {
      name: "Shaan Desai",
      imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/d17fc44-Shaan.jpg",
    },
  ]}
/>

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/agents/sql_agent/sql_agent.ipynb" />

## Motivation

Enterprise customers often store and handle information in relational databases but querying such databases effectively requires bespoke knowledge of the underlying database structure as well as strong SQL coding skills. One way to address these challenges is to build an LLM agent capable of generating and executing SQL queries based on natural language. For example, if a user asks: `what are the top 4 rows in table X`, the agent should be able to generate `SELECT * FROM X LIMIT 4`, execute this query and return the output to the user.

## Objective

In this notebook we explore how to setup a [Cohere ReAct Agent](https://github.com/langchain-ai/langchain-cohere/blob/main/libs/cohere/langchain_cohere/cohere_agent.py) to answer questions over SQL Databases. We show how this can be done seamlessly with langchain's existing [SQLDBToolkit](https://python.langchain.com/v0.1/docs/integrations/toolkits/sql_database/).

# Toolkit Setup \[#sec\_step0]

```python PYTHON
from langchain.agents import AgentExecutor
from langchain_cohere.react_multi_hop.agent import create_cohere_react_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_cohere.chat_models import ChatCohere
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
import os
import json
```

```python PYTHON
# Uncomment if you need to install the following packages
#!pip install --quiet langchain langchain_cohere langchain_experimental --upgrade
```

Langchain already has a SQLDBToolkit that consists of 4 tools to handle SQL query generation, execution and validation. To use this, you simply need to define your LLM and DB and pass these into the Toolkit.

These are the following tools:

* 'sql\_db\_query': executes SQL code on the database
* 'sql\_db\_schema': returns the schema of tables given the list of tables
* 'sql\_db\_list\_tables': lists the tables in the database
* 'sql\_db\_query\_checker': validates the SQL query

```python PYTHON
# load the cohere api key
os.environ["COHERE_API_KEY"] = ""
```

```python PYTHON
DB_NAME='Chinook.db'
MODEL="command-a-03-2025"
llm = ChatCohere(model=MODEL, temperature=0.1,verbose=True)
db = SQLDatabase.from_uri(f"sqlite:///{DB_NAME}")
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
context = toolkit.get_context()
tools = toolkit.get_tools()

print('**List of pre-defined Langchain Tools**')
print([tool.name for tool in tools])
```

```txt title="Output"
**List of pre-defined Langchain Tools**
['sql_db_query', 'sql_db_schema', 'sql_db_list_tables', 'sql_db_query_checker']
```

# SQL Agent \[#sec\_step1]

We follow the general cohere react agent setup in Langchain to build our SQL agent.

```python PYTHON
# define the prompt template
prompt = ChatPromptTemplate.from_template("{input}")

---

**Navigation:** [← Previous](./17-credentials-file-populate-if-you-are-running-in-a-.md) | [Index](./index.md) | [Next →](./19-instantiate-the-react-agent.md)
