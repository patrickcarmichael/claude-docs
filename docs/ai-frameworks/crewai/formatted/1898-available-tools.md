---
title: "Crewai: Available Tools"
description: "Available Tools section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Tools


### **Record Management**

<AccordionGroup>
  <Accordion title="salesforce/create_record_contact">
    **Description:** Create a new Contact record in Salesforce.

    **Parameters:**

    * `FirstName` (string, optional): First Name
    * `LastName` (string, required): Last Name - This field is required
    * `accountId` (string, optional): Account ID - The Account that the Contact belongs to
    * `Email` (string, optional): Email address
    * `Title` (string, optional): Title of the contact, such as CEO or Vice President
    * `Description` (string, optional): A description of the Contact
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Contact fields
  </Accordion>

  <Accordion title="salesforce/create_record_lead">
    **Description:** Create a new Lead record in Salesforce.

    **Parameters:**

    * `FirstName` (string, optional): First Name
    * `LastName` (string, required): Last Name - This field is required
    * `Company` (string, required): Company - This field is required
    * `Email` (string, optional): Email address
    * `Phone` (string, optional): Phone number
    * `Website` (string, optional): Website URL
    * `Title` (string, optional): Title of the contact, such as CEO or Vice President
    * `Status` (string, optional): Lead Status - Use Connect Portal Workflow Settings to select Lead Status
    * `Description` (string, optional): A description of the Lead
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Lead fields
  </Accordion>

  <Accordion title="salesforce/create_record_opportunity">
    **Description:** Create a new Opportunity record in Salesforce.

    **Parameters:**

    * `Name` (string, required): The Opportunity name - This field is required
    * `StageName` (string, optional): Opportunity Stage - Use Connect Portal Workflow Settings to select stage
    * `CloseDate` (string, optional): Close Date in YYYY-MM-DD format - Defaults to 30 days from current date
    * `AccountId` (string, optional): The Account that the Opportunity belongs to
    * `Amount` (string, optional): Estimated total sale amount
    * `Description` (string, optional): A description of the Opportunity
    * `OwnerId` (string, optional): The Salesforce user assigned to work on this Opportunity
    * `NextStep` (string, optional): Description of next task in closing Opportunity
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Opportunity fields
  </Accordion>

  <Accordion title="salesforce/create_record_task">
    **Description:** Create a new Task record in Salesforce.

    **Parameters:**

    * `whatId` (string, optional): Related to ID - The ID of the Account or Opportunity this Task is related to
    * `whoId` (string, optional): Name ID - The ID of the Contact or Lead this Task is related to
    * `subject` (string, required): Subject of the task
    * `activityDate` (string, optional): Activity Date in YYYY-MM-DD format
    * `description` (string, optional): A description of the Task
    * `taskSubtype` (string, required): Task Subtype - Options: task, email, listEmail, call
    * `Status` (string, optional): Status - Options: Not Started, In Progress, Completed
    * `ownerId` (string, optional): Assigned To ID - The Salesforce user assigned to this Task
    * `callDurationInSeconds` (string, optional): Call Duration in seconds
    * `isReminderSet` (boolean, optional): Whether reminder is set
    * `reminderDateTime` (string, optional): Reminder Date/Time in ISO format
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Task fields
  </Accordion>

  <Accordion title="salesforce/create_record_account">
    **Description:** Create a new Account record in Salesforce.

    **Parameters:**

    * `Name` (string, required): The Account name - This field is required
    * `OwnerId` (string, optional): The Salesforce user assigned to this Account
    * `Website` (string, optional): Website URL
    * `Phone` (string, optional): Phone number
    * `Description` (string, optional): Account description
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Account fields
  </Accordion>

  <Accordion title="salesforce/create_record_any">
    **Description:** Create a record of any object type in Salesforce.

    **Note:** This is a flexible tool for creating records of custom or unknown object types.
  </Accordion>
</AccordionGroup>

### **Record Updates**

