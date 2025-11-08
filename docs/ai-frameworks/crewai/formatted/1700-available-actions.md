---
title: "Crewai: Available Actions"
description: "Available Actions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Actions


<AccordionGroup>
  <Accordion title="google_docs/create_document">
    **Description:** Create a new Google Document.

    **Parameters:**

    * `title` (string, optional): The title for the new document.
  </Accordion>

  <Accordion title="google_docs/get_document">
    **Description:** Get the contents and metadata of a Google Document.

    **Parameters:**

    * `documentId` (string, required): The ID of the document to retrieve.
    * `includeTabsContent` (boolean, optional): Whether to include tab content. Default is `false`.
    * `suggestionsViewMode` (string, optional): The suggestions view mode to apply to the document. Enum: `DEFAULT_FOR_CURRENT_ACCESS`, `PREVIEW_SUGGESTIONS_ACCEPTED`, `PREVIEW_WITHOUT_SUGGESTIONS`. Default is `DEFAULT_FOR_CURRENT_ACCESS`.
  </Accordion>

  <Accordion title="google_docs/batch_update">
    **Description:** Apply one or more updates to a Google Document.

    **Parameters:**

    * `documentId` (string, required): The ID of the document to update.
    * `requests` (array, required): A list of updates to apply to the document. Each item is an object representing a request.
    * `writeControl` (object, optional): Provides control over how write requests are executed. Contains `requiredRevisionId` (string) and `targetRevisionId` (string).
  </Accordion>

  <Accordion title="google_docs/insert_text">
    **Description:** Insert text into a Google Document at a specific location.

    **Parameters:**

    * `documentId` (string, required): The ID of the document to update.
    * `text` (string, required): The text to insert.
    * `index` (integer, optional): The zero-based index where to insert the text. Default is `1`.
  </Accordion>

  <Accordion title="google_docs/replace_text">
    **Description:** Replace all instances of text in a Google Document.

    **Parameters:**

    * `documentId` (string, required): The ID of the document to update.
    * `containsText` (string, required): The text to find and replace.
    * `replaceText` (string, required): The text to replace it with.
    * `matchCase` (boolean, optional): Whether the search should respect case. Default is `false`.
  </Accordion>

  <Accordion title="google_docs/delete_content_range">
    **Description:** Delete content from a specific range in a Google Document.

    **Parameters:**

    * `documentId` (string, required): The ID of the document to update.
    * `startIndex` (integer, required): The start index of the range to delete.
    * `endIndex` (integer, required): The end index of the range to delete.
  </Accordion>

  <Accordion title="google_docs/insert_page_break">
    **Description:** Insert a page break at a specific location in a Google Document.

    **Parameters:**

    * `documentId` (string, required): The ID of the document to update.
    * `index` (integer, optional): The zero-based index where to insert the page break. Default is `1`.
  </Accordion>

  <Accordion title="google_docs/create_named_range">
    **Description:** Create a named range in a Google Document.

    **Parameters:**

    * `documentId` (string, required): The ID of the document to update.
    * `name` (string, required): The name for the named range.
    * `startIndex` (integer, required): The start index of the range.
    * `endIndex` (integer, required): The end index of the range.
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Google Docs Integration](./1699-setting-up-google-docs-integration.md)

**Next:** [Usage Examples →](./1701-usage-examples.md)
