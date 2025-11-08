---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


### Common Issues

**Permission Errors**

* Ensure your Google account has appropriate permissions for Google Slides
* Verify that the OAuth connection includes required scopes for presentations, spreadsheets, and drive access
* Check that presentations are shared with the authenticated account

**Presentation ID Issues**

* Verify that presentation IDs are correct and presentations exist
* Ensure you have access permissions to the presentations you're trying to modify
* Check that presentation IDs are properly formatted

**Content Update Issues**

* Ensure batch update requests are properly formatted according to Google Slides API specifications
* Verify that object IDs for slides and elements exist in the presentation
* Check that write control revision IDs are current if using optimistic concurrency

**Data Import Issues**

* Verify that Google Sheet IDs are correct and accessible
* Ensure data ranges are properly specified using A1 notation
* Check that you have read permissions for the source spreadsheets

**File Upload and Linking Issues**

* Ensure file data is properly encoded for upload
* Verify that Drive file IDs are correct when linking files
* Check that you have appropriate Drive permissions for file operations

**Page and Thumbnail Operations**

* Verify that page object IDs exist in the specified presentation
* Ensure presentations have content before attempting to generate thumbnails
* Check that page structure is valid for thumbnail generation

**Pagination and Listing Issues**

* Use appropriate page sizes for listing presentations
* Implement proper pagination using page tokens for large result sets
* Handle empty result sets gracefully

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Google Slides integration setup or troubleshooting.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create templates](./1751-task-to-create-templates.md)

**Next:** [HubSpot Integration →](./1753-hubspot-integration.md)
