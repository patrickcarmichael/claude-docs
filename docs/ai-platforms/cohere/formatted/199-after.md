---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## After

message = """Write a short summary from the following text in bullet point format, in different words.
  
  Equipment rental in North America is predicted to “normalize” going into 2024, according to Josh
  Nickell, vice president of equipment rental for the American Rental Association (ARA).
  “Rental is going back to ‘normal,’ but normal means that strategy matters again - geography
  matters, fleet mix matters, customer type matters,” Nickell said. “In late 2020 to 2022, you just
  showed up with equipment and you made money.
  “Everybody was breaking records, from the national rental chains to the smallest rental companies;
  everybody was having record years, and everybody was raising prices. The conversation was,
  ‘How much are you up?’ And now, the conversation is changing to ‘What’s my market like?’”
  Nickell stressed this shouldn’t be taken as a pessimistic viewpoint. It’s simply coming back
  down to Earth from unprecedented circumstances during the time of Covid. Rental companies are
  still seeing growth, but at a more moderate level.
"""

co.chat(
    messages=[{"role": "user", "content": message}],
    model="command-a-03-2025",
)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