<AccordionGroup>
  <Accordion title="salesforce/update_record_contact">
    **Description:** Update an existing Contact record in Salesforce.

    **Parameters:**

    * `recordId` (string, required): The ID of the record to update
    * `FirstName` (string, optional): First Name
    * `LastName` (string, optional): Last Name
    * `accountId` (string, optional): Account ID - The Account that the Contact belongs to
    * `Email` (string, optional): Email address
    * `Title` (string, optional): Title of the contact
    * `Description` (string, optional): A description of the Contact
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Contact fields
  </Accordion>

  <Accordion title="salesforce/update_record_lead">
    **Description:** Update an existing Lead record in Salesforce.

    **Parameters:**

    * `recordId` (string, required): The ID of the record to update
    * `FirstName` (string, optional): First Name
    * `LastName` (string, optional): Last Name
    * `Company` (string, optional): Company name
    * `Email` (string, optional): Email address
    * `Phone` (string, optional): Phone number
    * `Website` (string, optional): Website URL
    * `Title` (string, optional): Title of the contact
    * `Status` (string, optional): Lead Status
    * `Description` (string, optional): A description of the Lead
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Lead fields
  </Accordion>

  <Accordion title="salesforce/update_record_opportunity">
    **Description:** Update an existing Opportunity record in Salesforce.

    **Parameters:**

    * `recordId` (string, required): The ID of the record to update
    * `Name` (string, optional): The Opportunity name
    * `StageName` (string, optional): Opportunity Stage
    * `CloseDate` (string, optional): Close Date in YYYY-MM-DD format
    * `AccountId` (string, optional): The Account that the Opportunity belongs to
    * `Amount` (string, optional): Estimated total sale amount
    * `Description` (string, optional): A description of the Opportunity
    * `OwnerId` (string, optional): The Salesforce user assigned to work on this Opportunity
    * `NextStep` (string, optional): Description of next task in closing Opportunity
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Opportunity fields
  </Accordion>

  <Accordion title="salesforce/update_record_task">
    **Description:** Update an existing Task record in Salesforce.

    **Parameters:**

    * `recordId` (string, required): The ID of the record to update
    * `whatId` (string, optional): Related to ID - The ID of the Account or Opportunity this Task is related to
    * `whoId` (string, optional): Name ID - The ID of the Contact or Lead this Task is related to
    * `subject` (string, optional): Subject of the task
    * `activityDate` (string, optional): Activity Date in YYYY-MM-DD format
    * `description` (string, optional): A description of the Task
    * `Status` (string, optional): Status - Options: Not Started, In Progress, Completed
    * `ownerId` (string, optional): Assigned To ID - The Salesforce user assigned to this Task
    * `callDurationInSeconds` (string, optional): Call Duration in seconds
    * `isReminderSet` (boolean, optional): Whether reminder is set
    * `reminderDateTime` (string, optional): Reminder Date/Time in ISO format
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Task fields
  </Accordion>

  <Accordion title="salesforce/update_record_account">
    **Description:** Update an existing Account record in Salesforce.

    **Parameters:**

    * `recordId` (string, required): The ID of the record to update
    * `Name` (string, optional): The Account name
    * `OwnerId` (string, optional): The Salesforce user assigned to this Account
    * `Website` (string, optional): Website URL
    * `Phone` (string, optional): Phone number
    * `Description` (string, optional): Account description
    * `additionalFields` (object, optional): Additional fields in JSON format for custom Account fields
  </Accordion>

  <Accordion title="salesforce/update_record_any">
    **Description:** Update a record of any object type in Salesforce.

    **Note:** This is a flexible tool for updating records of custom or unknown object types.
  </Accordion>
</AccordionGroup>

### **Record Retrieval**

<AccordionGroup>
  <Accordion title="salesforce/get_record_by_id_contact">
    **Description:** Get a Contact record by its ID.

    **Parameters:**

    * `recordId` (string, required): Record ID of the Contact
  </Accordion>

  <Accordion title="salesforce/get_record_by_id_lead">
    **Description:** Get a Lead record by its ID.

    **Parameters:**

    * `recordId` (string, required): Record ID of the Lead
  </Accordion>

  <Accordion title="salesforce/get_record_by_id_opportunity">
    **Description:** Get an Opportunity record by its ID.

    **Parameters:**

    * `recordId` (string, required): Record ID of the Opportunity
  </Accordion>

  <Accordion title="salesforce/get_record_by_id_task">
    **Description:** Get a Task record by its ID.

    **Parameters:**

    * `recordId` (string, required): Record ID of the Task
  </Accordion>

  <Accordion title="salesforce/get_record_by_id_account">
    **Description:** Get an Account record by its ID.

    **Parameters:**

    * `recordId` (string, required): Record ID of the Account
  </Accordion>

  <Accordion title="salesforce/get_record_by_id_any">
    **Description:** Get a record of any object type by its ID.

    **Parameters:**

    * `recordType` (string, required): Record Type (e.g., "CustomObject\_\_c")
    * `recordId` (string, required): Record ID
  </Accordion>
</AccordionGroup>

### **Record Search**

