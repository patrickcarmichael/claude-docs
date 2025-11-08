---
title: "Crewai: Available Actions"
description: "Available Actions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Actions


<AccordionGroup>
  <Accordion title="box/save_file">
    **Description:** Save a file from URL in Box.

    **Parameters:**

    * `fileAttributes` (object, required): Attributes - File metadata including name, parent folder, and timestamps.
      ```json  theme={null}
      {
        "content_created_at": "2012-12-12T10:53:43-08:00",
        "content_modified_at": "2012-12-12T10:53:43-08:00",
        "name": "qwerty.png",
        "parent": { "id": "1234567" }
      }
      ```
    * `file` (string, required): File URL - Files must be smaller than 50MB in size. (example: "[https://picsum.photos/200/300](https://picsum.photos/200/300)").
  </Accordion>

  <Accordion title="box/save_file_from_object">
    **Description:** Save a file in Box.

    **Parameters:**

    * `file` (string, required): File - Accepts a File Object containing file data. Files must be smaller than 50MB in size.
    * `fileName` (string, required): File Name (example: "qwerty.png").
    * `folder` (string, optional): Folder - Use Connect Portal Workflow Settings to allow users to select the File's Folder destination. Defaults to the user's root folder if left blank.
  </Accordion>

  <Accordion title="box/get_file_by_id">
    **Description:** Get a file by ID in Box.

    **Parameters:**

    * `fileId` (string, required): File ID - The unique identifier that represents a file. (example: "12345").
  </Accordion>

  <Accordion title="box/list_files">
    **Description:** List files in Box.

    **Parameters:**

    * `folderId` (string, required): Folder ID - The unique identifier that represents a folder. (example: "0").
    * `filterFormula` (object, optional): A filter in disjunctive normal form - OR of AND groups of single conditions.
      ```json  theme={null}
      {
        "operator": "OR",
        "conditions": [
          {
            "operator": "AND",
            "conditions": [
              {
                "field": "direction",
                "operator": "$stringExactlyMatches",
                "value": "ASC"
              }
            ]
          }
        ]
      }
      ```
  </Accordion>

  <Accordion title="box/create_folder">
    **Description:** Create a folder in Box.

    **Parameters:**

    * `folderName` (string, required): Name - The name for the new folder. (example: "New Folder").
    * `folderParent` (object, required): Parent Folder - The parent folder where the new folder will be created.
      ```json  theme={null}
      {
        "id": "123456"
      }
      ```
  </Accordion>

  <Accordion title="box/move_folder">
    **Description:** Move a folder in Box.

    **Parameters:**

    * `folderId` (string, required): Folder ID - The unique identifier that represents a folder. (example: "0").
    * `folderName` (string, required): Name - The name for the folder. (example: "New Folder").
    * `folderParent` (object, required): Parent Folder - The new parent folder destination.
      ```json  theme={null}
      {
        "id": "123456"
      }
      ```
  </Accordion>

  <Accordion title="box/get_folder_by_id">
    **Description:** Get a folder by ID in Box.

    **Parameters:**

    * `folderId` (string, required): Folder ID - The unique identifier that represents a folder. (example: "0").
  </Accordion>

  <Accordion title="box/search_folders">
    **Description:** Search folders in Box.

    **Parameters:**

    * `folderId` (string, required): Folder ID - The folder to search within.
    * `filterFormula` (object, optional): A filter in disjunctive normal form - OR of AND groups of single conditions.
      ```json  theme={null}
      {
        "operator": "OR",
        "conditions": [
          {
            "operator": "AND",
            "conditions": [
              {
                "field": "sort",
                "operator": "$stringExactlyMatches",
                "value": "name"
              }
            ]
          }
        ]
      }
      ```
  </Accordion>

  <Accordion title="box/delete_folder">
    **Description:** Delete a folder in Box.

    **Parameters:**

    * `folderId` (string, required): Folder ID - The unique identifier that represents a folder. (example: "0").
    * `recursive` (boolean, optional): Recursive - Delete a folder that is not empty by recursively deleting the folder and all of its content.
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Box Integration](./1620-setting-up-box-integration.md)

**Next:** [Usage Examples →](./1622-usage-examples.md)
