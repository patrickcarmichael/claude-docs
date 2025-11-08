---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Troubleshooting Errors

<AccordionGroup>
  <Accordion title="When using Cohere's API, why am I encountering errors related to dataset creation, API key limitations, or missing artifacts, and how can these issues be resolved?">
    Here are some common errors and potential solutions for dealing with errors related to API key limitations or missing artifacts.

    #### API Key Limitations

    Cohere's API keys have certain limitations and permissions associated with them. If you are encountering errors related to API key limitations, it could be due to the following reasons:

    * Rate Limits: Cohere's API has rate limits in place to ensure fair usage. If you exceed the allowed number of requests within a specific time frame, you may receive an error. To resolve this, double check the rate limits for your API plan and ensure your usage is within the specified limits. You can also implement a rate-limiting mechanism in your code to control the frequency of API requests.
    * API Key Expiration: API keys may have an expiration date. If your key has expired, it will no longer work.Check the validity period of your API key and renew it if necessary. Contact Cohere's support team if you need assistance with key renewal.

    #### Missing Artifacts

    Cohere's dataset creation process involves generating artifacts, which are essential components for training models. If you receive errors about missing artifacts, consider the following:

    * Incorrect Dataset Format: Ensure your dataset is in the correct format required by Cohere's API. Different tasks (e.g., classification, generation) may have specific formatting requirements. Review the documentation for dataset formatting guidelines and ensure your data adheres to the specified structure.
    * File Upload Issues: Artifacts are generated after successfully uploading your dataset files. Issues with file uploads can lead to missing artifacts. Verify that your dataset files are accessible and not corrupted. You should also check file size limits to ensure your files meet the requirements.
    * Synchronization Delay: Sometimes, there might be a slight delay in generating artifacts after uploading the dataset. Wait for a few minutes and refresh the dataset status to see if the artifacts are generated.

    #### General Troubleshooting Steps

    If your problem doesn't fall into these buckets, here are a few other things you can try:

    * Check API Documentation: Review the Cohere [API documentation](https://docs.cohere.com/reference/about) for dataset creation to ensure you are following the correct steps and parameters.
    * Inspect API Responses: Carefully examine the error responses returned by the API. They often contain valuable information about the issue. Cohere uses conventional HTTP response codes to indicate the success or failure of an API request. In general:
      * Codes in the 2xx range indicate success.
      * Codes in the 4xx range indicate an error that failed given the information provided (e.g., a required parameter was omitted, a charge failed, etc.).
      * Codes in the 5xx range indicate an error with Cohere’s servers (these are rare).

    Review the [Errors page](https://docs.cohere.com/reference/errors) to learn more about how to deal with non-2xx response code.

    #### Reach Out to Cohere Support

    If the issue persists, contact Cohere's support team. They can provide personalized assistance and help identify any specific problems with your API integration.
  </Accordion>

  <Accordion title="Why am I unable to access and log in to the Cohere dashboard?">
    If you're encountering difficulties logging into your Cohere dashboard, there could be a few reasons.

    First, check our status page at status.cohere.com to see if any known issues or maintenance activities might impact your access.

    If the status page doesn't indicate any ongoing issues, the next step would be to reach out to our support teams. They're always ready to assist and can be contacted at [support@cohere.com](mailto:support@cohere.com). Our support team will be able to investigate further and provide you with the necessary guidance to resolve the login issue.
  </Accordion>

  <Accordion title="How can I resolve issues with logging in and authentication?">
    We understand that login and authentication issues can be frustrating. Here are some steps you can take to troubleshoot and resolve these problems:

    * Check Your Credentials: Ensure you use the correct username and password. It's easy to make a typo, so double-check your credentials before logging in again.
    * Clear Cache and Cookies: Sometimes, issues with logging in can be caused by cached data or cookies on your device. Try clearing your browser's cache and cookies, then attempt to log in again.
    * Contact Support: If none of the above steps resolve the issue, it's time to contact our support team. We are equipped to handle a wide range of login and authentication issues and can provide further assistance. You can contact us at [support@cohere.com](mailto:support@cohere.com).
  </Accordion>

  <Accordion title="What troubleshooting steps would you suggest for an issue suddenly occurring in a previously functional system or script?">
    If you're facing any technical challenges or need guidance, our support team is here to help. Contact us at [support@cohere.com](mailto:support@cohere.com), and our technical support engineers will provide the necessary assistance and expertise to resolve your issues.
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