<AccordionGroup>
  <Accordion title="salesforce/search_records_contact">
    **Description:** Search for Contact records with advanced filtering.

    **Parameters:**

    * `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `sortBy` (string, optional): Sort field (e.g., "CreatedDate")
    * `sortDirection` (string, optional): Sort direction - Options: ASC, DESC
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/search_records_lead">
    **Description:** Search for Lead records with advanced filtering.

    **Parameters:**

    * `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `sortBy` (string, optional): Sort field (e.g., "CreatedDate")
    * `sortDirection` (string, optional): Sort direction - Options: ASC, DESC
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/search_records_opportunity">
    **Description:** Search for Opportunity records with advanced filtering.

    **Parameters:**

    * `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `sortBy` (string, optional): Sort field (e.g., "CreatedDate")
    * `sortDirection` (string, optional): Sort direction - Options: ASC, DESC
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/search_records_task">
    **Description:** Search for Task records with advanced filtering.

    **Parameters:**

    * `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `sortBy` (string, optional): Sort field (e.g., "CreatedDate")
    * `sortDirection` (string, optional): Sort direction - Options: ASC, DESC
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/search_records_account">
    **Description:** Search for Account records with advanced filtering.

    **Parameters:**

    * `filterFormula` (object, optional): Advanced filter in disjunctive normal form with field-specific operators
    * `sortBy` (string, optional): Sort field (e.g., "CreatedDate")
    * `sortDirection` (string, optional): Sort direction - Options: ASC, DESC
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/search_records_any">
    **Description:** Search for records of any object type.

    **Parameters:**

    * `recordType` (string, required): Record Type to search
    * `filterFormula` (string, optional): Filter search criteria
    * `includeAllFields` (boolean, optional): Include all fields in results
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>
</AccordionGroup>

### **List View Retrieval**

