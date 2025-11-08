---
title: "Crewai: Available Actions"
description: "Available Actions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Actions


<AccordionGroup>
  <Accordion title="microsoft_excel/create_workbook">
    **Description:** Create a new Excel workbook in OneDrive or SharePoint.

    **Parameters:**

    * `file_path` (string, required): Path where to create the workbook (e.g., 'MyWorkbook.xlsx')
    * `worksheets` (array, optional): Initial worksheets to create
      ```json  theme={null}
      [
        {
          "name": "Sheet1"
        },
        {
          "name": "Data"
        }
      ]
      ```
  </Accordion>

  <Accordion title="microsoft_excel/get_workbooks">
    **Description:** Get all Excel workbooks from OneDrive or SharePoint.

    **Parameters:**

    * `select` (string, optional): Select specific properties to return
    * `filter` (string, optional): Filter results using OData syntax
    * `expand` (string, optional): Expand related resources inline
    * `top` (integer, optional): Number of items to return. Minimum: 1, Maximum: 999
    * `orderby` (string, optional): Order results by specified properties
  </Accordion>

  <Accordion title="microsoft_excel/get_worksheets">
    **Description:** Get all worksheets in an Excel workbook.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `select` (string, optional): Select specific properties to return (e.g., 'id,name,position')
    * `filter` (string, optional): Filter results using OData syntax
    * `expand` (string, optional): Expand related resources inline
    * `top` (integer, optional): Number of items to return. Minimum: 1, Maximum: 999
    * `orderby` (string, optional): Order results by specified properties
  </Accordion>

  <Accordion title="microsoft_excel/create_worksheet">
    **Description:** Create a new worksheet in an Excel workbook.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `name` (string, required): Name of the new worksheet
  </Accordion>

  <Accordion title="microsoft_excel/get_range_data">
    **Description:** Get data from a specific range in an Excel worksheet.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `range` (string, required): Range address (e.g., 'A1:C10')
  </Accordion>

  <Accordion title="microsoft_excel/update_range_data">
    **Description:** Update data in a specific range in an Excel worksheet.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `range` (string, required): Range address (e.g., 'A1:C10')
    * `values` (array, required): 2D array of values to set in the range
      ```json  theme={null}
      [
        ["Name", "Age", "City"],
        ["John", 30, "New York"],
        ["Jane", 25, "Los Angeles"]
      ]
      ```
  </Accordion>

  <Accordion title="microsoft_excel/add_table">
    **Description:** Create a table in an Excel worksheet.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `range` (string, required): Range for the table (e.g., 'A1:D10')
    * `has_headers` (boolean, optional): Whether the first row contains headers. Default: true
  </Accordion>

  <Accordion title="microsoft_excel/get_tables">
    **Description:** Get all tables in an Excel worksheet.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
  </Accordion>

  <Accordion title="microsoft_excel/add_table_row">
    **Description:** Add a new row to an Excel table.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `table_name` (string, required): Name of the table
    * `values` (array, required): Array of values for the new row
      ```json  theme={null}
      ["John Doe", 35, "Manager", "Sales"]
      ```
  </Accordion>

  <Accordion title="microsoft_excel/create_chart">
    **Description:** Create a chart in an Excel worksheet.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `chart_type` (string, required): Type of chart (e.g., 'ColumnClustered', 'Line', 'Pie')
    * `source_data` (string, required): Range of data for the chart (e.g., 'A1:B10')
    * `series_by` (string, optional): How to interpret the data ('Auto', 'Columns', or 'Rows'). Default: Auto
  </Accordion>

  <Accordion title="microsoft_excel/get_cell">
    **Description:** Get the value of a single cell in an Excel worksheet.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `row` (integer, required): Row number (0-based)
    * `column` (integer, required): Column number (0-based)
  </Accordion>

  <Accordion title="microsoft_excel/get_used_range">
    **Description:** Get the used range of an Excel worksheet (contains all data).

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
  </Accordion>

  <Accordion title="microsoft_excel/list_charts">
    **Description:** Get all charts in an Excel worksheet.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
  </Accordion>

  <Accordion title="microsoft_excel/delete_worksheet">
    **Description:** Delete a worksheet from an Excel workbook.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet to delete
  </Accordion>

  <Accordion title="microsoft_excel/delete_table">
    **Description:** Delete a table from an Excel worksheet.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
    * `worksheet_name` (string, required): Name of the worksheet
    * `table_name` (string, required): Name of the table to delete
  </Accordion>

  <Accordion title="microsoft_excel/list_names">
    **Description:** Get all named ranges in an Excel workbook.

    **Parameters:**

    * `file_id` (string, required): The ID of the Excel file
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Microsoft Excel Integration](./1797-setting-up-microsoft-excel-integration.md)

**Next:** [Usage Examples →](./1799-usage-examples.md)
