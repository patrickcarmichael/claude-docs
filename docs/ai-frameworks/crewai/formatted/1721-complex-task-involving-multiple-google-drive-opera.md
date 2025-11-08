---
title: "Crewai: Complex task involving multiple Google Drive operations"
description: "Complex task involving multiple Google Drive operations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Complex task involving multiple Google Drive operations

organization_task = Task(
    description="""
    1. List all files in the shared folder
    2. Create folders for different document types (Reports, Presentations, Spreadsheets)
    3. Move files to appropriate folders based on their type
    4. Set appropriate sharing permissions for each folder
    5. Create a summary document of the organization changes
    """,
    agent=file_organizer,
    expected_output="Files organized into categorized folders with proper permissions and summary report"
)

crew = Crew(
    agents=[file_organizer],
    tasks=[organization_task]
)

crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to upload and share documents](./1720-task-to-upload-and-share-documents.md)

**Next:** [Google Sheets Integration →](./1722-google-sheets-integration.md)
