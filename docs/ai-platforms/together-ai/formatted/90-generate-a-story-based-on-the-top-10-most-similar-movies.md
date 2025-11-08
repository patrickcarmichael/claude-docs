---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generate a story based on the top 10 most similar movies

response = client.chat.completions.create(
    model="meta-llama/Llama-3-8b-chat-hf",
    messages=[
        {
            "role": "system",
            "content": "You are a pulitzer award winning craftful story teller. Given only the overview of different plots you can weave together an interesting storyline.",
        },
        {
            "role": "user",
            "content": f"Tell me a story about {titles}. Here is some information about them {overviews}",
        },
    ],
)

print(response.choices[0].message.content)
```
Which produces the grounded output below:
```txt
What a delightful mix of plots! Here's a story that weaves them together:

In a world where superheroes are a thing of the past, Bob Parr, aka Mr. Incredible, has given up his life of saving the world to become an insurance adjuster in the suburbs. His wife, Helen, aka Elastigirl, has also hung up her superhero suit to raise their three children. However, when Bob receives a mysterious assignment from a secret organization, he's forced to don his old costume once again.

As Bob delves deeper into the assignment, he discovers that it's connected to a sinister plot to destroy the world. The plot is masterminded by a group of rogue superheroes, who were once part of the Watchmen, a group of vigilantes that were disbanded by the government in the 1980s.

The Watchmen, led by the enigmatic Rorschach, have been secretly rebuilding their team and are now determined to take revenge on the world that wronged them. Bob must team up with his old friends, including the brilliant scientist, Dr. Manhattan, to stop the Watchmen and prevent their destruction.

Meanwhile, in a different part of the world, a young boy named Sherman, who has a genius-level IQ, has built a time-travel machine with his dog, Penny. When the machine is stolen, Sherman and Penny must travel through time to prevent a series of catastrophic events from occurring.

As they travel through time, they encounter a group of friends who are making a zombie movie with a Super-8 camera. The friends, including a young boy named Charles, witness a train derailment and soon discover that it was no accident. They team up with Sherman and Penny to uncover the truth behind the crash and prevent a series of unexplained events and disappearances.

As the story unfolds, Bob and his friends must navigate a complex web of time travel and alternate realities to stop the Watchmen and prevent the destruction of the world. Along the way, they encounter a group of agents from the Men in Black, who are trying to prevent a catastrophic event from occurring.

The agents, led by Agents J and K, are on a mission to stop a powerful new super criminal, who is threatening to destroy the world. They team up with Bob and his friends to prevent the destruction and save the world.

In the end, Bob and his friends succeed in stopping the Watchmen and preventing the destruction of the world. However, the journey is not without its challenges, and Bob must confront his own demons and learn to balance his life as a superhero with his life as a husband and father.

The story concludes with Bob and his family returning to their normal lives, but with a newfound appreciation for the importance of family and the power of teamwork. The movie ends with a shot of the Parr family, including their three children, who are all wearing superhero costumes, ready to take on the next adventure that comes their way.
```typescript
Here we can see a simple RAG pipeline where we use semantic search to perform retrieval and pass relevant information into the prompt of a LLM to condition its generation.

To learn more about the Together AI API please refer to the [docs here](/intro) !


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
