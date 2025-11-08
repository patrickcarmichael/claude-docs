---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Troubleshooting

<Accordion title="NAME? Error: Unknown function: 'claude'">
  1. Ensure that you have enabled the extension for use in the current sheet
     1. Go to *Extensions* > *Add-ons* > *Manage add-ons*
     2. Click on the triple dot menu at the top right corner of the Claude for Sheets extension and make sure "Use in this document" is checked
        <img src="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/9cce371-Screenshot_2023-10-03_at_7.17.39_PM.png?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=7ac5b747f92f68f05055ecd143bd5fa8" alt="" data-og-width="712" width="712" data-og-height="174" height="174" data-path="images/9cce371-Screenshot_2023-10-03_at_7.17.39_PM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/9cce371-Screenshot_2023-10-03_at_7.17.39_PM.png?w=280&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=27a083fe65825128423ea09a03da3653 280w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/9cce371-Screenshot_2023-10-03_at_7.17.39_PM.png?w=560&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=9905542d704449f1727f5fe510242bb0 560w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/9cce371-Screenshot_2023-10-03_at_7.17.39_PM.png?w=840&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=8fed917d4e4ff142167cf8492febf442 840w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/9cce371-Screenshot_2023-10-03_at_7.17.39_PM.png?w=1100&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=e7d89ec0ed91b3c55a22a2e28da8ae25 1100w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/9cce371-Screenshot_2023-10-03_at_7.17.39_PM.png?w=1650&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=39998025b2c4afb6a49cf9efef63b266 1650w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/9cce371-Screenshot_2023-10-03_at_7.17.39_PM.png?w=2500&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=fe1bc4d35b3dd33c13b5c1e69e21f46a 2500w" />
  2. Refresh the page
</Accordion>

<Accordion title="#ERROR!, ⚠ DEFERRED ⚠ or ⚠ THROTTLED ⚠">
  You can manually recalculate `#ERROR!`, `⚠ DEFERRED ⚠` or `⚠ THROTTLED ⚠`cells by selecting from the recalculate options within the Claude for Sheets extension menu.

    <img src="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/f729ba9-Screenshot_2024-02-01_at_8.30.31_PM.png?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=7bd765250352e58047c2dfb3f1a3d8e9" alt="" data-og-width="1486" width="1486" data-og-height="1062" height="1062" data-path="images/f729ba9-Screenshot_2024-02-01_at_8.30.31_PM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/f729ba9-Screenshot_2024-02-01_at_8.30.31_PM.png?w=280&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=fb6b88b7a46b7322340d0839a740bc1e 280w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/f729ba9-Screenshot_2024-02-01_at_8.30.31_PM.png?w=560&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=fbf66142e6748a2bac8daad0007d24e6 560w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/f729ba9-Screenshot_2024-02-01_at_8.30.31_PM.png?w=840&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=c1e8c8648137d554ddb49b00e6007a18 840w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/f729ba9-Screenshot_2024-02-01_at_8.30.31_PM.png?w=1100&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=aa336dac0e2316b7699a20ec24e703e6 1100w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/f729ba9-Screenshot_2024-02-01_at_8.30.31_PM.png?w=1650&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=56d3ca83d0af273961f80f6122d02ccb 1650w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/f729ba9-Screenshot_2024-02-01_at_8.30.31_PM.png?w=2500&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=8a0522dcd0291612f474f077bcf826cb 2500w" />
</Accordion>

<Accordion title="Can't enter API key">
  1. Wait 20 seconds, then check again
  2. Refresh the page and wait 20 seconds again
  3. Uninstall and reinstall the extension
</Accordion>

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
