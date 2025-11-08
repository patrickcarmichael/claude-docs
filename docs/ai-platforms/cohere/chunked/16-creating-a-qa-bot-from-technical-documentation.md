**Navigation:** [← Previous](./15-multi-step-tool-use-with-cohere.md) | [Index](./index.md) | [Next →](./17-credentials-file-populate-if-you-are-running-in-a-.md)

---

# Creating a QA Bot From Technical Documentation

> This page describes how to use Cohere to build a simple question-answering system.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Creating_a_QA_bot_from_technical_documentation.ipynb" />

This notebook demonstrates how to create a chatbot (single turn) that answers user questions based on technical documentation made available to the model.

We use the `aws-documentation` dataset ([link](https://github.com/siagholami/aws-documentation/tree/main)) for representativeness. This dataset contains 26k+ AWS documentation pages, preprocessed into 120k+ chunks, and 100 questions based on real user questions.

We proceed as follows:

1. Embed the AWS documentation into a vector database using Cohere embeddings and `llama_index`
2. Build a retriever using Cohere's `rerank` for better accuracy, lower inference costs and lower latency
3. Create model answers for the eval set of 100 questions
4. Evaluate the model answers against the golden answers of the eval set

## Setup

```python PYTHON
%%capture
!pip install cohere datasets llama_index llama-index-llms-cohere llama-index-embeddings-cohere
```

```python PYTHON
import cohere
import datasets
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.core.schema import TextNode
from llama_index.embeddings.cohere import CohereEmbedding
import pandas as pd

import json
from pathlib import Path
from tqdm import tqdm
from typing import List

```

```python PYTHON
api_key = "" # <your api="" key="">
co = cohere.Client(api_key=api_key)
```

## 1. Embed technical documentation and store as vector database

* Load the dataset from HuggingFace
* Compute embeddings using Cohere's implementation in LlamaIndex, `CohereEmbedding`
* Store inside a vector database, `VectorStoreIndex` from LlamaIndex

Because this process is lengthy (\~2h for all documents on a MacBookPro), we store the index to disc for future reuse. We also provide a (commented) code snippet to index only a subset of the data. If you use this snippet, bear in mind that many documents will become unavailable to the model and, as a result, performance will suffer!

```python PYTHON
data = datasets.load_dataset("sauravjoshi23/aws-documentation-chunked")
print(data)

map_id2index = {sample["id"]: index for index, sample in enumerate(data["train"])}

```

```txt title="Output"
/usr/local/lib/python3.10/dist-packages/huggingface_hub/utils/_token.py:88: UserWarning:
The secret `HF_TOKEN` does not exist in your Colab secrets.
To authenticate with the Hugging Face Hub, create a token in your settings tab (https://huggingface.co/settings/tokens), set it as secret in your Google Colab and restart your session.
You will be able to reuse this secret in all of your notebooks.
Please note that authentication is recommended but still optional to access public models or datasets.
    warnings.warn(


DatasetDict({
    train: Dataset({
        features: ['id', 'text', 'source'],
        num_rows: 187147
    })
})
```

```python PYTHON

overwrite = True # only compute index if it doesn't exist
path_index = Path(".") / "aws-documentation_index_cohere"

embed_model = CohereEmbedding(
    cohere_api_key=api_key,
    model_name="embed-v4.0",
)

if not path_index.exists() or overwrite:
    # Documents are prechunked. Keep them as-is for now
    stub_len = len("https://github.com/siagholami/aws-documentation/tree/main/documents/")
    documents = [
        # -- for indexing full dataset --
        TextNode(
            text=sample["text"],
            title=sample["source"][stub_len:], # save source minus stub
            id_=sample["id"],
        ) for sample in data["train"]
        # -- for testing on subset --
        # TextNode(
        #     text=data["train"][index]["text"],
        #     title=data["train"][index]["source"][stub_len:],
        #     id_=data["train"][index]["id"],
        # ) for index in range(1_000)
    ]
    index = VectorStoreIndex(documents, embed_model=embed_model)
    index.storage_context.persist(path_index)

else:
    storage_context = StorageContext.from_defaults(persist_dir=path_index)
    index = load_index_from_storage(storage_context, embed_model=embed_model)

```

## 2. Build a retriever using Cohere's `rerank`

The vector database we built using `VectorStoreIndex` comes with an in-built retriever. We can call that retriever to fetch the top $k$ documents most relevant to the user question with:

```python PYTHON
retriever = index.as_retriever(similarity_top_k=top_k)
```

We recently released [Rerank-3](https://cohere.com/blog/rerank-3/) (April '24), which we can use to improve the quality of retrieval, as well as reduce latency and the cost of inference. To use the retriever with `rerank`, we create a thin wrapper around `index.as_retriever` as follows:

```python PYTHON
class RetrieverWithRerank:
    def __init__(self, retriever, api_key):
        self.retriever = retriever
        self.co = cohere.Client(api_key=api_key)

    def retrieve(self, query: str, top_n: int):
        # First call to the retriever fetches the closest indices
        nodes = self.retriever.retrieve(query)
        nodes = [
            {
                "text": node.node.text,
                "llamaindex_id": node.node.id_,
            }
            for node
            in nodes
        ]
        # Call co.rerank to improve the relevance of retrieved documents
        reranked = self.co.rerank(query=query, documents=nodes, model="rerank-english-v3.0", top_n=top_n)
        nodes = [nodes[node.index] for node in reranked.results]
        return nodes


top_k = 60 # how many documents to fetch on first pass
top_n = 20 # how many documents to sub-select with rerank

retriever = RetrieverWithRerank(
    index.as_retriever(similarity_top_k=top_k),
    api_key=api_key,
)

```

```python PYTHON
query = "What happens to my Amazon EC2 instances if I delete my Auto Scaling group?"

documents = retriever.retrieve(query, top_n=top_n)

resp = co.chat(message=query, model="command-r-08-2024", temperature=0., documents=documents)
print(resp.text)

```

This works! With `co.chat`, you get the additional benefit that citations are returned for every span of text. Here's a simple function to display the citations inside square brackets.

```python PYTHON
def build_answer_with_citations(response):
    """ """
    text = response.text
    citations = response.citations

    # Construct text_with_citations adding citation spans as we iterate through citations
    end = 0
    text_with_citations = ""

    for citation in citations:
        # Add snippet between last citatiton and current citation
        start = citation.start
        text_with_citations += text[end : start]
        end = citation.end  # overwrite
        citation_blocks = " [" + ", ".join([stub[4:] for stub in citation.document_ids]) + "] "
        text_with_citations += text[start : end] + citation_blocks
    # Add any left-over
    text_with_citations += text[end:]

    return text_with_citations

grounded_answer = build_answer_with_citations(resp)
print(grounded_answer)

```

## 3. Create model answers for 100 QA pairs

Now that we have a running pipeline, we need to assess its performance.

The author of the repository provides 100 QA pairs that we can test the model on. Let's download these questions, then run inference on all 100 questions. Later, we will use Command A -- Cohere's largest and most powerful model -- to measure performance.

```python PYTHON
url = "https://github.com/siagholami/aws-documentation/blob/main/QA_true.csv?raw=true"
qa_pairs = pd.read_csv(url)
qa_pairs.sample(2)

```

We'll use the fields as follows:

* `Question`: the user question, passed to `co.chat` to generate the answer
* `Answer_True`: treat as the ground gruth; compare to the model-generated answer to determine its correctness
* `Document_True`: treat as the (single) golden document; check the rank of this document inside the model's retrieved documents

We'll loop over each question and generate our model answer. We'll also complete two steps that will be useful for evaluating our model next:

1. We compute the rank of the golden document amid the retrieved documents -- this will inform how well our retrieval system performs
2. We prepare the grading prompts -- these will be sent to an LLM scorer to compute the goodness of responses

```python PYTHON

LLM_EVAL_TEMPLATE = """## References
{references}

QUESTION: based on the above reference documents, answer the following question: {question}
ANSWER: {answer}
STUDENT RESPONSE: {completion}

Based on the question and answer above, grade the studen't reponse. A correct response will contain exactly \
the same information as in the answer, even if it is worded differently. If the student's reponse is correct, \
give it a score of 1. Otherwise, give it a score of 0. Let's think step by step. Return your answer as \
as a compilable JSON with the following structure:
{{
    "reasoning": <reasoning>,
    "score: <score 0="" 1="" of="" or="">,
}}"""


def get_rank_of_golden_within_retrieved(golden: str, retrieved: List[dict]) -> int:
    """
    Returns the rank that the golden document (single) has within the retrieved documents
    * `golden` contains the source of the document, e.g. 'amazon-ec2-user-guide/EBSEncryption.md'
    * `retrieved` has a list of responses with key 'llamaindex_id', which links back to document sources
    """
    # Create {document: rank} map using llamaindex_id (count first occurrence of any document; they can
    # appear multiple times because they're chunked)
    doc_to_rank = {}
    for rank, doc in enumerate(retrieved):
        # retrieve source of document
        _id = doc["llamaindex_id"]
        source = data["train"][map_id2index[_id]]["source"]
        # format as in dataset
        source = source[stub_len:]  # remove stub
        source = source.replace("/doc_source", "")  # remove /doc_source/
        if source not in doc_to_rank:
            doc_to_rank[source] = rank + 1

    # Return rank of `golden`, defaulting to len(retrieved) + 1 if it's absent
    return doc_to_rank.get(golden, len(retrieved) + 1)

```

```python PYTHON
from tqdm import tqdm

answers = []
golden_answers = []
ranks = []
grading_prompts = []  # best computed in batch

for _, row in tqdm(qa_pairs.iterrows(), total=len(qa_pairs)):
    query, golden_answer, golden_doc = row["Question"], row["Answer_True"], row["Document_True"]
    golden_answers.append(golden_answer)

    # --- Produce answer using retriever ---
    documents = retriever.retrieve(query, top_n=top_n)
    resp = co.chat(message=query, model="command-r-08-2024", temperature=0., documents=documents)
    answer = resp.text
    answers.append(answer)

    # --- Do some prework for evaluation later ---
    # Rank
    rank = get_rank_of_golden_within_retrieved(golden_doc, documents)
    ranks.append(rank)
    # Score: construct the grading prompts for LLM evals, then evaluate in batch
    # Need to reformat documents slightly
    documents = [{"index": str(i), "text": doc["text"]} for i, doc in enumerate(documents)]
    references_text = "\n\n".join("\n".join([f"{k}: {v}" for k, v in doc.items()]) for doc in documents)
    # ^ snippet looks complicated, but all it does it unpack all kwargs from `documents`
    # into text separated by \n\n
    grading_prompt = LLM_EVAL_TEMPLATE.format(
        references=references_text, question=query, answer=golden_answer, completion=answer,
    )
    grading_prompts.append(grading_prompt)

```

## 4. Evaluate model performance

We want to test our model performance on two dimensions:

1. How good is the final answer? We'll compare our model answer to the golden answer using Command A as a judge.
2. How good is the retrieval? We'll use the rank of the golden document within the retrieved documents to this end.

Note that this pipeline is for illustration only. To measure performance in practice, we would want to run more in-depths tests on a broader, representative dataset.

```python PYTHON
results = pd.DataFrame()
results["answer"] = answers
results["golden_answer"] = qa_pairs["Answer_True"]
results["rank"] = ranks

```

### 4.1 Compare answer to golden answer

We'll use Command A as a judge of whether the answers produced by our model convey the same information as the golden answers. Since we've defined the grading prompts earlier, we can simply ask our LLM judge to evaluate that grading prompt. After a little bit of postprocessing, we can then extract our model scores.

````python PYTHON
scores = []
reasonings = []

def remove_backticks(text: str) -> str:
  """
  Some models are trained to output JSON in Markdown formatting:
  ```json {json object}```
  Remove the backticks from those model responses so that they become
  parasable by json.loads.
  """
  if text.startswith("```json"):
      text = text[7:]
  if text.endswith("```"):
      text = text[:-3]
  return text


for prompt in tqdm(grading_prompts, total=len(grading_prompts)):
  resp = co.chat(message=prompt, model="command-a-03-2025", temperature=0.)
  # Convert response to JSON to extract the `score` and `reasoning` fields
  # We remove backticks for compatibility with different LLMs
  parsed = json.loads(remove_backticks(resp.text))
  scores.append(parsed["score"])
  reasonings.append(parsed["reasoning"])

````

```python PYTHON
results["score"] = scores
results["reasoning"] = reasonings
```

```python PYTHON
print(f"Average score: {results['score'].mean():.3f}")

```

### 4.2 Compute rank

We've already computed the rank of the golden documents using `get_rank_of_golden_within_retrieved`. Here, we'll plot the histogram of ranks, using blue when the answer scored a 1, and red when the answer scored a 0.

```python PYTHON
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid", rc={"grid.color": ".8"})

results["rank_shifted_left"] = results["rank"] - 0.1
results["rank_shifted_right"] = results["rank"] + 0.1

f, ax = plt.subplots(figsize=(5, 3))
sns.histplot(data=results.loc[results["score"] == 1], x="rank_shifted_left", color="skyblue", label="Correct answer", binwidth=1)
sns.histplot(data=results.loc[results["score"] == 0], x="rank_shifted_right", color="red", label="False answer", binwidth=1)

ax.set_xticks([1, 5, 0, 10, 15, 20])
ax.set_title("Rank of golden document (max means golden doc. wasn't retrieved)")
ax.set_xlabel("Rank")
ax.legend();

```

We see that retrieval works well overall: for 80% of questions, the golden document is within the top 5 documents. However, we also notice that approx. half the false answers come from instances where the golden document wasn't retrieved (`rank = top_k = 20`). This should be improved, e.g. by adding metadata to the documents such as their section headings, or altering the chunking strategy.

There is also a non-negligible instance of false answers where the top document was retrieved. On closer inspection, many of these are due to the model phrasing its answers more verbosely than the (very laconic) golden documents. This highlights the importance of checking eval results before jumping to conclusions about model performance.

## Conclusions

In this notebook, we've built a QA bot that answers user questions based on technical documentation. We've learnt:

1. How to embed the technical documentation into a vector database using Cohere embeddings and `llama_index`
2. How to build a custom retriever that leverages Cohere's `rerank`
3. How to evaluate model performance against a predetermined set of golden QA pairs


# Financial CSV Agent with Native Multi-Step Cohere API

> This page describes how to use Cohere's models and its native API to build an agent able to work with CSV data.

<AuthorsContainer
  authors={[
    {
      name: "Jason Jung",
      imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/0803e3d-Jason_Jung.jpg",
    },
  ]}
/>

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/agents/financial-csv-agent/financial_csv_publication_native.ipynb" />

# Notebook Overview

## Motivation

Tabular data reasoning continues to be an exciting application of Agents, particularly in the financial domain, where multiple reasoning steps may be needed to identify the right answer. For example, a financial analyst working with financial statements may be interested in computing various financial ratios with natural language queries.

Some examples may include:

* ROE (Return on Equity) = Net Income / Shareholder's Equity
* Net Profit Margin = Net Income / Revenue
* Asset Turnover = Revenue / Average Total Assets
* Financial Leverage = Average Total Assets / Shareholder's Equity

Having an Agent which is able to correctly compute these and other ratios would be a great help for any analyst in the field of Finance.

## Objective

In this notebook we explore how to setup a [Cohere Agent](https://docs.cohere.com/docs/multi-step-tool-use) to answer questions over tables in Apple's SEC10K 2020 form. [Financial CSV Agent](https://docs.cohere.com/page/csv-agent) already showed how to use Langchain to ask questions about your data. This notebook will demonstrate how you can build the same agent using Cohere's native API with Langchain Python tool. We will also explore how to make your agent more resilient to errors.

# Setup \[#setup]

```python PYTHON
import os
from typing import List

import cohere
import langchain
import langchain_core
import langchain_experimental
import pandas as pd
from langchain.agents import Tool
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_experimental.utilities import PythonREPL
```

```python PYTHON
# Uncomment if you need to install the following packages
# !pip install --quiet langchain langchain_experimental cohere --upgrade
```

```python PYTHON
# versions
print('cohere version:', cohere.__version__)
print('langchain version:', langchain.__version__)
print('langchain_core version:', langchain_core.__version__)
print('langchain_experimental version:', langchain_experimental.__version__)
```

```txt title="Output"
cohere version: 5.5.1
langchain version: 0.2.0
langchain_core version: 0.2.0
langchain_experimental version: 0.0.59
```

### API Key

```python PYTHON
COHERE_API_KEY = os.environ["COHERE_API_KEY"]
CHAT_URL= "https://api.cohere.ai/v1/chat"
COHERE_MODEL = 'command-a-03-2025'
co = cohere.Client(api_key=COHERE_API_KEY)
```

### Data Loading

```python PYTHON
income_statement = pd.read_csv('income_statement.csv')
balance_sheet = pd.read_csv('balance_sheet.csv')
```

```python PYTHON
income_statement.head(2)
```

<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          Unnamed: 0
        </th>

        <th>
          index
        </th>

        <th>
          RevenueFromContractWithCustomerExcludingAssessedTax
        </th>

        <th>
          CostOfGoodsAndServicesSold
        </th>

        <th>
          GrossProfit
        </th>

        <th>
          ResearchAndDevelopmentExpense
        </th>

        <th>
          SellingGeneralAndAdministrativeExpense
        </th>

        <th>
          OperatingExpenses
        </th>

        <th>
          OperatingIncomeLoss
        </th>

        <th>
          NonoperatingIncomeExpense
        </th>

        <th>
          IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest
        </th>

        <th>
          IncomeTaxExpenseBenefit
        </th>

        <th>
          NetIncomeLoss
        </th>

        <th>
          EarningsPerShareBasic
        </th>

        <th>
          EarningsPerShareDiluted
        </th>

        <th>
          WeightedAverageNumberOfSharesOutstandingBasic
        </th>

        <th>
          WeightedAverageNumberOfDilutedSharesOutstanding
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          0
        </td>

        <td>
          2017-10-01-2018-09-29
        </td>

        <td>
          265595000000
        </td>

        <td>
          1.637560e+11
        </td>

        <td>
          101839000000
        </td>

        <td>
          1.423600e+10
        </td>

        <td>
          1.670500e+10
        </td>

        <td>
          3.094100e+10
        </td>

        <td>
          7.089800e+10
        </td>

        <td>
          2.005000e+09
        </td>

        <td>
          7.290300e+10
        </td>

        <td>
          1.337200e+10
        </td>

        <td>
          59531000000
        </td>

        <td>
          3.00
        </td>

        <td>
          2.98
        </td>

        <td>
          1.982151e+10
        </td>

        <td>
          2.000044e+10
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          1
        </td>

        <td>
          2018-09-30-2018-12-29
        </td>

        <td>
          84310000000
        </td>

        <td>
          NaN
        </td>

        <td>
          32031000000
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          19965000000
        </td>

        <td>
          1.05
        </td>

        <td>
          1.05
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>
      </tr>
    </tbody>
  </table>
</div>

```python PYTHON
balance_sheet.head(2)
```

<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          Unnamed: 0
        </th>

        <th>
          index
        </th>

        <th>
          CashAndCashEquivalentsAtCarryingValue
        </th>

        <th>
          MarketableSecuritiesCurrent
        </th>

        <th>
          AccountsReceivableNetCurrent
        </th>

        <th>
          InventoryNet
        </th>

        <th>
          NontradeReceivablesCurrent
        </th>

        <th>
          OtherAssetsCurrent
        </th>

        <th>
          AssetsCurrent
        </th>

        <th>
          MarketableSecuritiesNoncurrent
        </th>

        <th>
          ...
        </th>

        <th>
          LongTermDebtNoncurrent
        </th>

        <th>
          OtherLiabilitiesNoncurrent
        </th>

        <th>
          LiabilitiesNoncurrent
        </th>

        <th>
          Liabilities
        </th>

        <th>
          CommitmentsAndContingencies
        </th>

        <th>
          CommonStocksIncludingAdditionalPaidInCapital
        </th>

        <th>
          RetainedEarningsAccumulatedDeficit
        </th>

        <th>
          AccumulatedOtherComprehensiveIncomeLossNetOfTax
        </th>

        <th>
          StockholdersEquity
        </th>

        <th>
          LiabilitiesAndStockholdersEquity
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          0
        </td>

        <td>
          2017-09-30
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          ...
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          134047000000
        </td>

        <td>
          NaN
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          1
        </td>

        <td>
          2018-09-29
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          ...
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          107147000000
        </td>

        <td>
          NaN
        </td>
      </tr>
    </tbody>
  </table>

  <p>
    2 rows × 30 columns
  </p>
</div>

# Define Python Tool \[#define\_python\_tool]

Here we define the python tool using langchain's PythonREPL. We also define `functions_map` that will later be used by the Cohere Agent to correctly map function name to the actual function. Lastly, we define the tools that will be passed in the Cohere API.

```python PYTHON
python_repl = PythonREPL()
python_tool = Tool(
    name="python_repl",
    description="Executes python code and returns the result. The code runs in a static sandbox without interactive mode, so print output or save output to a file.",
    func=python_repl.run,
)
python_tool.name = "python_interpreter"

class ToolInput(BaseModel):
    code: str = Field(description="Python code to execute.")
python_tool.args_schema = ToolInput

def run_python_code(code: str) -> dict:
    """
    Function to run given python code
    """
    input_code = ToolInput(code=code)
    return {'python_answer': python_tool.func(input_code.code)}

functions_map = {
    "run_python_code": run_python_code,
}

tools = [
    {
        "name": "run_python_code",
        "description": "given a python code, runs it",
        "parameter_definitions": {
            "code": {
                "description": "executable python code",
                "type": "str",
                "required": True
            }
        }
    },]
```

# Create Cohere Agent \[#create\_cohere\_agent]

As [Multi-Step Tool Use](https://docs.cohere.com/page/basic-multi-step) shows, you have a lot of flexiblity on how you can customize and interact with the cohere agent. Here I am creating a wrapper so that it automatically determines when to stop calling the tools and output final answer. It will run maximum of 15 steps.

```python PYTHON
def cohere_agent(
    message: str,
    preamble: str,
    tools: List[dict],
    force_single_step=False,
    verbose: bool = False,
) -> str:
    """
    Function to handle multi-step tool use api.

    Args:
        message (str): The message to send to the Cohere AI model.
        preamble (str): The preamble or context for the conversation.
        tools (list of dict): List of tools to use in the conversation.
        verbose (bool, optional): Whether to print verbose output. Defaults to False.

    Returns:
        str: The final response from the call.
    """

    counter = 1

    response = co.chat(
        model=COHERE_MODEL,
        message=message,
        preamble=preamble,
        tools=tools,
        force_single_step=force_single_step,
    )

    if verbose:
        print(f"\nrunning 0th step.")
        print(response.text)

    while response.tool_calls:
        tool_results = []

        if verbose:
            print(f"\nrunning {counter}th step.")

        for tool_call in response.tool_calls:
            output = functions_map[tool_call.name](**tool_call.parameters)
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
            force_single_step=force_single_step,
            tool_results=tool_results,
        )

        if verbose:
            print(response.text)

            counter += 1

    return response.text


# test
output = cohere_agent("can you use python to answer 1 + 1", None, tools, verbose=True)
```

```txt title="Output"
running 0th step.
I will use Python to answer this question.

running 1th step.
= running tool run_python_code, with parameters: {'code': 'print(1 + 1)'}
== tool results: [{'python_answer': '2\n'}]
The answer is **2**.
```

# QnA over Single Table \[#qna\_over\_single\_table]

In the example below, we show how the Python tool can be used to load a dataframe and extract information from it. To do this successfully we need to:

* Pass the file name to the preamble so the model knows how to load the dataframe
* Pass a preview of the dataframe in the preamble so the model knows which columns/rows to query

We will ask the following questions given income statement data.

* What is the highest value of cost of goods and service?
* What is the largest gross profit margin?
* What is the minimum ratio of operating income loss divided by non operating income expense?

```python PYTHON
question_dict ={
    'q1': ['what is the highest value of cost of goods and service?',169559000000],
    'q2': ['what is the largest gross profit margin?',0.3836194330595236],
    'q3': ['what is the minimum ratio of operating income loss divided by non operating income expense?',35.360599]
}
```

```python PYTHON
preamble = """
You are an expert who answers the user's question. You are working with a pandas dataframe in Python. The name of the dataframe is `income_statement.csv`.
Here is a preview of the dataframe:
{head_df}
""".format(head_df=income_statement.head(3).to_markdown())

print(preamble)
```

You are an expert who answers the user's question. You are working with a pandas dataframe in Python. The name of the dataframe is `income_statement.csv`.
Here is a preview of the dataframe:

|    | Unnamed: 0 | index                 | RevenueFromContractWithCustomerExcludingAssessedTax | CostOfGoodsAndServicesSold |  GrossProfit | ResearchAndDevelopmentExpense | SellingGeneralAndAdministrativeExpense | OperatingExpenses | OperatingIncomeLoss | NonoperatingIncomeExpense | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | IncomeTaxExpenseBenefit | NetIncomeLoss | EarningsPerShareBasic | EarningsPerShareDiluted | WeightedAverageNumberOfSharesOutstandingBasic | WeightedAverageNumberOfDilutedSharesOutstanding |
| -: | ---------: | :-------------------- | --------------------------------------------------: | -------------------------: | -----------: | ----------------------------: | -------------------------------------: | ----------------: | ------------------: | ------------------------: | ------------------------------------------------------------------------------------------: | ----------------------: | ------------: | --------------------: | ----------------------: | --------------------------------------------: | ----------------------------------------------: |
|  0 |          0 | 2017-10-01-2018-09-29 |                                        265595000000 |                1.63756e+11 | 101839000000 |                    1.4236e+10 |                             1.6705e+10 |        3.0941e+10 |          7.0898e+10 |                 2.005e+09 |                                                                                  7.2903e+10 |              1.3372e+10 |   59531000000 |                     3 |                    2.98 |                                   1.98215e+10 |                                     2.00004e+10 |
|  1 |          1 | 2018-09-30-2018-12-29 |                                         84310000000 |                        nan |  32031000000 |                           nan |                                    nan |               nan |                 nan |                       nan |                                                                                         nan |                     nan |   19965000000 |                  1.05 |                    1.05 |                                           nan |                                             nan |
|  2 |          2 | 2018-09-30-2019-09-28 |                                        260174000000 |                1.61782e+11 |  98392000000 |                    1.6217e+10 |                             1.8245e+10 |        3.4462e+10 |           6.393e+10 |                 1.807e+09 |                                                                                  6.5737e+10 |              1.0481e+10 |   55256000000 |                  2.99 |                    2.97 |                                   1.84713e+10 |                                     1.85957e+10 |

```python PYTHON
for qsn,val in question_dict.items():
    print(f'question:{qsn}')
    question = val[0]
    answer = val[1]
    output = cohere_agent(question, preamble, tools, verbose=True)
    print(f'GT Answer:{val[1]}')
    print('-'*50)
```

```txt title="Output"
question:q1

running 0th step.
I will use Python to find the highest value of 'CostOfGoodsAndServicesSold' in the 'income_statement.csv' dataframe.

running 1th step.
= running tool run_python_code, with parameters: {'code': 'import pandas as pd\n\ndf = pd.read_csv(\'income_statement.csv\')\n\n# Find the highest value of \'CostOfGoodsAndServicesSold\'\nhighest_cost = df[\'CostOfGoodsAndServicesSold\'].max()\n\nprint(f"The highest value of \'CostOfGoodsAndServicesSold\' is {highest_cost}")'}
== tool results: [{'python_answer': "The highest value of 'CostOfGoodsAndServicesSold' is 169559000000.0\n"}]
The highest value of 'CostOfGoodsAndServicesSold' is 169559000000.0.
GT Answer:169559000000
--------------------------------------------------
question:q2

running 0th step.
I will write and execute Python code to find the largest gross profit margin.

running 1th step.
= running tool run_python_code, with parameters: {'code': 'import pandas as pd\n\ndf = pd.read_csv(\'income_statement.csv\')\n\n# Calculate gross profit margin\ndf[\'GrossProfitMargin\'] = df[\'GrossProfit\'] / df[\'RevenueFromContractWithCustomerExcludingAssessedTax\'] * 100\n\n# Find the largest gross profit margin\nlargest_gross_profit_margin = df[\'GrossProfitMargin\'].max()\n\nprint(f"The largest gross profit margin is {largest_gross_profit_margin:.2f}%")'}
== tool results: [{'python_answer': 'The largest gross profit margin is 38.36%\n'}]
The largest gross profit margin is 38.36%.
GT Answer:0.3836194330595236
--------------------------------------------------
question:q3

running 0th step.
I will use Python to find the minimum ratio of operating income loss divided by non-operating income expense.

running 1th step.
= running tool run_python_code, with parameters: {'code': 'import pandas as pd\n\ndf = pd.read_csv("income_statement.csv")\n\n# Calculate the ratio of operating income loss to non-operating income expense\ndf["OperatingIncomeLossRatio"] = df["OperatingIncomeLoss"] / df["NonoperatingIncomeExpense"]\n\n# Find the minimum ratio\nmin_ratio = df["OperatingIncomeLossRatio"].min()\n\nprint(f"The minimum ratio of operating income loss to non-operating income expense is: {min_ratio:.2f}")'}
== tool results: [{'python_answer': 'The minimum ratio of operating income loss to non-operating income expense is: 35.36\n'}]
The minimum ratio of operating income loss to non-operating income expense is 35.36.
GT Answer:35.360599
--------------------------------------------------
```

# QnA over Multiple Tables \[#qna\_over\_multiple\_tables]

We now make the task for the Agent more complicated by asking a question that can be only answered by retrieving relevant information from multiple tables:

* Q: What is the ratio of the largest stockholders equity to the smallest revenue?

As you will see below, this question can be obtained only by accessing both the balance sheet and the income statement.

```python PYTHON
question_dict ={
    'q1': ['what is the ratio of the largest stockholders equity to the smallest revenue'],
}
```

```python PYTHON
# get the largest stockholders equity
x = balance_sheet['StockholdersEquity'].astype(float).max()
print(f"The largest stockholders equity value is: {x}")

# get the smallest revenue
y = income_statement['RevenueFromContractWithCustomerExcludingAssessedTax'].astype(float).min()
print(f"The smallest revenue value is: {y}")

# compute the ratio
ratio = x/y
print(f"Their ratio is: {ratio}")
```

```txt title="Output"
The largest stockholders equity value is: 134047000000.0
The smallest revenue value is: 53809000000.0
Their ratio is: 2.4911631883142227
```

```python PYTHON
preamble = """
You are an expert who answers the user's question in complete sentences. You are working with two pandas dataframe in Python. Ensure your output is a string.

Here is a preview of the `income_statement.csv` dataframe:
{table_1}

Here is a preview of the `balance_sheet.csv` dataframe:
{table_2}
""".format(table_1=income_statement.head(3).to_markdown(),table_2=balance_sheet.head(3).to_markdown())


print(preamble)
```

```txt title="Output"
You are an expert who answers the user's question in complete sentences. You are working with two pandas dataframe in Python. Ensure your output is a string.

Here is a preview of the `income_statement.csv` dataframe:
|    |   Unnamed: 0 | index                 |   RevenueFromContractWithCustomerExcludingAssessedTax |   CostOfGoodsAndServicesSold |   GrossProfit |   ResearchAndDevelopmentExpense |   SellingGeneralAndAdministrativeExpense |   OperatingExpenses |   OperatingIncomeLoss |   NonoperatingIncomeExpense |   IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest |   IncomeTaxExpenseBenefit |   NetIncomeLoss |   EarningsPerShareBasic |   EarningsPerShareDiluted |   WeightedAverageNumberOfSharesOutstandingBasic |   WeightedAverageNumberOfDilutedSharesOutstanding |
|---:|-------------:|:----------------------|------------------------------------------------------:|-----------------------------:|--------------:|--------------------------------:|-----------------------------------------:|--------------------:|----------------------:|----------------------------:|----------------------------------------------------------------------------------------------:|--------------------------:|----------------:|------------------------:|--------------------------:|------------------------------------------------:|--------------------------------------------------:|
|  0 |            0 | 2017-10-01-2018-09-29 |                                          265595000000 |                  1.63756e+11 |  101839000000 |                      1.4236e+10 |                               1.6705e+10 |          3.0941e+10 |            7.0898e+10 |                   2.005e+09 |                                                                                    7.2903e+10 |                1.3372e+10 |     59531000000 |                    3    |                      2.98 |                                     1.98215e+10 |                                       2.00004e+10 |
|  1 |            1 | 2018-09-30-2018-12-29 |                                           84310000000 |                nan           |   32031000000 |                    nan          |                             nan          |        nan          |          nan          |                 nan         |                                                                                  nan          |              nan          |     19965000000 |                    1.05 |                      1.05 |                                   nan           |                                     nan           |
|  2 |            2 | 2018-09-30-2019-09-28 |                                          260174000000 |                  1.61782e+11 |   98392000000 |                      1.6217e+10 |                               1.8245e+10 |          3.4462e+10 |            6.393e+10  |                   1.807e+09 |                                                                                    6.5737e+10 |                1.0481e+10 |     55256000000 |                    2.99 |                      2.97 |                                     1.84713e+10 |                                       1.85957e+10 |

Here is a preview of the `balance_sheet.csv` dataframe:
|    |   Unnamed: 0 | index      |   CashAndCashEquivalentsAtCarryingValue |   MarketableSecuritiesCurrent |   AccountsReceivableNetCurrent |   InventoryNet |   NontradeReceivablesCurrent |   OtherAssetsCurrent |   AssetsCurrent |   MarketableSecuritiesNoncurrent |   PropertyPlantAndEquipmentNet |   OtherAssetsNoncurrent |   AssetsNoncurrent |        Assets |   AccountsPayableCurrent |   OtherLiabilitiesCurrent |   ContractWithCustomerLiabilityCurrent |   CommercialPaper |   LongTermDebtCurrent |   LiabilitiesCurrent |   LongTermDebtNoncurrent |   OtherLiabilitiesNoncurrent |   LiabilitiesNoncurrent |   Liabilities |   CommitmentsAndContingencies |   CommonStocksIncludingAdditionalPaidInCapital |   RetainedEarningsAccumulatedDeficit |   AccumulatedOtherComprehensiveIncomeLossNetOfTax |   StockholdersEquity |   LiabilitiesAndStockholdersEquity |
|---:|-------------:|:-----------|----------------------------------------:|------------------------------:|-------------------------------:|---------------:|-----------------------------:|---------------------:|----------------:|---------------------------------:|-------------------------------:|------------------------:|-------------------:|--------------:|-------------------------:|--------------------------:|---------------------------------------:|------------------:|----------------------:|---------------------:|-------------------------:|-----------------------------:|------------------------:|--------------:|------------------------------:|-----------------------------------------------:|-------------------------------------:|--------------------------------------------------:|---------------------:|-----------------------------------:|
|  0 |            0 | 2017-09-30 |                            nan          |                  nan          |                   nan          |    nan         |                 nan          |         nan          |   nan           |                    nan           |                   nan          |            nan          |      nan           | nan           |             nan          |               nan         |                            nan         |        nan        |           nan         |        nan           |             nan          |                 nan          |            nan          | nan           |                           nan |                                   nan          |                         nan          |                                        nan        |         134047000000 |                      nan           |
|  1 |            1 | 2018-09-29 |                            nan          |                  nan          |                   nan          |    nan         |                 nan          |         nan          |   nan           |                    nan           |                   nan          |            nan          |      nan           | nan           |             nan          |               nan         |                            nan         |        nan        |           nan         |        nan           |             nan          |                 nan          |            nan          | nan           |                           nan |                                   nan          |                         nan          |                                        nan        |         107147000000 |                      nan           |
|  2 |            2 | 2019-09-28 |                              4.8844e+10 |                    5.1713e+10 |                     2.2926e+10 |      4.106e+09 |                   2.2878e+10 |           1.2352e+10 |     1.62819e+11 |                      1.05341e+11 |                     3.7378e+10 |              3.2978e+10 |        1.75697e+11 |   3.38516e+11 |               4.6236e+10 |                 3.772e+10 |                              5.522e+09 |          5.98e+09 |             1.026e+10 |          1.05718e+11 |               9.1807e+10 |                   5.0503e+10 |              1.4231e+11 |   2.48028e+11 |                             0 |                                     4.5174e+10 |                           4.5898e+10 |                                         -5.84e+08 |          90488000000 |                        3.38516e+11 |
```

```python PYTHON
for qsn,val in question_dict.items():
    print(f'question:{qsn}')
    question = val[0]
    output = cohere_agent(question, preamble, tools, verbose=True)
```

```txt title="Output"
question:q1

running 0th step.
I will use the provided code to find the ratio of the largest stockholders equity to the smallest revenue.

running 1th step.
= running tool run_python_code, with parameters: {'code': 'import pandas as pd\n\n# Read the CSV files into dataframes\nincome_statement = pd.read_csv(\'income_statement.csv\')\nbalance_sheet = pd.read_csv(\'balance_sheet.csv\')\n\n# Find the smallest revenue\nsmallest_revenue = income_statement[\'RevenueFromContractWithCustomerExcludingAssessedTax\'].min()\n\n# Find the largest stockholders equity\nlargest_stockholders_equity = balance_sheet[\'StockholdersEquity\'].max()\n\n# Calculate the ratio\nratio = largest_stockholders_equity / smallest_revenue\nprint(f"The ratio of the largest stockholders equity to the smallest revenue is {ratio:.2f}")'}
== tool results: [{'python_answer': 'The ratio of the largest stockholders equity to the smallest revenue is 2.49\n'}]
The ratio of the largest stockholders equity to the smallest revenue is 2.49.
```

# Error Resilience \[#error\_resilience]

In the previous example over single table, the model successfully answered your questions. However, the model may not always have access to the preview of the data. You will see that when we remove the preview from the preamble, the model runs into an error and is not produce the answer. We will solve this problem with two different ways:

* Asking the model to keep trying until it fixes the issue.
* Giving the model another tool to view the data and telling it to preview the data before writing code.

You will see that the second method is able to come to the answer with fewer steps.

```python PYTHON
preamble = """
You are an expert who answers the user's question. You are working with a pandas dataframe in Python. The name of the dataframe is `income_statement.csv`.
"""

question1 = "what is the highest value of cost of goods and service?"

output = cohere_agent(question1, preamble, tools, verbose=True)
```

```txt title="Output"
running 0th step.
I will use Python to find the highest value of 'Cost of Goods and Service' in the 'income_statement.csv' file.

running 1th step.
= running tool run_python_code, with parameters: {'code': 'import pandas as pd\n\ndf = pd.read_csv(\'income_statement.csv\')\n\n# Find the highest value of \'Cost of Goods and Service\'\nhighest_cost = df[\'Cost of Goods and Service\'].max()\n\nprint(f"The highest value of \'Cost of Goods and Service\' is: {highest_cost}")'}
== tool results: [{'python_answer': "KeyError('Cost of Goods and Service')"}]
Sorry, there is no column named 'Cost of Goods and Service' in the 'income_statement.csv' file.
```

As you see above, the model failed to execute because it assumed certain column names but they turned out to be wrong. One simple fix is to tell the model to continue to solve the problem in the face of error.

```python PYTHON
preamble = """
You are an expert who answers the user's question. You are working with a pandas dataframe in Python. The name of the dataframe is `income_statement.csv`.
If you run into error, keep trying until you fix it. You may need to view the data to understand the error.
"""

question1 = "what is the highest value of cost of goods and service?"

output = cohere_agent(question1, preamble, tools, verbose=True)
```

```txt title="Output"
running 0th step.
I will use Python to find the highest value of cost of goods and service.

running 1th step.
= running tool run_python_code, with parameters: {'code': 'import pandas as pd\n\ndf = pd.read_csv(\'income_statement.csv\')\n\n# Find the highest value of \'Cost of Goods and Services\'\nhighest_cost = df[\'Cost of Goods and Services\'].max()\n\nprint(f"The highest value of \'Cost of Goods and Services\' is: {highest_cost}")'}
== tool results: [{'python_answer': "KeyError('Cost of Goods and Services')"}]
I encountered an error. I will now view the data to understand the error.

running 2th step.
= running tool run_python_code, with parameters: {'code': "import pandas as pd\n\ndf = pd.read_csv('income_statement.csv')\n\nprint(df.columns)"}
== tool results: [{'python_answer': "Index(['Unnamed: 0', 'index',\n       'RevenueFromContractWithCustomerExcludingAssessedTax',\n       'CostOfGoodsAndServicesSold', 'GrossProfit',\n       'ResearchAndDevelopmentExpense',\n       'SellingGeneralAndAdministrativeExpense', 'OperatingExpenses',\n       'OperatingIncomeLoss', 'NonoperatingIncomeExpense',\n       'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest',\n       'IncomeTaxExpenseBenefit', 'NetIncomeLoss', 'EarningsPerShareBasic',\n       'EarningsPerShareDiluted',\n       'WeightedAverageNumberOfSharesOutstandingBasic',\n       'WeightedAverageNumberOfDilutedSharesOutstanding'],\n      dtype='object')\n"}]
I found that the column name is 'CostOfGoodsAndServicesSold'. I will now use this to find the highest value.

running 3th step.
= running tool run_python_code, with parameters: {'code': 'import pandas as pd\n\ndf = pd.read_csv(\'income_statement.csv\')\n\n# Find the highest value of \'Cost of Goods and Services\'\nhighest_cost = df[\'CostOfGoodsAndServicesSold\'].max()\n\nprint(f"The highest value of \'Cost of Goods and Services\' is: {highest_cost}")'}
== tool results: [{'python_answer': "The highest value of 'Cost of Goods and Services' is: 169559000000.0\n"}]
The highest value of 'Cost of Goods and Services' is 169559000000.0.
```

### Add Viewing Tool \[#add\_viewing\_tool]

What if we directly give the model the ability to view the data as a tool so that it can explicitly use it instead of indirectly figuring it out?

```python PYTHON
def view_csv_data(path: str) -> dict:
    """
    Function to view the head, tail and shape of a given csv file.
    """
    df = pd.read_csv(path)

    return {
        "head": df.head().to_string(),
        "tail": df.tail().to_string(),
        "shape": str(df.shape),
    }

functions_map = {
    "run_python_code": run_python_code,
    "view_csv_data": view_csv_data
}

tools = [
    {
        "name": "run_python_code",
        "description": "given a python code, runs it",
        "parameter_definitions": {
            "code": {
                "description": "executable python code",
                "type": "str",
                "required": True
            }
        }
    },
    {
        "name": "view_csv_data",
        "description": "give path to csv data and get head, tail and shape of the data",
        "parameter_definitions": {
            "path": {
                "description": "path to csv",
                "type": "str",
                "required": True
            }
        }
    },
]
```

```python PYTHON
preamble = """
You are an expert who answers the user's question. You are working with a pandas dataframe in Python. The name of the dataframe is `income_statement.csv`.
Always view the data first to write flawless code.
"""

question1 = "what is the highest value of cost of goods and service?"

output = cohere_agent(question1, preamble, tools, verbose=True)
```

```txt title="Output"
running 0th step.
I will first view the data and then write and execute Python code to find the highest value of cost of goods and service.

running 1th step.
= running tool view_csv_data, with parameters: {'path': 'income_statement.csv'}
== tool results: [{'head': '   Unnamed: 0                  index  RevenueFromContractWithCustomerExcludingAssessedTax  CostOfGoodsAndServicesSold   GrossProfit  ResearchAndDevelopmentExpense  SellingGeneralAndAdministrativeExpense  OperatingExpenses  OperatingIncomeLoss  NonoperatingIncomeExpense  IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest  IncomeTaxExpenseBenefit  NetIncomeLoss  EarningsPerShareBasic  EarningsPerShareDiluted  WeightedAverageNumberOfSharesOutstandingBasic  WeightedAverageNumberOfDilutedSharesOutstanding\n0           0  2017-10-01-2018-09-29                                         265595000000                1.637560e+11  101839000000                   1.423600e+10                            1.670500e+10       3.094100e+10         7.089800e+10               2.005000e+09                                                                                 7.290300e+10             1.337200e+10    59531000000                   3.00                     2.98                                   1.982151e+10                                     2.000044e+10\n1           1  2018-09-30-2018-12-29                                          84310000000                         NaN   32031000000                            NaN                                     NaN                NaN                  NaN                        NaN                                                                                          NaN                      NaN    19965000000                   1.05                     1.05                                            NaN                                              NaN\n2           2  2018-09-30-2019-09-28                                         260174000000                1.617820e+11   98392000000                   1.621700e+10                            1.824500e+10       3.446200e+10         6.393000e+10               1.807000e+09                                                                                 6.573700e+10             1.048100e+10    55256000000                   2.99                     2.97                                   1.847134e+10                                     1.859565e+10\n3           3  2018-12-30-2019-03-30                                          58015000000                         NaN   21821000000                            NaN                                     NaN                NaN                  NaN                        NaN                                                                                          NaN                      NaN    11561000000                   0.62                     0.61                                            NaN                                              NaN\n4           4  2019-03-31-2019-06-29                                          53809000000                         NaN   20227000000                            NaN                                     NaN                NaN                  NaN                        NaN                                                                                          NaN                      NaN    10044000000                   0.55                     0.55                                            NaN                                              NaN', 'tail': '    Unnamed: 0                  index  RevenueFromContractWithCustomerExcludingAssessedTax  CostOfGoodsAndServicesSold   GrossProfit  ResearchAndDevelopmentExpense  SellingGeneralAndAdministrativeExpense  OperatingExpenses  OperatingIncomeLoss  NonoperatingIncomeExpense  IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest  IncomeTaxExpenseBenefit  NetIncomeLoss  EarningsPerShareBasic  EarningsPerShareDiluted  WeightedAverageNumberOfSharesOutstandingBasic  WeightedAverageNumberOfDilutedSharesOutstanding\n6            6  2019-09-29-2019-12-28                                          91819000000                         NaN   35217000000                            NaN                                     NaN                NaN                  NaN                        NaN                                                                                          NaN                      NaN    22236000000                   1.26                     1.25                                            NaN                                              NaN\n7            7  2019-09-29-2020-09-26                                         274515000000                1.695590e+11  104956000000                   1.875200e+10                            1.991600e+10       3.866800e+10         6.628800e+10                803000000.0                                                                                 6.709100e+10             9.680000e+09    57411000000                   3.31                     3.28                                   1.735212e+10                                     1.752821e+10\n8            8  2019-12-29-2020-03-28                                          58313000000                         NaN   22370000000                            NaN                                     NaN                NaN                  NaN                        NaN                                                                                          NaN                      NaN    11249000000                   0.64                     0.64                                            NaN                                              NaN\n9            9  2020-03-29-2020-06-27                                          59685000000                         NaN   22680000000                            NaN                                     NaN                NaN                  NaN                        NaN                                                                                          NaN                      NaN    11253000000                   0.65                     0.65                                            NaN                                              NaN\n10          10  2020-06-28-2020-09-26                                          64698000000                         NaN   24689000000                            NaN                                     NaN                NaN                  NaN                        NaN                                                                                          NaN                      NaN    12673000000                   0.74                     0.73                                            NaN                                              NaN', 'shape': '(11, 17)'}]
The column name is 'CostOfGoodsAndServicesSold'. I will now write and execute Python code to find the highest value in this column.

running 2th step.
= running tool run_python_code, with parameters: {'code': "import pandas as pd\n\ndf = pd.read_csv('income_statement.csv')\n\nprint(df['CostOfGoodsAndServicesSold'].max())"}
== tool results: [{'python_answer': '169559000000.0\n'}]
The highest value of cost of goods and services is 169559000000.0.
```

By being prescriptive, we were able to cut down a step and get to the answer faster.


# Financial CSV Agent with Langchain

> This page describes how to use Cohere's models to build an agent able to work with CSV data.

<AuthorsContainer
  authors={[
    {
      name: "Shaan Desai",
      imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/d17fc44-Shaan.jpg",
    },
  ]}
/>

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/agents/financial-csv-agent/financial_csv_publication.ipynb" />

# Notebook Overview

## Motivation

Tabular data reasoning continues to be an exciting application of Agents, particularly in the financial domain, where multiple reasoning steps may be needed to identify the right answer. For example, a financial analyst working with financial statements may be interested in computing various financial ratios with natural language queries.

Some examples may include:

* ROE (Return on Equity) = Net Income / Shareholder's Equity
* Net Profit Margin = Net Income / Revenue
* Asset Turnover = Revenue / Average Total Assets
* Financial Leverage = Average Total Assets / Shareholder's Equity

Having an Agent which is able to correctly compute these and other ratios would be a great help for any analyst in the field of Finance.

## Objective

In this notebook we explore how to setup a [Cohere ReAct Agent](https://github.com/langchain-ai/langchain-cohere/blob/main/libs/cohere/langchain_cohere/cohere_agent.py) to answer questions over tables in Apple's SEC10K 2020 form. We show how this can be done with two variants of a Langchain Python tool, one that requires you to pass the full path of the dataframe and another that requires the dataframe objects to be loaded in memory. While there is no major difference between the two approaches, we present both to show how to manage files that are loaded in memory vs files in storage.

# Setup \[#sec\_step0]

```python PYTHON
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.agents import AgentExecutor
from langchain_cohere.react_multi_hop.agent import create_cohere_react_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_cohere.chat_models import ChatCohere
import pandas as pd
from langchain.agents import Tool
from langchain_experimental.utilities import PythonREPL
from langchain_experimental.tools.python.tool import PythonAstREPLTool
```

```python PYTHON
# Uncomment if you need to install the following packages
#!pip install --quiet langchain langchain_cohere langchain_experimental --upgrade
#!pip install sec-api
```

# Introduction \[#sec\_step1]

The aim of this notebook is to showcase how Cohere Langchain Agents can be used to answer questions over tabular data.
This notebook assumes the input is a set of csv files extracted from Apple's SEC 10K filings.

### Data Loading

We use the sec-api to download the income statement and balance sheet from the SEC 10K .htm file. Please note that the tables need to be parsed such that the index is numerical as the python code generation struggles to filter based on index. We have processed the tables and provided them for you. They can be found [here](https://github.com/cohere-ai/cohere-developer-experience/tree/main/notebooks/agents/financial-csv-agent).

```python PYTHON
income_statement = pd.read_csv('income_statement.csv')
balance_sheet = pd.read_csv('balance_sheet.csv')
```

# QnA over Single Table{" "} \[#sec\_step2]

## Agent with Python Tool \[#sec\_step2\_sub1]

In the example below, we show how the python tool can be used to load a dataframe and extract information from it. To do this successfully we need to:

* Pass the file name to the preamble so the model knows how to load the dataframe.
* Pass a preview of the dataframe in the preamble so the model knows which columns/rows to query.

First, let's implement the ReAct agent.

```python PYTHON
# instantiate the Cohere llm
llm = ChatCohere(model="command-r", temperature=0.1,cohere_api_key="",verbose=True)

# create the python tool
python_repl = PythonREPL()
python_tool = Tool(
    name="python_repl",
    description="Executes python code and returns the result. The code runs in a static sandbox without interactive mode, so print output or save output to a file.",
    func=python_repl.run,
)
python_tool.name = "python_interpreter"

class ToolInput(BaseModel):
    code: str = Field(description="Python code to execute.")
python_tool.args_schema = ToolInput
tools=[python_tool]

# define the prompt template
prompt = ChatPromptTemplate.from_template("{input}")

# instantiate the ReAct agent
agent = create_cohere_react_agent(
   llm=llm,
   tools=tools,
   prompt=prompt,
)
agent_executor = AgentExecutor(agent=agent,
                               tools=tools,
                               verbose=True,
                               return_intermediate_steps=True
                    )
# finally, define the preamble
preamble = """
You are an expert who answers the user's question. You are working with a pandas dataframe in Python. The name of the dataframe is `income_statement.csv`.
Here is a preview of the dataframe:
{head_df}
""".format(head_df=income_statement.head(3).to_markdown())

```

Then, we define the dictionary including the questions we want the Agent to answer, and their answer.

```python PYTHON
question_dict ={
    'q1': ['what is the highest value of cost of goods and service?',169559000000],
    'q2': ['what is the largest gross profit margin?',0.3836194330595236],
    'q3': ['what is the minimum ratio of operating income loss divided by non operating income expense',35.360599]
}
```

Let's now see how the Agent answers each of the questions.

```python PYTHON
for qsn,val in question_dict.items():
    print(f'question:{qsn}')
    agent_executor.invoke({
       "input": val[0],
       "preamble": preamble,
    })
    print(f'GT Answer:{val[1]}')
    print('-'*50)
```

```txt title="Output"
question:q1


[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will write and execute Python code to find the highest value of Cost of Goods and Services Sold from the provided dataframe.
{'tool_name': 'python_interpreter', 'parameters': {'code': 'import pandas as pd\n\n# Read the CSV file into a DataFrame\ndf = pd.read_csv(\'income_statement.csv\')\n\n# Find the highest value in the \'CostOfGoodsAndServicesSold\' column\nmax_value = df[\'CostOfGoodsAndServicesSold\'].max()\n\nprint(f"The highest value of Cost of Goods and Services Sold is {max_value}")'}}
[0m[36;1m[1;3mThe highest value of Cost of Goods and Services Sold is 169559000000.0
[0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: The highest value of Cost of Goods and Services Sold is 169559000000.0.
Grounded answer: The highest value of Cost of Goods and Services Sold is <co: 0="">169559000000.0</co:>.[0m

[1m> Finished chain.[0m
GT Answer:169559000000
--------------------------------------------------
question:q2


[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will write and execute Python code to calculate the largest gross profit margin from the data frame provided.
{'tool_name': 'python_interpreter', 'parameters': {'code': 'import pandas as pd\n\n# Read the CSV file into a DataFrame\ndf = pd.read_csv(\'income_statement.csv\')\n\n# Calculate the gross profit margin as a percentage\ndf[\'GrossProfitMargin\'] = (df[\'GrossProfit\'] / df[\'RevenueFromContractWithCustomerExcludingAssessedTax\']) * 100\n\n# Find the row with the maximum gross profit margin\nmax_margin_row = df.loc[df[\'GrossProfitMargin\'].idxmax()]\n\nprint(f"The largest gross profit margin is {max_margin_row[\'GrossProfitMargin\']}% on {max_margin_row[\'index\']}")\n'}}
[0m[36;1m[1;3mThe largest gross profit margin is 38.36194330595236% on 2019-12-29-2020-03-28
[0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: The largest gross profit margin is approximately 38.36% on 2019-12-29 to 2020-03-28.
Grounded answer: The largest gross profit margin is <co: 0="">approximately 38.36</co:>% on <co: 0="">2019-12-29 to 2020-03-28</co:>.[0m

[1m> Finished chain.[0m
GT Answer:0.3836194330595236
--------------------------------------------------
question:q3


[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will write and execute Python code to calculate the minimum ratio of Operating Income Loss divided by Non Operating Income Expense.
{'tool_name': 'python_interpreter', 'parameters': {'code': 'import pandas as pd\n\n# Read the CSV file into a DataFrame\ndf = pd.read_csv(\'income_statement.csv\')\n\n# Calculate the ratio\nratios = df[\'OperatingIncomeLoss\'] / df[\'NonoperatingIncomeExpense\']\n\nprint("Minimum ratio:", ratios.min())'}}
[0m[36;1m[1;3mMinimum ratio: 35.36059850374065
[0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: The minimum ratio of Operating Income Loss divided by Non Operating Income Expense is approximately **35.36**.
Grounded answer: The minimum ratio of Operating Income Loss divided by Non Operating Income Expense is approximately *<co: 0="">*35.36</co:>**.[0m

[1m> Finished chain.[0m
GT Answer:35.360599
--------------------------------------------------
```

Nice! The agent uses the Python tool to write the code to access the data in the tables, and perform the required calculations.

## Agent with Python Tool that takes tables as input \[#sec\_step2\_sub2]

In the example above, the model needs to load the dataframe in the python call before carrying out operations. In this example, we show how to pass the dataframes to the python tool so it has the file already loaded.

```python PYTHON
# call the PythonAstREPLTool in order to pass tables to the tool
df_locals = {'df':pd.read_csv('income_statement.csv')}
tools = [PythonAstREPLTool(locals=df_locals)]

agent = create_cohere_react_agent(
   llm=llm,
   tools=tools,
   prompt=prompt,
)
agent_executor = AgentExecutor(agent=agent,
                               tools=tools,
                               verbose=True,
                               return_intermediate_steps=True
                    )

preamble = """
You are an expert who answers the user's question. You are working with a pandas dataframe in Python. The name of the dataframe is `df`.
Here is a preview of the dataframe:
{head_df}
""".format(head_df=income_statement.head(3).to_markdown())

```

Let's loop again over the same dictionary of questions.

```python PYTHON
for qsn,val in question_dict.items():
    print(f'question:{qsn}')
    agent_executor.invoke({
       "input": val[0],
       "preamble": preamble,
    })
    print(f'GT Answer:{val[1]}')
    print('-'*50)
```

```txt title="Output"
question:q1


[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will write and execute Python code to find the highest value of Cost of Goods and Services Sold from the provided dataframe.
{'tool_name': 'python_interpreter', 'parameters': {'code': "import pandas as pd\n\n# Read the CSV file into a DataFrame\ndf = pd.read_csv('income_statement.csv')\n\n# Find the highest value in the 'CostOfGoodsAndServicesSold' column\nmax_value = df['CostOfGoodsAndServicesSold'].max()\n\nprint(f'The highest value of Cost of Goods and Services Sold is {max_value:.2f}')\n"}}
[0m[36;1m[1;3mThe highest value of Cost of Goods and Services Sold is 169559000000.00
[0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: The highest value of Cost of Goods and Services Sold is 169559000000.00.
Grounded answer: The highest value of Cost of Goods and Services Sold is <co: 0="">169559000000.00</co:>.[0m

[1m> Finished chain.[0m
GT Answer:169559000000
--------------------------------------------------
question:q2


[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will write and execute Python code to calculate the largest gross profit margin from the data frame provided.
{'tool_name': 'python_interpreter', 'parameters': {'code': 'import pandas as pd\n\n# Read the CSV file into a DataFrame\ndf = pd.read_csv(\'income_statement.csv\')\n\n# Calculate the gross profit margin as a percentage\ndf[\'GrossProfitMargin\'] = (df[\'GrossProfit\'] / df[\'RevenueFromContractWithCustomerExcludingAssessedTax\']) * 100\n\n# Find the row with the maximum gross profit margin\nmax_margin_row = df.loc[df[\'GrossProfitMargin\'].idxmax()]\n\nprint(f"The largest gross profit margin is {max_margin_row[\'GrossProfitMargin\']}% on {max_margin_row[\'index\']}")\n'}}
[0m[36;1m[1;3mThe largest gross profit margin is 38.36194330595236% on 2019-12-29-2020-03-28
[0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: The largest gross profit margin is approximately 38.36% on 2019-12-29 to 2020-03-28.
Grounded answer: The largest gross profit margin is <co: 0="">approximately 38.36</co:>% on <co: 0="">2019-12-29 to 2020-03-28</co:>.[0m

[1m> Finished chain.[0m
GT Answer:0.3836194330595236
--------------------------------------------------
question:q3


[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will write and execute Python code to calculate the minimum ratio of Operating Income Loss divided by Non Operating Income Expense.
{'tool_name': 'python_interpreter', 'parameters': {'code': "import pandas as pd\n\n# Read the CSV file into a DataFrame\ndf = pd.read_csv('income_statement.csv')\n\n# Calculate the ratio\nratios = df['OperatingIncomeLoss'] / df['NonoperatingIncomeExpense']\n\n# Find the minimum ratio\nmin_ratio = ratios.min()\n\nprint(f'Minimum ratio: {min_ratio:.2f}')\n"}}
[0m[36;1m[1;3mMinimum ratio: 35.36
[0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: The minimum ratio of Operating Income Loss divided by Non Operating Income Expense is approximately **35.36**.
Grounded answer: The minimum ratio of Operating Income Loss divided by Non Operating Income Expense is approximately *<co: 0="">*35.36</co:>**.[0m

[1m> Finished chain.[0m
GT Answer:35.360599
--------------------------------------------------
```

Also in this case, the Agent correctly answers all the questions.

# QnA over Multiple Tables \[#sec\_step3]

We now make the task for the Agent more complicated, by asking it questions whose answer can be computed only by retrieving relevant information from multiple tables.

```python PYTHON
# define the Agent
python_repl = PythonREPL()
python_tool = Tool(
    name="python_repl",
    description="Executes python code and returns the result. The code runs in a static sandbox without interactive mode, so print output or save output to a file.",
    func=python_repl.run,
)
python_tool.name = "python_interpreter"

class ToolInput(BaseModel):
    code: str = Field(description="Python code to execute.")
python_tool.args_schema = ToolInput
tools=[python_tool]

prompt = ChatPromptTemplate.from_template("{input}")
agent = create_cohere_react_agent(
   llm=llm,
   tools=tools,
   prompt=prompt,
)
agent_executor = AgentExecutor(agent=agent,
                               tools=tools,
                               verbose=True,
                               return_intermediate_steps=True
                    )

preamble = """
You are an expert who answers the user's question in complete sentences. You are working with two pandas dataframe in Python. Ensure your output is a string.

Here is a preview of the `income_statement.csv` dataframe:
{table_1}

Here is a preview of the `balance_sheet.csv` dataframe:
{table_2}
""".format(table_1=income_statement.head(3).to_markdown(),table_2=balance_sheet.head(3).to_markdown())

```

We now define a new question.

```python PYTHON
question_dict ={
    'q1': ['what is the ratio of the largest stockholders equity to the smallest revenue'],
}
```

The answer to this question can be obtained only by accessing both the balance sheet and the income statement, as shown below:

```python PYTHON
# get the largest stockholders equity
x = balance_sheet['StockholdersEquity'].astype(float).max()
print(f"The largest stockholders equity value is: {x}")

# get the smallest revenue
y = income_statement['RevenueFromContractWithCustomerExcludingAssessedTax'].astype(float).min()
print(f"The smallest revenue value is: {y}")

# compute the ratio
ratio = x/y
print(f"Their ratio is: {ratio}")
```

```txt title="Output"
The largest stockholders equity value is: 134047000000.0
The smallest revenue value is: 53809000000.0
Their ratio is: 2.4911631883142227
```

Let's now get the answer from the Agent.

```python PYTHON
for qsn,val in question_dict.items():
    print(f'question:{qsn}')
    agent_executor.invoke({
       "input": val[0],
       "preamble": preamble,
    })
```

```txt title="Output"
question:q1


[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will write and execute Python code to find the largest and smallest values in the relevant columns of the dataframes, then calculate the ratio.
{'tool_name': 'python_interpreter', 'parameters': {'code': "import pandas as pd\n\nincome_statement = pd.read_csv('income_statement.csv')\nbalance_sheet = pd.read_csv('balance_sheet.csv')\n\n# Find largest and smallest values in relevant columns\nmax_stockholders_equity = max([balance_sheet['StockholdersEquity'].iloc[i] for i in range(len(balance_sheet))])\nmin_revenue = min([income_statement['RevenueFromContractWithCustomerExcludingAssessedTax'].iloc[i] for i in range(len(income_statement))])\n\n# Calculate ratio\nratio = max_stockholders_equity / min_revenue\n\nprint(f'The ratio of the largest stockholders equity to the smallest revenue is {ratio:.2f}'\n    )"}}
[0m[36;1m[1;3mNameError("name 'balance_sheet' is not defined")[0m[32;1m[1;3m
My code has thrown an error because the variable `balance_sheet` has not been defined. I will fix this by adding the line `balance_sheet = pd.read_csv('balance_sheet.csv')` to the beginning of my code.
{'tool_name': 'python_interpreter', 'parameters': {'code': "import pandas as pd\n\nincome_statement = pd.read_csv('income_statement.csv')\n\nbalance_sheet = pd.read_csv('balance_sheet.csv')\n\n# Find largest and smallest values in relevant columns\nmax_stockholders_equity = max([balance_sheet['StockholdersEquity'].iloc[i] for i in range(len(balance_sheet))])\nmin_revenue = min([income_statement['RevenueFromContractWithCustomerExcludingAssessedTax'].iloc[i] for i in range(len(income_statement))])\n\n# Calculate ratio\nratio = max_stockholders_equity / min_revenue\n\nprint(f'The ratio of the largest stockholders equity to the smallest revenue is {ratio:.2f}'\n    )"}}
[0m[36;1m[1;3mNameError("name 'balance_sheet' is not defined")[0m[32;1m[1;3m
The same error has occurred again, so I will check my code carefully to make sure the variable is being defined correctly.
{'tool_name': 'python_interpreter', 'parameters': {'code': "import pandas as pd\n\n# Load data\nincome_statement = pd.read_csv('income_statement.csv')\nbalance_sheet = pd.read_csv('balance_sheet.csv')\n\n# Find largest and smallest values in relevant columns\nmax_stockholders_equity = max(balance_sheet['StockholdersEquity'])\nmin_revenue = min(income_statement['RevenueFromContractWithCustomerExcludingAssessedTax'])\n\n# Calculate ratio\nratio = max_stockholders_equity / min_revenue\n\nprint(f'The ratio of the largest stockholders equity to the smallest revenue is {ratio:.2f}')"}}
[0m[36;1m[1;3mThe ratio of the largest stockholders equity to the smallest revenue is 2.49
[0m[32;1m[1;3mRelevant Documents: 0,1,2
Cited Documents: 2
Answer: The ratio of the largest stockholders equity to the smallest revenue is approximately **2.49**.
Grounded answer: The ratio of the largest stockholders equity to the smallest revenue is approximately *<co: 2="">*2.49</co:>**.[0m

[1m> Finished chain.[0m
```

The Agent defined a plan ("write and execute Python code to find the largest and smallest values in the relevant columns of the dataframes, then calculate the ratio") and executed it. It made some mistakes when coding, that resulted in NameError errors, but it fixed them and finally got to the correct answer


# Migrating away from create_csv_agent in langchain-cohere

> This page contains a tutorial on how to build a CSV agent without the deprecated `create_csv_agent` abstraction in langchain-cohere v0.3.5 and beyond.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/agents/csv-agent-migration/migrate_csv_agent.ipynb" />

# How to build a CSV Agent without using deprecated `create_csv_agent` - langchain-cohere

Starting from version 0.3.5 of the langchain-cohere package, the `create_csv_agent` abstraction has been deprecated.
In this guide, we will demonstrate how to build a custom CSV agent without it.

```
!pip install langchain langchain-core langchain-experimental langchain-cohere pandas -qq
```

```python
# Import packages
from datetime import datetime
from io import IOBase
from typing import List, Optional, Union
import pandas as pd
from pydantic import BaseModel, Field

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.language_models import BaseLanguageModel
from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    SystemMessage,
)
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)

from langchain_core.tools import Tool, BaseTool
from langchain_core.prompts.chat import (
    BaseMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain_experimental.tools.python.tool import PythonAstREPLTool
from langchain_cohere.chat_models import ChatCohere
```

```python
# Replace this cell with your actual cohere api key
os.env["COHERE_API_KEY"] = "cohere_api_key"
```

```python
# Define prompts that we want to use in the csv agent
FUNCTIONS_WITH_DF = """
This is the result of `print(df.head())`:
{df_head}

Do note that the above df isn't the complete df. It is only the first {number_of_head_rows} rows of the df.
Use this as a sample to understand the structure of the df. However, donot use this to make any calculations directly!

The complete path for the csv files are for the corresponding dataframe is:
{csv_path}
"""  # noqa E501

FUNCTIONS_WITH_MULTI_DF = """
This is the result of `print(df.head())` for each dataframe:
{dfs_head}

Do note that the above dfs aren't the complete df. It is only the first {number_of_head_rows} rows of the df.
Use this as a sample to understand the structure of the df. However, donot use this to make any calculations directly!

The complete path for the csv files are for the corresponding dataframes are:
{csv_paths}
"""  # noqa E501

PREFIX_FUNCTIONS = """
You are working with a pandas dataframe in Python. The name of the dataframe is `df`."""  # noqa E501

MULTI_DF_PREFIX_FUNCTIONS = """
You are working with {num_dfs} pandas dataframes in Python named df1, df2, etc."""  # noqa E501

CSV_PREAMBLE = """## Task And Context
You use your advanced complex reasoning capabilities to help people by answering their questions and other requests interactively. You will be asked a very wide array of requests on all kinds of topics. You will be equipped with a wide range of search engines or similar tools to help you, which you use to research your answer. You may need to use multiple tools in parallel or sequentially to complete your task. You should focus on serving the user's needs as best you can, which will be wide-ranging. The current date is {current_date}

## Style Guide
Unless the user asks for a different style of answer, you should answer in full sentences, using proper grammar and spelling
"""  # noqa E501
```

### Define tools necessary for the agent

The below cell introduces a suite of tools that are provided to the csv agent. These tools allow the agent to fcilitate meaningful interactions with uploaded files and providing Python code execution functionality. The toolkit comprises three main components:

**File Peek Tool**: Offers a convenient way to inspect a CSV file by providing a quick preview of the first few rows in a Markdown format, making it easy to get a glimpse of the data.

**File Read Tool**: Allows for a comprehensive exploration of the CSV file by reading and presenting its full contents in a user-friendly Markdown format.

**Python Interpreter Tool**: Enables secure execution of Python code within a sandboxed environment, providing users with the output of the code execution.

```python
# Define tools that we want the csv agent to have access to


def get_file_peek_tool() -> Tool:
    def file_peek(filename: str, num_rows: int = 5) -> str:
        """Returns the first textual contents of an uploaded file

        Args:
            table_path: the table path
            num_rows: the number of rows of the table to preview.
        """  # noqa E501
        if ".csv" in filename:
            return pd.read_csv(filename).head(num_rows).to_markdown()
        else:
            return "the table_path was not recognised"

    class file_peek_inputs(BaseModel):
        filename: str = Field(
            description="The name of the attached file to show a peek preview."
        )

    file_peek_tool = Tool(
        name="file_peek",
        description="The name of the attached file to show a peek preview.",  # noqa E501
        func=file_peek,
        args_schema=file_peek_inputs,
    )

    return file_peek_tool


def get_file_read_tool() -> Tool:
    def file_read(filename: str) -> str:
        """Returns the textual contents of an uploaded file, broken up in text chunks

        Args:
            filename (str): The name of the attached file to read.
        """  # noqa E501
        if ".csv" in filename:
            return pd.read_csv(filename).to_markdown()
        else:
            return "the table_path was not recognised"

    class file_read_inputs(BaseModel):
        filename: str = Field(
            description="The name of the attached file to read."
        )

    file_read_tool = Tool(
        name="file_read",
        description="Returns the textual contents of an uploaded file, broken up in text chunks",  # noqa E501
        func=file_read,
        args_schema=file_read_inputs,
    )

    return file_read_tool


def get_python_tool() -> Tool:
    """Returns a tool that will execute python code and return the output."""

    def python_interpreter(code: str) -> str:
        """A function that will return the output of the python code.

        Args:
            code: the python code to run.
        """
        return python_repl.run(code)

    python_repl = PythonAstREPLTool()
    python_tool = Tool(
        name="python_interpreter",
        description="Executes python code and returns the result. The code runs in a static sandbox without interactive mode, so print output or save output to a file.",  # noqa E501
        func=python_interpreter,
    )

    class PythonToolInput(BaseModel):
        code: str = Field(description="Python code to execute.")

    python_tool.args_schema = PythonToolInput
    return python_tool
```

### Create helper functions

In the cell below, we will create some important helper functions that we can call to properly assemble the full prompt that the csv agent can utilize.

```python
def create_prompt(
    system_message: Optional[BaseMessage] = SystemMessage(
        content="You are a helpful AI assistant."
    ),
    extra_prompt_messages: Optional[
        List[BaseMessagePromptTemplate]
    ] = None,
) -> ChatPromptTemplate:
    """Create prompt for this agent.

    Args:
        system_message: Message to use as the system message that will be the
            first in the prompt.
        extra_prompt_messages: Prompt messages that will be placed between the
            system message and the new human input.

    Returns:
        A prompt template to pass into this agent.
    """
    _prompts = extra_prompt_messages or []
    messages: List[Union[BaseMessagePromptTemplate, BaseMessage]]
    if system_message:
        messages = [system_message]
    else:
        messages = []

    messages.extend(
        [
            *_prompts,
            HumanMessagePromptTemplate.from_template("{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )
    return ChatPromptTemplate(messages=messages)


def _get_csv_head_str(path: str, number_of_head_rows: int) -> str:
    with open(path, "r") as file:
        lines = []
        for _ in range(number_of_head_rows):
            lines.append(file.readline().strip("\n"))
        # validate that the head contents are well formatted csv

        return " ".join(lines)


def _get_prompt(
    path: Union[str, List[str]], number_of_head_rows: int
) -> ChatPromptTemplate:
    if isinstance(path, str):
        lines = _get_csv_head_str(path, number_of_head_rows)
        prompt_message = f"The user uploaded the following attachments:\nFilename: {path}\nWord Count: {count_words_in_file(path)}\nPreview: {lines}"  # noqa: E501

    elif isinstance(path, list):
        prompt_messages = []
        for file_path in path:
            lines = _get_csv_head_str(file_path, number_of_head_rows)
            prompt_messages.append(
                f"The user uploaded the following attachments:\nFilename: {file_path}\nWord Count: {count_words_in_file(file_path)}\nPreview: {lines}"  # noqa: E501
            )
        prompt_message = " ".join(prompt_messages)

    prompt = create_prompt(
        system_message=HumanMessage(prompt_message)
    )
    return prompt


def count_words_in_file(file_path: str) -> int:
    try:
        with open(file_path, "r") as file:
            content = file.readlines()
            words = [len(sentence.split()) for sentence in content]
            return sum(words)
    except FileNotFoundError:
        print("File not found.")
        return 0
    except Exception as e:
        print("An error occurred:", str(e))
        return 0
```

### Build the core csv agent abstraction

The cells below outline the assembly of the various components to build an agent abstraction tailored for intelligent CSV file interactions. We use langchain to provide the agent that has access to the tools declared above, along with additional capabilities to provide additional tools if needed, and put together an agentic abstraction using the prompts defined earlier to deliver an abstraction that can easily be called for natural language querying over csv files!

```python
# Build the agent abstraction itself
def create_csv_agent(
    llm: BaseLanguageModel,
    path: Union[str, List[str]],
    extra_tools: List[BaseTool] = [],
    pandas_kwargs: Optional[dict] = None,
    prompt: Optional[ChatPromptTemplate] = None,
    number_of_head_rows: int = 5,
    verbose: bool = True,
    return_intermediate_steps: bool = True,
) -> AgentExecutor:
    """Create csv agent with the specified language model.

    Args:
        llm: Language model to use for the agent.
        path: A string path, or a list of string paths
            that can be read in as pandas DataFrames with pd.read_csv().
        number_of_head_rows: Number of rows to display in the prompt for sample data
        include_df_in_prompt: Display the DataFrame sample values in the prompt.
        pandas_kwargs: Named arguments to pass to pd.read_csv().
        prefix: Prompt prefix string.
        suffix: Prompt suffix string.
        prompt: Prompt to use for the agent. This takes precedence over the other prompt arguments, such as suffix and prefix.
        temp_path_dir: Temporary directory to store the csv files in for the python repl.
        delete_temp_path: Whether to delete the temporary directory after the agent is done. This only works if temp_path_dir is not provided.

    Returns:
        An AgentExecutor with the specified agent_type agent and access to
        a PythonREPL and any user-provided extra_tools.

    Example:
        .. code-block:: python

            from langchain_cohere import ChatCohere, create_csv_agent

            llm = ChatCohere(model="command-a-03-2025", temperature=0)
            agent_executor = create_csv_agent(
                llm,
                "titanic.csv"
            )
            resp = agent_executor.invoke({"input":"How many people were on the titanic?"})
            print(resp.get("output"))
    """  # noqa: E501
    try:
        import pandas as pd
    except ImportError:
        raise ImportError(
            "pandas package not found, please install with `pip install pandas`."
        )

    _kwargs = pandas_kwargs or {}
    if isinstance(path, (str)):
        df = pd.read_csv(path, **_kwargs)

    elif isinstance(path, list):
        df = []
        for item in path:
            if not isinstance(item, (str, IOBase)):
                raise ValueError(
                    f"Expected str or file-like object, got {type(path)}"
                )
            df.append(pd.read_csv(item, **_kwargs))
    else:
        raise ValueError(
            f"Expected str, list, or file-like object, got {type(path)}"
        )

    if not prompt:
        prompt = _get_prompt(path, number_of_head_rows)

    final_tools = [
        get_file_read_tool(),
        get_file_peek_tool(),
        get_python_tool(),
    ] + extra_tools
    if "preamble" in llm.__dict__ and not llm.__dict__.get(
        "preamble"
    ):
        llm = ChatCohere(**llm.__dict__)
        llm.preamble = CSV_PREAMBLE.format(
            current_date=datetime.now().strftime(
                "%A, %B %d, %Y %H:%M:%S"
            )
        )

    agent = create_tool_calling_agent(
        llm=llm, tools=final_tools, prompt=prompt
    )
    agent_executor = AgentExecutor(
        agent=agent,
        tools=final_tools,
        verbose=verbose,
        return_intermediate_steps=return_intermediate_steps,
    )
    return agent_executor
```

# Using the CSV agent

Let's create a dummy CSV file for demo

```python
import csv

# Data to be written to the CSV file
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
# Try out an example
llm = ChatCohere(model="command-a-03-2025", temperature=0)
agent_executor = create_csv_agent(llm, "movies_tickets.csv")
resp = agent_executor.invoke(
    {"input": "Who all watched Shawshank redemption?"}
)
print(resp.get("output"))
```

The output returned is:

```
John, Jerry, Jack and Jeremy watched Shawshank Redemption.
```


# A Data Analyst Agent Built with Cohere and Langchain

> This page describes how to build a data-analysis system out of Cohere's models.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/agents/Data_Analyst_Agent_Cohere_and_Langchain.ipynb" />

Tool use is a method which allows developers to connect Cohere's Command models to external tools like search engines, APIs, databases, and other software tools. Just like how [Retrieval-Augmented Generation (RAG)](https://docs.cohere.com/docs/retrieval-augmented-generation-rag) allows a model to use an external data source to improve factual generation, tool use is a capability that allows retrieving data from multiple sources. But it goes beyond simply retrieving information and is able to use software tools to execute code, or even create entries in a CRM system.

In this notebook, we'll see how we can use two tools to create a simple data analyst agent that is able to search the web and run code in a python interpreter. This agent uses Cohere's Command R+ mode and Langchain.

<img alt="" src="https://raw.githubusercontent.com/cohere-ai/cohere-developer-experience/main/notebooks/images/tool-use-notebook-header.png" />

Let's start by installing the required libraries

```python PYTHON
! pip install --quiet langchain langchain_cohere langchain_experimental
```

## Setup

We'll need a Cohere API key here. Grab your key and paste it in the next slide if you have one, or [register](https://dashboard.cohere.ai/welcome/register) and create a new API key.

```python PYTHON
### LLMs
import os
os.environ['COHERE_API_KEY'] = "<insert api="" cohere="" here="" key="">"
```

```python PYTHON
from langchain_cohere.chat_models import ChatCohere
chat = ChatCohere(model="command-a-03-2025", temperature=0.3)
```

Our simple data analyst will be equipped with a web search tool, and a python interpreter (which we can use to run plotting code, for example).

### Web search

Let's first equip our agent with web search! We can use the Tavily API for this. Head on to [tavily.com](https://tavily.com) and grab an API key to use here.

```python PYTHON
from langchain_community.tools.tavily_search import TavilySearchResults

os.environ['TAVILY_API_KEY'] = "<insert api="" here="" key="" tavily="">"

internet_search = TavilySearchResults()
internet_search.name = "internet_search"
internet_search.description = "Returns a list of relevant document snippets for a textual query retrieved from the internet."


from langchain_core.pydantic_v1 import BaseModel, Field
class TavilySearchInput(BaseModel):
    query: str = Field(description="Query to search the internet with")
internet_search.args_schema = TavilySearchInput
```

### Python interpreter tool

Let's equip our agent with a python interpreter!

```python PYTHON
from langchain.agents import Tool
from langchain_experimental.utilities import PythonREPL

python_repl = PythonREPL()
repl_tool = Tool(
    name="python_repl",
    description="Executes python code and returns the result. The code runs in a static sandbox without interactive mode, so print output or save output to a file.",
    func=python_repl.run,
)
repl_tool.name = "python_interpreter"

class ToolInput(BaseModel):
    code: str = Field(description="Python code to execute.")
repl_tool.args_schema = ToolInput

```

```python PYTHON
from langchain.agents import AgentExecutor
from langchain_cohere.react_multi_hop.agent import create_cohere_react_agent
from langchain_core.prompts import ChatPromptTemplate
```

```python PYTHON
prompt = ChatPromptTemplate.from_template("{input}")


agent = create_cohere_react_agent(
    llm=chat,
    tools=[internet_search, repl_tool],
    prompt=prompt,
)
```

```python PYTHON
agent_executor = AgentExecutor(agent=agent, tools=[internet_search, repl_tool], verbose=True)
```

```python PYTHON
agent_executor.invoke({
    "input": "Create a plot of the number of full time employees at the 3 tech companies with the highest market cap in the United States in 2024.",
})
```

```txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
First, I will search for the three tech companies with the highest market cap in the US in 2024. Then, I will search for the number of full-time employees at each of these companies, and plot the data using Python.
{'tool_name': 'internet_search', 'parameters': {'query': 'top 3 tech companies highest market cap US 2024'}}
[0m[36;1m[1;3m[{'url': 'https://www.fool.com/research/largest-companies-by-market-cap/', 'content': "It's the most valuable automaker in the world and has the world's best-selling car in the Model Y.\nTesla is most famous for its vehicles, and it's second only to China's BYD Company (OTC:BYDDY) among the largest EV companies in terms of manufacturing. While it's most famous for Windows, Microsoft also has a diverse selection of products and services that has helped to build on its success, including:\nMicrosoft has been the world's largest company before, and it briefly surpassed Apple for the biggest market cap in 2021. Walmart\nWalmart (NYSE:WMT) may not have the largest market cap, but it is No. 1 in terms of revenue, and it’s the largest retailer in the world. Microsoft\nConsidering the popularity of the Windows operating system, it’s no surprise that Microsoft (NASDAQ:MSFT) has consistently ranked as one of the largest companies in the world. Although the top spot has changed hands on multiple occasions, Apple has spent the most time there and is currently the most valuable company in the world.\n"}, {'url': 'https://www.financecharts.com/screener/biggest-country-us', 'content': 'Biggest Companies in the US by Market Cap for Apr 2024. The most valuable company in the US is Microsoft (MSFT) with a market cap of $3.159T, followed by Apple (AAPL) and NVIDIA (NVDA). Last updated Apr 05, 2024.'}, {'url': 'https://www.statista.com/statistics/1350976/leading-tech-companies-worldwide-by-market-cap/', 'content': 'Digital &amp; Trend reports\nOverview and forecasts on trending topics\nIndustry &amp; Market reports\nIndustry and market insights and forecasts\nCompanies &amp; Products reports\nKey figures and rankings about companies and products\nConsumer &amp; Brand reports\nConsumer and brand insights and preferences in various industries\nPolitics &amp; Society reports\nDetailed information about political and social topics\nCountry &amp; Region reports\nAll key figures about countries and regions\nMarket forecast and expert KPIs for 1000+ markets in 190+ countries &amp; territories\nInsights on consumer attitudes and behavior worldwide\nBusiness information on 100m+ public and private companies\nExplore Company Insights\nDetailed information for 39,000+ online stores and marketplaces\nDirectly accessible data for 170 industries from 150+ countries\nand over 1\xa0Mio. facts.\n Other statistics on the topicAI chips\nHardware\nLeading semiconductor companies worldwide 2023, by market cap\nHardware\nSemiconductor market revenue growth worldwide 1988-2024\nHardware\nNvidia revenue worldwide 2015-2023, by segment\nHardware\nSemiconductor market size worldwide 2020-2030, by application\nYou only have access to basic statistics.\n Other statistics that may interest you\nOther statistics that may interest you Statistics on\nAbout the industry\nAbout the region\nOther regions\nRelated statistics\nFurther related statistics\nFurther Content: You might find this interesting as well\nStatistics\nTopics Transforming data into design:\nStatista Content &amp; Design\nStrategy and business building for the data-driven economy:\nLeading tech companies worldwide 2023, by market cap\nApple\nSamsung\nLeading tech companies worldwide 2023, by market capitalization\n(in billion U.S. dollars)\n Additional Information\nShow sources information\nShow publisher information\nUse Ask Statista Research Service\nAugust 2023\nWorldwide\n2023\n'}, {'url': 'https://www.forbes.com/advisor/investing/best-tech-stocks/', 'content': 'eToro\nThe Best Tech Stocks of November 2023\nApple Inc. (AAPL)\n$2.8 trillion\n0.5%\n27.1%\n$2.8 trillion\n0.5%\n27.1%\nApple\xa0 was founded in Los Altos, Calif., by Steve Jobs and Steve Wozniak in 1976. ASML Holding NV (ASML)\n$248 billion\n1.0%\n22.8%\n$248 billion\n1.0%\n22.8%\nASML is a Netherlands-based company that designs and manufactures the machinery used by companies that make microchips. Taiwan Semiconductor Manufacturing Company (TSM)\n$443 billion\n2.0%\n20.6%\n$443 billion\n2.0%\n20.6%\nTaiwan Semiconductor Manufacturing Company could be the biggest tech company you’ve never heard of. NVIDIA Corp (NVDA)\n$1.1 trillion\n0.0%\n62.8%\n$1.1 trillion\n0.0%\n62.8%\nNVIDIA was founded in 1993 to produce graphic cards for the burgeoning personal computer market. Microsoft Corporation (MSFT)\n$2.6 trillion\n0.8%\n27.3%\n$2.6 trillion\n0.8%\n27.3%\nMicrosoft\xa0 was founded in 1975 by Bill Gates and Paul Allen in Albuquerque, N.M.'}, {'url': 'https://disfold.com/united-states/sector/technology/companies/', 'content': 'Unlock Financial AI:\nStart your Free Trial of\nDisfold AI, Now!\nTop Technology Companies from the United States as of Jan. 01, 2024\n(Dec. 1, 2023)\nTop Technology Companies from the United States as of Jan. 01, 2024\n1.\nApple\nMarket Cap (USD):\n$2.866 T\nStock:\nAAPL\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nConsumer Electronics\n2.\nMicrosoft\nMarket Cap (USD):\n$2.755 T\nStock:\nMSFT\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Infrastructure\n3.\nNvidia\nMarket Cap (USD):\n$1.186 T\nStock:\nNVDA\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n4.\nBroadcom\nMarket Cap (USD):\n$495.95 B\nStock:\nAVGO\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n5.\nOracle\nMarket Cap (USD):\n$282.01 B\nStock:\nORCL\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Infrastructure\n6.\n Marvell Technology, Inc.\nMarket Cap (USD):\n$49.61 B\nStock:\n9MW\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n35.\nAutodesk, Inc.\nMarket Cap (USD):\n$48.97 B\nStock:\nADSK\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Application\n36.\nMicrochip Technology Incorporated\nMarket Cap (USD):\n$45.77 B\nStock:\nMCHP\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n37.\nFortinet, Inc.\nMarket Cap (USD):\n$44.84 B\nStock:\n Analog Devices\nMarket Cap (USD):\n$93.79 B\nStock:\nADI\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n20.\nMicron Technology, Inc.\nMarket Cap (USD):\n$91.30 B\nStock:\nMU\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n21.\nPalo Alto Networks\nMarket Cap (USD):\n$90.41 B\nStock:\nPANW\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Infrastructure\n22.\n Fiserv\nMarket Cap (USD):\n$79.73 B\nStock:\nFI\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nInformation Technology Services\n23.\nKLA\nMarket Cap (USD):\n$75.13 B\nStock:\nKLAC\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductor Equipment &amp; Materials\n24.\nSynopsys\nMarket Cap (USD):\n$74.64 B\nStock:\nSNPS\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Infrastructure\n25.\n Salesforce\nMarket Cap (USD):\n$243.78 B\nStock:\nCRM\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Application\n8.\nAMD\nMarket Cap (USD):\n$219.72 B\nStock:\nAMD\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n9.\nCisco\nMarket Cap (USD):\n$205.21 B\nStock:\nCSCO\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nCommunication Equipment\n10.\n'}][0m[32;1m[1;3m
I have found that the three tech companies with the highest market cap in the US in 2024 are Microsoft, Apple and NVIDIA. Now, I will search for the number of full-time employees at each of these companies and plot the data.
{'tool_name': 'internet_search', 'parameters': {'query': 'Microsoft full time employees 2024'}}
[0m[36;1m[1;3m[{'url': 'https://www.statista.com/statistics/273475/number-of-employees-at-the-microsoft-corporation-since-2005/', 'content': 'Digital &amp; Trend reports\nOverview and forecasts on trending topics\nIndustry &amp; Market reports\nIndustry and market insights and forecasts\nCompanies &amp; Products reports\nKey figures and rankings about companies and products\nConsumer &amp; Brand reports\nConsumer and brand insights and preferences in various industries\nPolitics &amp; Society reports\nDetailed information about political and social topics\nCountry &amp; Region reports\nAll key figures about countries and regions\nMarket forecast and expert KPIs for 1000+ markets in 190+ countries &amp; territories\nInsights on consumer attitudes and behavior worldwide\nBusiness information on 100m+ public and private companies\nExplore Company Insights\nDetailed information for 39,000+ online stores and marketplaces\nDirectly accessible data for 170 industries from 150+ countries\nand over 1\xa0Mio. facts.\n Other statistics on the topicMicrosoft\nSoftware\nMicrosoft\'s expenditure on research and development 2002-2023\nSoftware\nOffice productivity software market share worldwide 2022\nIT Services\nCloud infrastructure services market share quarterly worldwide 2017-2022, by vendor\nSoftware\nMicrosoft\'s revenue 2008-2024, by fiscal quarter\nTo download this statistic in XLS format you need a Statista Account\nTo download this statistic in PNG format you need a Statista Account\nTo download this statistic in PDF format you need a Statista Account\nTo download this statistic in PPT format you need a Statista Account\nAs a Premium user you get access to the detailed source references and background information about this statistic.\n Statistics on\n"\nMicrosoft\n"\nOther statistics that may interest you Microsoft\nOverview\nCompany financials\nSegments\nCompetitors: Software\nCompetitors: Cloud\nCompetitors: Devices\nFurther related statistics\nFurther Content: You might find this interesting as well\nStatistics\nTopics Number of Microsoft employees 2005-2023\nHow many employees does Microsoft have?\nNumber of employees at the Microsoft Corporation from 2005 to 2023\n(in 1,000s)\nAdditional Information\nShow sources information\nShow publisher information\nUse Ask Statista Research Service\nJuly 2023\nWorldwide\n2005 to 2023\nMicrosoft\'s fiscal year ends on June 30.\n Transforming data into design:\nStatista Content &amp; Design\nStrategy and business building for the data-driven economy:\nIndustry-specific and extensively researched technical data (partially from exclusive partnerships).'}, {'url': 'https://stockanalysis.com/stocks/msft/employees/', 'content': "MSFT News. 1 day ago - Microsoft Pushes LinkedIn Further Into the Connected Economy - PYMNTS 1 day ago - Softchoice to Advance Generative AI and Security Solutions Through New Agreement With Microsoft - Business Wire 1 day ago - AMD, Samsung, Check Point, Microsoft, and Other Tech Stocks in Focus Today - Barrons 1 day ago - Don't chase the value rebound, tech still has a few surprises up its ..."}, {'url': 'https://www.macrotrends.net/stocks/charts/MSFT/microsoft/number-of-employees', 'content': 'Interactive chart of Microsoft (MSFT) annual worldwide employee count from 2010 to 2023. Microsoft total number of employees in 2023 was 221,000, a 0% decline from 2022. Microsoft total number of employees in 2022 was 221,000, a 22.1% increase from 2021. Microsoft total number of employees in 2021 was 181,000, a 11.04% increase from 2020.'}, {'url': 'https://www.microsoft.com/investor/reports/ar23/index.html', 'content': 'As of June 30, 2023, we employed approximately 221,000 people on a full-time basis, 120,000 in the U.S. and 101,000 internationally. Of the total employed people, 89,000 were in operations, including manufacturing, distribution, product support, and consulting services; 72,000 were in product research and development; 45,000 were in sales and ...'}, {'url': 'https://www.microsoft.com/en-us/investor/earnings/fy-2024-q2/press-release-webcast', 'content': 'Microsoft Cloud Strength Drives Second Quarter Results. REDMOND, Wash. — January 30, 2024 — Microsoft Corp. today announced the following results for the quarter ended December 31, 2023, as compared to the corresponding period of last fiscal year: · Revenue was $62.0 billion and increased 18% (up 16% in constant currency) · Operating income was $27.0 billion and increased 33%, and ...'}][0m[32;1m[1;3m
{'tool_name': 'internet_search', 'parameters': {'query': 'Apple full time employees 2024'}}
[0m[36;1m[1;3m[{'url': 'https://www.macrotrends.net/stocks/charts/AAPL/apple/number-of-employees', 'content': 'Employee Count. Interactive chart of Apple (AAPL) annual worldwide employee count from 2010 to 2023. Apple total number of employees in 2023 was 161,000, a 1.83% decline from 2022. Apple total number of employees in 2022 was 164,000, a 6.49% increase from 2021. Apple total number of employees in 2021 was 154,000, a 4.76% increase from 2020.'}, {'url': 'https://www.businessinsider.com/apple-layoffs-tim-cook-getting-serious-challenges-car-china-iphone-2024-4?op=1', 'content': "2024-04-05T12:27:33Z An curved arrow pointing right. Share. The ... That's especially so when considering that Apple had about 161,000 full-time employees at the end of its last fiscal year."}, {'url': 'https://www.statista.com/statistics/273439/number-of-employees-of-apple-since-2005/', 'content': 'Digital &amp; Trend reports\nOverview and forecasts on trending topics\nIndustry &amp; Market reports\nIndustry and market insights and forecasts\nCompanies &amp; Products reports\nKey figures and rankings about companies and products\nConsumer &amp; Brand reports\nConsumer and brand insights and preferences in various industries\nPolitics &amp; Society reports\nDetailed information about political and social topics\nCountry &amp; Region reports\nAll key figures about countries and regions\nMarket forecast and expert KPIs for 1000+ markets in 190+ countries &amp; territories\nInsights on consumer attitudes and behavior worldwide\nBusiness information on 100m+ public and private companies\nExplore Company Insights\nDetailed information for 39,000+ online stores and marketplaces\nDirectly accessible data for 170 industries from 150+ countries\nand over 1\xa0Mio. facts.\n Other statistics on the topicApple\nConsumer Electronics\nApple\'s revenue worldwide 2004-2023\nConsumer Electronics\nApple\'s revenue broken down by geographical region 2012-2023, by quarter\nTelecommunications\nQuarterly market share of smartphone vendors in the U.S. 2016-2023\nConsumer Electronics\nApple: expenditure on research and development 2007-2023\nTo download this statistic in XLS format you need a Statista Account\nTo download this statistic in PNG format you need a Statista Account\nTo download this statistic in PDF format you need a Statista Account\nTo download this statistic in PPT format you need a Statista Account\nAs a Premium user you get access to the detailed source references and background information about this statistic.\n Statistics on\n"\nApple in the U.S.\n"\nOther statistics that may interest you Apple in the U.S.\nOverview: Apple\nOverview: Apple in the U.S.\nSegment: iPhone\nSegment: iPad\nSegment: Mac\nSegment: Wearables &amp; Smart home\nFurther related statistics\nFurther Content: You might find this interesting as well\nStatistics\nTopics Number of employees of Apple 2005-2023\nApple Corporation – additional information\nApple products\nApple\'s number of employees in the fiscal years 2005 to 2023\n(in 1,000s)\nAdditional Information\nShow sources information\nShow publisher information\nUse Ask Statista Research Service\nNovember 2023\nWorldwide\n2005 to 2023\n Transforming data into design:\nStatista Content &amp; Design\nStrategy and business building for the data-driven economy:\nIndustry-specific and extensively researched technical data (partially from exclusive partnerships).'}, {'url': 'https://jobs.apple.com/en-us/details/200542480/fy-24-full-time-opportunity-for-fresh-graduates-general', 'content': "Shop and Learn\nServices\nAccount\nApple Store\nFor Business\nFor Education\nFor Healthcare\nFor Government\nApple Values\nAbout Apple Summary\nKey Qualifications\nDescription\nEducation &amp; Experience\nAdditional Requirements\nAdd a favorite\nDon’t have an Apple ID?\nApple Footer\nApple is an equal opportunity employer that is committed to inclusion and diversity. If you’re applying for a position in San Francisco,review the\nSan Francisco Fair Chance Ordinance guidelines (opens in a new window)\napplicable in your area.\n FY'24 Full Time Opportunity for Fresh Graduates - General\nAdd a favorite\nDon’t have an Apple ID?\n Learn more about your EEO rights as an applicant (Opens in a new window) .\n"}, {'url': 'https://jobs.apple.com/en-us/details/200544662/wiml-2024-full-time-opportunities-at-apple', 'content': 'Shop and Learn\nServices\nAccount\nApple Store\nFor Business\nFor Education\nFor Healthcare\nFor Government\nApple Values\nAbout Apple Summary\nKey Qualifications\nDescription\nEducation &amp; Experience\nAdditional Requirements\nAdd a favorite\nDon’t have an Apple ID?\nApple Footer\nApple is an equal opportunity employer that is committed to inclusion and diversity. If you’re applying for a position in San Francisco,review the\nSan Francisco Fair Chance Ordinance guidelines (opens in a new window)\napplicable in your area.\n WiML 2024 - Full Time Opportunities at Apple\nAdd a favorite\nDon’t have an Apple ID?\n Learn more about your EEO rights as an applicant (Opens in a new window) .\n'}][0m[32;1m[1;3m
{'tool_name': 'internet_search', 'parameters': {'query': 'NVIDIA full time employees 2024'}}
[0m[36;1m[1;3m[{'url': 'https://www.macrotrends.net/stocks/charts/NVDA/nvidia/number-of-employees', 'content': 'Employee Count. Interactive chart of NVIDIA (NVDA) annual worldwide employee count from 2010 to 2024. NVIDIA total number of employees in 2024 was 29,600, a 12.99% increase from 2023. NVIDIA total number of employees in 2023 was 26,196, a 16.57% increase from 2022. NVIDIA total number of employees in 2022 was 22,473, a 18.43% increase from 2021.'}, {'url': 'https://www.statista.com/statistics/1369575/nvidia-number-of-employees-by-region/', 'content': 'Digital &amp; Trend reports\nOverview and forecasts on trending topics\nIndustry &amp; Market reports\nIndustry and market insights and forecasts\nCompanies &amp; Products reports\nKey figures and rankings about companies and products\nConsumer &amp; Brand reports\nConsumer and brand insights and preferences in various industries\nPolitics &amp; Society reports\nDetailed information about political and social topics\nCountry &amp; Region reports\nAll key figures about countries and regions\nMarket forecast and expert KPIs for 1000+ markets in 190+ countries &amp; territories\nInsights on consumer attitudes and behavior worldwide\nBusiness information on 100m+ public and private companies\nExplore Company Insights\nDetailed information for 39,000+ online stores and marketplaces\nDirectly accessible data for 170 industries from 150+ countries\nand over 1\xa0Mio. facts.\n Other statistics on the topicNvidia\nHardware\nSemiconductor market revenue worldwide 1987-2024\nHardware\nLeading semiconductor companies worldwide 2024, by market cap\nHardware\nSemiconductor companies market revenue share worldwide 2008-2023\nHardware\nSemiconductor market revenue growth worldwide 1988-2024\nTo download this statistic in XLS format you need a Statista Account\nTo download this statistic in PNG format you need a Statista Account\nTo download this statistic in PDF format you need a Statista Account\nTo download this statistic in PPT format you need a Statista Account\nAs a Premium user you get access to the detailed source references and background information about this statistic.\n Nvidia number of employees 2023, by region\nNvidia number of employees in 2023, by region\nAdditional Information\nShow sources information\nShow publisher information\nUse Ask Statista Research Service\nJuly 2023\nWorldwide\n2023\nIncludes full-time and part-time employees.\n Statistics on\n"\nNvidia\n"\nOther statistics that may interest you Nvidia\nOverview\nFinancials\nSegments\nESG\nCompetitors\nFurther Content: You might find this interesting as well\nTopics Transforming data into design:\nStatista Content &amp; Design\nStrategy and business building for the data-driven economy:\nIndustry-specific and extensively researched technical data (partially from exclusive partnerships).'}, {'url': 'https://finance.yahoo.com/news/nvidia-announces-financial-results-fourth-212000202.html', 'content': "Proceeds related to employee stock plans\n-\n5\n403\n355\nPayments related to repurchases of common stock\n(2,660\n)\n(1,212\n)\n(9,533\n)\n(10,039\n)\nPayments related to tax on restricted stock units\n(841\n)\n(344\n)\n(2,783\n)\n(1,475\n)\nRepayment of debt\n-\n-\n(1,250\n)\n-\nDividends paid\n(99\n)\n(98\n)\n(395\n)\n(398\n)\nPrincipal payments on property and equipment and intangible assets\n(29\n)\n(4\n)\n(74\n)\n(58\n)\nOther\n-\n(3\n)\n(1\n)\n(2\n)\nNet cash used in financing activities\n(3,629\n)\n(1,656\n)\n(13,633\n)\n(11,617\n)\nChange in cash and cash equivalents\n1,761\n589\n3,891\n1,399\nCash and cash equivalents at beginning of period\n5,519\n2,800\n3,389\n1,990\nCash and cash equivalents at end of period\n$\n7,280\n$\n3,389\n$\n7,280\n$\n3,389\nSupplemental disclosures of cash flow information:\nCash paid for income taxes, net\n$\n1,874\n$\n32\n$\n6,549\n$\n1,404\nCash paid for interest\n$\n26\n$\n28\n$\n252\n$\n254\nNVIDIA CORPORATION\nRECONCILIATION OF GAAP TO NON-GAAP FINANCIAL MEASURES\n(In millions, except per share data)\n(Unaudited)\nThree Months Ended\nTwelve Months Ended\nJanuary 28,\nOctober 29,\nJanuary 29,\nJanuary 28,\nJanuary 29,\n2024\n2023\n2023\n2024\n2023\nGAAP gross profit\n$\n16,791\n$\n13,400\n$\n3,833\n$\n44,301\n$\n15,356\nGAAP gross margin\n76.0\n%\n74.0\n%\n63.3\n%\n72.7\n%\n56.9\n%\nAcquisition-related and other costs (A)\n119\n119\n120\n477\n455\nStock-based compensation expense (B)\n45\n38\n30\n141\n138\nIP-related costs\n4\n26\n16\n40\n16\nNon-GAAP gross profit\n$\n16,959\n$\n13,583\n$\n3,999\n$\n44,959\n$\n15,965\nNon-GAAP gross margin\n76.7\n%\n75.0\n%\n66.1\n%\n73.8\n%\n59.2\n%\nGAAP operating expenses\n$\n3,176\n$\n2,983\n$\n2,576\n$\n11,329\n$\n11,132\nStock-based compensation expense (B)\n(948\n)\n(941\n)\n(709\n)\n(3,408\n)\n(2,572\n)\nAcquisition-related and other costs (A)\n(18\n)\n(16\n)\n(54\n)\n(106\n)\n(219\n)\nAcquisition termination cost\n-\n-\n-\n-\n(1,353\n)\nOther (C)\n-\n-\n(38\n)\n10\n(63\n)\nNon-GAAP operating expenses\n$\n2,210\n$\n2,026\n$\n1,775\n$\n7,825\n$\n6,925\nGAAP operating income\n$\n13,615\n$\n10,417\n$\n1,257\n$\n32,972\n$\n4,224\nTotal impact of non-GAAP adjustments to operating income\n1,134\n1,140\n967\n4,162\n4,816\nNon-GAAP operating income\n$\n14,749\n$\n11,557\n$\n2,224\n$\n37,134\n$\n9,040\nGAAP other income (expense), net\n$\n491\n$\n105\n$\n32\n$\n846\n$\n(43\n)\n(Gains) losses from non-affiliated investments\n(260\n)\n69\n10\n(238\n)\n45\nInterest expense related to amortization of debt discount\n1\n1\n1\n4\n5\nNon-GAAP other income (expense), net\n$\n232\n$\n175\n$\n43\n$\n612\n$\n7\nGAAP net income\n$\n12,285\n$\n9,243\n$\n1,414\n$\n29,760\n$\n4,368\nTotal pre-tax impact of non-GAAP adjustments\n875\n1,210\n978\n3,928\n4,865\nIncome tax impact of non-GAAP adjustments (D)\n(321\n)\n(433\n)\n(218\n)\n(1,376\n)\n(867\n)\n Other, net\n260\n(18\n)\n237\n(48\n)\nOther income (expense), net\n491\n32\n846\n(43\n)\nIncome before income tax\n14,106\n1,289\n33,818\n4,181\nIncome tax expense (benefit)\n1,821\n(125\n)\n4,058\n(187\n)\nNet income\n$\n12,285\n$\n1,414\n$\n29,760\n$\n4,368\nNet income per share:\nBasic\n$\n4.98\n$\n0.57\n$\n12.05\n$\n1.76\nDiluted\n$\n4.93\n$\n0.57\n$\n11.93\n$\n1.74\nWeighted average shares used in per share computation:\nBasic\n2,466\n2,464\n2,469\n2,487\nDiluted\n2,490\n2,477\n2,494\n2,507\nNVIDIA CORPORATION\nCONDENSED CONSOLIDATED BALANCE SHEETS\n(In millions)\n(Unaudited)\nJanuary 28,\nJanuary 29,\n2024\n2023\nASSETS\nCurrent assets:\nCash, cash equivalents and marketable securities\n$\n25,984\n$\n13,296\nAccounts receivable, net\n9,999\n3,827\nInventories\n5,282\n5,159\nPrepaid expenses and other current assets\n3,080\n791\nTotal current assets\n44,345\n23,073\nProperty and equipment, net\n3,914\n3,807\nOperating lease assets\n1,346\n1,038\nGoodwill\n4,430\n4,372\nIntangible assets, net\n1,112\n1,676\nDeferred income tax assets\n6,081\n3,396\nOther assets\n4,500\n3,820\nTotal assets\n$\n65,728\n$\n41,182\nLIABILITIES AND SHAREHOLDERS' EQUITY\nCurrent liabilities:\nAccounts payable\n$\n2,699\n$\n1,193\nAccrued and other current liabilities\n6,682\n4,120\nShort-term debt\n1,250\n1,250\nTotal current liabilities\n10,631\n6,563\nLong-term debt\n8,459\n9,703\nLong-term operating lease liabilities\n1,119\n902\nOther long-term liabilities\n2,541\n1,913\nTotal liabilities\n22,750\n19,081\nShareholders' equity\n42,978\n22,101\nTotal liabilities and shareholders' equity\n$\n65,728\n$\n41,182\nNVIDIA CORPORATION\nCONDENSED CONSOLIDATED STATEMENTS OF CASH FLOWS\n(In millions)\n(Unaudited)\nThree Months Ended\nTwelve Months Ended\nJanuary 28,\nJanuary 29,\nJanuary 28,\nJanuary 29,\n2024\n2023\n2024\n2023\nCash flows from operating activities:\nNet income\n$\n12,285\n$\n1,414\n$\n29,760\n$\n4,368\nAdjustments to reconcile net income to net cash\nprovided by operating activities:\nStock-based compensation expense\n993\n738\n3,549\n2,709\nDepreciation and amortization\n387\n426\n1,508\n1,544\nDeferred income taxes\n(78\n)\n(647\n)\n(2,489\n)\n(2,164\n)\n(Gains) losses on investments in non-affiliated entities, net\n(260\n)\n10\n(238\n)\n45\nAcquisition termination cost\n-\n-\n-\n1,353\nOther\n(109\n)\n20\n(278\n)\n(7\n)\nChanges in operating assets and liabilities, net of acquisitions:\n Q4 Fiscal 2024 Summary\nGAAP\n($ in millions, except earnings per share)\nQ4 FY24\nQ3 FY24\nQ4 FY23\nQ/Q\nY/Y\nRevenue\n$22,103\n$18,120\n$6,051\nUp 22%\nUp 265%\nGross margin\n76.0%\n74.0%\n63.3%\nUp 2.0 pts\nUp 12.7 pts\nOperating expenses\n$3,176\n$2,983\n$2,576\nUp 6%\nUp 23%\nOperating income\n$13,615\n$10,417\n$1,257\nUp 31%\nUp 983%\nNet income\n$12,285\n$9,243\n$1,414\nUp 33%\nUp 769%\nDiluted earnings per share\n$4.93\n$3.71\n$0.57\nUp 33%\nUp 765%\nNon-GAAP\n($ in millions, except earnings per share)\nQ4 FY24\nQ3 FY24\nQ4 FY23\nQ/Q\nY/Y\nRevenue\n$22,103\n$18,120\n$6,051\nUp 22%\nUp 265%\nGross margin\n76.7%\n75.0%\n66.1%\nUp 1.7 pts\nUp 10.6 pts\nOperating expenses\n$2,210\n$2,026\n$1,775\nUp 9%\nUp 25%\nOperating income\n$14,749\n$11,557\n$2,224\nUp 28%\nUp 563%\nNet income\n$12,839\n$10,020\n$2,174\nUp 28%\nUp 491%\nDiluted earnings per share\n$5.16\n$4.02\n$0.88\nUp 28%\nUp 486%\nFiscal 2024 Summary\nGAAP\n($ in millions, except earnings per share)\n 2024\n2023\n2023\n2024\n2023\nCost of revenue\n$\n119\n$\n119\n$\n120\n$\n477\n$\n455\nResearch and development\n$\n12\n$\n12\n$\n10\n$\n49\n$\n39\nSales, general and administrative\n$\n6\n$\n4\n$\n44\n$\n57\n$\n180\n(B) Stock-based compensation consists of the following:\nThree Months Ended\nTwelve Months Ended\nJanuary 28,\nOctober 29,\nJanuary 29,\nJanuary 28,\nJanuary 29,\n2024\n2023\n2023\n2024\n2023\nCost of revenue\n$\n45\n$\n38\n$\n30\n$\n141\n$\n138\nResearch and development\n$\n706\n$\n701\n$\n527\n$\n2,532\n$\n1,892\nSales, general and administrative\n NVIDIA CORPORATION\nCONDENSED CONSOLIDATED STATEMENTS OF INCOME\n(In millions, except per share data)\n(Unaudited)\nThree Months Ended\nTwelve Months Ended\nJanuary 28,\nJanuary 29,\nJanuary 28,\nJanuary 29,\n2024\n2023\n2024\n2023\nRevenue\n$\n22,103\n$\n6,051\n$\n60,922\n$\n26,974\nCost of revenue\n5,312\n2,218\n16,621\n11,618\nGross profit\n16,791\n3,833\n44,301\n15,356\nOperating expenses\nResearch and development\n2,465\n1,951\n8,675\n7,339\nSales, general and administrative\n711\n625\n2,654\n2,440\nAcquisition termination cost\n-\n-\n-\n1,353\nTotal operating expenses\n3,176\n2,576\n11,329\n11,132\nOperating Income\n13,615\n1,257\n32,972\n4,224\nInterest income\n294\n115\n866\n267\nInterest expense\n(63\n)\n(65\n)\n(257\n)\n(262\n)\n"}, {'url': 'https://stockanalysis.com/stocks/nvda/employees/', 'content': 'NVIDIA had 29,600 employees on January 28, 2024. The number of employees increased by 3,404 or 12.99% compared to the previous year. Employees 29,600. Change (1Y) 3,404. ... Real-time quotes provided by IEX Cloud. Other market data may be delayed by 15 minutes or more. ...'}, {'url': 'https://investor.nvidia.com/news/press-release-details/2024/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2024/?ref=robotradingnet.ghost.io', 'content': 'SANTA CLARA, Calif., Feb. 21, 2024 (GLOBE NEWSWIRE) -- NVIDIA (NASDAQ: NVDA) today reported revenue for the fourth quarter ended January 28, 2024, of $22.1 billion, up 22% from the previous quarter and up 265% from a year ago. For the quarter, GAAP earnings per diluted share was $4.93, up 33% from the previous quarter and up 765% from a year ...'}][0m[32;1m[1;3m
I have found the following data on the number of full-time employees at each company:
Microsoft: 221,000
Apple: 161,000
NVIDIA: 29,600
Now, I will write and execute Python code to plot this data.
{'tool_name': 'python_interpreter', 'parameters': {'code': 'import matplotlib.pyplot as plt\n\n# Data on the number of full-time employees at each company\ncompanies = [\n    "Microsoft", "Apple", "NVIDIA"\n]\nfull_time_employees = [221000, 161000, 29600]\n\n# Plot the data\nplt.bar(companies, full_time_employees)\nplt.xlabel("Company")\nplt.ylabel("Number of Full Time Employees")\nplt.xticks(rotation=45)\nplt.tight_layout()\nplt.savefig("tech_companies_market_cap_employees.png")'}}
[0m[33;1m[1;3m[0m[32;1m[1;3mRelevant Documents: 0,1,3,4,5,7,8,9,10,11,12,15,18,20
Cited Documents: 1,3,4,7,8,10,11,15,18,20
Answer: Here is a plot showing the number of full-time employees at the three US tech companies with the highest market cap in 2024:

<img alt="Number of Full Time Employees" src="'tech_companies_market_cap_employees.png'"/>

The companies with the highest number of full-time employees are Microsoft with 221,000, Apple with 161,000 and NVIDIA with 29,600.
Grounded answer: Here is a plot showing the number of full-time employees at the three US tech companies with the highest market cap in 2024:
<co: 20="">! [Number of Full Time Employees]('tech_companies_market_cap_employees.png')</co:>

The companies with the highest number of full-time employees are <co: 1,4="">Microsoft</co:> with <co: 7,8="">221,000</co:>, <co: 1,3,4="">Apple</co:> with <co: 10,11="">161,000</co:> and <co: 1,4="">NVIDIA</co:> with <co: 15,18="">29,600</co:>.[0m

[1m> Finished chain.[0m





{'input': 'Create a plot of the number of full time employees at the 3 tech companies with the highest market cap in the United States in 2024.',
 'output': "Here is a plot showing the number of full-time employees at the three US tech companies with the highest market cap in 2024:\n! [Number of Full Time Employees]('tech_companies_market_cap_employees.png')\n\nThe companies with the highest number of full-time employees are Microsoft with 221,000, Apple with 161,000 and NVIDIA with 29,600.",
 'citations': [CohereCitation(start=125, end=201, text="! [Number of Full Time Employees]('tech_companies_market_cap_employees.png')", documents=[{'output': ''}]),
  CohereCitation(start=268, end=277, text='Microsoft', documents=[{'url': 'https://www.financecharts.com/screener/biggest-country-us', 'content': 'Biggest Companies in the US by Market Cap for Apr 2024. The most valuable company in the US is Microsoft (MSFT) with a market cap of $3.159T, followed by Apple (AAPL) and NVIDIA (NVDA). Last updated Apr 05, 2024.'}, {'url': 'https://disfold.com/united-states/sector/technology/companies/', 'content': 'Unlock Financial AI:\nStart your Free Trial of\nDisfold AI, Now!\nTop Technology Companies from the United States as of Jan. 01, 2024\n(Dec. 1, 2023)\nTop Technology Companies from the United States as of Jan. 01, 2024\n1.\nApple\nMarket Cap (USD):\n$2.866 T\nStock:\nAAPL\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nConsumer Electronics\n2.\nMicrosoft\nMarket Cap (USD):\n$2.755 T\nStock:\nMSFT\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Infrastructure\n3.\nNvidia\nMarket Cap (USD):\n$1.186 T\nStock:\nNVDA\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n4.\nBroadcom\nMarket Cap (USD):\n$495.95 B\nStock:\nAVGO\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n5.\nOracle\nMarket Cap (USD):\n$282.01 B\nStock:\nORCL\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Infrastructure\n6.\n Marvell Technology, Inc.\nMarket Cap (USD):\n$49.61 B\nStock:\n9MW\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n35.\nAutodesk, Inc.\nMarket Cap (USD):\n$48.97 B\nStock:\nADSK\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Application\n36.\nMicrochip Technology Incorporated\nMarket Cap (USD):\n$45.77 B\nStock:\nMCHP\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n37.\nFortinet, Inc.\nMarket Cap (USD):\n$44.84 B\nStock:\n Analog Devices\nMarket Cap (USD):\n$93.79 B\nStock:\nADI\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n20.\nMicron Technology, Inc.\nMarket Cap (USD):\n$91.30 B\nStock:\nMU\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n21.\nPalo Alto Networks\nMarket Cap (USD):\n$90.41 B\nStock:\nPANW\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Infrastructure\n22.\n Fiserv\nMarket Cap (USD):\n$79.73 B\nStock:\nFI\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nInformation Technology Services\n23.\nKLA\nMarket Cap (USD):\n$75.13 B\nStock:\nKLAC\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductor Equipment &amp; Materials\n24.\nSynopsys\nMarket Cap (USD):\n$74.64 B\nStock:\nSNPS\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Infrastructure\n25.\n Salesforce\nMarket Cap (USD):\n$243.78 B\nStock:\nCRM\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Application\n8.\nAMD\nMarket Cap (USD):\n$219.72 B\nStock:\nAMD\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n9.\nCisco\nMarket Cap (USD):\n$205.21 B\nStock:\nCSCO\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nCommunication Equipment\n10.\n'}]),
  CohereCitation(start=283, end=290, text='221,000', documents=[{'url': 'https://www.microsoft.com/investor/reports/ar23/index.html', 'content': 'As of June 30, 2023, we employed approximately 221,000 people on a full-time basis, 120,000 in the U.S. and 101,000 internationally. Of the total employed people, 89,000 were in operations, including manufacturing, distribution, product support, and consulting services; 72,000 were in product research and development; 45,000 were in sales and ...'}, {'url': 'https://www.macrotrends.net/stocks/charts/MSFT/microsoft/number-of-employees', 'content': 'Interactive chart of Microsoft (MSFT) annual worldwide employee count from 2010 to 2023. Microsoft total number of employees in 2023 was 221,000, a 0% decline from 2022. Microsoft total number of employees in 2022 was 221,000, a 22.1% increase from 2021. Microsoft total number of employees in 2021 was 181,000, a 11.04% increase from 2020.'}]),
  CohereCitation(start=292, end=297, text='Apple', documents=[{'url': 'https://www.financecharts.com/screener/biggest-country-us', 'content': 'Biggest Companies in the US by Market Cap for Apr 2024. The most valuable company in the US is Microsoft (MSFT) with a market cap of $3.159T, followed by Apple (AAPL) and NVIDIA (NVDA). Last updated Apr 05, 2024.'}, {'url': 'https://www.forbes.com/advisor/investing/best-tech-stocks/', 'content': 'eToro\nThe Best Tech Stocks of November 2023\nApple Inc. (AAPL)\n$2.8 trillion\n0.5%\n27.1%\n$2.8 trillion\n0.5%\n27.1%\nApple\xa0 was founded in Los Altos, Calif., by Steve Jobs and Steve Wozniak in 1976. ASML Holding NV (ASML)\n$248 billion\n1.0%\n22.8%\n$248 billion\n1.0%\n22.8%\nASML is a Netherlands-based company that designs and manufactures the machinery used by companies that make microchips. Taiwan Semiconductor Manufacturing Company (TSM)\n$443 billion\n2.0%\n20.6%\n$443 billion\n2.0%\n20.6%\nTaiwan Semiconductor Manufacturing Company could be the biggest tech company you’ve never heard of. NVIDIA Corp (NVDA)\n$1.1 trillion\n0.0%\n62.8%\n$1.1 trillion\n0.0%\n62.8%\nNVIDIA was founded in 1993 to produce graphic cards for the burgeoning personal computer market. Microsoft Corporation (MSFT)\n$2.6 trillion\n0.8%\n27.3%\n$2.6 trillion\n0.8%\n27.3%\nMicrosoft\xa0 was founded in 1975 by Bill Gates and Paul Allen in Albuquerque, N.M.'}, {'url': 'https://disfold.com/united-states/sector/technology/companies/', 'content': 'Unlock Financial AI:\nStart your Free Trial of\nDisfold AI, Now!\nTop Technology Companies from the United States as of Jan. 01, 2024\n(Dec. 1, 2023)\nTop Technology Companies from the United States as of Jan. 01, 2024\n1.\nApple\nMarket Cap (USD):\n$2.866 T\nStock:\nAAPL\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nConsumer Electronics\n2.\nMicrosoft\nMarket Cap (USD):\n$2.755 T\nStock:\nMSFT\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Infrastructure\n3.\nNvidia\nMarket Cap (USD):\n$1.186 T\nStock:\nNVDA\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n4.\nBroadcom\nMarket Cap (USD):\n$495.95 B\nStock:\nAVGO\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n5.\nOracle\nMarket Cap (USD):\n$282.01 B\nStock:\nORCL\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Infrastructure\n6.\n Marvell Technology, Inc.\nMarket Cap (USD):\n$49.61 B\nStock:\n9MW\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n35.\nAutodesk, Inc.\nMarket Cap (USD):\n$48.97 B\nStock:\nADSK\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Application\n36.\nMicrochip Technology Incorporated\nMarket Cap (USD):\n$45.77 B\nStock:\nMCHP\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n37.\nFortinet, Inc.\nMarket Cap (USD):\n$44.84 B\nStock:\n Analog Devices\nMarket Cap (USD):\n$93.79 B\nStock:\nADI\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n20.\nMicron Technology, Inc.\nMarket Cap (USD):\n$91.30 B\nStock:\nMU\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n21.\nPalo Alto Networks\nMarket Cap (USD):\n$90.41 B\nStock:\nPANW\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Infrastructure\n22.\n Fiserv\nMarket Cap (USD):\n$79.73 B\nStock:\nFI\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nInformation Technology Services\n23.\nKLA\nMarket Cap (USD):\n$75.13 B\nStock:\nKLAC\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductor Equipment &amp; Materials\n24.\nSynopsys\nMarket Cap (USD):\n$74.64 B\nStock:\nSNPS\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Infrastructure\n25.\n Salesforce\nMarket Cap (USD):\n$243.78 B\nStock:\nCRM\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Application\n8.\nAMD\nMarket Cap (USD):\n$219.72 B\nStock:\nAMD\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n9.\nCisco\nMarket Cap (USD):\n$205.21 B\nStock:\nCSCO\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nCommunication Equipment\n10.\n'}]),
  CohereCitation(start=303, end=310, text='161,000', documents=[{'url': 'https://www.macrotrends.net/stocks/charts/AAPL/apple/number-of-employees', 'content': 'Employee Count. Interactive chart of Apple (AAPL) annual worldwide employee count from 2010 to 2023. Apple total number of employees in 2023 was 161,000, a 1.83% decline from 2022. Apple total number of employees in 2022 was 164,000, a 6.49% increase from 2021. Apple total number of employees in 2021 was 154,000, a 4.76% increase from 2020.'}, {'url': 'https://www.businessinsider.com/apple-layoffs-tim-cook-getting-serious-challenges-car-china-iphone-2024-4?op=1', 'content': "2024-04-05T12:27:33Z An curved arrow pointing right. Share. The ... That's especially so when considering that Apple had about 161,000 full-time employees at the end of its last fiscal year."}]),
  CohereCitation(start=315, end=321, text='NVIDIA', documents=[{'url': 'https://www.financecharts.com/screener/biggest-country-us', 'content': 'Biggest Companies in the US by Market Cap for Apr 2024. The most valuable company in the US is Microsoft (MSFT) with a market cap of $3.159T, followed by Apple (AAPL) and NVIDIA (NVDA). Last updated Apr 05, 2024.'}, {'url': 'https://disfold.com/united-states/sector/technology/companies/', 'content': 'Unlock Financial AI:\nStart your Free Trial of\nDisfold AI, Now!\nTop Technology Companies from the United States as of Jan. 01, 2024\n(Dec. 1, 2023)\nTop Technology Companies from the United States as of Jan. 01, 2024\n1.\nApple\nMarket Cap (USD):\n$2.866 T\nStock:\nAAPL\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nConsumer Electronics\n2.\nMicrosoft\nMarket Cap (USD):\n$2.755 T\nStock:\nMSFT\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Infrastructure\n3.\nNvidia\nMarket Cap (USD):\n$1.186 T\nStock:\nNVDA\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n4.\nBroadcom\nMarket Cap (USD):\n$495.95 B\nStock:\nAVGO\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n5.\nOracle\nMarket Cap (USD):\n$282.01 B\nStock:\nORCL\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Infrastructure\n6.\n Marvell Technology, Inc.\nMarket Cap (USD):\n$49.61 B\nStock:\n9MW\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n35.\nAutodesk, Inc.\nMarket Cap (USD):\n$48.97 B\nStock:\nADSK\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Application\n36.\nMicrochip Technology Incorporated\nMarket Cap (USD):\n$45.77 B\nStock:\nMCHP\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n37.\nFortinet, Inc.\nMarket Cap (USD):\n$44.84 B\nStock:\n Analog Devices\nMarket Cap (USD):\n$93.79 B\nStock:\nADI\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n20.\nMicron Technology, Inc.\nMarket Cap (USD):\n$91.30 B\nStock:\nMU\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n21.\nPalo Alto Networks\nMarket Cap (USD):\n$90.41 B\nStock:\nPANW\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Infrastructure\n22.\n Fiserv\nMarket Cap (USD):\n$79.73 B\nStock:\nFI\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nInformation Technology Services\n23.\nKLA\nMarket Cap (USD):\n$75.13 B\nStock:\nKLAC\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductor Equipment &amp; Materials\n24.\nSynopsys\nMarket Cap (USD):\n$74.64 B\nStock:\nSNPS\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Infrastructure\n25.\n Salesforce\nMarket Cap (USD):\n$243.78 B\nStock:\nCRM\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSoftware—Application\n8.\nAMD\nMarket Cap (USD):\n$219.72 B\nStock:\nAMD\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nSemiconductors\n9.\nCisco\nMarket Cap (USD):\n$205.21 B\nStock:\nCSCO\nwb_incandescent\nCountry:\nUnited States\nSector:\nTechnology\nIndustry:\nCommunication Equipment\n10.\n'}]),
  CohereCitation(start=327, end=333, text='29,600', documents=[{'url': 'https://stockanalysis.com/stocks/nvda/employees/', 'content': 'NVIDIA had 29,600 employees on January 28, 2024. The number of employees increased by 3,404 or 12.99% compared to the previous year. Employees 29,600. Change (1Y) 3,404. ... Real-time quotes provided by IEX Cloud. Other market data may be delayed by 15 minutes or more. ...'}, {'url': 'https://www.macrotrends.net/stocks/charts/NVDA/nvidia/number-of-employees', 'content': 'Employee Count. Interactive chart of NVIDIA (NVDA) annual worldwide employee count from 2010 to 2024. NVIDIA total number of employees in 2024 was 29,600, a 12.99% increase from 2023. NVIDIA total number of employees in 2023 was 26,196, a 16.57% increase from 2022. NVIDIA total number of employees in 2022 was 22,473, a 18.43% increase from 2021.'}])]}
```

```python PYTHON
agent_executor.invoke({
    "input": "Hey how are you?",
})
```

````txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3mPlan: I will respond to the user's greeting.
Action: ```json JSON
[
    {
        "tool_name": "directly_answer",
        "parameters": {}
    }
]
```
Relevant Documents: None
Cited Documents: None
Answer: Hey, I'm doing well, thank you for asking! How can I help you today?
Grounded answer: Hey, I'm doing well, thank you for asking! How can I help you today?[0m

[1m> Finished chain.[0m





{'input': 'Hey how are you?',
 'output': "Hey, I'm doing well, thank you for asking! How can I help you today?",
 'citations': []}
````

This is a simple example to get you started. There [are many tools](https://python.langchain.com/docs/integrations/tools/) you can equip your agent with. Once you're comfortable with these ideas, you can also proceed to define your tools (see [Multi-step tool use in Action](https://docs.cohere.com/docs/multi-step-tool-use#multi-step-tool-use-in-action)).


# Advanced Document Parsing For Enterprises

> This page describes how to use Cohere's models to build a document-parsing agent.

<AuthorsContainer
  authors={[
    {
      name: "Giannis Chatziveroglou",
      imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/73153cb-giannis.jpeg",
    },
  ]}
/>

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Document_Parsing_For_Enterprises.ipynb" />

## Introduction

The bread and butter of natural language processing technology is text. Once we can reduce a set of data into text, we can do all kinds of things with it: question answering, summarization, classification, sentiment analysis, searching and indexing, and more.

In the context of enterprise Retrieval Augmented Generation (RAG), the information is often locked in complex file types such as PDFs. These formats are made for sharing information between humans, but not so much with language models.

In this notebook, we will use a real-world pharmaceutical drug label to test out various performant approaches to parsing PDFs. This will allow us to use [Cohere's Command-R model](https://cohere.com/blog/command-r/) in a RAG setting to answer questions and asks about this label, such as "I need a succinct summary of the compound name, indication, route of administration, and mechanism of action of" a given pharmaceutical.

<img alt="Document Parsing Result" src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/document-parsing-2.png" />

## PDF Parsing \[#top]

We will go over five proprietary as well as open source options for processing PDFs. The parsing mechanisms demonstrated in the following sections are

* [Google Document AI](#gcp)
* [AWS Textract](#aws)
* [Unstructured.io](#unstructured)
* [LlamaParse](#llama)
* [pdf2image + pytesseract](#pdf2image)

By way of example, we will be parsing a [21-page PDF](https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/215500s000lbl.pdf) containing the label for a recent FDA drug approval, the beginning of which is shown below. Then, we will perform a series of basic RAG tasks with our different parsings and evaluate their performance.

<img alt="Drug Label Snippet" src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/document-parsing-1.png" />

## Getting Set Up

Before we dive into the technical weeds, we need to set up the notebook's runtime and filesystem environments. The code cells below do the following:

* Install required libraries
* Confirm that data dependencies from the GitHub repo have been downloaded. These will be under `data/document-parsing` and contain the following:
  * the PDF document that we will be working with, `fda-approved-drug.pdf` (this can also be found here: [https://www.accessdata.fda.gov/drugsatfda\_docs/label/2023/215500s000lbl.pdf](https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/215500s000lbl.pdf))
  * precomputed parsed documents for each parsing solution. While the point of this notebook is to illustrate how this is done, we provide the parsed final results to allow readers to skip ahead to the RAG section without having to set up the required infrastructure for each solution.)
* Add utility functions needed for later sections

```python PYTHON
%%capture
! sudo apt install tesseract-ocr poppler-utils
! pip install "cohere<5" fsspec hnswlib google-cloud-documentai google-cloud-storage boto3 langchain-text-splitters llama_parse pytesseract pdf2image pandas

```

```python PYTHON
data_dir = "data/document-parsing"
source_filename = "fda-approved-drug"
extension = "pdf"
```

```python PYTHON
from pathlib import Path

sources = ["gcp", "aws", "unstructured-io", "llamaparse-text", "llamaparse-markdown", "pytesseract"]

filenames = ["{}-parsed-fda-approved-drug.txt".format(source) for source in sources]
filenames.append("fda-approved-drug.pdf")

for filename in filenames:
    file_path = Path(f"{data_dir}/{filename}")
    if file_path.is_file() == False:
        print(f"File {filename} not found at {data_dir}!")
```

### Utility Functions

Make sure to include the notebook's utility functions in the runtime.

```python PYTHON
def store_document(path: str, doc_content: str):
    with open(path, 'w') as f:
      f.write(doc_content)
```

```python PYTHON
import json

def insert_citations_in_order(text, citations, documents):
    """
    A helper function to pretty print citations.
    """

    citations_reference = {}
    for index, doc in enumerate(documents):
        citations_reference[index] = doc

    offset = 0
    # Process citations in the order they were provided
    for citation in citations:
        # Adjust start/end with offset
        start, end = citation['start'] + offset, citation['end'] + offset
        citation_numbers = []
        for doc_id in citation["document_ids"]:
            for citation_index, doc in citations_reference.items():
                if doc["id"] == doc_id:
                    citation_numbers.append(citation_index)
        references = "(" + ", ".join("[{}]".format(num) for num in citation_numbers) + ")"
        modification = f'{text[start:end]} {references}'
        # Replace the cited text with its bolded version + placeholder
        text = text[:start] + modification + text[end:]
        # Update the offset for subsequent replacements
        offset += len(modification) - (end - start)

    # Add the citations at the bottom of the text
    text_with_citations = f'{text}'
    citations_reference = ["[{}]: {}".format(x["id"], x["text"]) for x in citations_reference.values()]

    return text_with_citations, "\n".join(citations_reference)
```

```python PYTHON
def format_docs_for_chat(documents):
  return [{"id": str(index), "text": x} for index, x in enumerate(documents)]
```

## Document Parsing Solutions

For demonstration purposes, we have collected and saved the parsed documents from each solution in this notebook. Skip to the [next section](#document-questions) to run RAG with Command-A on the pre-fetched versions. You can find all parsed resources in detail at the link [here](https://github.com/gchatz22/temp-cohere-resources/tree/main/data).

### Solution 1: Google Cloud Document AI [\[Back to Solutions\]](#top) \[#gcp]

Document AI helps developers create high-accuracy processors to extract, classify, and split documents.

External documentation: [https://cloud.google.com/document-ai](https://cloud.google.com/document-ai)

#### Parsing the document

The following block can be executed in one of two ways:

* Inside a Google Vertex AI environment
  * No authentication needed
* From this notebook
  * Authentication is needed
  * There are pointers inside the code on which lines to uncomment in order to make this work

**Note: You can skip to the next block if you want to use the pre-existing parsed version.**

```python PYTHON
"""
Extracted from https://cloud.google.com/document-ai/docs/samples/documentai-batch-process-document
"""

import re
from typing import Optional

from google.api_core.client_options import ClientOptions
from google.api_core.exceptions import InternalServerError
from google.api_core.exceptions import RetryError
from google.cloud import documentai  # type: ignore
from google.cloud import storage

project_id = ""
location = ""
processor_id = ""
gcs_output_uri = ""

---

**Navigation:** [← Previous](./15-multi-step-tool-use-with-cohere.md) | [Index](./index.md) | [Next →](./17-credentials-file-populate-if-you-are-running-in-a-.md)
