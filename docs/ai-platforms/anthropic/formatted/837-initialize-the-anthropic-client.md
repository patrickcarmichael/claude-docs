---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Initialize the Anthropic client

client = anthropic.Anthropic()

def summarize_document(text, details_to_extract, model="claude-sonnet-4-5", max_tokens=1000):

    # Format the details to extract to be placed within the prompt's context

    details_to_extract_str = '\n'.join(details_to_extract)
    
    # Prompt the model to summarize the sublease agreement

    prompt = f"""Summarize the following sublease agreement. Focus on these key aspects:

    {details_to_extract_str}

    Provide the summary in bullet points nested within the XML header for each section. For example:

    <parties involved>
    - Sublessor: [Name]
    // Add more details as needed
    </parties involved>
    
    If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.

    Sublease agreement text:
    {text}
    """

    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system="You are a legal analyst specializing in real estate law, known for highly accurate and detailed summaries of sublease agreements.",
        messages=[
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": "Here is the summary of the sublease agreement: <summary>"}
        ],
        stop_sequences=["</summary>"]
    )

    return response.content[0].text

sublease_summary = summarize_document(document_text, details_to_extract)
print(sublease_summary)
```
This code implements a `summarize_document` function that uses Claude to summarize the contents of a sublease agreement. The function accepts a text string and a list of details to extract as inputs. In this example, we call the function with the `document_text` and `details_to_extract` variables that were defined in the previous code snippets.

Within the function, a prompt is generated for Claude, including the document to be summarized, the details to extract, and specific instructions for summarizing the document. The prompt instructs Claude to respond with a summary of each detail to extract nested within XML headers.

Because we decided to output each section of the summary within tags, each section can easily be parsed out as a post-processing step. This approach enables structured summaries that can be adapted for your use case, so that each summary follows the same pattern.

### Evaluate your prompt

Prompting often requires testing and optimization for it to be production ready. To determine the readiness of your solution, evaluate the quality of your summaries using a systematic process combining quantitative and qualitative methods. Creating a [strong empirical evaluation](/en/docs/test-and-evaluate/develop-tests#building-evals-and-test-cases) based on your defined success criteria will allow you to optimize your prompts. Here are some metrics you may wish to include within your empirical evaluation:

<AccordionGroup>
  <Accordion title="ROUGE scores">This measures the overlap between the generated summary and an expert-created reference summary. This metric primarily focuses on recall and is useful for evaluating content coverage.</Accordion>
  <Accordion title="BLEU scores">While originally developed for machine translation, this metric can be adapted for summarization tasks. BLEU scores measure the precision of n-gram matches between the generated summary and reference summaries. A higher score indicates that the generated summary contains similar phrases and terminology to the reference summary. </Accordion>
  <Accordion title="Contextual embedding similarity">This metric involves creating vector representations (embeddings) of both the generated and reference summaries. The similarity between these embeddings is then calculated, often using cosine similarity. Higher similarity scores indicate that the generated summary captures the semantic meaning and context of the reference summary, even if the exact wording differs.</Accordion>
  <Accordion title="LLM-based grading">This method involves using an LLM such as Claude to evaluate the quality of generated summaries against a scoring rubric. The rubric can be tailored to your specific needs, assessing key factors like accuracy, completeness, and coherence. For guidance on implementing LLM-based grading, view these [tips](/en/docs/test-and-evaluate/develop-tests#tips-for-llm-based-grading).</Accordion>
  <Accordion title="Human evaluation">In addition to creating the reference summaries, legal experts can also evaluate the quality of the generated summaries. While this is expensive and time-consuming at scale, this is often done on a few summaries as a sanity check before deploying to production.</Accordion>
</AccordionGroup>

### Deploy your prompt

Here are some additional considerations to keep in mind as you deploy your solution to production.

1. **Ensure no liability:** Understand the legal implications of errors in the summaries, which could lead to legal liability for your organization or clients. Provide disclaimers or legal notices clarifying that the summaries are generated by AI and should be reviewed by legal professionals.

2. **Handle diverse document types:** In this guide, we’ve discussed how to extract text from PDFs. In the real-world, documents may come in a variety of formats (PDFs, Word documents, text files, etc.). Ensure your data extraction pipeline can convert all of the file formats you expect to receive.

3. **Parallelize API calls to Claude:** Long documents with a large number of tokens may require up to a minute for Claude to generate a summary. For large document collections, you may want to send API calls to Claude in parallel so that the summaries can be completed in a reasonable timeframe. Refer to Anthropic’s [rate limits](/en/api/rate-limits#rate-limits) to determine the maximum amount of API calls that can be performed in parallel.

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
