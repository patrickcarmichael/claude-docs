---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How to do standard OCR with Together SDK

Together AI provides powerful vision models that can process images and extract text with high accuracy.

The basic approach involves sending an image to a vision model and receiving extracted text in return.\
A great example of this implementation can be found at [llamaOCR.com](https://llamaocr.com/).

Here's a basic Typescript/Python implementation for standard OCR:
```typescript

  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const billUrl =
      "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/1627e746-7eda-46d3-8d08-8c8eec0d6c9c/nobu.jpg?x-id=PutObject";

    const response = await together.chat.completions.create({
      model: "meta-llama/Llama-4-Scout-17B-16E-Instruct",
      messages: [
        {
          role: "system",
          content:
            "You are an expert at extracting information from receipts. Extract all the content from the receipt.",
        },
        {
          role: "user",
          content: [
            { type: "text", text: "Extract receipt information" },
            { type: "image_url", image_url: { url: billUrl } },
          ],
        },
      ],
    });

    if (response?.choices?.[0]?.message?.content) {
      console.log(response.choices[0].message.content);
      return (response.choices[0].message.content);
    }

    throw new Error("Failed to extract receipt information");
  }

  main();
```
```python
  from together import Together

  client = Together()

  prompt = "You are an expert at extracting information from receipts. Extract all the content from the receipt."

  imageUrl = "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/1627e746-7eda-46d3-8d08-8c8eec0d6c9c/nobu.jpg?x-id=PutObject"


  stream = client.chat.completions.create(
      model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": prompt},
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": imageUrl,
                      },
                  },
              ],
          }
      ],
      stream=True,
  )

  for chunk in stream:
      print(
          chunk.choices[0].delta.content or "" if chunk.choices else "",
          end="",
          flush=True,
      )
```

Here's the output from the code snippet above – we're simply giving it a receipt and asking it to extract all the information:
```text
**Restaurant Information:**
- Name: Noby 
- Location: Los Angeles
- Address: 903 North La Cienega 
- Phone Number: 310-657-5111

**Receipt Details:**
- Date: 04/16/2011
- Time: 9:19 PM
- Server: Daniel
- Guest Count: 15
- Reprint #: 2

**Ordered Items:**
1. **Pina Martini** - $14.00
2. **Jasmine Calpurnina** - $14.00
3. **Yamasaki L. Decar** - $14.00
4. **Ma Margarita** - $4.00
5. **Diet Coke** - $27.00
6. **Lychee Martini (2 @ $14.00)** - $28.00
7. **Lynchee Martini** - $48.00
8. **Green Tea Decaf** - $12.00
9. **Glass Icecube R/Eising** - $0.00
10. **Green Tea Donation ($2)** - $2.00
11. **Lychee Martini (2 @ $14.00)** - $28.00
12. **YS50** - $225.00
13. **Green Tea ($40.00)** - $0.00
14. **Tiradito (3 @ $25.00)** - $75.00
15. **Tiradito** - $25
16. **Tiradito #20** - $20.00
17. **New-F-BOTAN (3 @ $30.00)** - $90.00
18. **Coke Refill** - $0.00
19. **Diet Coke Refill** - $0.00
20. **Bamboo** - $0.00
21. **Admin Fee** - $300.00
22. **TESSLER (15 @ $150.00)** - $2250.00
23. **Sparkling Water Large** - $9.00
24. **King Crab Asasu (3 @ $26.00)** - $78.00
25. **Mexican white shirt (15 @ $5.00)** - $75.00
26. **NorkFish Pate Cav** - $22.00

**Billing Information:**
- **Subtotal** - $3830.00
- **Tax** - $766.00
- **Total** - $4477.72
- **Gratuity** - $4277.72 
- **Total** - $5043.72
- **Balance Due** - $5043.72
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
