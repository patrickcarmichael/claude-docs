#!/usr/bin/env python3
"""
Markdown Formatter for AI Platform Documentation

This script formats llms-full.txt files into clean, well-structured markdown
with proper hierarchy, code blocks, and navigation.
"""

import re
import os
from pathlib import Path
from typing import List, Dict, Tuple
from datetime import date


class MarkdownFormatter:
    """Format and organize markdown documentation."""

    def __init__(self, platform_name: str):
        self.platform_name = platform_name
        self.sections = []
        self.current_section = None

    def parse_file(self, file_path: str) -> str:
        """Read and parse the llms-full.txt file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()

    def detect_language(self, code_block: str) -> str:
        """Detect programming language from code block content."""
        code_lower = code_block.lower().strip()

        # Check for specific language markers
        if 'import anthropic' in code_lower or 'from anthropic' in code_lower:
            return 'python'
        elif 'def ' in code_lower or 'print(' in code_lower:
            return 'python'
        elif 'const ' in code_lower or 'let ' in code_lower or '=>' in code_lower:
            return 'javascript'
        elif 'import ' in code_lower and "'" in code_lower:
            return 'typescript'
        elif 'curl ' in code_lower or code_lower.startswith('curl'):
            return 'bash'
        elif code_lower.startswith('http') or code_lower.startswith('post') or code_lower.startswith('get'):
            return 'http'
        elif code_lower.startswith('{') or code_lower.startswith('['):
            return 'json'
        elif '<?php' in code_lower:
            return 'php'
        elif 'package main' in code_lower or 'func ' in code_lower:
            return 'go'
        elif 'public class' in code_lower or 'public static' in code_lower:
            return 'java'
        elif 'namespace' in code_lower or 'using System' in code_lower:
            return 'csharp'
        elif 'export ' in code_lower or 'interface ' in code_lower:
            return 'typescript'

        return ''

    def clean_code_blocks(self, content: str) -> str:
        """Clean and properly format code blocks."""
        # First pass: Remove language labels with theme annotations (case insensitive)
        # e.g., "```typescript TypeScript theme={null}" -> "```typescript"
        # e.g., "```curl cURL theme={null}" -> "```bash"
        content = re.sub(
            r'```(\w+)\s+\w+\s+theme=\{[^}]*\}',
            r'```\1',
            content,
            flags=re.IGNORECASE
        )

        # Second pass: Remove standalone theme annotations
        # e.g., "```http  theme={null}" -> "```http"
        content = re.sub(
            r'```(\w+)?\s*theme=\{[^}]*\}',
            r'```\1',
            content
        )

        # Third pass: Clean up curl -> bash
        content = re.sub(r'```curl\b', r'```bash', content, flags=re.IGNORECASE)

        # Third pass: Match and clean code blocks
        pattern = r'```(\w+)?\s*\n(.*?)```'

        def replace_code_block(match):
            lang = match.group(1) or ''
            code = match.group(2)

            # Auto-detect language if not specified
            if not lang:
                lang = self.detect_language(code)

            # Clean common language aliases
            lang_map = {
                'typescript': 'typescript',
                'python': 'python',
                'curl': 'bash',
                'http': 'http',
                'json': 'json',
                'javascript': 'javascript',
                'js': 'javascript',
                'ts': 'typescript',
                'sh': 'bash',
                'shell': 'bash',
                'csharp': 'csharp',
                'java': 'java',
                'go': 'go',
                'php': 'php',
                'ruby': 'ruby',
                'rust': 'rust'
            }
            lang = lang_map.get(lang.lower(), lang) if lang else ''

            return f'```{lang}\n{code}```'

        return re.sub(pattern, replace_code_block, content, flags=re.DOTALL)

    def convert_special_tags(self, content: str) -> str:
        """Convert special HTML-like tags to markdown."""
        # Convert <Info>, <Warning>, <Note> tags to blockquotes
        content = re.sub(
            r'<Info>\s*(.*?)\s*</Info>',
            r'> **ℹ️ Info**\n>\n> \1',
            content,
            flags=re.DOTALL | re.IGNORECASE
        )

        content = re.sub(
            r'<Warning>\s*(.*?)\s*</Warning>',
            r'> **⚠️ Warning**\n>\n> \1',
            content,
            flags=re.DOTALL | re.IGNORECASE
        )

        content = re.sub(
            r'<Note>\s*(.*?)\s*</Note>',
            r'> **📝 Note**\n>\n> \1',
            content,
            flags=re.DOTALL | re.IGNORECASE
        )

        # Remove <CodeGroup> tags
        content = re.sub(r'<CodeGroup>\s*', '', content, flags=re.IGNORECASE)
        content = re.sub(r'\s*</CodeGroup>', '', content, flags=re.IGNORECASE)

        # Fix indented code blocks (often from CodeGroup sections)
        # Remove leading whitespace from code block markers
        content = re.sub(r'\n\s+(```)', r'\n\1', content)

        return content

    def fix_lists(self, content: str) -> str:
        """Fix list formatting and indentation."""
        lines = content.split('\n')
        fixed_lines = []
        in_blockquote = False

        for i, line in enumerate(lines):
            # Check if we're in a blockquote
            if line.strip().startswith('>'):
                in_blockquote = True
                # Fix list items in blockquotes
                if '*' in line or '-' in line:
                    # Ensure proper spacing after >
                    line = re.sub(r'>\s*\*', r'>   *', line)
                    line = re.sub(r'>\s*-', r'>   -', line)
            elif in_blockquote and not line.strip().startswith('>'):
                in_blockquote = False

            fixed_lines.append(line)

        return '\n'.join(fixed_lines)

    def fix_heading_hierarchy(self, content: str) -> str:
        """Ensure proper heading hierarchy with single H1."""
        lines = content.split('\n')
        fixed_lines = []
        h1_count = 0

        for line in lines:
            # Count heading level
            if line.startswith('#'):
                level = len(line) - len(line.lstrip('#'))

                # If we find an H1 after the first one, demote it to H2
                if level == 1:
                    h1_count += 1
                    if h1_count > 1:
                        line = '#' + line

            fixed_lines.append(line)

        return '\n'.join(fixed_lines)

    def add_spacing(self, content: str) -> str:
        """Ensure proper spacing between sections."""
        # Add blank line before headings (if not already there)
        content = re.sub(r'([^\n])\n(#{1,6} )', r'\1\n\n\2', content)

        # Add blank line after headings (if not already there)
        content = re.sub(r'(#{1,6} [^\n]+)\n([^\n#])', r'\1\n\n\2', content)

        # Remove excessive blank lines (more than 2)
        content = re.sub(r'\n{4,}', '\n\n\n', content)

        return content

    def add_front_matter(self, content: str, platform_name: str) -> str:
        """Add YAML front matter to the content."""
        today = date.today().strftime("%Y-%m-%d")

        # Extract title from first H1 if exists
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        if title_match:
            title = title_match.group(1)
        else:
            title = f"{platform_name} Documentation"

        front_matter = f"""---
