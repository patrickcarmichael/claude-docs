# Documentation Formatting Script

**Script:** `format_docs.py`
**Purpose:** Convert llms-full.txt files into well-formatted, navigable markdown documentation

---

## Quick Start

```bash
# Format all frameworks
cd /home/user/claude-docs/docs/ai-frameworks
python3 format_docs.py

# Format specific frameworks only
python3 format_docs.py langchain mcp crewai
```

---

## What It Does

The script processes `llms-full.txt` files and creates:

1. **`formatted/documentation.md`** - Complete formatted documentation in one file
2. **`formatted/XX-section.md`** - Individual section files with navigation
3. **`formatted/index.md`** - Navigation hub linking to all formats
4. **Updated README.md** - Adds formatted documentation links

---

## Features

### Content Processing
- ✓ Cleans HTML and converts to markdown
- ✓ Improves markdown formatting (headings, lists, code blocks)
- ✓ Adds language identifiers to code blocks (python, javascript, bash, etc.)
- ✓ Splits content into logical sections
- ✓ Preserves tables, links, and formatting

### Metadata & Structure
- ✓ Adds YAML front matter with title, description, source URL, date
- ✓ Generates table of contents
- ✓ Creates navigation footers
- ✓ Numbers sections for ordering (00-, 01-, 02-, etc.)
- ✓ Creates URL-friendly filenames

### Navigation
- ✓ Index page with links to all sections
- ✓ Previous/Next navigation in each section
- ✓ Links back to original source and other formats
- ✓ Cross-references to full documentation

---

## Output Structure

```
framework/
├── llms-full.txt           # Original (unchanged)
├── chunked/                # Existing (unchanged)
└── formatted/              # NEW - Created by script
    ├── index.md            # Navigation hub
    ├── documentation.md    # Complete formatted doc
    ├── 00-introduction.md  # Section files
    ├── 01-section-name.md
    ├── 02-section-name.md
    └── ...
```

---

## How It Works

### 1. Read Source
```python
# Reads llms-full.txt
content = read_source()
```

### 2. Clean Content
```python
# If HTML: convert to markdown
# If markdown: improve formatting
content = clean_html_content(content)
content = improve_formatting(content)
```

### 3. Split Sections
```python
# Split by H1 and H2 headings
sections = split_into_sections(content)
# Result: [(title, content, filename), ...]
```

### 4. Create Files
```python
# For each section
for title, content, filename in sections:
    # Add front matter
    # Add navigation footer
    # Write to formatted/XX-section.md
```

### 5. Create Index & Documentation
```python
# Create index.md with TOC
# Create documentation.md with all sections
# Update README.md
```

---

## Customization

### Change Output Directory
Edit line ~30:
```python
self.formatted_dir = framework_dir / "formatted"  # Change "formatted"
```

### Modify Front Matter
Edit the `create_frontmatter()` method:
```python
def create_frontmatter(self, title, description, source_url):
    # Add custom fields here
    return f"""---
title: "{title}"
description: "{description}"
source: "{source_url}"
last_updated: "{datetime.now().strftime('%Y-%m-%d')}"
custom_field: "value"  # Add this
---

"""
```

### Change Navigation Footer
Edit the `create_footer_navigation()` method to customize links.

### Add Custom Processing
Edit the `improve_formatting()` method to add custom formatting rules.

---

## Supported Frameworks

Currently configured for:
- LangChain
- LangGraph
- CrewAI
- LlamaIndex
- Haystack
- MCP (Model Context Protocol)

To add new frameworks:
1. Create `framework_name/llms-full.txt`
2. Add framework name to the list in `main()`
3. Run: `python3 format_docs.py framework_name`

---

## Requirements

- Python 3.6 or higher
- No external dependencies (uses stdlib only)
- Write permissions in ai-frameworks directory

---

## Error Handling

The script handles:
- Missing llms-full.txt files (skips with warning)
- HTML vs. markdown content (auto-detects)
- Large files (streaming processing)
- Individual framework errors (continues with others)
- Missing directories (creates as needed)

---

## Performance

| Metric | Value |
|--------|-------|
| Lines processed | ~75,000 |
| Files created | 3,189 |
| Processing time | ~30 seconds |
| Memory usage | Low (streaming) |

---

## Output Quality

### Code Blocks
Automatically detects and adds language identifiers:
- `python` - Detects: import, def, class, print()
- `javascript` - Detects: const, let, var, function, =>
- `bash` - Detects: npm, pip, curl, git, cd
- `json` - Detects: { with :
- `yaml` - Detects: ---, key:

### Headings
- Normalizes heading levels
- Adds proper spacing before/after
- Creates anchor links in TOC

### Tables
- Preserves markdown tables
- Maintains proper formatting
- Handles complex table structures

### Links
- Preserves all hyperlinks
- Creates internal navigation links
- Maintains relative references

---

## Troubleshooting

### Script fails on specific framework
```bash
# Run with just that framework to see detailed error
python3 format_docs.py problematic_framework
```

### Output looks wrong
Check the source file:
```bash
# View first 100 lines of source
head -100 framework/llms-full.txt
```

### Navigation links broken
Verify section file naming:
```bash
# List all section files
ls -1 framework/formatted/*.md
```

### Re-run formatting
Simply run the script again - it will overwrite existing files:
```bash
python3 format_docs.py
```

---

## Examples

### Before (llms-full.txt)
```
<!DOCTYPE html>
<html>
...
<h1>Getting Started</h1>
<p>This is content</p>
...
```

### After (formatted/01-getting-started.md)
```markdown
---
title: "Framework: Getting Started"
description: "Getting Started section"
source: "https://example.com"
last_updated: "2025-11-08"
---

# Getting Started

This is content

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Introduction](./00-introduction.md)
**Next:** [Installation →](./02-installation.md)
```

---

## Extending the Script

### Add Custom Formatters
```python
def custom_formatter(self, content: str) -> str:
    """Add your custom formatting logic."""
    # Example: Add callout boxes
    content = re.sub(
        r'NOTE: (.+)',
        r'> **Note:** \1',
        content
    )
    return content

# Add to improve_formatting() method
def improve_formatting(self, content: str) -> str:
    # ... existing code ...
    content = self.custom_formatter(content)
    return content
```

### Add Custom Section Metadata
```python
# In create_frontmatter()
def create_frontmatter(self, title, description, source_url):
    # Extract keywords from title
    keywords = title.lower().split()[:5]

    return f"""---
title: "{title}"
description: "{description}"
source: "{source_url}"
last_updated: "{datetime.now().strftime('%Y-%m-%d')}"
keywords: {keywords}
---

"""
```

---

## Best Practices

1. **Backup First**: Keep original llms-full.txt files
2. **Test One Framework**: Test changes on one framework first
3. **Review Output**: Check a few formatted files manually
4. **Version Control**: Commit changes incrementally
5. **Re-run As Needed**: Script is idempotent - safe to re-run

---

## Maintenance

### Update All Docs
```bash
# Re-format all frameworks after source updates
python3 format_docs.py
```

### Update Specific Framework
```bash
# Re-format just one framework
python3 format_docs.py langchain
```

### Clean and Rebuild
```bash
# Remove formatted directories
rm -rf */formatted/

# Rebuild all
python3 format_docs.py
```

---

## Contributing

To improve the formatting script:

1. Edit `format_docs.py`
2. Test on all frameworks or specific ones
3. Verify output quality
4. Update this README if adding features
5. Document any new parameters or options

---

## License

Same as parent repository.

---

**Last Updated:** 2025-11-08
**Version:** 1.0
**Author:** Created via Claude Code
