---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Wikipedia Semantic Search with Cohere + Weaviate

> This page contains a description of building a Wikipedia-focused search engine with Cohere's LLM platform and the Weaviate vector database.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Wikipedia_search_demo_cohere_weaviate.ipynb" />

This is starter code that you can use to search 10 million vectors from Wikipedia embedded with Cohere's multilingual model and hosted as a Weaviate public dataset. This dataset contains 1M vectors in each of the Wikipedia sites in these languages: English, German, French, Spanish, Italian, Japanese, Arabic, Chinese (Simplified), Korean, Hindi \[respective language codes: `en, de, fr, es, it, ja, ar, zh, ko, hi`]
```python PYTHON
import weaviate

cohere_api_key = ''

auth_config = weaviate.auth.AuthApiKey(api_key="76320a90-53d8-42bc-b41d-678647c6672e")
client = weaviate.Client(
    url="https://cohere-demo.weaviate.network/",
    auth_client_secret=auth_config,
    additional_headers={
        "X-Cohere-Api-Key": cohere_api_key,
    }
)

client.is_ready() #check if True
```
```txt title="Output"
True
```
Let's now define the search function that queries our vector database. Optionally, we want the ability to filter by language.
```python PYTHON

def semantic_serch(query, results_lang=''):
    """
    Query the vectors database and return the top results.


    Parameters
    ----------
        query: str
            The search query

        results_lang: str (optional)
            Retrieve results only in the specified language.
            The demo dataset has those languages:
            en, de, fr, es, it, ja, ar, zh, ko, hi

    """

    nearText = {"concepts": [query]}
    properties = ["text", "title", "url", "views", "lang", "_additional {distance}"]

    # To filter by language

    if results_lang != '':
        where_filter = {
        "path": ["lang"],
        "operator": "Equal",
        "valueString": results_lang
        }
        response = (
            client.query
            .get("Articles", properties)
            .with_where(where_filter)
            .with_near_text(nearText)
            .with_limit(5)
            .do()
        )

    # Search all languages

    else:
        response = (
            client.query
            .get("Articles", properties)
            .with_near_text(nearText)
            .with_limit(5)
            .do()
        )


    result = response['data']['Get']['Articles']

    return result


def print_result(result):
    """ Print results with colorful formatting """
    for item in result:
        print(f"\033[95m{item['title']} ({item['views']}) {item['_additional']['distance']}\033[0m")
        print(f"\033[4m{item['url']}\033[0m")
        print(item['text'])
        print()
```
We can now query the database with any query we want. In the background, Weaviate uses your Cohere API key to embed the query, then retrun the most relevant passages to the query.
```python PYTHON
query_result = semantic_serch("time travel plot twist")

print_result(query_result)
```
```txt title="Output"
[95mThe Adam Project (3000) -147.31755[0m
[4mhttps://en.wikipedia.org/wiki?curid=65867428[0m
Due to a safety feature preventing him from flying because of his injuries, Adam must bring along the younger Adam and use his DNA to enter his jet. They both are soon attacked by Maya Sorian, the leader of the dystopian world, and her assistant Christos, but are saved by Laura, who had faked her death and stayed off-grid in an unknown location. After surviving the attack and comparing notes, Laura and the Adams realize that after the invention of time travel by Louis Reed and his subsequent death, Sorian had monopolized the discovery. During her visit to 2018, Laura learned Sorian frequently came and advised her past self in order to secure her future wealth and power. To protect her secret, Sorian ordered Laura's death. Although Laura survived the assassination attempt, destruction of her time jet left her stranded in the past. The sudden arrival of Sorian's goons interrupts the reunion, and Laura fights off the attack long enough for the two Adams to escape to 2018.

[95mKang the Conqueror (2000) -146.57275[0m
[4mhttps://en.wikipedia.org/wiki?curid=393437[0m
Nathaniel Richards, a 31st-century scholar and descendant of Reed Richards' time traveling father Nathaniel, becomes fascinated with history and discovers the time travel technology created by Victor von Doom, another possible ancestor of his. He then travels back in time to ancient Egypt aboard a Sphinx-shaped timeship and becomes the Pharaoh Rama-Tut, with plans to claim En Sabah Nur—the mutant destined to become Apocalypse—as his heir. Rama-Tut's rule is cut short when he is defeated by the time-displaced Fantastic Four. An embittered Nathaniel Richards travels forward to the 20th century where he meets Doctor Doom, whom he believes might be his ancestor. He later designs an armor based on Doom's and, calling himself the Scarlet Centurion, pits the Avengers team against alternate-reality counterparts. He plans to dispose of all of them, but the Avengers manage to force him from the timeline.

[95mBack to the Future (3000) -146.4269[0m
[4mhttps://en.wikipedia.org/wiki?curid=42993[0m
That night, Marty meets his eccentric scientist friend, Emmett "Doc" Brown, in the Twin Pines mall parking lot. Doc unveils a time machine built from a modified DeLorean, powered by plutonium he swindled from Libyan terrorists. After Doc inputs a destination time of November5, 1955—the day he first conceived his time travel invention—the terrorists arrive unexpectedly and gun Doc down. Marty flees in the DeLorean, inadvertently activating time travel when he reaches .

[95mTime (2000) -146.41129[0m
[4mhttps://en.wikipedia.org/wiki?curid=30012[0m
Time travel is the concept of moving backwards or forwards to different points in time, in a manner analogous to moving through space, and different from the normal "flow" of time to an earthbound observer. In this view, all points in time (including future times) "persist" in some way. Time travel has been a plot device in fiction since the 19th century. Travelling backwards or forwards in time has never been verified as a process, and doing so presents many theoretical problems and contradictive logic which to date have not been overcome. Any technological device, whether fictional or hypothetical, that is used to achieve time travel is known as a time machine.

[95mIn Time (2000) -145.93015[0m
[4mhttps://en.wikipedia.org/wiki?curid=29446866[0m
Will and Sylvia rob Weis' time banks, giving the time capsules to the needy. They soon realize they can't significantly change anything, as prices are raised faster to compensate for the extra time. Fortis' gang ambushes them intending to collect the reward for their capture, but Will kills Fortis and his gang. Will and Sylvia then decide to rob Weis' vault of a one-million year capsule. Leon chases them back to Dayton but fails to stop them from distributing the stolen time; Leon times out, having neglected to collect his day's salary. Will and Sylvia nearly time out themselves but survive by taking Leon's salary.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
