---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How are Large Language Models Trained?

Eliding a great deal of technical complexity, a large language model is just a neural network trained to predict the [next token](/docs/tokens-and-tokenizers#what-is-a-token), given the tokens that have come before. Take a sentence like "Hang on, I need to go inside and grab my \_\_\_." As a human being with a great deal of experience using natural language, you can make some reasonable guesses about which token will complete this sentence even with no additional context:

* "Hang on, I need to go inside and grab my **bag**."
* "Hang on, I need to go inside and grab my **keys**."
* Etc.

Of course, there are other possibilities that are plausible, but less likely:

* "Hang on, I need to go inside and grab my **friend**."
* "Hang on, I need to go inside and grab my **book**."

And, there's a long-tail of possibilities that are technically grammatically correct but which effectively never occur in a real exchange:

* "Hang on, I need to go inside and grab my **giraffe**."

*You* have an intuitive sense of how a sentence like this will end because you've been using language all your life. A model like Command R+ must learn how to perform the same feat by seeing billions of token sequences and figuring out a statistical distribution over them that allows it to predict what comes next.

Once it's done so, it can take a prompt like "Help me generate some titles for a blog post about quantum computing," and use the distribution it has learned to generate the series of tokens it *thinks* would follow such a request. Since it's an *AI* system *generating* tokens, it's known as "generative AI," and with models as powerful as Cohere's, the results are often surprisingly good.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
