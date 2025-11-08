---
title: "Crewai: Available Actions"
description: "Available Actions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Actions


<AccordionGroup>
  <Accordion title="microsoft_onedrive/list_files">
    **Description:** List files and folders in OneDrive.

    **Parameters:**

    * `top` (integer, optional): Number of items to retrieve (max 1000). Default is `50`.
    * `orderby` (string, optional): Order by field (e.g., "name asc", "lastModifiedDateTime desc"). Default is "name asc".
    * `filter` (string, optional): OData filter expression.
  </Accordion>

  <Accordion title="microsoft_onedrive/get_file_info">
    **Description:** Get information about a specific file or folder.

    **Parameters:**

    * `item_id` (string, required): The ID of the file or folder.
  </Accordion>

  <Accordion title="microsoft_onedrive/download_file">
    **Description:** Download a file from OneDrive.

    **Parameters:**

    * `item_id` (string, required): The ID of the file to download.
  </Accordion>

  <Accordion title="microsoft_onedrive/upload_file">
    **Description:** Upload a file to OneDrive.

    **Parameters:**

    * `file_name` (string, required): Name of the file to upload.
    * `content` (string, required): Base64 encoded file content.
  </Accordion>

  <Accordion title="microsoft_onedrive/create_folder">
    **Description:** Create a new folder in OneDrive.

    **Parameters:**

    * `folder_name` (string, required): Name of the folder to create.
  </Accordion>

  <Accordion title="microsoft_onedrive/delete_item">
    **Description:** Delete a file or folder from OneDrive.

    **Parameters:**

    * `item_id` (string, required): The ID of the file or folder to delete.
  </Accordion>

  <Accordion title="microsoft_onedrive/copy_item">
    **Description:** Copy a file or folder in OneDrive.

    **Parameters:**

    * `item_id` (string, required): The ID of the file or folder to copy.
    * `parent_id` (string, optional): The ID of the destination folder (optional, defaults to root).
    * `new_name` (string, optional): New name for the copied item (optional).
  </Accordion>

  <Accordion title="microsoft_onedrive/move_item">
    **Description:** Move a file or folder in OneDrive.

    **Parameters:**

    * `item_id` (string, required): The ID of the file or folder to move.
    * `parent_id` (string, required): The ID of the destination folder.
    * `new_name` (string, optional): New name for the item (optional).
  </Accordion>

  <Accordion title="microsoft_onedrive/search_files">
    **Description:** Search for files and folders in OneDrive.

    **Parameters:**

    * `query` (string, required): Search query string.
    * `top` (integer, optional): Number of results to return (max 1000). Default is `50`.
  </Accordion>

  <Accordion title="microsoft_onedrive/share_item">
    **Description:** Create a sharing link for a file or folder.

    **Parameters:**

    * `item_id` (string, required): The ID of the file or folder to share.
    * `type` (string, optional): Type of sharing link. Enum: `view`, `edit`, `embed`. Default is `view`.
    * `scope` (string, optional): Scope of the sharing link. Enum: `anonymous`, `organization`. Default is `anonymous`.
  </Accordion>

  <Accordion title="microsoft_onedrive/get_thumbnails">
    **Description:** Get thumbnails for a file.

    **Parameters:**

    * `item_id` (string, required): The ID of the file.
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Microsoft OneDrive Integration](./1812-setting-up-microsoft-onedrive-integration.md)

**Next:** [Usage Examples →](./1814-usage-examples.md)
