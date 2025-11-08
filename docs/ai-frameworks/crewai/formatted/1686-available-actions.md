---
title: "Crewai: Available Actions"
description: "Available Actions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Actions


<AccordionGroup>
  <Accordion title="google_contacts/get_contacts">
    **Description:** Retrieve user's contacts from Google Contacts.

    **Parameters:**

    * `pageSize` (integer, optional): Number of contacts to return (max 1000). Minimum: 1, Maximum: 1000
    * `pageToken` (string, optional): The token of the page to retrieve.
    * `personFields` (string, optional): Fields to include (e.g., 'names,emailAddresses,phoneNumbers'). Default: names,emailAddresses,phoneNumbers
    * `requestSyncToken` (boolean, optional): Whether the response should include a sync token. Default: false
    * `sortOrder` (string, optional): The order in which the connections should be sorted. Options: LAST\_MODIFIED\_ASCENDING, LAST\_MODIFIED\_DESCENDING, FIRST\_NAME\_ASCENDING, LAST\_NAME\_ASCENDING
  </Accordion>

  <Accordion title="google_contacts/search_contacts">
    **Description:** Search for contacts using a query string.

    **Parameters:**

    * `query` (string, required): Search query string
    * `readMask` (string, required): Fields to read (e.g., 'names,emailAddresses,phoneNumbers')
    * `pageSize` (integer, optional): Number of results to return. Minimum: 1, Maximum: 30
    * `pageToken` (string, optional): Token specifying which result page to return.
    * `sources` (array, optional): The sources to search in. Options: READ\_SOURCE\_TYPE\_CONTACT, READ\_SOURCE\_TYPE\_PROFILE. Default: READ\_SOURCE\_TYPE\_CONTACT
  </Accordion>

  <Accordion title="google_contacts/list_directory_people">
    **Description:** List people in the authenticated user's directory.

    **Parameters:**

    * `sources` (array, required): Directory sources to search within. Options: DIRECTORY\_SOURCE\_TYPE\_DOMAIN\_PROFILE, DIRECTORY\_SOURCE\_TYPE\_DOMAIN\_CONTACT. Default: DIRECTORY\_SOURCE\_TYPE\_DOMAIN\_PROFILE
    * `pageSize` (integer, optional): Number of people to return. Minimum: 1, Maximum: 1000
    * `pageToken` (string, optional): Token specifying which result page to return.
    * `readMask` (string, optional): Fields to read (e.g., 'names,emailAddresses')
    * `requestSyncToken` (boolean, optional): Whether the response should include a sync token. Default: false
    * `mergeSources` (array, optional): Additional data to merge into the directory people responses. Options: CONTACT
  </Accordion>

  <Accordion title="google_contacts/search_directory_people">
    **Description:** Search for people in the directory.

    **Parameters:**

    * `query` (string, required): Search query
    * `sources` (string, required): Directory sources (use 'DIRECTORY\_SOURCE\_TYPE\_DOMAIN\_PROFILE')
    * `pageSize` (integer, optional): Number of results to return
    * `readMask` (string, optional): Fields to read
  </Accordion>

  <Accordion title="google_contacts/list_other_contacts">
    **Description:** List other contacts (not in user's personal contacts).

    **Parameters:**

    * `pageSize` (integer, optional): Number of contacts to return. Minimum: 1, Maximum: 1000
    * `pageToken` (string, optional): Token specifying which result page to return.
    * `readMask` (string, optional): Fields to read
    * `requestSyncToken` (boolean, optional): Whether the response should include a sync token. Default: false
  </Accordion>

  <Accordion title="google_contacts/search_other_contacts">
    **Description:** Search other contacts.

    **Parameters:**

    * `query` (string, required): Search query
    * `readMask` (string, required): Fields to read (e.g., 'names,emailAddresses')
    * `pageSize` (integer, optional): Number of results
  </Accordion>

  <Accordion title="google_contacts/get_person">
    **Description:** Get a single person's contact information by resource name.

    **Parameters:**

    * `resourceName` (string, required): The resource name of the person to get (e.g., 'people/c123456789')
    * `personFields` (string, optional): Fields to include (e.g., 'names,emailAddresses,phoneNumbers'). Default: names,emailAddresses,phoneNumbers
  </Accordion>

  <Accordion title="google_contacts/create_contact">
    **Description:** Create a new contact in the user's address book.

    **Parameters:**

    * `names` (array, optional): Person's names
      ```json  theme={null}
      [
        {
          "givenName": "John",
          "familyName": "Doe",
          "displayName": "John Doe"
        }
      ]
      ```
    * `emailAddresses` (array, optional): Email addresses
      ```json  theme={null}
      [
        {
          "value": "john.doe@example.com",
          "type": "work"
        }
      ]
      ```
    * `phoneNumbers` (array, optional): Phone numbers
      ```json  theme={null}
      [
        {
          "value": "+1234567890",
          "type": "mobile"
        }
      ]
      ```
    * `addresses` (array, optional): Postal addresses
      ```json  theme={null}
      [
        {
          "formattedValue": "123 Main St, City, State 12345",
          "type": "home"
        }
      ]
      ```
    * `organizations` (array, optional): Organizations/companies
      ```json  theme={null}
      [
        {
          "name": "Company Name",
          "title": "Job Title",
          "type": "work"
        }
      ]
      ```
  </Accordion>

  <Accordion title="google_contacts/update_contact">
    **Description:** Update an existing contact's information.

    **Parameters:**

    * `resourceName` (string, required): The resource name of the person to update (e.g., 'people/c123456789')
    * `updatePersonFields` (string, required): Fields to update (e.g., 'names,emailAddresses,phoneNumbers')
    * `names` (array, optional): Person's names
    * `emailAddresses` (array, optional): Email addresses
    * `phoneNumbers` (array, optional): Phone numbers
  </Accordion>

  <Accordion title="google_contacts/delete_contact">
    **Description:** Delete a contact from the user's address book.

    **Parameters:**

    * `resourceName` (string, required): The resource name of the person to delete (e.g., 'people/c123456789')
  </Accordion>

  <Accordion title="google_contacts/batch_get_people">
    **Description:** Get information about multiple people in a single request.

    **Parameters:**

    * `resourceNames` (array, required): Resource names of people to get. Maximum: 200 items
    * `personFields` (string, optional): Fields to include (e.g., 'names,emailAddresses,phoneNumbers'). Default: names,emailAddresses,phoneNumbers
  </Accordion>

  <Accordion title="google_contacts/list_contact_groups">
    **Description:** List the user's contact groups (labels).

    **Parameters:**

    * `pageSize` (integer, optional): Number of contact groups to return. Minimum: 1, Maximum: 1000
    * `pageToken` (string, optional): Token specifying which result page to return.
    * `groupFields` (string, optional): Fields to include (e.g., 'name,memberCount,clientData'). Default: name,memberCount
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Google Contacts Integration](./1685-setting-up-google-contacts-integration.md)

**Next:** [Usage Examples →](./1687-usage-examples.md)