title: "{title}"
description: "Formatted documentation for {platform_name}"
source: "llms-full.txt"
last_updated: "{today}"
---

"""
        return front_matter + content

    def split_into_sections(self, content: str) -> List[Dict[str, str]]:
        """Split content into logical sections based on H1 and H2 headings."""
        sections = []
        current_section = {
            'title': '',
            'content': [],
            'filename': '',
            'level': 0
        }

        lines = content.split('\n')
        section_number = 1

        # Skip front matter if present
        in_front_matter = False
        content_start = 0
        for i, line in enumerate(lines):
            if i == 0 and line == '---':
                in_front_matter = True
            elif in_front_matter and line == '---':
                in_front_matter = False
                content_start = i + 1
                break

        for i in range(content_start, len(lines)):
            line = lines[i]

            # Check for H1 or H2 headers
            if line.startswith('# ') or line.startswith('## '):
                # Save previous section if it has content
                if current_section['content']:
                    sections.append(current_section.copy())

                # Start new section
                level = 2 if line.startswith('## ') else 1
                title = line.lstrip('#').strip()

                # Create filename from title
                filename = re.sub(r'[^\w\s-]', '', title.lower())
                filename = re.sub(r'[-\s]+', '-', filename)

                # Limit filename length (max 200 chars total, leaving room for number and extension)
                max_name_length = 190
                if len(filename) > max_name_length:
                    filename = filename[:max_name_length].rstrip('-')

                filename = f"{section_number:02d}-{filename}.md"

                current_section = {
                    'title': title,
                    'content': [line],
                    'filename': filename,
                    'level': level
                }
                section_number += 1
            else:
                current_section['content'].append(line)

        # Add the last section
        if current_section['content']:
            sections.append(current_section)

        return sections

    def add_navigation(self, content: str, platform_name: str) -> str:
        """Add navigation footer to section files."""
        nav = f"""
---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
"""
        return content + nav

    def format_content(self, content: str) -> str:
        """Apply all formatting transformations."""
        content = self.clean_code_blocks(content)
        content = self.convert_special_tags(content)
        content = self.fix_lists(content)
        content = self.fix_heading_hierarchy(content)
        content = self.add_spacing(content)
        return content

    def create_index(self, sections: List[Dict[str, str]], platform_name: str) -> str:
        """Create an index file for the formatted documentation."""
        today = date.today().strftime("%Y-%m-%d")

        index = f"""---
title: "{platform_name} Documentation Index"
description: "Organized documentation for {platform_name}"
last_updated: "{today}"
---

# {platform_name} Documentation

Formatted and organized documentation for easy reading.

## 📖 Reading Options

