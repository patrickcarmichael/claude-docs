---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Get Started

### Example with text

In the example below, we use the [Rerank API endpoint](/reference/rerank) to index the list of `documents` from most to least relevant to the query `What animals can I find near Peru?`.
```py
  from together import Together

  client = Together()

  query = "What animals can I find near Peru?"

  documents = [
      "The giant panda (Ailuropoda melanoleuca), also known as the panda bear or simply panda, is a bear species endemic to China.",
      "The llama is a domesticated South American camelid, widely used as a meat and pack animal by Andean cultures since the pre-Columbian era.",
      "The wild Bactrian camel (Camelus ferus) is an endangered species of camel endemic to Northwest China and southwestern Mongolia.",
      "The guanaco is a camelid native to South America, closely related to the llama. Guanacos are one of two wild South American camelids; the other species is the vicuña, which lives at higher elevations.",
  ]

  response = client.rerank.create(
      model="Salesforce/Llama-Rank-V1",
      query=query,
      documents=documents,
      top_n=2,
  )

  for result in response.results:
      print(f"Document Index: {result.index}")
      print(f"Document: {documents[result.index]}")
      print(f"Relevance Score: {result.relevance_score}")
```
```ts
  import Together from "together-ai";

  const client = new Together();

  const documents = [
    "The giant panda (Ailuropoda melanoleuca), also known as the panda bear or simply panda, is a bear species endemic to China.",
    "The llama is a domesticated South American camelid, widely used as a meat and pack animal by Andean cultures since the pre-Columbian era.",
    "The wild Bactrian camel (Camelus ferus) is an endangered species of camel endemic to Northwest China and southwestern Mongolia.",
    "The guanaco is a camelid native to South America, closely related to the llama. Guanacos are one of two wild South American camelids; the other species is the vicuña, which lives at higher elevations.",
  ];

  const response = await client.rerank({
    model: "Salesforce/Llama-Rank-V1",
    query: "What animals can I find near Peru?",
    documents,
    top_n: 2,
  });

  for (const result of response.results) {
    console.log(`Document index: ${result.index}`);
    console.log(`Document: ${documents[result.index]}`);
    console.log(`Relevance score: ${result.relevance_score}`);
  }
```
```sh
  curl -X POST "https://api.together.xyz/v1/rerank" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "Salesforce/Llama-Rank-v1",
         "query": "What animals can I find near Peru?",
         "documents": [{
            "title": "Llama",
            "text": "The llama is a domesticated South American camelid, widely used as a meat and pack animal by Andean cultures since the pre-Columbian era."
          },
          {
            "title": "Panda",
            "text": "The giant panda (Ailuropoda melanoleuca), also known as the panda bear or simply panda, is a bear species endemic to China."
          },
          {
            "title": "Guanaco",
            "text": "The guanaco is a camelid native to South America, closely related to the llama. Guanacos are one of two wild South American camelids; the other species is the vicuña, which lives at higher elevations."
          },
          {
            "title": "Wild Bactrian camel",
            "text": "The wild Bactrian camel (Camelus ferus) is an endangered species of camel endemic to Northwest China and southwestern Mongolia."
          }]
       }'
```

### Example with JSON Data

Alternatively, you can pass in a JSON object and specify the fields you’d like to rank over, and the order they should be considered in. If you do not pass in any `rank_fields`, it will default to the text key.

