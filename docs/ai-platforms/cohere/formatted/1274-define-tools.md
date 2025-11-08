---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Define tools

Your agent will be equipped with the following tools. The model can pick between

* doing a search on the web
* and/or retrieving data from a vector store
* and/or using a python interpreter
* and/or directly answering \[ this tool comes out of the box! ]

Plus the model can self-reflect.

#### Web search

You can easily equip your agent with web search!
```python PYTHON
from langchain_community.tools.tavily_search import TavilySearchResults

os.environ["TAVILY_API_KEY"] = <your-api-key> # you can create an API key for free on Tavily's website

internet_search = TavilySearchResults()
internet_search.name = "internet_search"
internet_search.description = "Returns a list of relevant document snippets for a textual query retrieved from the internet."


from langchain_core.pydantic_v1 import BaseModel, Field
class TavilySearchInput(BaseModel):
    query: str = Field(description="Query to search the internet with")
internet_search.args_schema = TavilySearchInput
```

#### Vector store

You can easily equip your agent with a vector store!
```python PYTHON
!pip --quiet install faiss-cpu tiktoken
```
```txt title="Output"
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m27.0/27.0 MB[0m [31m41.4 MB/s[0m eta [36m0:00:00[0m
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m1.8/1.8 MB[0m [31m58.3 MB/s[0m eta [36m0:00:00[0m
[?25h
```
```python PYTHON
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_cohere import CohereEmbeddings

embd = CohereEmbeddings()

urls = [
    "https://paulgraham.com/best.html",
]

docs = [WebBaseLoader(url).load() for url in urls]
docs_list = [item for sublist in docs for item in sublist]

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=512, chunk_overlap=0
)
doc_splits = text_splitter.split_documents(docs_list)

vectorstore = FAISS.from_documents(
    documents=doc_splits,
    embedding=embd,
)

vectorstore_retriever = vectorstore.as_retriever()
```
```python PYTHON
from langchain.tools.retriever import create_retriever_tool

vectorstore_search = create_retriever_tool(
    retriever=vectorstore_retriever,
    name="vectorstore_search",
    description="Retrieve relevant info from a vectorstore that contains information from Paul Graham about how to write good essays."
)
```

#### Python interpreter tool

You can easily equip your agent with a python interpreter!
```python PYTHON
from langchain.agents import Tool
from langchain_experimental.utilities import PythonREPL

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
```

#### Transform any Python function in a Tool

You can easily equip your agent with any Python function!
```python PYTHON
from langchain_core.tools import tool
import random

@tool
def random_operation_tool(a: int, b: int):
  """Calculates a random operation between the inputs."""
  coin_toss = random.uniform(0, 1)
  if coin_toss > 0.5:
    return {'output': a*b}
  else:
    return {'output': a+b}

random_operation_tool.name = "random_operation" # use python case

random_operation_tool.description = "Calculates a random operation between the inputs."

from langchain_core.pydantic_v1 import BaseModel, Field
class random_operation_inputs(BaseModel):
    a: int = Field(description="First input")
    b: int = Field(description="Second input")
random_operation_tool.args_schema = random_operation_inputs
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
