---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 4. Monitor Training Progress

After successful job creation, you'll see:
```
✅ Created Reinforcement Fine-tuning Job
   name: accounts/pyroworks/reinforcementFineTuningJobs/sdnld4yn

📊 Dashboard Links:
   Evaluator: https://app.fireworks.ai/dashboard/evaluators/test-svgagent-test-svg-generation-evaluation
   Dataset:   https://app.fireworks.ai/dashboard/datasets/svgbench-dataset
   RFT Job:   https://app.fireworks.ai/dashboard/fine-tuning/reinforcement/sdnld4yn
```
Click on the **RFT Job** link to view real-time training progress, epoch counts, and rollout data.

### Training Results

After successful training, you should see performance improvements reflected in the training metrics:

<img src="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/graph.png?fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=049359a9ff673f1ebbe79870bebc646e" alt="SVG Agent Training Progress" data-og-width="1145" width="1145" data-og-height="727" height="727" data-path="images/graph.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/graph.png?w=280&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=c134ea53f61e553faed64f894fbd0968 280w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/graph.png?w=560&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=33b9a24999f60e61c13de78a55e3825a 560w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/graph.png?w=840&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=029ff347c5522122c86cdc6e5f98036b 840w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/graph.png?w=1100&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=e8920443c785f7a525342f33a80183fd 1100w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/graph.png?w=1650&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=5d4544e02181f10132840bb4c748d38f 1650w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/graph.png?w=2500&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=b064462ba16e5906472fe66a7c4b5b98 2500w" />

### SVG Quality Improvement

You can inspect individual rollouts to see the dramatic improvement in SVG generation quality. Below is a comparison between the first epoch and the final 8th epoch:

**Before (1st Epoch):**
<img src="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/before.png?fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=7160c0606439b6a7c5bc851d207975f7" alt="SVG Generation - Before Training" data-og-width="1606" width="1606" data-og-height="1136" height="1136" data-path="images/before.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/before.png?w=280&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=c3dc3ebfa621ef702648f84c4ebe2657 280w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/before.png?w=560&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=48d46aad8b93acc9e9eb40c42137d6b7 560w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/before.png?w=840&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=94f322bcf6fd77d3709ae6cebd4e9f5f 840w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/before.png?w=1100&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=03476db9954ce10c5179f934f235d60c 1100w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/before.png?w=1650&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=328e7e71e39095a6c868bb1cc40f4c19 1650w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/before.png?w=2500&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=5088edd903f4c0d3c71c18e6ff70c74b 2500w" />

**After (8th Epoch):**
<img src="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/after.png?fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=4d99b24ddb6cd458f35f2b4b00fd8646" alt="SVG Generation - After Training" data-og-width="2030" width="2030" data-og-height="1134" height="1134" data-path="images/after.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/after.png?w=280&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=1679375e0cf298aee49b0d0b666ca55e 280w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/after.png?w=560&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=f8ec41ee5416fdecf791041e61fe197d 560w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/after.png?w=840&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=622917132d20de1c72529156353d4cbe 840w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/after.png?w=1100&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=c6d98d80618948496ec32998486c4564 1100w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/after.png?w=1650&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=29b3e697b5b9667255a04a6ede7e6c06 1650w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/after.png?w=2500&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=02b71ab52b92f08ef90eade45d365361 2500w" />

The reinforcement fine tuning process significantly improves the model's ability to generate accurate, detailed SVG graphics that better match the input descriptions.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
