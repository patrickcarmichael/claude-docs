---
title: "Crewai: Interactive Testing"
description: "Interactive Testing section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Interactive Testing


<Info>
  **Why no "Send" button?** Since each CrewAI AMP user has their own unique crew URL, we use **reference mode** instead of an interactive playground to avoid confusion. This shows you exactly what the requests should look like without non-functional send buttons.
</Info>

Each endpoint page shows you:

* ✅ **Exact request format** with all parameters
* ✅ **Response examples** for success and error cases
* ✅ **Code samples** in multiple languages (cURL, Python, JavaScript, etc.)
* ✅ **Authentication examples** with proper Bearer token format

### **To Test Your Actual API:**

<CardGroup cols={2}>
  <Card title="Copy cURL Examples" icon="terminal">
    Copy the cURL examples and replace the URL + token with your real values
  </Card>

  <Card title="Use Postman/Insomnia" icon="play">
    Import the examples into your preferred API testing tool
  </Card>
</CardGroup>

**Example workflow:**

1. **Copy this cURL example** from any endpoint page
2. **Replace `your-actual-crew-name.crewai.com`** with your real crew URL
3. **Replace the Bearer token** with your real token from the dashboard
4. **Run the request** in your terminal or API client

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Error Handling](./2404-error-handling.md)

**Next:** [Need Help? →](./2406-need-help.md)
