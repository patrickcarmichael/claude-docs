---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


### Common Issues

**Authentication Errors**

* Ensure your Microsoft account has the necessary permissions for mail, calendar, and contact access.
* Required scopes include: `Mail.Read`, `Mail.Send`, `Calendars.Read`, `Calendars.ReadWrite`, `Contacts.Read`, `Contacts.ReadWrite`.
* Verify that the OAuth connection includes all required scopes.

**Email Sending Issues**

* Ensure `to_recipients`, `subject`, and `body` are provided for `send_email`.
* Check that email addresses are properly formatted.
* Verify that the account has `Mail.Send` permissions.

**Calendar Event Creation**

* Ensure `subject`, `start_datetime`, and `end_datetime` are provided.
* Use proper ISO 8601 format for datetime fields (e.g., '2024-01-20T10:00:00').
* Verify timezone settings if events appear at incorrect times.

**Contact Management**

* For `create_contact`, ensure `displayName` is provided as it's required.
* When providing `emailAddresses`, use the proper object format with `address` and `name` properties.

**Search and Filter Issues**

* Use proper OData syntax for `filter` parameters.
* For date filters, use ISO 8601 format (e.g., "receivedDateTime ge '2024-01-01T00:00:00Z'").

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Microsoft Outlook integration setup or troubleshooting.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create a meeting and add a contact](./1835-task-to-create-a-meeting-and-add-a-contact.md)

**Next:** [Microsoft SharePoint Integration →](./1837-microsoft-sharepoint-integration.md)
