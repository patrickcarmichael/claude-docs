---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Creating Secrets

<Steps>
  <Step title="Navigate to the secrets page on your dashboard">
        <img src="https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/new.png?fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=5a5a1f8a626c6e678d22a44addde7fc5" alt="new.png" data-og-width="1540" width="1540" data-og-height="1106" height="1106" data-path="images/new.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/new.png?w=280&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=fad25753520447ffdbb63182fc92d194 280w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/new.png?w=560&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=ed05cd99096aa33925c989fc19157402 560w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/new.png?w=840&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=bcc4928202a856b5a0d8593dfce2d5e8 840w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/new.png?w=1100&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=bc5a42177b80825f9d73531180c34088 1100w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/new.png?w=1650&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=7e78b4e3c90000837e7967da461cd13a 1650w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/new.png?w=2500&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=d279764c7f5a0b7c4f94bc853fb19950 2500w" />
  </Step>

  <Step title="Create a new secret">
        <img src="https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/test.png?fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=5b398ccbb320787377d235b9114bdc8d" alt="test.png" data-og-width="1826" width="1826" data-og-height="964" height="964" data-path="images/test.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/test.png?w=280&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=23ec9e053dfaccbac993cf5554db0c5e 280w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/test.png?w=560&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=87d4aa204ceee34d9b2bb7826a7786b8 560w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/test.png?w=840&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=98ed857288a080843053ecc42d52b809 840w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/test.png?w=1100&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=2342b7078b857409fa37724cd0e9ac92 1100w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/test.png?w=1650&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=b8653468aa02bb04f0c7621ec1d13f40 1650w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/test.png?w=2500&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=f47a1dd88880fa5976571540f91478d0 2500w" />

    All secrets created here will be injected as environment variables for your Evaluator to access.
  </Step>

  <Step title="Update the Evaluator to access the new secret">
    <img src="https://mintcdn.com/fireworksai/kZCV7UvEi6F9hwE9/evaluators/developer_guide/images/llm-judge-w-secret-example.png?fit=max&auto=format&n=kZCV7UvEi6F9hwE9&q=85&s=361f2aaad5c4db9f675c8c976bb2a8b0" alt="llm-judge-w-secret-example.png" data-og-width="1532" width="1532" data-og-height="1590" height="1590" data-path="evaluators/developer_guide/images/llm-judge-w-secret-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/kZCV7UvEi6F9hwE9/evaluators/developer_guide/images/llm-judge-w-secret-example.png?w=280&fit=max&auto=format&n=kZCV7UvEi6F9hwE9&q=85&s=d6b821591273d52965c0cb2cb81e71d1 280w, https://mintcdn.com/fireworksai/kZCV7UvEi6F9hwE9/evaluators/developer_guide/images/llm-judge-w-secret-example.png?w=560&fit=max&auto=format&n=kZCV7UvEi6F9hwE9&q=85&s=9bc6628ccdc7b629942e98a84f2c3ac1 560w, https://mintcdn.com/fireworksai/kZCV7UvEi6F9hwE9/evaluators/developer_guide/images/llm-judge-w-secret-example.png?w=840&fit=max&auto=format&n=kZCV7UvEi6F9hwE9&q=85&s=f5f2ba98695daf6da69d6b8fcb812cac 840w, https://mintcdn.com/fireworksai/kZCV7UvEi6F9hwE9/evaluators/developer_guide/images/llm-judge-w-secret-example.png?w=1100&fit=max&auto=format&n=kZCV7UvEi6F9hwE9&q=85&s=c7509aadebfa1aff99b72aebb6fcd20d 1100w, https://mintcdn.com/fireworksai/kZCV7UvEi6F9hwE9/evaluators/developer_guide/images/llm-judge-w-secret-example.png?w=1650&fit=max&auto=format&n=kZCV7UvEi6F9hwE9&q=85&s=d09e34ac5e5abcd720cd2d0c50dc0797 1650w, https://mintcdn.com/fireworksai/kZCV7UvEi6F9hwE9/evaluators/developer_guide/images/llm-judge-w-secret-example.png?w=2500&fit=max&auto=format&n=kZCV7UvEi6F9hwE9&q=85&s=3059f16a9eede3714ce3dfd15c1d7276 2500w" />
    See [LLM as a judge](/evaluators/examples/advanced_examples/advanced_reward_functions#llm-as-a-judge) section for full code example
  </Step>
</Steps>

And that's it! If you want to learn more about creating evaluators, see:

1. Learn about [Evaluation Workflows](/evaluators/developer_guide/evaluation_workflows) for testing and deploying your functions
2. Explore [Advanced Reward Functions](/evaluators/examples/advanced_examples/advanced_reward_functions) to see these types in action
3. Check the [API Reference](/evaluators/api_reference/data_models) for complete details on all data types


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
