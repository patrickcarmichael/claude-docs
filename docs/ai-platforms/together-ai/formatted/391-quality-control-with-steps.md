---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Quality Control with Steps

Compare different step counts for quality vs. speed:
```python
import time

prompt = "A majestic mountain landscape"
step_counts = [1, 6, 12]

for steps in step_counts:
    start = time.time()
    response = client.images.generate(
        prompt=prompt,
        model="black-forest-labs/FLUX.1-schnell",
        steps=steps,
        seed=42,  # Same seed for fair comparison

    )
    elapsed = time.time() - start
    print(f"Steps: {steps} - Generated in {elapsed:.2f}s")
```

<img src="https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=c6dad7983bb96503032966b36ad41716" alt="Reference image: steps.png" data-og-width="1458" width="1458" data-og-height="511" height="511" data-path="images/steps.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?w=280&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=4ac6dc13d95356376c441407f9e3aea3 280w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?w=560&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=4441ef2ff0f4f656dfe005c46d001b1d 560w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?w=840&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=ed6e70593fcdbd62d8387a57b1e05e4c 840w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?w=1100&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=b28573546f8b32bbb049a6f7d5de7dd0 1100w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?w=1650&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=60a317f47e10d95ed43d6e32e194fc2b 1650w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?w=2500&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=d32a39c2ef3ac49c5d0e48e6b3f2d87f 2500w" />

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
