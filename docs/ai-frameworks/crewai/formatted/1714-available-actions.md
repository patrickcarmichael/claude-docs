---
title: "Crewai: Available Actions"
description: "Available Actions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Actions


<AccordionGroup>
  <Accordion title="google_drive/get_file">
    **Description:** Get a file by ID from Google Drive.

    **Parameters:**

    * `file_id` (string, required): The ID of the file to retrieve.
  </Accordion>

  <Accordion title="google_drive/list_files">
    **Description:** List files in Google Drive.

    **Parameters:**

    * `q` (string, optional): Query string to filter files (example: "name contains 'report'").
    * `page_size` (integer, optional): Maximum number of files to return (default: 100, max: 1000).
    * `page_token` (string, optional): Token for retrieving the next page of results.
    * `order_by` (string, optional): Sort order (example: "name", "createdTime desc", "modifiedTime").
    * `spaces` (string, optional): Comma-separated list of spaces to query (drive, appDataFolder, photos).
  </Accordion>

  <Accordion title="google_drive/upload_file">
    **Description:** Upload a file to Google Drive.

    **Parameters:**

    * `name` (string, required): Name of the file to create.
    * `content` (string, required): Content of the file to upload.
    * `mime_type` (string, optional): MIME type of the file (example: "text/plain", "application/pdf").
    * `parent_folder_id` (string, optional): ID of the parent folder where the file should be created.
    * `description` (string, optional): Description of the file.
  </Accordion>

  <Accordion title="google_drive/download_file">
    **Description:** Download a file from Google Drive.

    **Parameters:**

    * `file_id` (string, required): The ID of the file to download.
    * `mime_type` (string, optional): MIME type for export (required for Google Workspace documents).
  </Accordion>

  <Accordion title="google_drive/create_folder">
    **Description:** Create a new folder in Google Drive.

    **Parameters:**

    * `name` (string, required): Name of the folder to create.
    * `parent_folder_id` (string, optional): ID of the parent folder where the new folder should be created.
    * `description` (string, optional): Description of the folder.
  </Accordion>

  <Accordion title="google_drive/delete_file">
    **Description:** Delete a file from Google Drive.

    **Parameters:**

    * `file_id` (string, required): The ID of the file to delete.
  </Accordion>

  <Accordion title="google_drive/share_file">
    **Description:** Share a file in Google Drive with specific users or make it public.

    **Parameters:**

    * `file_id` (string, required): The ID of the file to share.
    * `role` (string, required): The role granted by this permission (reader, writer, commenter, owner).
    * `type` (string, required): The type of the grantee (user, group, domain, anyone).
    * `email_address` (string, optional): The email address of the user or group to share with (required for user/group types).
    * `domain` (string, optional): The domain to share with (required for domain type).
    * `send_notification_email` (boolean, optional): Whether to send a notification email (default: true).
    * `email_message` (string, optional): A plain text custom message to include in the notification email.
  </Accordion>

  <Accordion title="google_drive/update_file">
    **Description:** Update an existing file in Google Drive.

    **Parameters:**

    * `file_id` (string, required): The ID of the file to update.
    * `name` (string, optional): New name for the file.
    * `content` (string, optional): New content for the file.
    * `mime_type` (string, optional): New MIME type for the file.
    * `description` (string, optional): New description for the file.
    * `add_parents` (string, optional): Comma-separated list of parent folder IDs to add.
    * `remove_parents` (string, optional): Comma-separated list of parent folder IDs to remove.
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Google Drive Integration](./1713-setting-up-google-drive-integration.md)

**Next:** [Usage Examples →](./1715-usage-examples.md)
