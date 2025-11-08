---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Billing, Pricing, Licensing, Account Management

<AccordionGroup>
  <Accordion title="How can I get in touch with Cohere's support team?">
    Please reach out to our support team at [support@cohere.com](mailto:support@cohere.com). When reaching out to the support team, please keep the following questions in mind:

    * What model are you referring to?
    * Copy paste the error message
      * Please note that this is our error message information:
        * 400 - invalid combination of parameters
        * 422 - request is malformed (eg: unsupported enum value, unknown param)
        * 499 - request is canceled by the user
        * 401 - invalid api token (not relevant on AWS)
        * 404 - model not found (not relevant on AWS)
        * 429 - rate limit reached (not relevant on AWS)
    * What is the request seq length you are passing in?
    * What are the generation max tokens you are requesting?
    * Are all the requests of various input/output shapes failing?
    * Share any logs
  </Accordion>

  <Accordion title="Where can I find information about Cohere's pricing?">
    Please refer to our dedicated pricing page for most up-to-date [pricing](https://cohere.com/pricing).
  </Accordion>

  <Accordion title="How can I manage and understand the rate limits and usage of my API key?">
    Cohere offers two types of API keys: trial keys and production keys.

    *Trial Key Limitations*

    Trial keys are rate-limited depending on the endpoint you want to use. For example, the Embed endpoint is limited to 5 calls per minute, while the Chat endpoint is limited to 20 calls per minute. All other endpoints on trail keys are 1,000 calls per month.
    If you want to use Cohere endpoints in a production application or require higher throughput, you can upgrade to a production key.

    *Production Key Specifications*

    Production keys for all endpoints are rate-limited at 1,000 calls per minute, with unlimited monthly use and are intended for serving Cohere in a public-facing application and testing purposes. Usage of production keys is metered at price points which can be found on the Cohere [pricing page](https://cohere.com/pricing).

    To get a production key, you'll need to be the admin of your organization or ask your organization's admin to create one. Please visit your [API Keys](https://dashboard.cohere.com/api-keys) > [Dashboard](https://dashboard.cohere.com/), where the process should take less than three minutes and will generate a production key that you can use to serve Cohere APIs in production.
  </Accordion>

  <Accordion title="How can I monitor and manage my token usage and API calls for personal projects within the limitations of a free plan?">
    Cohere offers a convenient way to keep track of your usage and billing information. All our endpoints provide this data as metadata for each conversation, which is directly accessible via the API. This ensures you can easily monitor your usage.
    Our Dashboard provides an additional layer of control for standard accounts. You can set a monthly spending limit to manage your expenses effectively. To learn more about this feature and how to enable it, please visit the Billing & Usage section on the Dashboard, specifically the [Spending Limit](https://dashboard.cohere.com/billing?tab=spending-limit) tab.
  </Accordion>

  <Accordion title="What is the process for making changes to my account, and who should I contact for specific requests?">
    If you need to make changes to your account or have specific requests, Cohere has a straightforward process. All the essential details about your account can be found under the [Dashboard](https://dashboard.cohere.com). This is a great starting point for any account-related queries.

    However, if you have a request that requires further assistance or if the changes you wish to make are not covered by the Dashboard, our support team is here to help. Please feel free to reach out directly at [support@cohere.com](mailto:support@cohere.com) or ask your question in our [Discord community](https://discord.gg/co-mmunity).
  </Accordion>

  <Accordion title="How can I get in touch with Cohere support to discuss plan options and pricing?">
    Please reach out to our Sales team at [sales@cohere.com](mailto:sales@cohere.com)
  </Accordion>

  <Accordion title="How is the cost of using Cohere's API calculated and what factors influence the number of billed tokens?">
    Cohere's API pricing is based on a simple and transparent token-based model. The cost of using the API is calculated based on the number of tokens consumed during the API calls.

    Check our [pricing page](https://cohere.com/pricing) for more information.
  </Accordion>

  <Accordion title="What are the rate limits for the free trial API, and how is the monthly limit calculated?">
    Trial keys are rate-limited depending on the endpoint you want to use, and the monthly limit is 1000 calls per month.

    Check our [free trial documentation](https://docs.cohere.com/docs/rate-limits#trial-key-limitations) for more information.
  </Accordion>

  <Accordion title="Is it possible for a small startup or any commercial entity to use Cohere's technology for production or commercial purposes, and if so, what licenses or permissions are required?">
    Absolutely! Cohere's platform empowers businesses, including startups, to leverage our technology for production and commercial purposes.

    In terms of usage guidelines, we've compiled a comprehensive set of resources to ensure a smooth and compliant experience. You can access these guidelines [here](https://docs.cohere.com/docs/usage-guidelines).

    We're excited to support your business and its unique needs. If you have any further questions or require additional assistance, please don't hesitate to reach out to our team at [sales@cohere.com](mailto:sales@cohere.com) or [support@cohere.com](mailto:support@cohere.com) for more details.
  </Accordion>

  <Accordion title="How can I manage my Cohere account, specifically regarding deletion, team invitations, and account merging?">
    You can access all the necessary tools and information through your account's dashboard [here](https://dashboard.cohere.com/team).

    If you're unable to find the specific feature or information regarding merging accounts, our support team is always eager to help.

    Simply start a new chat with them using the chat bubble on our website or reach out via email to [support@cohere.com](mailto:support@cohere.com).
  </Accordion>

  <Accordion title="How does the token limit work for multiple documents in a single query?">
    The token limit for multiple documents in a single query can vary depending on the model or service you're using. For instance, our Chat Model has a long-context window of 128k tokens. This means that as long as the combined length of your input and output tokens stays within this limit, the number of documents you include in your query shouldn't be an issue.

    It's important to note that different models may have different token and document limits. To ensure you're working within the appropriate parameters, we've provided detailed information about these limits for each model in [this](https://docs.cohere.com/docs/models) model overview section.

    We understand that managing token limits can be a crucial aspect of your work, and we're here to support you in navigating these considerations effectively. If you have any further questions or require additional assistance, please don't hesitate to reach out to our team at [support@cohere.com](mailto:support@cohere.com)
  </Accordion>

  <Accordion title="What are the pricing plans and models available for Cohere's API endpoints, and are there any additional costs associated with specific features or workflows?">
    Please find the pricing information about our model and services [here](https://cohere.com/pricing).

    Should you have any further questions please feel free to reach out to our sales team at [sales@cohere.com](mailto:sales@cohere.com) or [support@cohere.com](mailto:support@cohere.com) for more details.
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
