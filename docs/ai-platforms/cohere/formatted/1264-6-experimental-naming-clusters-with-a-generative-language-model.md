---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 6- (Experimental) Naming clusters with a generative language model

While the extracted keywords do add a lot of information to help us identify the clusters at a glance, we should be able to have a generative model look at these keywords and suggest a name. So far I have reasonable results from a prompt that looks like this:
```
The common theme of the following words: books, book, read, the, you, are, what, best, in, your
is that they all relate to favorite books to read.
---
The common theme of the following words: startup, company, yc, failed
is that they all relate to startup companies and their failures.
---
The common theme of the following words: freelancer, wants, hired, be, who, seeking, to, 2014, 2020, april
is that they all relate to hiring for a freelancer to join the team of a startup.
---
The common theme of the following words: <insert keywords here>
is that they all relate to
```
There's a lot of room for improvement though. I'm really excited by this use case because it adds so much information. Imagine if the in the following tree of topics, you assigned each cluster an intelligible name. Then imagine if you assigned each *branching* a name as well

<img alt="" src="https://raw.githubusercontent.com/cohere-ai/cohere-developer-experience/main/notebooks/images/kmeans-centroid-dendrogram.png" />

We can’t wait to see what you start building! Share your projects or find support on our [Discord server](https://discord.com/invite/co-mmunity).


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
