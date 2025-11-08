---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Initialize the Anthropic client

client = anthropic.Anthropic()

def chunk_text(text, chunk_size=20000):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def summarize_long_document(text, details_to_extract, model="claude-sonnet-4-5", max_tokens=1000):

    # Format the details to extract to be placed within the prompt's context

    details_to_extract_str = '\n'.join(details_to_extract)

    # Iterate over chunks and summarize each one

    chunk_summaries = [summarize_document(chunk, details_to_extract, model=model, max_tokens=max_tokens) for chunk in chunk_text(text)]
    
    final_summary_prompt = f"""
    
    You are looking at the chunked summaries of multiple documents that are all related. 
    Combine the following summaries of the document from different truthful sources into a coherent overall summary:

    <chunked_summaries>
    {"".join(chunk_summaries)}
    </chunked_summaries>

    Focus on these key aspects:
    {details_to_extract_str})

    Provide the summary in bullet points nested within the XML header for each section. For example:

    <parties involved>
    - Sublessor: [Name]
    // Add more details as needed
    </parties involved>
    
    If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.
    """

    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system="You are a legal expert that summarizes notes on one document.",
        messages=[
            {"role": "user",  "content": final_summary_prompt},
            {"role": "assistant", "content": "Here is the summary of the sublease agreement: <summary>"}

        ],
        stop_sequences=["</summary>"]
    )
    
    return response.content[0].text

long_summary = summarize_long_document(document_text, details_to_extract)
print(long_summary)
```
The `summarize_long_document` function builds upon the earlier `summarize_document` function by splitting the document into smaller chunks and summarizing each chunk individually.

The code achieves this by applying the `summarize_document` function to each chunk of 20,000 characters within the original document. The individual summaries are then combined, and a final summary is created from these chunk summaries.

Note that the `summarize_long_document` function isn’t strictly necessary for our example pdf, as the entire document fits within Claude’s context window. However, it becomes essential for documents exceeding Claude’s context window or when summarizing multiple related documents together. Regardless, this meta-summarization technique often captures additional important details in the final summary that were missed in the earlier single-summary approach.

### Use summary indexed documents to explore a large collection of documents

Searching a collection of documents with an LLM usually involves retrieval-augmented generation (RAG). However, in scenarios involving large documents or when precise information retrieval is crucial, a basic RAG approach may be insufficient. Summary indexed documents is an advanced RAG approach that provides a more efficient way of ranking documents for retrieval, using less context than traditional RAG methods. In this approach, you first use Claude to generate a concise summary for each document in your corpus, and then use Clade to rank the relevance of each summary to the query being asked. For further details on this approach, including a code-based example, check out the summary indexed documents section in the [summarization cookbook](https://github.com/anthropics/anthropic-cookbook/blob/main/skills/summarization/guide.ipynb).

### Fine-tune Claude to learn from your dataset

Another advanced technique to improve Claude's ability to generate summaries is fine-tuning. Fine-tuning involves training Claude on a custom dataset that specifically aligns with your legal summarization needs, ensuring that Claude adapts to your use case. Here’s an overview on how to perform fine-tuning:

1. **Identify errors:** Start by collecting instances where Claude’s summaries fall short - this could include missing critical legal details, misunderstanding context, or using inappropriate legal terminology.

2. **Curate a dataset:** Once you've identified these issues, compile a dataset of these problematic examples. This dataset should include the original legal documents alongside your corrected summaries, ensuring that Claude learns the desired behavior.

3. **Perform fine-tuning:** Fine-tuning involves retraining the model on your curated dataset to adjust its weights and parameters. This retraining helps Claude better understand the specific requirements of your legal domain, improving its ability to summarize documents according to your standards.

4. **Iterative improvement:** Fine-tuning is not a one-time process. As Claude continues to generate summaries, you can iteratively add new examples where it has underperformed, further refining its capabilities. Over time, this continuous feedback loop will result in a model that is highly specialized for your legal summarization tasks.

<Tip>Fine-tuning is currently only available via Amazon Bedrock. Additional details are available in the [AWS launch blog](https://aws.amazon.com/blogs/machine-learning/fine-tune-anthropics-claude-3-haiku-in-amazon-bedrock-to-boost-model-accuracy-and-quality/).</Tip>

<CardGroup cols={2}>
  <Card title="Summarization cookbook" icon="link" href="https://github.com/anthropics/anthropic-cookbook/blob/main/skills/summarization/guide.ipynb">
    View a fully implemented code-based example of how to use Claude to summarize contracts.
  </Card>

  <Card title="Citations cookbook" icon="link" href="https://github.com/anthropics/anthropic-cookbook/blob/main/misc/using_citations.ipynb">
    Explore our Citations cookbook recipe for guidance on how to ensure accuracy and explainability of information.
  </Card>
</CardGroup>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
