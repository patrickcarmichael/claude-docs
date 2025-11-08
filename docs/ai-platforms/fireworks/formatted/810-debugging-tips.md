---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Debugging Tips

When your training is running, you have several powerful tools to debug and monitor your rollouts:

### Rollout Overview

Clicking on any **Epoch** or **Step** in the training dashboard, then clicking the **table icon** to the right, will show you a comprehensive table of all rollouts. It's a good high-level overview to see if any rollouts failed and for what reason.

<img src="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollouts.png?fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=4e6dda85703f77bcce58b83a391e0f2d" alt="Rollout Overview Table" data-og-width="981" width="981" data-og-height="824" height="824" data-path="images/rollouts.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollouts.png?w=280&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=0a39037d8e3818f7ffe5dd311c210b74 280w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollouts.png?w=560&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=2bbe1b8c9b5ade0376fa8363fe8d5ec2 560w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollouts.png?w=840&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=54cf4174612678513d44af4afb7a4387 840w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollouts.png?w=1100&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=ec2e71a16032151cbb3f0c647f16a94f 1100w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollouts.png?w=1650&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=f9cd11af326b4329adf16993bb1a970e 1650w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollouts.png?w=2500&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=94ab07e54df7e21f8f2b9cf216c3d961 2500w" />

### Individual Rollout Details

If you click on a specific row in the rollout table, you can see exactly what the prompt was and how the model responded. You can even copy and paste out the SVG code generated and render it yourself to see what the model did. This is how we got the results above in the before and after comparison.

<img src="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollout_details.png?fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=0f1384d546a1d5f5f2e85cef97242265" alt="Individual Rollout Details" data-og-width="1497" width="1497" data-og-height="958" height="958" data-path="images/rollout_details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollout_details.png?w=280&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=c38dbe0ea185fc439889ec216b4d7d89 280w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollout_details.png?w=560&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=20831b5ff6710155343ec26a519c69cd 560w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollout_details.png?w=840&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=6de20cd4112cc11966b92792eb9d38f6 840w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollout_details.png?w=1100&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=e7fc0f01da318743bd0d0d47539ef9c9 1100w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollout_details.png?w=1650&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=082a3a517842f905b4b002ec6898c22d 1650w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollout_details.png?w=2500&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=237f8903eefb31bb1f66937cf2979769 2500w" />

### Live Log Streaming

Clicking on **View Logs** takes you to a page of logs being streamed in. Here, you can see precisely what errors are happening to the rollouts. This is useful to debug and fix any issues with your rollouts.

<img src="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/logs.png?fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=66aed2a6eac9532a37f0106c0f5a526a" alt="Live Log Streaming" data-og-width="1399" width="1399" data-og-height="958" height="958" data-path="images/logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/logs.png?w=280&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=9b5d411a6c5810f975952bda32990a74 280w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/logs.png?w=560&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=3b1067074975220120cf884e2fe4e04e 560w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/logs.png?w=840&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=990e0d1a4815818d085cfe6e8319185c 840w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/logs.png?w=1100&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=a6f64807089b7221495cbac2e8eeea5a 1100w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/logs.png?w=1650&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=658c42b53a98ce57d8746106ec2b7b03 1650w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/logs.png?w=2500&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=b726b75b643b3837231aa5e4c3cf795c 2500w" />

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
