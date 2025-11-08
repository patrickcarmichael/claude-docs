---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Usage Notes

For general guidance on how to responsibly leverage the Cohere platform, we recommend you consult our [Usage Guidelines](https://docs.cohere.com/docs/usage-guidelines) page.

In the next few sections, we offer some model-specific usage notes.

### Model Toxicity and Bias

Language  models  learn  the  statistical  relationships  present  in  training  datasets,  which  may  include toxic language and historical biases along race, gender, sexual orientation, ability, language, cultural, and  intersectional  dimensions. We recommend that developers be especially attuned to risks presented by toxic degeneration and the reinforcement of historical social biases.

#### Toxic  Degeneration

Models have been trained on a wide variety of text from many sources that contain toxic content (see Luccioni and Viviano, 2021). As a result, models  may  generate  toxic  text. This  may  include  obscenities, sexually  explicit content, and  messages  which  mischaracterize or stereotype  groups of people based on problematic historical biases perpetuated by internet communities (see Gehman et al., 2020 for more about toxic language model degeneration).

We have put safeguards in place to avoid generating harmful text, and while they are effective (see the "Safety Benchmarks" section above), it is still possible to encounter toxicity, especially over long conversations with multiple turns.

#### Reinforcing Historical Social Biases

Language models capture problematic associations and stereotypes that are prominent on the internet and society at large. They should not be used to make decisions about individuals or the groups they belong to. For example, it can be dangerous to use Generation model outputs in CV ranking systems due to known biases (Nadeem et al., 2020).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
