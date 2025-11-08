---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generate the podcast script

script = generate_script(SYSTEM_PROMPT, text, Script)
```

Above we are also handling the erroneous case which will let us know if the script was not generated following the `Script` class.

Now we can have a look at the script that is generated:
```json
[DialogueItem(speaker='Host (Jane)', text='Welcome to today’s podcast. I’m your host, Jane. Joining me is Junlin Wang, a researcher from Duke University and Together AI. Junlin, welcome to the show!'),
 DialogueItem(speaker='Guest', text='Thanks for having me, Jane. I’m excited to be here.'),
 DialogueItem(speaker='Host (Jane)', text='Junlin, your recent paper proposes a new approach to enhancing large language models (LLMs) by leveraging the collective strengths of multiple models. Can you tell us more about this?'),
 DialogueItem(speaker='Guest', text='Our approach is called Mixture-of-Agents (MoA). We found that LLMs exhibit a phenomenon we call collaborativeness, where they generate better responses when presented with outputs from other models, even if those outputs are of lower quality.'),
 DialogueItem(speaker='Host (Jane)', text='That’s fascinating. Can you walk us through how MoA works?'),
 DialogueItem(speaker='Guest', text='MoA consists of multiple layers, each comprising multiple LLM agents. Each agent takes all the outputs from agents in the previous layer as auxiliary information in generating its response. This process is repeated for several cycles until a more robust and comprehensive response is obtained.'),
 DialogueItem(speaker='Host (Jane)', text='I see. And what kind of results have you seen with MoA?'),
 DialogueItem(speaker='Guest', text='We evaluated MoA on several benchmarks, including AlpacaEval 2.0, MT-Bench, and FLASK. Our results show substantial improvements in response quality, with MoA achieving state-of-the-art performance on these benchmarks.'),
 DialogueItem(speaker='Host (Jane)', text='Wow, that’s impressive. What about the cost-effectiveness of MoA?'),
 DialogueItem(speaker='Guest', text='We found that MoA can deliver performance comparable to GPT-4 Turbo while being 2x more cost-effective. This is because MoA can leverage the strengths of multiple models, reducing the need for expensive and computationally intensive training.'),
 DialogueItem(speaker='Host (Jane)', text='That’s great to hear. Junlin, what do you think is the potential impact of MoA on the field of natural language processing?'),
 DialogueItem(speaker='Guest', text='I believe MoA has the potential to significantly enhance the effectiveness of LLM-driven chat assistants, making AI more accessible to a wider range of people. Additionally, MoA can improve the interpretability of models, facilitating better alignment with human reasoning.'),
 DialogueItem(speaker='Host (Jane)', text='That’s a great point. Junlin, thank you for sharing your insights with us today.'),
 DialogueItem(speaker='Guest', text='Thanks for having me, Jane. It was a pleasure discussing MoA with you.')]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
