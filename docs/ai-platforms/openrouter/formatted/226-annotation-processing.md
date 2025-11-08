---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Annotation Processing

Extract and process citation information:
```typescript title="TypeScript"
  function extractCitations(response: any) {
    const messageOutput = response.output?.find((o: any) => o.type === 'message');
    const textContent = messageOutput?.content?.find((c: any) => c.type === 'output_text');
    const annotations = textContent?.annotations || [];

    return annotations
      .filter((annotation: any) => annotation.type === 'url_citation')
      .map((annotation: any) => ({
        url: annotation.url,
        text: textContent.text.slice(annotation.start_index, annotation.end_index),
        startIndex: annotation.start_index,
        endIndex: annotation.end_index,
      }));
  }

  const result = await response.json();
  const citations = extractCitations(result);
  console.log('Found citations:', citations);
```
```python title="Python"
  def extract_citations(response_data):
      output = response_data.get('output', [])
      message_output = next((o for o in output if o.get('type') == 'message'), {})
      content = message_output.get('content', [])
      text_content = next((c for c in content if c.get('type') == 'output_text'), {})
      annotations = text_content.get('annotations', [])
      text = text_content.get('text', '')

      citations = []
      for annotation in annotations:
          if annotation.get('type') == 'url_citation':
              citations.append({
                  'url': annotation.get('url'),
                  'text': text[annotation.get('start_index', 0):annotation.get('end_index', 0)],
                  'start_index': annotation.get('start_index'),
                  'end_index': annotation.get('end_index'),
              })

      return citations

  result = response.json()
  citations = extract_citations(result)
  print(f'Found citations: {citations}')
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
