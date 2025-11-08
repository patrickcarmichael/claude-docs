---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 7:  Add the Cohere Reranker

Cohere rerank functions as a second stage search that can improve the precision of your first stage search results

![](file:470cf874-d7a4-45c4-9b12-aaf0776e2930)
```python
def rerank_documents(query: str, documents, top_n: int = 3):
    # Perform reranking with Cohere ReRank Model

    try:
        response = co.rerank(
            model="rerank-english-v3.0",
            query=query,
            documents=documents,
            top_n=top_n,
            rank_fields=["company", "reports", "combined_attributes"],
        )

        # Extract the top reranked documents

        top_documents_after_rerank = []
        for result in response.results:
            original_doc = documents[result.index]
            top_documents_after_rerank.append(
                {
                    "company": original_doc["company"],
                    "combined_attributes": original_doc[
                        "combined_attributes"
                    ],
                    "reports": original_doc["reports"],
                    "vector_search_score": original_doc["score"],
                    "relevance_score": result.relevance_score,
                }
            )

        return top_documents_after_rerank

    except Exception as e:
        print(f"An error occurred during reranking: {e}")
        # Return top N documents without reranking

        return documents[:top_n]
```
```python
import pprint

query = "What companies have negative market reports or negative sentiment that might deter from investment in the long term"

get_knowledge = vector_search(query, collection)
pd.DataFrame(get_knowledge).head()
```
<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          reports
        </th>

        <th>
          company
        </th>

        <th>
          combined_attributes
        </th>

        <th>
          score
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          \[{'author': 'Jordan Garcia, Senior Tech Analys...
        </td>

        <td>
          GreenEnergy Corp
        </td>

        <td>
          GreenEnergy Corp Information Technology 2023 G...
        </td>

        <td>
          0.659524
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          \[{'author': 'Morgan Smith, Technology Sector L...
        </td>

        <td>
          BioTech Therapeutics
        </td>

        <td>
          BioTech Therapeutics Information Technology 20...
        </td>

        <td>
          0.646300
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          \[{'author': 'Casey Davis, Technology Sector Le...
        </td>

        <td>
          RenewableEnergy Innovations
        </td>

        <td>
          RenewableEnergy Innovations Information Techno...
        </td>

        <td>
          0.645224
        </td>
      </tr>

      <tr>
        <th>
          3
        </th>

        <td>
          \[{'author': 'Morgan Johnson, Technology Sector...
        </td>

        <td>
          QuantumSensor Corp
        </td>

        <td>
          QuantumSensor Corp Information Technology 2023...
        </td>

        <td>
          0.644383
        </td>
      </tr>

      <tr>
        <th>
          4
        </th>

        <td>
          \[{'author': 'Morgan Williams, Senior Tech Anal...`
        </td>

        <td>
          BioEngineering Corp
        </td>

        <td>
          BioEngineering Corp Information Technology 202...
        </td>

        <td>
          0.643690
        </td>
      </tr>
    </tbody>
  </table>
</div>
```python
reranked_documents = rerank_documents(query, get_knowledge)
pd.DataFrame(reranked_documents).head()
```
<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          company
        </th>

        <th>
          combined_attributes
        </th>

        <th>
          reports
        </th>

        <th>
          vector_search_score
        </th>

        <th>
          relevance_score
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          GreenEnergy Corp
        </td>

        <td>
          GreenEnergy Corp Information Technology 2023 G...
        </td>

        <td>
          \[{'author': 'Jordan Garcia, Senior Tech Analys...
        </td>

        <td>
          0.659524
        </td>

        <td>
          0.000147
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          BioEngineering Corp
        </td>

        <td>
          BioEngineering Corp Information Technology 202...
        </td>

        <td>
          \[{'author': 'Morgan Williams, Senior Tech Anal...
        </td>

        <td>
          0.643690
        </td>

        <td>
          0.000065
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          QuantumSensor Corp
        </td>

        <td>
          QuantumSensor Corp Information Technology 2023...
        </td>

        <td>
          \[{'author': 'Morgan Johnson, Technology Sector...
        </td>

        <td>
          0.644383
        </td>

        <td>
          0.000054
        </td>
      </tr>
    </tbody>
  </table>
</div>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
