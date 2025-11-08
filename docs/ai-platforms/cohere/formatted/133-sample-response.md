---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Sample response

['popularity of NSync', 'popularity of Backstreet Boys']
```
Indeed, to generate a factually accurate answer to the question "Who is more popular: Nsync or Backstreet Boys?", looking up `popularity of NSync` and `popularity of Backstreet Boys` first would be helpful.

<Accordion title="Customizing the generation of search queries">
  You can then update the system message and/or the tool definition to generate queries that are more relevant to your use case.

  For example, you can update the system message to encourage a longer list of search queries to be generated.
```python PYTHON
  instructions = "Write a search query that will find helpful information for answering the user's question accurately. If you need more than one search query, write a list of search queries. If you decide that a search is very unlikely to find information that would be useful in constructing a response to the user, you should instead directly answer."
```
  Example response:
```mdx
  ['NSync popularity', 'Backstreet Boys popularity', 'NSync vs Backstreet Boys popularity comparison', 'Which boy band is more popular NSync or Backstreet Boys', 'NSync and Backstreet Boys fan base size comparison', 'Who has sold more albums NSync or Backstreet Boys', 'NSync and Backstreet Boys chart performance comparison']
```
</Accordion>

### Step 2: Fetching relevant documents

The next step is to fetch documents from the relevant data source using the generated search queries. For example, to answer the question about the two pop sensations *NSYNC* and *Backstreet Boys*, one might want to use an API from a web search engine, and fetch the contents of the websites listed at the top of the search results.

We won't go into details of fetching data in this guide, since it's very specific to the search API you're querying. However we should mention that breaking up documents into small chunks of ±400 words will help you get the best performance from Cohere models.

<Accordion title="Context length limit">
  When trying to stay within the context length limit, you might need to omit some of the documents from the request. To make sure that only the least relevant documents are omitted, we recommend using the [Rerank endpoint](https://docs.cohere.com/reference/rerank) endpoint which will sort the documents by relevancy to the query. The lowest ranked documents are the ones you should consider dropping first.
</Accordion>

#### Formatting documents

The Chat endpoint supports a few different options for structuring documents in the `documents` parameter:

* List of objects with `data` object: Each document is passed as a `data` object (with an optional `id` field to be used in citations). The `data` object is a string-any dictionary containing the document's contents. For example, a web search document can contain a `title`, `text`, and `url` for the document's title, text, and URL.
* List of objects with `data` string: Each document is passed as a `data` string (with an optional `id` field to be used in citations).
* List of strings: Each document is passed as a string.

The following examples demonstrate the options mentioned above.

<Tabs>
  <Tab title="'data' object">
```python PYTHON
    documents = [
        {
            "data": {
                "title": "Tall penguins",
                "snippet": "Emperor penguins are the tallest.",
            }
        }
    ]
```
  </Tab>

  <Tab title="'data' string">
```python PYTHON
    documents = [
        {"data": "Tall penguins: Emperor penguins are the tallest."}
    ]
```
  </Tab>

  <Tab title="string">
```python PYTHON
    documents = [
        "Tall penguins: Emperor penguins are the tallest.",
    ]
```
  </Tab>
</Tabs>

The `id` field will be used in citation generation as the reference document IDs. If no `id` field is passed in an API call, the API will automatically generate the IDs based on the documents position in the list. For more information, see the guide on [using custom IDs](https://docs.cohere.com/docs/rag-citations).

### Step 3: Generating a response with citations

In the final step, we will be calling the Chat API again, but this time passing along the `documents` you acquired in Step 2. We recommend using a few descriptive keys such as `"title"`, `"snippet"`, or `"last updated"` and only including semantically relevant data. The keys and the values will be formatted into the prompt and passed to the model.
```python PYTHON
documents = [
    {
        "data": {
            "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
            "snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: Backstreet Boys Popularity Analysis\n\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\n\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\n\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.",
        }
    },
    {
        "data": {
            "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
            "snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: NSYNC Popularity Analysis\n\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\n\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\n\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.",
        }
    },
    {
        "data": {
            "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
            "snippet": " 1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\n\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\n\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.",
        }
    },
    {
        "data": {
            "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
            "snippet": " Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\n\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.",
        }
    },
]

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
