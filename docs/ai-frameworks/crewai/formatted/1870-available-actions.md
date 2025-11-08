---
title: "Crewai: Available Actions"
description: "Available Actions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Actions


<AccordionGroup>
  <Accordion title="microsoft_word/get_documents">
    **Description:** Get all Word documents from OneDrive or SharePoint.

    **Parameters:**

    * `select` (string, optional): Select specific properties to return.
    * `filter` (string, optional): Filter results using OData syntax.
    * `expand` (string, optional): Expand related resources inline.
    * `top` (integer, optional): Number of items to return (min 1, max 999).
    * `orderby` (string, optional): Order results by specified properties.
  </Accordion>

  <Accordion title="microsoft_word/create_text_document">
    **Description:** Create a text document (.txt) with content. RECOMMENDED for programmatic content creation that needs to be readable and editable.

    **Parameters:**

    * `file_name` (string, required): Name of the text document (should end with .txt).
    * `content` (string, optional): Text content for the document. Default is "This is a new text document created via API."
  </Accordion>

  <Accordion title="microsoft_word/get_document_content">
    **Description:** Get the content of a document (works best with text files).

    **Parameters:**

    * `file_id` (string, required): The ID of the document.
  </Accordion>

  <Accordion title="microsoft_word/get_document_properties">
    **Description:** Get properties and metadata of a document.

    **Parameters:**

    * `file_id` (string, required): The ID of the document.
  </Accordion>

  <Accordion title="microsoft_word/delete_document">
    **Description:** Delete a document.

    **Parameters:**

    * `file_id` (string, required): The ID of the document to delete.
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Microsoft Word Integration](./1869-setting-up-microsoft-word-integration.md)

**Next:** [Usage Examples →](./1871-usage-examples.md)
