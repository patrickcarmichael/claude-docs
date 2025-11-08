---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Sending messages to the model

We will use the Cohere Chat API to send messages and genereate responses from the model. The required inputs to the Chat endpoint are the `model` (the model name) and `messages` (a list of messages in chronological order). In the example below, we send a single message to the model `command-a-03-2025`:
```python PYTHON
response = co.chat(
    model="command-a-03-2025",
    messages=[
        {
            "role": "user",
            "content": "I'm joining a new startup called Co1t today. Could you help me write a short introduction message to my teammates.",
        },
    ],
)

print(response.message)
```
Notice that in addition to the message "content", there is also a field titled "role". Messages with the role "user" represent prompts from the user interacting with the chatbot. Responses from model will always have a message with the role "assistant". Below is the response message from the API:
```PYTHON
{
    role='assistant',
    content=[
        {
            type='text', 
            text='Absolutely! Here’s a warm and professional introduction message you can use to connect with your new teammates at Co1t:\n\n---\n\n**Subject:** Excited to Join the Co1t Team!  \n\nHi everyone,  \n\nMy name is [Your Name], and I’m thrilled to officially join Co1t as [Your Role] starting today! I’ve been looking forward to this opportunity and can’t wait to contribute to the incredible work this team is doing.  \n\nA little about me: [Share a brief personal or professional detail, e.g., "I’ve spent the last few years working in [industry/field], and I’m passionate about [specific skill or interest]." or "Outside of work, I love [hobby or interest] and am always up for a good [book/podcast/movie] recommendation!"]  \n\nI’m excited to get to know each of you, learn from your experiences, and collaborate on driving Co1t’s mission forward. Please feel free to reach out—I’d love to chat and hear more about your roles and what you’re working on.  \n\nLooking forward to an amazing journey together!  \n\nBest regards,  \n[Your Name]  \n[Your Role]  \nCo1t  \n\n---\n\nFeel free to customize it further to match your style and the culture of Co1t. Good luck on your first day! 🚀'
        }
    ],
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
