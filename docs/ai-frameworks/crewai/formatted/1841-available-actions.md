---
title: "Crewai: Available Actions"
description: "Available Actions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Actions


<AccordionGroup>
  <Accordion title="microsoft_sharepoint/get_sites">
    **Description:** Get all SharePoint sites the user has access to.

    **Parameters:**

    * `search` (string, optional): Search query to filter sites
    * `select` (string, optional): Select specific properties to return (e.g., 'displayName,id,webUrl')
    * `filter` (string, optional): Filter results using OData syntax
    * `expand` (string, optional): Expand related resources inline
    * `top` (integer, optional): Number of items to return. Minimum: 1, Maximum: 999
    * `skip` (integer, optional): Number of items to skip. Minimum: 0
    * `orderby` (string, optional): Order results by specified properties (e.g., 'displayName desc')
  </Accordion>

  <Accordion title="microsoft_sharepoint/get_site">
    **Description:** Get information about a specific SharePoint site.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
    * `select` (string, optional): Select specific properties to return (e.g., 'displayName,id,webUrl,drives')
    * `expand` (string, optional): Expand related resources inline (e.g., 'drives,lists')
  </Accordion>

  <Accordion title="microsoft_sharepoint/get_site_lists">
    **Description:** Get all lists in a SharePoint site.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
  </Accordion>

  <Accordion title="microsoft_sharepoint/get_list">
    **Description:** Get information about a specific list.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
    * `list_id` (string, required): The ID of the list
  </Accordion>

  <Accordion title="microsoft_sharepoint/get_list_items">
    **Description:** Get items from a SharePoint list.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
    * `list_id` (string, required): The ID of the list
    * `expand` (string, optional): Expand related data (e.g., 'fields')
  </Accordion>

  <Accordion title="microsoft_sharepoint/create_list_item">
    **Description:** Create a new item in a SharePoint list.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
    * `list_id` (string, required): The ID of the list
    * `fields` (object, required): The field values for the new item
      ```json  theme={null}
      {
        "Title": "New Item Title",
        "Description": "Item description",
        "Status": "Active"
      }
      ```
  </Accordion>

  <Accordion title="microsoft_sharepoint/update_list_item">
    **Description:** Update an item in a SharePoint list.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
    * `list_id` (string, required): The ID of the list
    * `item_id` (string, required): The ID of the item to update
    * `fields` (object, required): The field values to update
      ```json  theme={null}
      {
        "Title": "Updated Title",
        "Status": "Completed"
      }
      ```
  </Accordion>

  <Accordion title="microsoft_sharepoint/delete_list_item">
    **Description:** Delete an item from a SharePoint list.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
    * `list_id` (string, required): The ID of the list
    * `item_id` (string, required): The ID of the item to delete
  </Accordion>

  <Accordion title="microsoft_sharepoint/upload_file_to_library">
    **Description:** Upload a file to a SharePoint document library.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
    * `file_path` (string, required): The path where to upload the file (e.g., 'folder/filename.txt')
    * `content` (string, required): The file content to upload
  </Accordion>

  <Accordion title="microsoft_sharepoint/get_drive_items">
    **Description:** Get files and folders from a SharePoint document library.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
  </Accordion>

  <Accordion title="microsoft_sharepoint/delete_drive_item">
    **Description:** Delete a file or folder from SharePoint document library.

    **Parameters:**

    * `site_id` (string, required): The ID of the SharePoint site
    * `item_id` (string, required): The ID of the file or folder to delete
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Microsoft SharePoint Integration](./1840-setting-up-microsoft-sharepoint-integration.md)

**Next:** [Usage Examples →](./1842-usage-examples.md)