The example below shows passing in some emails, with the query `Which pricing did we get from Oracle?`.
```py
  from together import Together

  client = Together()

  query = "Which pricing did we get from Oracle?"

  documents = [
      {
          "from": "Paul Doe <paul_fake_doe@oracle.com>",
          "to": ["Steve <steve@me.com>", "lisa@example.com"],
          "date": "2024-03-27",
          "subject": "Follow-up",
          "text": "We are happy to give you the following pricing for your project.",
      },
      {
          "from": "John McGill <john_fake_mcgill@microsoft.com>",
          "to": ["Steve <steve@me.com>"],
          "date": "2024-03-28",
          "subject": "Missing Information",
          "text": "Sorry, but here is the pricing you asked for for the newest line of your models.",
      },
      {
          "from": "John McGill <john_fake_mcgill@microsoft.com>",
          "to": ["Steve <steve@me.com>"],
          "date": "2024-02-15",
          "subject": "Commited Pricing Strategy",
          "text": "I know we went back and forth on this during the call but the pricing for now should follow the agreement at hand.",
      },
      {
          "from": "Generic Airline Company<no_reply@generic_airline_email.com>",
          "to": ["Steve <steve@me.com>"],
          "date": "2023-07-25",
          "subject": "Your latest flight travel plans",
          "text": "Thank you for choose to fly Generic Airline Company. Your booking status is confirmed.",
      },
      {
          "from": "Generic SaaS Company<marketing@generic_saas_email.com>",
          "to": ["Steve <steve@me.com>"],
          "date": "2024-01-26",
          "subject": "How to build generative AI applications using Generic Company Name",
          "text": "Hey Steve! Generative AI is growing so quickly and we know you want to build fast!",
      },
      {
          "from": "Paul Doe <paul_fake_doe@oracle.com>",
          "to": ["Steve <steve@me.com>", "lisa@example.com"],
          "date": "2024-04-09",
          "subject": "Price Adjustment",
          "text": "Re: our previous correspondence on 3/27 we'd like to make an amendment on our pricing proposal. We'll have to decrease the expected base price by 5%.",
      },
  ]

  response = client.rerank.create(
      model="Salesforce/Llama-Rank-V1",
      query=query,
      documents=documents,
      return_documents=True,
      rank_fields=["from", "to", "date", "subject", "text"],
  )

  print(response)
```
```ts
  import Together from "together-ai";

  const client = new Together();

  const documents = [
    {
      from: "Paul Doe <paul_fake_doe@oracle.com>",
      to: ["Steve <steve@me.com>", "lisa@example.com"],
      date: "2024-03-27",
      subject: "Follow-up",
      text: "We are happy to give you the following pricing for your project.",
    },
    {
      from: "John McGill <john_fake_mcgill@microsoft.com>",
      to: ["Steve <steve@me.com>"],
      date: "2024-03-28",
      subject: "Missing Information",
      text: "Sorry, but here is the pricing you asked for for the newest line of your models.",
    },
    {
      from: "John McGill <john_fake_mcgill@microsoft.com>",
      to: ["Steve <steve@me.com>"],
      date: "2024-02-15",
      subject: "Commited Pricing Strategy",
      text: "I know we went back and forth on this during the call but the pricing for now should follow the agreement at hand.",
    },
    {
      from: "Generic Airline Company<no_reply@generic_airline_email.com>",
      to: ["Steve <steve@me.com>"],
      date: "2023-07-25",
      subject: "Your latest flight travel plans",
      text: "Thank you for choose to fly Generic Airline Company. Your booking status is confirmed.",
    },
    {
      from: "Generic SaaS Company<marketing@generic_saas_email.com>",
      to: ["Steve <steve@me.com>"],
      date: "2024-01-26",
      subject:
        "How to build generative AI applications using Generic Company Name",
      text: "Hey Steve! Generative AI is growing so quickly and we know you want to build fast!",
    },
    {
      from: "Paul Doe <paul_fake_doe@oracle.com>",
      to: ["Steve <steve@me.com>", "lisa@example.com"],
      date: "2024-04-09",
      subject: "Price Adjustment",
      text: "Re: our previous correspondence on 3/27 we'd like to make an amendment on our pricing proposal. We'll have to decrease the expected base price by 5%.",
    },
  ];

  const response = await client.rerank({
    model: "Salesforce/Llama-Rank-V1",
    query: "Which pricing did we get from Oracle?",
    documents,
    return_documents: true,
    rank_fields: ["from", "to", "date", "subject", "text"],
  });

  console.log(response);
```
```sh
  curl -X POST "https://api.together.xyz/v1/rerank" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "Salesforce/Llama-Rank-v1",
         "query": "Which pricing did we get from Oracle?",
         "documents": [
           {
             "from": "Paul Doe <paul_fake_doe@oracle.com>",
             "to": ["Steve <steve@me.com>", "lisa@example.com"],
             "date": "2024-03-27",
             "subject": "Follow-up",
             "text": "We are happy to give you the following pricing for your project."
           },
           {
             "from": "John McGill <john_fake_mcgill@microsoft.com>",
             "to": ["Steve <steve@me.com>"],
             "date": "2024-03-28",
             "subject": "Missing Information",
             "text": "Sorry, but here is the pricing you asked for for the newest line of your models."
           },
           {
             "from": "John McGill <john_fake_mcgill@microsoft.com>",
             "to": ["Steve <steve@me.com>"],
             "date": "2024-02-15",
             "subject": "Commited Pricing Strategy",
             "text": "I know we went back and forth on this during the call but the pricing for now should follow the agreement at hand."
           },
           {
             "from": "Generic Airline Company<no_reply@generic_airline_email.com>",
             "to": ["Steve <steve@me.com>"],
             "date": "2023-07-25",
             "subject": "Your latest flight travel plans",
             "text": "Thank you for choose to fly Generic Airline Company. Your booking status is confirmed."
           },
           {
             "from": "Generic SaaS Company<marketing@generic_saas_email.com>",
             "to": ["Steve <steve@me.com>"],
             "date": "2024-01-26",
             "subject": "How to build generative AI applications using Generic Company Name",
             "text": "Hey Steve! Generative AI is growing so quickly and we know you want to build fast!"
           },
           {
             "from": "Paul Doe <paul_fake_doe@oracle.com>",
             "to": ["Steve <steve@me.com>", "lisa@example.com"],
             "date": "2024-04-09",
             "subject": "Price Adjustment",
             "text": "Re: our previous correspondence on 3/27 we'\''d like to make an amendment on our pricing proposal. We'\''ll have to decrease the expected base price by 5%."
           }
         ],
         "return_documents": true,
         "rank_fields": ["from", "to", "date", "subject", "text"]
       }'
```