<AccordionGroup>
  <Accordion title="salesforce/get_record_by_view_id_contact">
    **Description:** Get Contact records from a specific List View.

    **Parameters:**

    * `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/get_record_by_view_id_lead">
    **Description:** Get Lead records from a specific List View.

    **Parameters:**

    * `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/get_record_by_view_id_opportunity">
    **Description:** Get Opportunity records from a specific List View.

    **Parameters:**

    * `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/get_record_by_view_id_task">
    **Description:** Get Task records from a specific List View.

    **Parameters:**

    * `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/get_record_by_view_id_account">
    **Description:** Get Account records from a specific List View.

    **Parameters:**

    * `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>

  <Accordion title="salesforce/get_record_by_view_id_any">
    **Description:** Get records of any object type from a specific List View.

    **Parameters:**

    * `recordType` (string, required): Record Type
    * `listViewId` (string, required): List View ID
    * `paginationParameters` (object, optional): Pagination settings with pageCursor
  </Accordion>
</AccordionGroup>

### **Custom Fields**

<AccordionGroup>
  <Accordion title="salesforce/create_custom_field_contact">
    **Description:** Deploy custom fields for Contact objects.

    **Parameters:**

    * `label` (string, required): Field Label for displays and internal reference
    * `type` (string, required): Field Type - Options: Checkbox, Currency, Date, Email, Number, Percent, Phone, Picklist, MultiselectPicklist, Text, TextArea, LongTextArea, Html, Time, Url
    * `defaultCheckboxValue` (boolean, optional): Default value for checkbox fields
    * `length` (string, required): Length for numeric/text fields
    * `decimalPlace` (string, required): Decimal places for numeric fields
    * `pickListValues` (string, required): Values for picklist fields (separated by new lines)
    * `visibleLines` (string, required): Visible lines for multiselect/text area fields
    * `description` (string, optional): Field description
    * `helperText` (string, optional): Helper text shown on hover
    * `defaultFieldValue` (string, optional): Default field value
  </Accordion>

  <Accordion title="salesforce/create_custom_field_lead">
    **Description:** Deploy custom fields for Lead objects.

    **Parameters:**

    * `label` (string, required): Field Label for displays and internal reference
    * `type` (string, required): Field Type - Options: Checkbox, Currency, Date, Email, Number, Percent, Phone, Picklist, MultiselectPicklist, Text, TextArea, LongTextArea, Html, Time, Url
    * `defaultCheckboxValue` (boolean, optional): Default value for checkbox fields
    * `length` (string, required): Length for numeric/text fields
    * `decimalPlace` (string, required): Decimal places for numeric fields
    * `pickListValues` (string, required): Values for picklist fields (separated by new lines)
    * `visibleLines` (string, required): Visible lines for multiselect/text area fields
    * `description` (string, optional): Field description
    * `helperText` (string, optional): Helper text shown on hover
    * `defaultFieldValue` (string, optional): Default field value
  </Accordion>

  <Accordion title="salesforce/create_custom_field_opportunity">
    **Description:** Deploy custom fields for Opportunity objects.

    **Parameters:**

    * `label` (string, required): Field Label for displays and internal reference
    * `type` (string, required): Field Type - Options: Checkbox, Currency, Date, Email, Number, Percent, Phone, Picklist, MultiselectPicklist, Text, TextArea, LongTextArea, Html, Time, Url
    * `defaultCheckboxValue` (boolean, optional): Default value for checkbox fields
    * `length` (string, required): Length for numeric/text fields
    * `decimalPlace` (string, required): Decimal places for numeric fields
    * `pickListValues` (string, required): Values for picklist fields (separated by new lines)
    * `visibleLines` (string, required): Visible lines for multiselect/text area fields
    * `description` (string, optional): Field description
    * `helperText` (string, optional): Helper text shown on hover
    * `defaultFieldValue` (string, optional): Default field value
  </Accordion>

  <Accordion title="salesforce/create_custom_field_task">
    **Description:** Deploy custom fields for Task objects.

    **Parameters:**

    * `label` (string, required): Field Label for displays and internal reference
    * `type` (string, required): Field Type - Options: Checkbox, Currency, Date, Email, Number, Percent, Phone, Picklist, MultiselectPicklist, Text, TextArea, Time, Url
    * `defaultCheckboxValue` (boolean, optional): Default value for checkbox fields
    * `length` (string, required): Length for numeric/text fields
    * `decimalPlace` (string, required): Decimal places for numeric fields
    * `pickListValues` (string, required): Values for picklist fields (separated by new lines)
    * `visibleLines` (string, required): Visible lines for multiselect fields
    * `description` (string, optional): Field description
    * `helperText` (string, optional): Helper text shown on hover
    * `defaultFieldValue` (string, optional): Default field value
  </Accordion>

  <Accordion title="salesforce/create_custom_field_account">
    **Description:** Deploy custom fields for Account objects.

    **Parameters:**

    * `label` (string, required): Field Label for displays and internal reference
    * `type` (string, required): Field Type - Options: Checkbox, Currency, Date, Email, Number, Percent, Phone, Picklist, MultiselectPicklist, Text, TextArea, LongTextArea, Html, Time, Url
    * `defaultCheckboxValue` (boolean, optional): Default value for checkbox fields
    * `length` (string, required): Length for numeric/text fields
    * `decimalPlace` (string, required): Decimal places for numeric fields
    * `pickListValues` (string, required): Values for picklist fields (separated by new lines)
    * `visibleLines` (string, required): Visible lines for multiselect/text area fields
    * `description` (string, optional): Field description
    * `helperText` (string, optional): Helper text shown on hover
    * `defaultFieldValue` (string, optional): Default field value
  </Accordion>

  <Accordion title="salesforce/create_custom_field_any">
    **Description:** Deploy custom fields for any object type.

    **Note:** This is a flexible tool for creating custom fields on custom or unknown object types.
  </Accordion>
</AccordionGroup>

### **Advanced Operations**

<AccordionGroup>
  <Accordion title="salesforce/write_soql_query">
    **Description:** Execute custom SOQL queries against your Salesforce data.

    **Parameters:**

    * `query` (string, required): SOQL Query (e.g., "SELECT Id, Name FROM Account WHERE Name = 'Example'")
  </Accordion>

  <Accordion title="salesforce/create_custom_object">
    **Description:** Deploy a new custom object in Salesforce.

    **Parameters:**

    * `label` (string, required): Object Label for tabs, page layouts, and reports
    * `pluralLabel` (string, required): Plural Label (e.g., "Accounts")
    * `description` (string, optional): A description of the Custom Object
    * `recordName` (string, required): Record Name that appears in layouts and searches (e.g., "Account Name")
  </Accordion>

  <Accordion title="salesforce/describe_action_schema">
    **Description:** Get the expected schema for operations on specific object types.

    **Parameters:**

    * `recordType` (string, required): Record Type to describe
    * `operation` (string, required): Operation Type (e.g., "CREATE\_RECORD" or "UPDATE\_RECORD")

    **Note:** Use this function first when working with custom objects to understand their schema before performing operations.
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Salesforce Integration](./1897-setting-up-salesforce-integration.md)

**Next:** [Usage Examples →](./1899-usage-examples.md)
