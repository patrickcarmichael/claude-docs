---
title: "Crewai: Available Actions"
description: "Available Actions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Actions


<AccordionGroup>
  <Accordion title="google_sheets/get_spreadsheet">
    **Description:** Retrieve properties and data of a spreadsheet.

    **Parameters:**

    * `spreadsheetId` (string, required): The ID of the spreadsheet to retrieve.
    * `ranges` (array, optional): The ranges to retrieve from the spreadsheet.
    * `includeGridData` (boolean, optional): True if grid data should be returned. Default: false
    * `fields` (string, optional): The fields to include in the response. Use this to improve performance by only returning needed data.
  </Accordion>

  <Accordion title="google_sheets/get_values">
    **Description:** Returns a range of values from a spreadsheet.

    **Parameters:**

    * `spreadsheetId` (string, required): The ID of the spreadsheet to retrieve data from.
    * `range` (string, required): The A1 notation or R1C1 notation of the range to retrieve values from.
    * `valueRenderOption` (string, optional): How values should be represented in the output. Options: FORMATTED\_VALUE, UNFORMATTED\_VALUE, FORMULA. Default: FORMATTED\_VALUE
    * `dateTimeRenderOption` (string, optional): How dates, times, and durations should be represented in the output. Options: SERIAL\_NUMBER, FORMATTED\_STRING. Default: SERIAL\_NUMBER
    * `majorDimension` (string, optional): The major dimension that results should use. Options: ROWS, COLUMNS. Default: ROWS
  </Accordion>

  <Accordion title="google_sheets/update_values">
    **Description:** Sets values in a range of a spreadsheet.

    **Parameters:**

    * `spreadsheetId` (string, required): The ID of the spreadsheet to update.
    * `range` (string, required): The A1 notation of the range to update.
    * `values` (array, required): The data to be written. Each array represents a row.
      ```json  theme={null}
      [
        ["Value1", "Value2", "Value3"],
        ["Value4", "Value5", "Value6"]
      ]
      ```
    * `valueInputOption` (string, optional): How the input data should be interpreted. Options: RAW, USER\_ENTERED. Default: USER\_ENTERED
  </Accordion>

  <Accordion title="google_sheets/append_values">
    **Description:** Appends values to a spreadsheet.

    **Parameters:**

    * `spreadsheetId` (string, required): The ID of the spreadsheet to update.
    * `range` (string, required): The A1 notation of a range to search for a logical table of data.
    * `values` (array, required): The data to append. Each array represents a row.
      ```json  theme={null}
      [
        ["Value1", "Value2", "Value3"],
        ["Value4", "Value5", "Value6"]
      ]
      ```
    * `valueInputOption` (string, optional): How the input data should be interpreted. Options: RAW, USER\_ENTERED. Default: USER\_ENTERED
    * `insertDataOption` (string, optional): How the input data should be inserted. Options: OVERWRITE, INSERT\_ROWS. Default: INSERT\_ROWS
  </Accordion>

  <Accordion title="google_sheets/create_spreadsheet">
    **Description:** Creates a new spreadsheet.

    **Parameters:**

    * `title` (string, required): The title of the new spreadsheet.
    * `sheets` (array, optional): The sheets that are part of the spreadsheet.
      ```json  theme={null}
      [
        {
          "properties": {
            "title": "Sheet1"
          }
        }
      ]
      ```
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Google Sheets Integration](./1725-setting-up-google-sheets-integration.md)

**Next:** [Usage Examples →](./1727-usage-examples.md)