- **[Complete Documentation](./documentation.md)** - Single formatted file with all content
- **Organized Sections** - Browse by topic:
"""

        for section in sections:
            index += f"  - [{section['title']}](./{section['filename']})\n"

        index += f"""
## 🔗 Other Formats

- **[Original llms-full.txt](../llms-full.txt)** - AI-optimized plain text
- **[Chunked Version](../chunked/index.md)** - Manageable chunks with navigation (if available)

---

*Last updated: {today}*
"""

        return index

    def process_platform(self, input_file: str, output_dir: str):
        """Process a platform's llms-full.txt file."""
        print(f"Processing {self.platform_name}...")

        # Read and format content
        raw_content = self.parse_file(input_file)
        formatted_content = self.format_content(raw_content)
        formatted_with_fm = self.add_front_matter(formatted_content, self.platform_name)

        # Create output directory
        os.makedirs(output_dir, exist_ok=True)

        # Write complete formatted file
        complete_file = os.path.join(output_dir, 'documentation.md')
        with open(complete_file, 'w', encoding='utf-8') as f:
            f.write(formatted_with_fm)
        print(f"  ✓ Created {complete_file}")

        # Split into sections
        sections = self.split_into_sections(formatted_content)

        # Write section files
        section_files = []
        for section in sections:
            section_content = '\n'.join(section['content'])
            section_with_fm = self.add_front_matter(section_content, self.platform_name)
            section_with_nav = self.add_navigation(section_with_fm, self.platform_name)

            section_file = os.path.join(output_dir, section['filename'])
            with open(section_file, 'w', encoding='utf-8') as f:
                f.write(section_with_nav)
            section_files.append(section_file)
            print(f"  ✓ Created {section_file}")

        # Create index file
        index_content = self.create_index(sections, self.platform_name)
        index_file = os.path.join(output_dir, 'index.md')
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(index_content)
        print(f"  ✓ Created {index_file}")

        return {
            'complete_file': complete_file,
            'section_files': section_files,
            'index_file': index_file,
            'total_sections': len(sections)
        }


def update_readme(readme_path: str, platform_name: str):
    """Update platform README with link to formatted docs."""
    if not os.path.exists(readme_path):
        print(f"  ⚠️  README not found at {readme_path}")
        return

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if formatted link already exists
    if '✨ [Formatted]' in content:
        print(f"  ℹ️  README already has formatted link")
        return

    # Find the first heading and add links below it
    lines = content.split('\n')
    updated_lines = []
    added = False

    for i, line in enumerate(lines):
        updated_lines.append(line)

        # Add links after the first H1 heading
        if not added and line.startswith('# '):
            updated_lines.append('')
            updated_lines.append('📄 [Full Documentation](./llms-full.txt) | 📑 [Chunked](./chunked/index.md) | ✨ [Formatted](./formatted/index.md)')
            updated_lines.append('')
            added = True

    if added:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(updated_lines))
        print(f"  ✓ Updated README with formatted docs link")


def main():
    """Main function to process all platforms."""
    platforms = {
        'Anthropic': '/home/user/claude-docs/docs/ai-platforms/anthropic',
        'Cohere': '/home/user/claude-docs/docs/ai-platforms/cohere',
        'Fireworks': '/home/user/claude-docs/docs/ai-platforms/fireworks',
        'Google Gemini': '/home/user/claude-docs/docs/ai-platforms/google-gemini',
        'OpenRouter': '/home/user/claude-docs/docs/ai-platforms/openrouter',
        'Together AI': '/home/user/claude-docs/docs/ai-platforms/together-ai'
    }

    total_files = 0
    results = {}

    print("=" * 60)
    print("Markdown Formatter for AI Platform Documentation")
    print("=" * 60)
    print()

    for platform_name, platform_dir in platforms.items():
        input_file = os.path.join(platform_dir, 'llms-full.txt')
        output_dir = os.path.join(platform_dir, 'formatted')
        readme_path = os.path.join(platform_dir, 'README.md')

        if not os.path.exists(input_file):
            print(f"⚠️  Skipping {platform_name} - llms-full.txt not found")
            continue

        formatter = MarkdownFormatter(platform_name)
        result = formatter.process_platform(input_file, output_dir)

        # Update README
        update_readme(readme_path, platform_name)

        results[platform_name] = result
        total_files += 1 + len(result['section_files']) + 1  # complete + sections + index
        print()

    # Print summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Platforms processed: {len(results)}")
    print(f"Total files created: {total_files}")
    print()

    for platform_name, result in results.items():
        print(f"{platform_name}:")
        print(f"  - Complete documentation: 1 file")
        print(f"  - Section files: {result['total_sections']} files")
        print(f"  - Index: 1 file")
        print(f"  - Total: {result['total_sections'] + 2} files")
        print()


if __name__ == '__main__':
    main()
