---
title: "Crewai: Available Actions"
description: "Available Actions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Actions


<AccordionGroup>
  <Accordion title="google_slides/create_blank_presentation">
    **Description:** Creates a blank presentation with no content.

    **Parameters:**

    * `title` (string, required): The title of the presentation.
  </Accordion>

  <Accordion title="google_slides/get_presentation">
    **Description:** Retrieves a presentation by ID.

    **Parameters:**

    * `presentationId` (string, required): The ID of the presentation to retrieve.
    * `fields` (string, optional): The fields to include in the response. Use this to improve performance by only returning needed data.
  </Accordion>

  <Accordion title="google_slides/batch_update_presentation">
    **Description:** Applies updates, add content, or remove content from a presentation.

    **Parameters:**

    * `presentationId` (string, required): The ID of the presentation to update.
    * `requests` (array, required): A list of updates to apply to the presentation.
      ```json  theme={null}
      [
        {
          "insertText": {
            "objectId": "slide_id",
            "text": "Your text content here"
          }
        }
      ]
      ```
    * `writeControl` (object, optional): Provides control over how write requests are executed.
      ```json  theme={null}
      {
        "requiredRevisionId": "revision_id_string"
      }
      ```
  </Accordion>

  <Accordion title="google_slides/get_page">
    **Description:** Retrieves a specific page by its ID.

    **Parameters:**

    * `presentationId` (string, required): The ID of the presentation.
    * `pageObjectId` (string, required): The ID of the page to retrieve.
  </Accordion>

  <Accordion title="google_slides/get_thumbnail">
    **Description:** Generates a page thumbnail.

    **Parameters:**

    * `presentationId` (string, required): The ID of the presentation.
    * `pageObjectId` (string, required): The ID of the page for thumbnail generation.
  </Accordion>

  <Accordion title="google_slides/import_data_from_sheet">
    **Description:** Imports data from a Google Sheet into a presentation.

    **Parameters:**

    * `presentationId` (string, required): The ID of the presentation.
    * `sheetId` (string, required): The ID of the Google Sheet to import from.
    * `dataRange` (string, required): The range of data to import from the sheet.
  </Accordion>

  <Accordion title="google_slides/upload_file_to_drive">
    **Description:** Uploads a file to Google Drive associated with the presentation.

    **Parameters:**

    * `file` (string, required): The file data to upload.
    * `presentationId` (string, required): The ID of the presentation to link the uploaded file.
  </Accordion>

  <Accordion title="google_slides/link_file_to_presentation">
    **Description:** Links a file in Google Drive to a presentation.

    **Parameters:**

    * `presentationId` (string, required): The ID of the presentation.
    * `fileId` (string, required): The ID of the file to link.
  </Accordion>

  <Accordion title="google_slides/get_all_presentations">
    **Description:** Lists all presentations accessible to the user.

    **Parameters:**

    * `pageSize` (integer, optional): The number of presentations to return per page.
    * `pageToken` (string, optional): A token for pagination.
  </Accordion>

  <Accordion title="google_slides/delete_presentation">
    **Description:** Deletes a presentation by ID.

    **Parameters:**

    * `presentationId` (string, required): The ID of the presentation to delete.
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Google Slides Integration](./1741-setting-up-google-slides-integration.md)

**Next:** [Usage Examples →](./1743-usage-examples.md)
