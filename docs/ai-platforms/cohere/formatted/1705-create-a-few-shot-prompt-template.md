---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create a few-shot prompt template

In the above step, we've created a simple system prompt. Now, let us see how we can create a better few shot prompt template in this section. Few-shot examples are used to provide the model with context and improve its performance on specific tasks. In this case, we'll prepare examples of natural language queries and their corresponding SQL queries to help the model generate accurate SQL statements for our database.

In this example, we use `SemanticSimilarityExampleSelector` to select the top k examples that are most similar to an input query out of all the examples available.
```python PYTHON
examples = [
    {
        "input": "What was the average processing time for all stations on April 3rd 2024?",
        "query": "SELECT station_name, AVG(CAST(duration AS INTEGER)) AS avg_processing_time FROM product_tracking WHERE date = '2024-04-03' AND zone = 'wip' GROUP BY station_name ORDER BY station_name;",
    },
    {
        "input": "What was the average processing time for all stations on April 3rd 2024 between 4pm and 6pm?",
        "query": "SELECT station_name, AVG(CAST(duration AS INTEGER)) AS avg_processing_time FROM product_tracking WHERE date = '2024-04-03' AND CAST(hour AS INTEGER) BETWEEN 16 AND 18 AND zone = 'wip' GROUP BY station_name ORDER BY station_name;",
    },
    {
        "input": "What was the average processing time for stn4 on April 3rd 2024?",
        "query": "SELECT AVG(CAST(duration AS INTEGER)) AS avg_processing_time FROM product_tracking WHERE date = '2024-04-03' AND station_name = 'stn4' AND zone = 'wip';",
    },
    {
        "input": "How much downtime did stn2 have on April 3rd 2024?",
        "query": "SELECT COUNT(*) AS downtime_count FROM status WHERE date = '2024-04-03' AND station_name = 'stn2' AND station_status = 'downtime';",
    },
    {
        "input": "What were the productive time and downtime numbers for all stations on April 3rd 2024?",
        "query": "SELECT station_name, station_status, COUNT(*) as total_time FROM status WHERE date = '2024-04-03' GROUP BY station_name, station_status;",
    },
    {
        "input": "What was the bottleneck station on April 3rd 2024?",
        "query": "SELECT station_name, AVG(CAST(duration AS INTEGER)) AS avg_processing_time FROM product_tracking WHERE date = '2024-04-03' AND zone = 'wip' GROUP BY station_name ORDER BY avg_processing_time DESC LIMIT 1;",
    },
    {
        "input": "Which percentage of the time was stn5 down in the last week of May?",
        "query": "SELECT SUM(CASE WHEN station_status = 'downtime' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS percentage_downtime FROM status WHERE station_name = 'stn5' AND date >= '2024-05-25' AND date <= '2024-05-31';",
    },
]
```
```python PYTHON
example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
    CohereEmbeddings(
        cohere_api_key=os.getenv("COHERE_API_KEY"), model="embed-v4.0"
    ),
    FAISS,
    k=5,
    input_keys=["input"],
)
```
```python PYTHON
from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotPromptTemplate,
    MessagesPlaceholder,
    PromptTemplate,
    SystemMessagePromptTemplate,
)

system_prefix = """You are an agent designed to interact with a SQL database.
You are an expert at answering questions about manufacturing data.
Given an input question, create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
Always start with checking the schema of the available tables.
Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most {top_k} results.
You can order the results by a relevant column to return the most interesting examples in the database.
Never query for all the columns from a specific table, only ask for the relevant columns given the question.
You have access to tools for interacting with the database.
Only use the given tools. Only use the information returned by the tools to construct your final answer.
You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.

DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.

The current date is {date}.

For questions regarding productive time, downtime, productive or productivity, use minutes as units.

For questions regarding productive time, downtime, productive or productivity use the status table.

For questions regarding processing time and average processing time, use minutes as units.

For questions regarding bottlenecks, processing time and average processing time use the product_tracking table.

If the question does not seem related to the database, just return "I don't know" as the answer.

Here are some examples of user inputs and their corresponding SQL queries:
"""

few_shot_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=PromptTemplate.from_template(
        "User input: {input}\nSQL query: {query}"
    ),
    input_variables=["input", "dialect", "top_k","date"],
    prefix=system_prefix,
    suffix="",
)
```
```python PYTHON
full_prompt = ChatPromptTemplate.from_messages(
    [
        # In the previous section, this was system_prompt instead without the few shot examples.

        # We can use either prompting style as required

        SystemMessagePromptTemplate(prompt=few_shot_prompt),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
