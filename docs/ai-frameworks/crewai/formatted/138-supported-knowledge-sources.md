---
title: "Crewai: Supported Knowledge Sources"
description: "Supported Knowledge Sources section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Supported Knowledge Sources


CrewAI supports various types of knowledge sources out of the box:

<CardGroup cols={2}>
  <Card title="Text Sources" icon="text">
    * Raw strings
    * Text files (.txt)
    * PDF documents
  </Card>

  <Card title="Structured Data" icon="table">
    * CSV files
    * Excel spreadsheets
    * JSON documents
  </Card>
</CardGroup>

### Text File Knowledge Source

```python  theme={null}
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource

text_source = TextFileKnowledgeSource(
    file_paths=["document.txt", "another.txt"]
)
```

### PDF Knowledge Source

```python  theme={null}
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

pdf_source = PDFKnowledgeSource(
    file_paths=["document.pdf", "another.pdf"]
)
```

### CSV Knowledge Source

```python  theme={null}
from crewai.knowledge.source.csv_knowledge_source import CSVKnowledgeSource

csv_source = CSVKnowledgeSource(
    file_paths=["data.csv"]
)
```

### Excel Knowledge Source

```python  theme={null}
from crewai.knowledge.source.excel_knowledge_source import ExcelKnowledgeSource

excel_source = ExcelKnowledgeSource(
    file_paths=["spreadsheet.xlsx"]
)
```

### JSON Knowledge Source

```python  theme={null}
from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource

json_source = JSONKnowledgeSource(
    file_paths=["data.json"]
)
```

<Note>
  Please ensure that you create the ./knowledge folder. All source files (e.g., .txt, .pdf, .xlsx, .json) should be placed in this folder for centralized management.
</Note>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with the knowledge store](./137-create-an-agent-with-the-knowledge-store.md)

**Next:** [Agent vs Crew Knowledge: Complete Guide →](./139-agent-vs-crew-knowledge-complete-guide.md)
