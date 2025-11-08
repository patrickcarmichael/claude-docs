---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How to use Cline with DeepSeek V3 to build faster

Source: https://docs.together.ai/docs/how-to-use-cline

Use Cline (an AI coding agent) with DeepSeek V3 (a powerful open source model) to code faster.

Cline is a popular open source AI coding agent with nearly 2 million installs that is installable through any IDE including VS Code, Cursor, and Windsurf. In this quick guide, we want to take you through how you can combine Cline with powerful open source models on Together AI like DeepSeek V3 to supercharge your development process.

With Cline's agent, you can ask it to build features, fix bugs, or start new projects for you – and it's fully transparent in terms of the cost and tokens used as you use it. Here's how you can start using it with DeepSeek V3 on Together AI:

### 1. Install Cline

Navigate to [https://cline.bot/](https://cline.bot/) to install Cline in your preferred IDE.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/3a344cdc2e177da38ae745e627c90052375f7ef394151410723deef1629308bd-1-cline-homepage.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=cb016220da9ef86b8c3d676d47258b66" alt="" data-og-width="2922" width="2922" data-og-height="2428" height="2428" data-path="images/3a344cdc2e177da38ae745e627c90052375f7ef394151410723deef1629308bd-1-cline-homepage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/3a344cdc2e177da38ae745e627c90052375f7ef394151410723deef1629308bd-1-cline-homepage.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=3ef9417a598aa6d878f17ead86b18bd4 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/3a344cdc2e177da38ae745e627c90052375f7ef394151410723deef1629308bd-1-cline-homepage.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=63be1b6d752aa29af2f7c06881c93ba7 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/3a344cdc2e177da38ae745e627c90052375f7ef394151410723deef1629308bd-1-cline-homepage.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=b3376e576e797f15eee3b892b28f6ffe 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/3a344cdc2e177da38ae745e627c90052375f7ef394151410723deef1629308bd-1-cline-homepage.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=c10e47a92786e1cf3a4be14e9f03cd4f 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/3a344cdc2e177da38ae745e627c90052375f7ef394151410723deef1629308bd-1-cline-homepage.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=d75151d884fb6a9353a0ff69ccfbae81 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/3a344cdc2e177da38ae745e627c90052375f7ef394151410723deef1629308bd-1-cline-homepage.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=f22cab2e6a301255dc31f7ff889123b9 2500w" />
</Frame>

### 2. Select Cline

After it's installed, select Cline from the menu of your IDE to configure it.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/a78933f0e35bade4b946f7b2995730e2e4554694fc6cd2c596f3b4584abde5be-2-open-cline.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=9a332b14348eed5ceaf5ef1e20c87ca1" alt="" data-og-width="2586" width="2586" data-og-height="2476" height="2476" data-path="images/a78933f0e35bade4b946f7b2995730e2e4554694fc6cd2c596f3b4584abde5be-2-open-cline.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/a78933f0e35bade4b946f7b2995730e2e4554694fc6cd2c596f3b4584abde5be-2-open-cline.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=8972e49a62c3033f05d70cbcfe2db8ec 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/a78933f0e35bade4b946f7b2995730e2e4554694fc6cd2c596f3b4584abde5be-2-open-cline.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=8ce72d4fef3ab9a4e7e68f08f1f82da6 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/a78933f0e35bade4b946f7b2995730e2e4554694fc6cd2c596f3b4584abde5be-2-open-cline.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=a151d274b3e5df18f097e2867088cec3 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/a78933f0e35bade4b946f7b2995730e2e4554694fc6cd2c596f3b4584abde5be-2-open-cline.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=49ee5dcaf43d4d1bb0d578d42be76741 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/a78933f0e35bade4b946f7b2995730e2e4554694fc6cd2c596f3b4584abde5be-2-open-cline.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=0ea67175a06aad22e2109986aa64d1ca 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/a78933f0e35bade4b946f7b2995730e2e4554694fc6cd2c596f3b4584abde5be-2-open-cline.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=02314c65bed8b47a8ac0a46a79c3c0f8 2500w" />
</Frame>

### 3. Configure Together AI & DeepSeek V3

Click "Use your own API key". After this, select Together as the API Provider, paste in your [Together API key](https://api.together.xyz/settings/api-keys), and type in any of our models to use. We recommend using `deepseek-ai/DeepSeek-V3` as its a powerful coding model.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/297b1c91ff9103ff87d50a8a1fb75dc29588fd47124fa081bac1de5ed1acece5-3-put-in-together.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=0a07e5d79ec8ab98d1b3dc0beb5be426" alt="" data-og-width="1330" width="1330" data-og-height="1632" height="1632" data-path="images/297b1c91ff9103ff87d50a8a1fb75dc29588fd47124fa081bac1de5ed1acece5-3-put-in-together.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/297b1c91ff9103ff87d50a8a1fb75dc29588fd47124fa081bac1de5ed1acece5-3-put-in-together.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=d84cd10832842a2263d0ffccde061d4a 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/297b1c91ff9103ff87d50a8a1fb75dc29588fd47124fa081bac1de5ed1acece5-3-put-in-together.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=7f5a39347baa3fcbd28617a4fe278ff5 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/297b1c91ff9103ff87d50a8a1fb75dc29588fd47124fa081bac1de5ed1acece5-3-put-in-together.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=0cba6f483bf913162823056b69c8e82c 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/297b1c91ff9103ff87d50a8a1fb75dc29588fd47124fa081bac1de5ed1acece5-3-put-in-together.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=b4606469d26d77b553fbed3bf33f07a6 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/297b1c91ff9103ff87d50a8a1fb75dc29588fd47124fa081bac1de5ed1acece5-3-put-in-together.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=0c11e3aef7950e29c33fdd551c655a10 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/297b1c91ff9103ff87d50a8a1fb75dc29588fd47124fa081bac1de5ed1acece5-3-put-in-together.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=c111f40eceb970815ba3aa933263d158 2500w" />
</Frame>

That's it! You can now build faster with one of the most popular coding agents running a fast, secure, and private open source model hosted on Together AI.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
