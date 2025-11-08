---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Troubleshooting

### Common issues and solutions

<AccordionGroup>
  <Accordion title="Deployment not found error">
    **Problem**: Getting 404 errors when trying to use the deployment.

    **Solutions**:

    * Verify the deployment ID is correct in the [Fireworks dashboard](https://app.fireworks.ai/dashboard/deployments)
    * Ensure the deployment is in "Running" status
    * Check that you're using the correct Fireworks API key
    * Confirm the deployment belongs to your account/organization
  </Accordion>

  <Accordion title="Model mismatch warnings">
    **Problem**: The model parameter doesn't match the actual deployed model.

    **Solutions**:

    * Check what model your deployment is actually running in the dashboard
    * Update the `model` parameter to match the deployed model
    * If unsure, you can often find the model information in the deployment details
  </Accordion>

  <Accordion title="Authentication errors">
    **Problem**: Getting authentication errors when connecting to the deployment.

    **Solutions**:

    * Verify your `FIREWORKS_API_KEY` environment variable is set correctly
    * Ensure your API key has access to the deployment
    * Check that the deployment belongs to your account or organization
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
