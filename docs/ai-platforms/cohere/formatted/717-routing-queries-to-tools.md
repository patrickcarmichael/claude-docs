---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Routing queries to tools

Let's ask the agent a few questions, starting with this one about the Embed endpoint.

Because the question asks about a specific feature, the agent decides to use the `search_developer_docs` tool (instead of retrieving from all the data sources it's connected to).

It first generates a tool plan that describes how it will handle the query. Then, it generates tool calls to the `search_developer_docs` tool with the associated `query` parameter.

The tool does indeed contain the information asked by the user, which the agent then uses to generate its response.
```python PYTHON
messages = run_agent("How many languages does Embed support?")
```
```mdx
QUESTION:
How many languages does Embed support?
==================================================
TOOL PLAN:
I will search the Cohere developer documentation for 'how many languages does Embed support'. 

TOOL CALLS:
Tool name: search_developer_docs | Parameters: {"query":"how many languages does Embed support"}
==================================================
RESPONSE:
The Embed endpoint supports over 100 languages.
==================================================
CITATIONS:

Start: 28| End:47| Text:'over 100 languages.' 
Sources:
1. search_developer_docs_gwt5g55gjc3w:2
```
Let's now ask the agent a question about setting up the Notion API so we can connect it to LLMs. This information is not likely to be found in the developer documentation or code examples because it is not Cohere-specific, so we can expect the agent to use the internet search tool.

And this is exactly what the agent does. This time, it decides to use the `search_internet` tool, triggers the search through Tavily search, and uses the results to generate its response.
```python PYTHON
messages = run_agent("How to set up the Notion API.")
```
```mdx
QUESTION:
How to set up the Notion API.
==================================================
TOOL PLAN:
I will search for 'Notion API setup' to find out how to set up the Notion API. 

TOOL CALLS:
Tool name: search_internet | Parameters: {"query":"Notion API setup"}
==================================================
RESPONSE:
To set up the Notion API, you need to create a new integration in Notion's integrations dashboard. You can do this by navigating to https://www.notion.com/my-integrations and clicking '+ New integration'.

Once you've done this, you'll need to get your API secret by visiting the Configuration tab. You should keep your API secret just that – a secret! You can refresh your secret if you accidentally expose it.

Next, you'll need to give your integration page permissions. To do this, you'll need to pick or create a Notion page, then click on the ... More menu in the top-right corner of the page. Scroll down to + Add Connections, then search for your integration and select it. You'll then need to confirm the integration can access the page and all of its child pages.

If your API requests are failing, you should confirm you have given the integration permission to the page you are trying to update.

You can also create a Notion API integration and get your internal integration token. You'll then need to create a .env file and add environmental variables, get your Notion database ID and add your integration to your database.

For more information on what you can build with Notion's API, you can refer to this guide.
==================================================
CITATIONS:

Start: 38| End:62| Text:'create a new integration' 
Sources:
1. search_internet_cwabyfc5mn8c:0
2. search_internet_cwabyfc5mn8c:2


Start: 75| End:98| Text:'integrations dashboard.' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 132| End:170| Text:'https://www.notion.com/my-integrations' 
Sources:
1. search_internet_cwabyfc5mn8c:0


Start: 184| End:203| Text:''+ New integration'' 
Sources:
1. search_internet_cwabyfc5mn8c:0
2. search_internet_cwabyfc5mn8c:2


Start: 244| End:263| Text:'get your API secret' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 280| End:298| Text:'Configuration tab.' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 310| End:351| Text:'keep your API secret just that – a secret' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 361| End:411| Text:'refresh your secret if you accidentally expose it.' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 434| End:473| Text:'give your integration page permissions.' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 501| End:529| Text:'pick or create a Notion page' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 536| End:599| Text:'click on the ... More menu in the top-right corner of the page.' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 600| End:632| Text:'Scroll down to + Add Connections' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 639| End:681| Text:'search for your integration and select it.' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 702| End:773| Text:'confirm the integration can access the page and all of its child pages.' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 783| End:807| Text:'API requests are failing' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 820| End:907| Text:'confirm you have given the integration permission to the page you are trying to update.' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 922| End:953| Text:'create a Notion API integration' 
Sources:
1. search_internet_cwabyfc5mn8c:1


Start: 958| End:994| Text:'get your internal integration token.' 
Sources:
1. search_internet_cwabyfc5mn8c:1


Start: 1015| End:1065| Text:'create a .env file and add environmental variables' 
Sources:
1. search_internet_cwabyfc5mn8c:1


Start: 1067| End:1094| Text:'get your Notion database ID' 
Sources:
1. search_internet_cwabyfc5mn8c:1


Start: 1099| End:1137| Text:'add your integration to your database.' 
Sources:
1. search_internet_cwabyfc5mn8c:1


Start: 1223| End:1229| Text:'guide.' 
Sources:
1. search_internet_cwabyfc5mn8c:3
```
Let's ask the agent a final question, this time about tutorials that are relevant for enterprises.

Again, the agent uses the context of the query to decide on the most relevant tool. In this case, it selects the `search_code_examples` tool and provides a response based on the information found.
```python PYTHON
messages = run_agent(
    "Any tutorials that are relevant for enterprises?"
)
```
```mdx

QUESTION:
Any tutorials that are relevant for enterprises?
==================================================
TOOL PLAN:
I will search for 'enterprise tutorials' in the code examples and tutorials tool. 

TOOL CALLS:
Tool name: search_code_examples | Parameters: {"query":"enterprise tutorials"}
==================================================
RESPONSE:
I found a tutorial called 'Advanced Document Parsing For Enterprises'.
==================================================
CITATIONS:

Start: 26| End:69| Text:''Advanced Document Parsing For Enterprises'' 
Sources:
1. search_code_examples_jhh40p32wxpw:4
```typescript

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
