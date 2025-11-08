---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


### Common Issues

**Permission Errors**

* Ensure your Microsoft account has appropriate permissions for Excel and OneDrive/SharePoint
* Verify that the OAuth connection includes required scopes (Files.Read.All, Files.ReadWrite.All)
* Check that you have access to the specific workbooks you're trying to modify

**File ID and Path Issues**

* Verify that file IDs are correct and files exist in your OneDrive or SharePoint
* Ensure file paths are properly formatted when creating new workbooks
* Check that workbook files have the correct .xlsx extension

**Worksheet and Range Issues**

* Verify that worksheet names exist in the specified workbook
* Ensure range addresses are properly formatted (e.g., 'A1:C10')
* Check that ranges don't exceed worksheet boundaries

**Data Format Issues**

* Ensure data values are properly formatted for Excel (strings, numbers, integers)
* Verify that 2D arrays for ranges have consistent row and column counts
* Check that table data includes proper headers when has\_headers is true

**Chart Creation Issues**

* Verify that chart types are supported (ColumnClustered, Line, Pie, etc.)
* Ensure source data ranges contain appropriate data for the chart type
* Check that the source data range exists and contains data

**Table Management Issues**

* Ensure table names are unique within worksheets
* Verify that table ranges don't overlap with existing tables
* Check that new row data matches the table's column structure

**Cell and Range Operations**

* Verify that row and column indices are 0-based for cell operations
* Ensure ranges contain data when using get\_used\_range
* Check that named ranges exist before referencing them

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Microsoft Excel integration setup or troubleshooting.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task for financial modeling](./1807-task-for-financial-modeling.md)

**Next:** [Microsoft OneDrive Integration →](./1809-microsoft-onedrive-integration.md)
