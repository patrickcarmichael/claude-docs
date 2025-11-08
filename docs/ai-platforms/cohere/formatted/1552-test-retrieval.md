---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Test Retrieval

```python PYTHON
vectorstore.retrieve("multi-head attention definition")
```
```
[{'text': 'The attention step used in transformer models is actually much more powerful, and it’s called multi-head attention. In multi-head attention, several different embeddings are used to modify the vectors and add context to them. Multi-head attention has helped language models reach much higher levels of efficacy when processing and generating text.',
  'title': 'Transformer Models',
  'url': 'https://docs.cohere.com/docs/transformer-models'},
 {'text': "What you learned in this chapter is simple self-attention. However, we can do much better than that. There is a method called multi-head attention, in which one doesn't only consider one embedding, but several different ones. These are all obtained from the original by transforming it in different ways. Multi-head attention has been very successful at the task of adding context to text. If you'd like to learn more about the self and multi-head attention, you can check out the following two",
  'title': 'The Attention Mechanism',
  'url': 'https://docs.cohere.com/docs/the-attention-mechanism'},
 {'text': 'Attention helps give context to each word, based on the other words in the sentence (or text).',
  'title': 'Transformer Models',
  'url': 'https://docs.cohere.com/docs/transformer-models'}]
```
Next, we implement a class to handle the interaction between the user and the chatbot. It takes an instance of the `Vectorstore` class as input.

The `run()` method will be used to run the chatbot application. It begins with the logic for getting the user message, along with a way for the user to end the conversation.

Based on the user message, the chatbot needs to decide if it needs to consult external information before responding. If so, the chatbot determines an optimal set of search queries to use for retrieval. When we call `co.chat()` with `search_queries_only=True`, the Chat endpoint handles this for us automatically.

The generated queries can be accessed from the `search_queries` field of the object that is returned. Then, what happens next depends on how many queries are returned.

* If queries are returned, we call the `retrieve()` method of the Vectorstore object for the retrieval step. The retrieved document chunks are then passed to the Chat endpoint by adding a `documents` parameter when we call `co.chat()` again.
* Otherwise, if no queries are returned, we call the Chat endpoint another time, passing the user message and without needing to add any documents to the call.

In either case, we also pass the `conversation_id` parameter, which retains the interactions between the user and the chatbot in the same conversation thread. We also enable the `stream` parameter so we can stream the chatbot response.

We then print the chatbot's response. In the case that the external information was used to generate a response, we also display citations.
```python PYTHON
class Chatbot:
    def __init__(self, vectorstore: Vectorstore):
        """
        Initializes an instance of the Chatbot class.

        Parameters:
        vectorstore (Vectorstore): An instance of the Vectorstore class.

        """
        self.vectorstore = vectorstore
        self.conversation_id = str(uuid.uuid4())

    def run(self):
        """
        Runs the chatbot application.

        """
        while True:
            # Get the user message

            message = input("User: ")

            # Typing "quit" ends the conversation

            if message.lower() == "quit":
              print("Ending chat.")
              break
            # else:                       # Uncomment for Google Colab to avoid printing the same thing twice

              # print(f"User: {message}") # Uncomment for Google Colab to avoid printing the same thing twice

            # Generate search queries (if any)

            response = co.chat(message=message,
                               model="command-r",
                               search_queries_only=True)

            # If there are search queries, retrieve document chunks and respond

            if response.search_queries:
                print("Retrieving information...", end="")

                # Retrieve document chunks for each query

                documents = []
                for query in response.search_queries:
                    documents.extend(self.vectorstore.retrieve(query.text))

                # Use document chunks to respond

                response = co.chat_stream(
                    message=message,
                    model="command-r",
                    documents=documents,
                    conversation_id=self.conversation_id,
                )

            # If there is no search query, directly respond

            else:
                response = co.chat_stream(
                    message=message,
                    model="command-r",
                    conversation_id=self.conversation_id,
                )

            # Print the chatbot response, citations, and documents

            print("\nChatbot:")
            citations = []
            cited_documents = []

            # Display response

            for event in response:
                if event.event_type == "text-generation":
                    print(event.text, end="")
                elif event.event_type == "citation-generation":
                    citations.extend(event.citations)
                elif event.event_type == "search-results":
                    cited_documents = event.documents

            # Display citations and source documents

            if citations:
              print("\n\nCITATIONS:")
              for citation in citations:
                print(citation)

              print("\nDOCUMENTS:")
              for document in cited_documents:
                print(document)

            print(f"\n{'-'*100}\n")
```
We can now run the chatbot. For this, we create the instance of `Chatbot` and run the chatbot by invoking the `run()` method.

