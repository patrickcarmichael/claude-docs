---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Model Sizing Update + Improvements

> We're updating our generative AI models to offer improved Medium and X-Large options.

Effective December 2, 2022, we will be consolidating our generative models and only serving our Medium (focused on speed) and X-Large (focused on quality). We will also be discontinuing support for our Medium embedding model.

This means that as of this date, our Small and Large generative models and Medium embedding model will be deprecated.

If you are currently using a Small or Large generative model, then we recommend that you proactively change to a Medium or X-Large model before December 2, 2022. Additionally, if you are currently using a Medium embed model, we recommend that you change to a Small embed model.

Calls to Generate large-20220926 and xlarge-20220609 will route to the new and improved X-Large model (xlarge-20221108). Calls to Generate small-20220926 will route to the new and improved Medium model (medium-20221108).

If you have any questions or concerns about this change, please don’t hesitate to contact us at: [team@cohere.com](mailto:team@cohere.com).


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
