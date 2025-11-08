---
title: "Crewai: Available Tools"
description: "Available Tools section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Tools


### **Ticket Management**

<AccordionGroup>
  <Accordion title="zendesk/create_ticket">
    **Description:** Create a new support ticket in Zendesk.

    **Parameters:**

    * `ticketSubject` (string, required): Ticket subject line (e.g., "Help, my printer is on fire!")
    * `ticketDescription` (string, required): First comment that appears on the ticket (e.g., "The smoke is very colorful.")
    * `requesterName` (string, required): Name of the user requesting support (e.g., "Jane Customer")
    * `requesterEmail` (string, required): Email of the user requesting support (e.g., "[jane@example.com](mailto:jane@example.com)")
    * `assigneeId` (string, optional): Zendesk Agent ID assigned to this ticket - Use Connect Portal Workflow Settings to allow users to select an assignee
    * `ticketType` (string, optional): Ticket type - Options: problem, incident, question, task
    * `ticketPriority` (string, optional): Priority level - Options: urgent, high, normal, low
    * `ticketStatus` (string, optional): Ticket status - Options: new, open, pending, hold, solved, closed
    * `ticketDueAt` (string, optional): Due date for task-type tickets (ISO 8601 timestamp)
    * `ticketTags` (string, optional): Array of tags to apply (e.g., `["enterprise", "other_tag"]`)
    * `ticketExternalId` (string, optional): External ID to link tickets to local records
    * `ticketCustomFields` (object, optional): Custom field values in JSON format
  </Accordion>

  <Accordion title="zendesk/update_ticket">
    **Description:** Update an existing support ticket in Zendesk.

    **Parameters:**

    * `ticketId` (string, required): ID of the ticket to update (e.g., "35436")
    * `ticketSubject` (string, optional): Updated ticket subject
    * `requesterName` (string, required): Name of the user who requested this ticket
    * `requesterEmail` (string, required): Email of the user who requested this ticket
    * `assigneeId` (string, optional): Updated assignee ID - Use Connect Portal Workflow Settings
    * `ticketType` (string, optional): Updated ticket type - Options: problem, incident, question, task
    * `ticketPriority` (string, optional): Updated priority - Options: urgent, high, normal, low
    * `ticketStatus` (string, optional): Updated status - Options: new, open, pending, hold, solved, closed
    * `ticketDueAt` (string, optional): Updated due date (ISO 8601 timestamp)
    * `ticketTags` (string, optional): Updated tags array
    * `ticketExternalId` (string, optional): Updated external ID
    * `ticketCustomFields` (object, optional): Updated custom field values
  </Accordion>

  <Accordion title="zendesk/get_ticket_by_id">
    **Description:** Retrieve a specific ticket by its ID.

    **Parameters:**

    * `ticketId` (string, required): The ticket ID to retrieve (e.g., "35436")
  </Accordion>

  <Accordion title="zendesk/add_comment_to_ticket">
    **Description:** Add a comment or internal note to an existing ticket.

    **Parameters:**

    * `ticketId` (string, required): ID of the ticket to add comment to (e.g., "35436")
    * `commentBody` (string, required): Comment message (accepts plain text or HTML, e.g., "Thanks for your help!")
    * `isInternalNote` (boolean, optional): Set to true for internal notes instead of public replies (defaults to false)
    * `isPublic` (boolean, optional): True for public comments, false for internal notes
  </Accordion>

  <Accordion title="zendesk/search_tickets">
    **Description:** Search for tickets using various filters and criteria.

    **Parameters:**

    * `ticketSubject` (string, optional): Filter by text in ticket subject
    * `ticketDescription` (string, optional): Filter by text in ticket description and comments
    * `ticketStatus` (string, optional): Filter by status - Options: new, open, pending, hold, solved, closed
    * `ticketType` (string, optional): Filter by type - Options: problem, incident, question, task, no\_type
    * `ticketPriority` (string, optional): Filter by priority - Options: urgent, high, normal, low, no\_priority
    * `requesterId` (string, optional): Filter by requester user ID
    * `assigneeId` (string, optional): Filter by assigned agent ID
    * `recipientEmail` (string, optional): Filter by original recipient email address
    * `ticketTags` (string, optional): Filter by ticket tags
    * `ticketExternalId` (string, optional): Filter by external ID
    * `createdDate` (object, optional): Filter by creation date with operator (EQUALS, LESS\_THAN\_EQUALS, GREATER\_THAN\_EQUALS) and value
    * `updatedDate` (object, optional): Filter by update date with operator and value
    * `dueDate` (object, optional): Filter by due date with operator and value
    * `sort_by` (string, optional): Sort field - Options: created\_at, updated\_at, priority, status, ticket\_type
    * `sort_order` (string, optional): Sort direction - Options: asc, desc
  </Accordion>
</AccordionGroup>

### **User Management**

<AccordionGroup>
  <Accordion title="zendesk/create_user">
    **Description:** Create a new user in Zendesk.

    **Parameters:**

    * `name` (string, required): User's full name
    * `email` (string, optional): User's email address (e.g., "[jane@example.com](mailto:jane@example.com)")
    * `phone` (string, optional): User's phone number
    * `role` (string, optional): User role - Options: admin, agent, end-user
    * `externalId` (string, optional): Unique identifier from another system
    * `details` (string, optional): Additional user details
    * `notes` (string, optional): Internal notes about the user
  </Accordion>

  <Accordion title="zendesk/update_user">
    **Description:** Update an existing user's information.

    **Parameters:**

    * `userId` (string, required): ID of the user to update
    * `name` (string, optional): Updated user name
    * `email` (string, optional): Updated email (adds as secondary email on update)
    * `phone` (string, optional): Updated phone number
    * `role` (string, optional): Updated role - Options: admin, agent, end-user
    * `externalId` (string, optional): Updated external ID
    * `details` (string, optional): Updated user details
    * `notes` (string, optional): Updated internal notes
  </Accordion>

  <Accordion title="zendesk/get_user_by_id">
    **Description:** Retrieve a specific user by their ID.

    **Parameters:**

    * `userId` (string, required): The user ID to retrieve
  </Accordion>

  <Accordion title="zendesk/search_users">
    **Description:** Search for users using various criteria.

    **Parameters:**

    * `name` (string, optional): Filter by user name
    * `email` (string, optional): Filter by user email (e.g., "[jane@example.com](mailto:jane@example.com)")
    * `role` (string, optional): Filter by role - Options: admin, agent, end-user
    * `externalId` (string, optional): Filter by external ID
    * `sort_by` (string, optional): Sort field - Options: created\_at, updated\_at
    * `sort_order` (string, optional): Sort direction - Options: asc, desc
  </Accordion>
</AccordionGroup>

### **Administrative Tools**

<AccordionGroup>
  <Accordion title="zendesk/get_ticket_fields">
    **Description:** Retrieve all standard and custom fields available for tickets.

    **Parameters:**

    * `paginationParameters` (object, optional): Pagination settings
      * `pageCursor` (string, optional): Page cursor for pagination
  </Accordion>

  <Accordion title="zendesk/get_ticket_audits">
    **Description:** Get audit records (read-only history) for tickets.

    **Parameters:**

    * `ticketId` (string, optional): Get audits for specific ticket (if empty, retrieves audits for all non-archived tickets, e.g., "1234")
    * `paginationParameters` (object, optional): Pagination settings
      * `pageCursor` (string, optional): Page cursor for pagination
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Zendesk Integration](./1952-setting-up-zendesk-integration.md)

**Next:** [Custom Fields →](./1954-custom-fields.md)
