---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


### Common Issues

**Authentication Errors**

* Ensure your Google account has the necessary permissions for calendar access
* Verify that the OAuth connection includes all required scopes for Google Calendar API
* Check if calendar sharing settings allow the required access level

**Event Creation Issues**

* Verify that time formats are correct (RFC3339 format)
* Ensure attendee email addresses are properly formatted
* Check that the target calendar exists and is accessible
* Verify time zones are correctly specified

**Availability and Time Conflicts**

* Use proper RFC3339 format for time ranges when checking availability
* Ensure time zones are consistent across all operations
* Verify that calendar IDs are correct when checking multiple calendars

**Event Updates and Deletions**

* Verify that event IDs are correct and events exist
* Ensure you have edit permissions for the events
* Check that calendar ownership allows modifications

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Google Calendar integration setup or troubleshooting.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Complex scheduling automation task](./1680-complex-scheduling-automation-task.md)

**Next:** [Google Contacts Integration →](./1682-google-contacts-integration.md)
