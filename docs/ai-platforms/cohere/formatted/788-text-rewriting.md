---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Text rewriting

Text rewriting is a powerful capability that allows us to adapt content for different purposes while preserving the core message. This involves transforming the style, tone, or format of text to better suit the target audience or medium.

Let's look at an example where we convert a customer support chat response into a formal email. We'll construct the prompt by first stating our goal to rewrite the text, then providing the original chat response as context.
```python PYTHON
prompt = f"""Rewrite this customer support agent response into an email format, ready to send to the customer.

If you're experiencing brief periods of slow data speeds or difficulty sending text messages and connecting to your mobile network, here are some troubleshooting steps you can follow:

1. Check your signal strength - Move to an area with better coverage.
2. Restart your device and try connecting again.
3. Ensure your account is active and not suspended.
4. Contact customer support for further assistance. (This can include updating your plan for better network performance.)

Did these steps help resolve the issue? Let me know if you need further assistance."""

response = generate_text(prompt)

print(response.message.content[0].text)
```
```mdx
Subject: Troubleshooting Slow Data Speeds and Network Connection Issues

Dear [Customer's Name],

I hope this email finds you well. I understand that you may be facing some challenges with your mobile network, including slow data speeds and difficulties sending text messages. Here are some recommended troubleshooting steps to help resolve these issues:

- Signal Strength: Check the signal strength on your device and move to a different location if the signal is weak. Moving to an area with better coverage can often improve your connection.

- Restart Your Device: Sometimes, a simple restart can resolve temporary glitches. Please restart your device and then try connecting to the network again.

- Account Status: Verify that your account is active and in good standing. In some cases, service providers may temporarily suspend accounts due to various reasons, which can impact your network access. 

- Contact Customer Support: If the issue persists, please reach out to our customer support team for further assistance. Our team can help troubleshoot and provide additional guidance. We can also discuss your current plan and explore options to enhance your network performance if needed.

I hope these steps will help resolve the issue promptly. Please feel free to reply to this email if you have any further questions or if the problem continues. We are committed to ensuring your satisfaction and providing a seamless network experience.

Best regards,
[Your Name]
[Customer Support Agent]
[Company Name]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
