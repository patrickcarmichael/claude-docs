---
title: "Langgraph: Test multi-turn conversation"
description: "Test multi-turn conversation section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Test multi-turn conversation


Let's test a multi turn conversation with this application.

```python
thread_config = {"configurable": {"thread_id": uuid.uuid4()}}

inputs = [
    # 1st round of conversation,
    {
        "role": "user",
        "content": "i wanna go somewhere warm in the caribbean",
        "id": str(uuid.uuid4()),
    },
    # Since we're using `interrupt`, we'll need to resume using the Command primitive.
    # 2nd round of conversation,
    Command(
        resume="could you recommend a nice hotel in one of the areas and tell me which area it is."
    ),
    # 3rd round of conversation,
    Command(
        resume="i like the first one. could you recommend something to do near the hotel?"
    ),
]

for idx, user_input in enumerate(inputs):
    print()
    print(f"--- Conversation Turn {idx + 1} ---")
    print()
    print(f"User: {user_input}")
    print()
    for update in multi_turn_graph.stream(
        user_input,
        config=thread_config,
        stream_mode="updates",
    ):
        for node_id, value in update.items():
            if isinstance(value, list) and value:
                last_message = value[-1]
                if isinstance(last_message, dict) or last_message.type != "ai":
                    continue
                print(f"{node_id}: {last_message.content}")
```
```output
--- Conversation Turn 1 ---

User: {'role': 'user', 'content': 'i wanna go somewhere warm in the caribbean', 'id': 'f48d82a7-7efa-43f5-ad4c-541758c95f61'}

call_travel_advisor: Based on the recommendations, Aruba would be an excellent choice for your Caribbean getaway! Known as "One Happy Island," Aruba offers:
- Year-round warm weather with consistent temperatures around 82°F (28°C)
- Beautiful white sand beaches like Eagle Beach and Palm Beach
- Crystal clear waters perfect for swimming and snorkeling
- Minimal rainfall and location outside the hurricane belt
- Rich culture blending Dutch and Caribbean influences
- Various activities from water sports to desert-like landscape exploration
- Excellent dining and shopping options

Would you like me to help you find suitable accommodations in Aruba? I can transfer you to our hotel advisor who can recommend specific hotels based on your preferences.

--- Conversation Turn 2 ---

User: Command(resume='could you recommend a nice hotel in one of the areas and tell me which area it is.')

call_hotel_advisor: I can recommend two excellent options in different areas:

1. The Ritz-Carlton, Aruba - Located in Palm Beach
- Luxury beachfront resort
- Located in the vibrant Palm Beach area, known for its lively atmosphere
- Close to restaurants, shopping, and nightlife
- Perfect for those who want a more active vacation with plenty of amenities nearby

2. Bucuti & Tara Beach Resort - Located in Eagle Beach
- Adults-only boutique resort
- Situated on the quieter Eagle Beach
- Known for its romantic atmosphere and excellent service
- Ideal for couples seeking a more peaceful, intimate setting

Would you like more specific information about either of these properties or their locations?

--- Conversation Turn 3 ---

User: Command(resume='i like the first one. could you recommend something to do near the hotel?')

call_travel_advisor: Near The Ritz-Carlton in Palm Beach, here are some popular activities you can enjoy:

1. Palm Beach Strip - Take a walk along this bustling strip filled with restaurants, shops, and bars
2. Visit the Bubali Bird Sanctuary - Just a short distance away
3. Try your luck at the Stellaris Casino - Located right in The Ritz-Carlton
4. Water Sports at Palm Beach - Right in front of the hotel you can:
   - Go parasailing
   - Try jet skiing
   - Take a sunset sailing cruise
5. Visit the Palm Beach Plaza Mall - High-end shopping just a short walk away
6. Enjoy dinner at Madame Janette's - One of Aruba's most famous restaurants nearby

Would you like more specific information about any of these activities or other suggestions in the area?
```

---

how-tos/persistence-functional.ipynb

---

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define hotel advisor ReAct agent](./168-define-hotel-advisor-react-agent.md)

**Next:** [How to add thread-level persistence (functional API) →](./170-how-to-add-thread-level-persistence-functional-api.md)