The format of each citation is:

* `start`: The starting point of a span where one or more documents are referenced
* `end`: The ending point of a span where one or more documents are referenced
* `text`: The text representing this span
* `document_ids`: The IDs of the documents being referenced (`doc_0` being the ID of the first document passed to the `documents` creating parameter in the endpoint call, and so on)
```python PYTHON
chatbot = Chatbot(vectorstore)

chatbot.run()
```
```
Chatbot:
Hello! What's your question? I'm here to help you in any way I can.
----------------------------------------------------------------------------------------------------

Retrieving information...
Chatbot:
Word embeddings associate words with lists of numbers, so that similar words are close to each other and dissimilar words are further away.
Sentence embeddings do the same thing, but for sentences. Each sentence is associated with a vector of numbers in a coherent way, so that similar sentences are assigned similar vectors, and different sentences are given different vectors.

CITATIONS:
start=0 end=15 text='Word embeddings' document_ids=['doc_0']
start=16 end=53 text='associate words with lists of numbers' document_ids=['doc_0']
start=63 end=100 text='similar words are close to each other' document_ids=['doc_0']
start=105 end=139 text='dissimilar words are further away.' document_ids=['doc_0']
start=140 end=159 text='Sentence embeddings' document_ids=['doc_0', 'doc_2']
start=160 end=177 text='do the same thing' document_ids=['doc_0', 'doc_2']
start=198 end=211 text='Each sentence' document_ids=['doc_0', 'doc_2']
start=215 end=250 text='associated with a vector of numbers' document_ids=['doc_0', 'doc_2']
start=256 end=264 text='coherent' document_ids=['doc_2']
start=278 end=295 text='similar sentences' document_ids=['doc_0', 'doc_2']
start=300 end=324 text='assigned similar vectors' document_ids=['doc_0', 'doc_2']
start=330 end=349 text='different sentences' document_ids=['doc_0', 'doc_2']
start=354 end=378 text='given different vectors.' document_ids=['doc_0', 'doc_2']

DOCUMENTS:
{'id': 'doc_0', 'text': 'In the previous chapters, you learned about word and sentence embeddings and similarity between words and sentences. In short, a word embedding is a way to associate words with lists of numbers (vectors) in such a way that similar words are associated with numbers that are close by, and dissimilar words with numbers that are far away from each other. A sentence embedding does the same thing, but associating a vector to every sentence. Similarity is a way to measure how similar two words (or', 'title': 'The Attention Mechanism', 'url': 'https://docs.cohere.com/docs/the-attention-mechanism'}
{'id': 'doc_1', 'text': 'Sentence embeddings\n\nSo word embeddings seem to be pretty useful, but in reality, human language is much more complicated than simply a bunch of words put together. Human language has structure, sentences, etc. How would one be able to represent, for instance, a sentence? Well, here’s an idea. How about the sums of scores of all the words? For example, say we have a word embedding that assigns the following scores to these words:\n\nNo: [1,0,0,0]\n\nI: [0,2,0,0]\n\nAm: [-1,0,1,0]\n\nGood: [0,0,1,3]', 'title': 'Text Embeddings', 'url': 'https://docs.cohere.com/docs/text-embeddings'}
{'id': 'doc_2', 'text': 'This is where sentence embeddings come into play. A sentence embedding is just like a word embedding, except it associates every sentence with a vector full of numbers, in a coherent way. By coherent, I mean that it satisfies similar properties as a word embedding. For instance, similar sentences are assigned to similar vectors, different sentences are assigned to different vectors, and most importantly, each of the coordinates of the vector identifies some (whether clear or obscure) property of', 'title': 'Text Embeddings', 'url': 'https://docs.cohere.com/docs/text-embeddings'}

----------------------------------------------------------------------------------------------------

Retrieving information...
Chatbot:
The similarities between words and sentences are both quantitative measures of how close the two given items are. There are two types of similarities that can be defined: dot product similarity, and cosine similarity. These methods can determine how similar two words, or sentences, are.

CITATIONS:
start=54 end=75 text='quantitative measures' document_ids=['doc_0']
start=79 end=88 text='how close' document_ids=['doc_0']
start=124 end=133 text='two types' document_ids=['doc_0', 'doc_4']
start=171 end=193 text='dot product similarity' document_ids=['doc_0', 'doc_4']
start=199 end=217 text='cosine similarity.' document_ids=['doc_0', 'doc_4']
start=236 end=257 text='determine how similar' document_ids=['doc_0', 'doc_4']

DOCUMENTS:
{'id': 'doc_0', 'text': 'Now that we know embeddings quite well, let’s move on to using them to find similarities. There are two types of similarities we’ll define in this post: dot product similarity and cosine similarity. Both are very similar and very useful to determine if two words (or sentences) are similar.', 'title': 'Similarity Between Words and Sentences', 'url': 'https://docs.cohere.com/docs/similarity-between-words-and-sentences'}
{'id': 'doc_1', 'text': 'But let me add some numbers to this reasoning to make it more clear. Imagine that we calculate similarities for the words in each sentence, and we get the following:\n\nThis similarity makes sense in the following ways:\n\nThe similarity between each word and itself is 1.\n\nThe similarity between any irrelevant word (“the”, “of”, etc.) and any other word is 0.\n\nThe similarity between “bank” and “river” is 0.11.\n\nThe similarity between “bank” and “money” is 0.25.', 'title': 'The Attention Mechanism', 'url': 'https://docs.cohere.com/docs/the-attention-mechanism'}
{'id': 'doc_2', 'text': 'And the results are:\n\nThe similarity between sentences 1 and 2: 6738.2858668486715\n\nThe similarity between sentences 1 and 3: -122.22666955510499\n\nThe similarity between sentences 2 and 3: -3.494608113647928\n\nThese results certainly confirm our predictions. The similarity between sentences 1 and 2 is 6738, which is high. The similarities between sentences 1 and 3, and 2 and 3, are -122 and -3.5 (dot products are allowed to be negative too!), which are much lower.', 'title': 'Similarity Between Words and Sentences', 'url': 'https://docs.cohere.com/docs/similarity-between-words-and-sentences'}
{'id': 'doc_3', 'text': 'But let me add some numbers to this reasoning to make it more clear. Imagine that we calculate similarities for the words in each sentence, and we get the following:\n\nThis similarity makes sense in the following ways:\n\nThe similarity between each word and itself is 1.\n\nThe similarity between any irrelevant word (“the”, “of”, etc.) and any other word is 0.\n\nThe similarity between “bank” and “river” is 0.11.\n\nThe similarity between “bank” and “money” is 0.25.', 'title': 'The Attention Mechanism', 'url': 'https://docs.cohere.com/docs/the-attention-mechanism'}
{'id': 'doc_4', 'text': 'Now that we know embeddings quite well, let’s move on to using them to find similarities. There are two types of similarities we’ll define in this post: dot product similarity and cosine similarity. Both are very similar and very useful to determine if two words (or sentences) are similar.', 'title': 'Similarity Between Words and Sentences', 'url': 'https://docs.cohere.com/docs/similarity-between-words-and-sentences'}
{'id': 'doc_5', 'text': 'And the results are:\n\nThe similarity between sentences 1 and 2: 6738.2858668486715\n\nThe similarity between sentences 1 and 3: -122.22666955510499\n\nThe similarity between sentences 2 and 3: -3.494608113647928\n\nThese results certainly confirm our predictions. The similarity between sentences 1 and 2 is 6738, which is high. The similarities between sentences 1 and 3, and 2 and 3, are -122 and -3.5 (dot products are allowed to be negative too!), which are much lower.', 'title': 'Similarity Between Words and Sentences', 'url': 'https://docs.cohere.com/docs/similarity-between-words-and-sentences'}

----------------------------------------------------------------------------------------------------

Ending chat.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
