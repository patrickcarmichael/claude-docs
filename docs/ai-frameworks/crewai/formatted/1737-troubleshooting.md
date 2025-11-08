---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


### Common Issues

**Permission Errors**

* Ensure your Google account has edit access to the target spreadsheets
* Verify that the OAuth connection includes required scopes for Google Sheets API
* Check that spreadsheets are shared with the authenticated account

**Spreadsheet Structure Issues**

* Ensure worksheets have proper column headers before creating or updating rows
* Verify that range notation (A1 format) is correct for the target cells
* Check that the specified spreadsheet ID exists and is accessible

**Data Type and Format Issues**

* Ensure data values match the expected format for each column
* Use proper date formats for date columns (ISO format recommended)
* Verify that numeric values are properly formatted for number columns

**Range and Cell Reference Issues**

* Use proper A1 notation for ranges (e.g., "A1:C10", "Sheet1!A1:B5")
* Ensure range references don't exceed the actual spreadsheet dimensions
* Verify that sheet names in range references match actual sheet names

**Value Input and Rendering Options**

* Choose appropriate `valueInputOption` (RAW vs USER\_ENTERED) for your data
* Select proper `valueRenderOption` based on how you want data formatted
* Consider `dateTimeRenderOption` for consistent date/time handling

**Spreadsheet Creation Issues**

* Ensure spreadsheet titles are unique and follow naming conventions
* Verify that sheet properties are properly structured when creating sheets
* Check that you have permissions to create new spreadsheets in your account

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Google Sheets integration setup or troubleshooting.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Complex workflow task](./1736-complex-workflow-task.md)

**Next:** [Google Slides Integration →](./1738-google-slides-integration.md)
