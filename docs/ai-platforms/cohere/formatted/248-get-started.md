---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Get Started

### Example with Texts

In the example below, we use the [Rerank API endpoint](/reference/rerank-1) to index the list of `documents` from most to least relevant to the query `"What is the capital of the United States?"`.

**Request**

In this example, the documents being passed in are a list of strings:

<CodeBlocks>
```python PYTHON
  import cohere

  co = cohere.ClientV2()

  query = "What is the capital of the United States?"
  docs = [
      "Carson City is the capital city of the American state of Nevada. At the 2010 United States Census, Carson City had a population of 55,274.",
      "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean that are a political division controlled by the United States. Its capital is Saipan.",
      "Charlotte Amalie is the capital and largest city of the United States Virgin Islands. It has about 20,000 people. The city is on the island of Saint Thomas.",
      "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district. The President of the USA and many major national government offices are in the territory. This makes it the political center of the United States of America.",
      "Capital punishment has existed in the United States since before the United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states. The federal government (including the United States military) also uses capital punishment.",
  ]

  results = co.rerank(
      model="rerank-v3.5", query=query, documents=docs, top_n=5
  )
```
```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/rerank \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
      "model": "rerank-v3.5",
      "query": "What is the capital of the United States?",
      "documents": [
        "Carson City is the capital city of the American state of Nevada. At the 2010 United States Census, Carson City had a population of 55,274.",
        "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean that are a political division controlled by the United States. Its capital is Saipan.",
        "Charlotte Amalie is the capital and largest city of the United States Virgin Islands. It has about 20,000 people. The city is on the island of Saint Thomas.",
        "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district. The President of the USA and many major national government offices are in the territory. This makes it the political center of the United States of America.",
        "Capital punishment has existed in the United States since before the United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states. The federal government (including the United States military) also uses capital punishment."
      ],
      "top_n": 5
    }'
```
</CodeBlocks>

**Response**
```jsx
{
  "id": "97813271-fe74-465d-b9d5-577e77079253",
  "results": [
    {
      "index": 3, // "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) ..."
      "relevance_score": 0.9990564
    },
    {
      "index": 4, // "Capital punishment has existed in the United States since before the United States was a country. As of 2017 ..."
      "relevance_score": 0.7516481
    },
    {
      "index": 1, // "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean that are a political division ..."
      "relevance_score": 0.08882029
    },
    {
      "index": 0, // "Carson City is the capital city of the American state of Nevada. At the 2010 United States Census, Carson City had a ..."
      "relevance_score": 0.058238626
    },
    {
      "index": 2, // ""Charlotte Amalie is the capital and largest city of the United States Virgin Islands. It has about 20,000 people ..."
      "relevance_score": 0.019946935
    }
  ],
  "meta": {
    "api_version": {
      "version": "2"
    },
    "billed_units": {
      "search_units": 1
    }
  }
}
```

### Example with Structured Data:

If your documents contain structured data, for best performance we recommend formatting them as YAML strings.

**Request**

<CodeBlocks>
```python PYTHON
  import yaml
  import cohere

  co = cohere.ClientV2()

  query = "What is the capital of the United States?"
  docs = [
      {
          "Title": "Facts about Carson City",
          "Content": "Carson City is the capital city of the American state of Nevada. At the 2010 United States Census, Carson City had a population of 55,274.",
      },
      {
          "Title": "The Commonwealth of Northern Mariana Islands",
          "Content": "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean that are a political division controlled by the United States. Its capital is Saipan.",
      },
      {
          "Title": "The Capital of United States Virgin Islands",
          "Content": "Charlotte Amalie is the capital and largest city of the United States Virgin Islands. It has about 20,000 people. The city is on the island of Saint Thomas.",
      },
      {
          "Title": "Washington D.C.",
          "Content": "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district. The President of the USA and many major national government offices are in the territory. This makes it the political center of the United States of America.",
      },
      {
          "Title": "Capital Punishment in the US",
          "Content": "Capital punishment has existed in the United States since before the United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states. The federal government (including the United States military) also uses capital punishment.",
      },
  ]

  yaml_docs = [yaml.dump(doc, sort_keys=False) for doc in docs]

  results = co.rerank(
      model="rerank-v3.5", query=query, documents=yaml_docs, top_n=5
  )
```
```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/rerank \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
      "model": "rerank-v3.5",
      "query": "What is the capital of the United States?",
      "documents": [
        "Title: Facts about Carson City\nContent: Carson City is the capital city of the American state of Nevada. At the 2010 United States Census, Carson City had a population of 55,274.\n",
        "Title: The Commonwealth of Northern Mariana Islands\nContent: The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean that are a political division controlled by the United States. Its capital is Saipan.\n",
        "Title: The Capital of United States Virgin Islands\nContent: Charlotte Amalie is the capital and largest city of the United States Virgin Islands. It has about 20,000 people. The city is on the island of Saint Thomas.\n",
        "Title: Washington D.C.\nContent: Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district. The President of the USA and many major national government offices are in the territory. This makes it the political center of the United States of America.\n",
        "Title: Capital Punishment in the US\nContent: Capital punishment has existed in the United States since before the United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states. The federal government (including the United States military) also uses capital punishment.\n"
      ],
      "top_n": 5
    }'
```
</CodeBlocks>

In the `documents` parameter, we are passing in a list YAML strings, representing the structured data.

**Response**
```jsx
{
	"id": "75a94aa7-6761-4a64-a2ae-4bc0a62bc601",
	"results": [
		{
			"index": 3,
			"relevance_score": 0.9987405
		},
		{
			"index": 4,
			"relevance_score": 0.5011778
		},
		{
			"index": 2,
			"relevance_score": 0.10070161
		},
		{
			"index": 1,
			"relevance_score": 0.03197956
		},
		{
			"index": 0,
			"relevance_score": 0.019456575
		}
	],
	"meta": {
		"api_version": {
			"version": "2022-12-06"
		},
		"billed_units": {
			"search_units": 1
		}
	}
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