In the `documents` parameter, we are passing in a list of objects which have the key values: `['from', 'to', 'date', 'subject', 'text']`. As part of the Rerank call, under `rank_fields` we are specifying which keys to rank over, as well as the order in which the key value pairs should be considered.

When the model returns rankings, we'll also receive each email in the response because the `return_documents` option is set to true.
```json
{
  "model": "Salesforce/Llama-Rank-v1",
  "choices": [
    {
      "index": 0,
      "document": {
        "text": "{\"from\":\"Paul Doe <paul_fake_doe@oracle.com>\",\"to\":[\"Steve <steve@me.com>\",\"lisa@example.com\"],\"date\":\"2024-03-27\",\"subject\":\"Follow-up\",\"text\":\"We are happy to give you the following pricing for your project.\"}"
      },
      "relevance_score": 0.606349439153678
    },
    {
      "index": 5,
      "document": {
        "text": "{\"from\":\"Paul Doe <paul_fake_doe@oracle.com>\",\"to\":[\"Steve <steve@me.com>\",\"lisa@example.com\"],\"date\":\"2024-04-09\",\"subject\":\"Price Adjustment\",\"text\":\"Re: our previous correspondence on 3/27 we'd like to make an amendment on our pricing proposal. We'll have to decrease the expected base price by 5%.\"}"
      },
      "relevance_score": 0.5059948716207964
    },
    {
      "index": 1,
      "document": {
        "text": "{\"from\":\"John McGill <john_fake_mcgill@microsoft.com>\",\"to\":[\"Steve <steve@me.com>\"],\"date\":\"2024-03-28\",\"subject\":\"Missing Information\",\"text\":\"Sorry, but here is the pricing you asked for for the newest line of your models.\"}"
      },
      "relevance_score": 0.2271930688841643
    },
    {
      "index": 2,
      "document": {
        "text": "{\"from\":\"John McGill <john_fake_mcgill@microsoft.com>\",\"to\":[\"Steve <steve@me.com>\"],\"date\":\"2024-02-15\",\"subject\":\"Commited Pricing Strategy\",\"text\":\"I know we went back and forth on this during the call but the pricing for now should follow the agreement at hand.\"}"
      },
      "relevance_score": 0.2229844295907072
    },
    {
      "index": 4,
      "document": {
        "text": "{\"from\":\"Generic SaaS Company<marketing@generic_saas_email.com>\",\"to\":[\"Steve <steve@me.com>\"],\"date\":\"2024-01-26\",\"subject\":\"How to build generative AI applications using Generic Company Name\",\"text\":\"Hey Steve! Generative AI is growing so quickly and we know you want to build fast!\"}"
      },
      "relevance_score": 0.0021253144747196517
    },
    {
      "index": 3,
      "document": {
        "text": "{\"from\":\"Generic Airline Company<no_reply@generic_airline_email.com>\",\"to\":[\"Steve <steve@me.com>\"],\"date\":\"2023-07-25\",\"subject\":\"Your latest flight travel plans\",\"text\":\"Thank you for choose to fly Generic Airline Company. Your booking status is confirmed.\"}"
      },
      "relevance_score": 0.0010322494264659
    }
  ]
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
