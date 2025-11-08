#!/usr/bin/env python3
"""
Format llms-full.txt files into well-structured markdown documentation.

This script processes llms-full.txt files from AI framework directories and creates:
- formatted/documentation.md - Complete formatted documentation
- formatted/XX-section.md - Individual section files
- formatted/index.md - Navigation hub
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Tuple, Dict


class DocumentFormatter:
    """Formats documentation from llms-full.txt files."""

    def __init__(self, framework_dir: Path):
        self.framework_dir = framework_dir
        self.framework_name = framework_dir.name.title()
        self.source_file = framework_dir / "llms-full.txt"
        self.formatted_dir = framework_dir / "formatted"
        self.sections: List[Tuple[str, str, str]] = []  # (title, content, filename)

    def read_source(self) -> str:
        """Read the source llms-full.txt file."""
        if not self.source_file.exists():
            raise FileNotFoundError(f"Source file not found: {self.source_file}")

        with open(self.source_file, 'r', encoding='utf-8') as f:
            content = f.read()

        return content

    def extract_source_url(self, content: str) -> str:
        """Extract source URL from content if present."""
        # Look for "Source: URL" pattern at the beginning
        match = re.search(r'^Source:\s*(.+?)$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()

        # Look for canonical URL in HTML
        match = re.search(r'<meta.*?canonical.*?content="(.+?)"', content)
        if match:
            return match.group(1).strip()

        match = re.search(r'<link.*?canonical.*?href="(.+?)"', content)
        if match:
            return match.group(1).strip()

        return f"https://{self.framework_name.lower()}.com"

    def clean_html_content(self, content: str) -> str:
        """Clean HTML content and convert to markdown."""
        if not content.strip().startswith('<!DOCTYPE') and not content.strip().startswith('<html'):
            # Already markdown, just return cleaned version
            return content

        # This is HTML - extract text and convert to basic markdown
        # Remove script tags and content
        content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)

        # Remove style tags and content
        content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)

        # Remove HTML comments
        content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)

        # Extract main content - look for common content containers
        # Try to find article, main, or content div
        patterns = [
            r'<article[^>]*>(.*?)</article>',
            r'<main[^>]*>(.*?)</main>',
            r'<div[^>]*class="[^"]*content[^"]*"[^>]*>(.*?)</div>',
        ]

        for pattern in patterns:
            match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
            if match:
                content = match.group(1)
                break

        # Convert common HTML tags to markdown
        # Headers
        for i in range(6, 0, -1):
            content = re.sub(f'<h{i}[^>]*>(.*?)</h{i}>', f"{'#' * i} \\1\n", content, flags=re.IGNORECASE | re.DOTALL)

        # Paragraphs
        content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', content, flags=re.IGNORECASE | re.DOTALL)

        # Lists
        content = re.sub(r'<ul[^>]*>', '\n', content, flags=re.IGNORECASE)
        content = re.sub(r'</ul>', '\n', content, flags=re.IGNORECASE)
        content = re.sub(r'<ol[^>]*>', '\n', content, flags=re.IGNORECASE)
        content = re.sub(r'</ol>', '\n', content, flags=re.IGNORECASE)
        content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', content, flags=re.IGNORECASE | re.DOTALL)

        # Code blocks
        content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'```\n\1\n```\n', content, flags=re.IGNORECASE | re.DOTALL)
        content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', content, flags=re.IGNORECASE | re.DOTALL)

        # Links
        content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', content, flags=re.IGNORECASE | re.DOTALL)

        # Bold and italic
        content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', content, flags=re.IGNORECASE | re.DOTALL)
        content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', content, flags=re.IGNORECASE | re.DOTALL)
        content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', content, flags=re.IGNORECASE | re.DOTALL)
        content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', content, flags=re.IGNORECASE | re.DOTALL)

        # Remove remaining HTML tags
        content = re.sub(r'<[^>]+>', '', content)

        # Clean up HTML entities
        content = content.replace('&nbsp;', ' ')
        content = content.replace('&lt;', '<')
        content = content.replace('&gt;', '>')
        content = content.replace('&amp;', '&')
        content = content.replace('&quot;', '"')
        content = content.replace('&#39;', "'")

        # Clean up whitespace
        content = re.sub(r'\n{3,}', '\n\n', content)
        content = re.sub(r' +', ' ', content)

        return content.strip()

    def improve_formatting(self, content: str) -> str:
        """Improve markdown formatting."""
        lines = content.split('\n')
        improved = []
        in_code_block = False
        in_table = False
        prev_line_empty = True

        for i, line in enumerate(lines):
            # Track code blocks
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                improved.append(line)
                prev_line_empty = False
                continue

            if in_code_block:
                improved.append(line)
                prev_line_empty = False
                continue

            # Track tables
            if '|' in line and not in_code_block:
                in_table = True
            elif in_table and not '|' in line:
                in_table = False

            # Ensure proper spacing around headings
            if line.startswith('#'):
                # Add space before heading if previous line wasn't empty
                if not prev_line_empty and improved:
                    improved.append('')
                improved.append(line)
                # Add space after heading
                if i + 1 < len(lines) and lines[i + 1].strip():
                    improved.append('')
                prev_line_empty = False
                continue

            # Ensure proper spacing around horizontal rules
            if line.strip() in ['---', '***', '___']:
                if not prev_line_empty and improved:
                    improved.append('')
                improved.append(line)
                improved.append('')
                prev_line_empty = False
                continue

            # Handle empty lines
            if not line.strip():
                if not prev_line_empty:
                    improved.append(line)
                    prev_line_empty = True
                continue

            improved.append(line)
            prev_line_empty = False

        # Join and clean up
        result = '\n'.join(improved)

        # Ensure code blocks have language identifiers where obvious
        result = self.add_code_language_hints(result)

        # Clean up excessive blank lines
        result = re.sub(r'\n{3,}', '\n\n', result)

        return result.strip()

    def add_code_language_hints(self, content: str) -> str:
        """Add language identifiers to code blocks where obvious."""
        lines = content.split('\n')
        result = []

        for i, line in enumerate(lines):
            if line.strip() == '```' and i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                # Detect language
                lang = ''
                if any(x in next_line for x in ['import ', 'from ', 'def ', 'class ', 'print(']):
                    lang = 'python'
                elif any(x in next_line for x in ['const ', 'let ', 'var ', 'function ', '=>', 'import {']):
                    lang = 'javascript'
                elif any(x in next_line for x in ['npm ', 'pip ', 'curl ', 'wget ', 'git ', 'cd ', 'ls ']):
                    lang = 'bash'
                elif next_line.startswith('{') and ':' in next_line:
                    lang = 'json'
                elif next_line.startswith('---') or 'title:' in next_line or 'description:' in next_line:
                    lang = 'yaml'

                if lang:
                    result.append(f'```{lang}')
                else:
                    result.append(line)
            else:
                result.append(line)

        return '\n'.join(result)

    def split_into_sections(self, content: str) -> List[Tuple[str, str, str]]:
        """Split content into sections based on h1 or h2 headings."""
        sections = []

        # Split by h1 or h2 headings
        parts = re.split(r'\n(#{1,2})\s+(.+?)(\n|$)', content)

        if len(parts) <= 1:
            # No clear sections, create a single section
            sections.append(("Overview", content, "01-overview.md"))
            return sections

        # First part is intro (before first heading)
        intro = parts[0].strip()
        if intro:
            sections.append(("Introduction", intro, "00-introduction.md"))

        # Process remaining parts
        section_num = 1
        i = 1
        current_title = ""
        current_content = ""

        while i < len(parts):
            if i + 2 < len(parts) and parts[i] in ['#', '##']:
                # Save previous section if exists
                if current_title and current_content:
                    filename = f"{section_num:02d}-{self._slugify(current_title)}.md"
                    sections.append((current_title, current_content.strip(), filename))
                    section_num += 1

                # Start new section
                heading_level = parts[i]
                current_title = parts[i + 1].strip()
                current_content = heading_level + ' ' + current_title + '\n\n'
                i += 3

                # Collect content until next heading
                while i < len(parts):
                    if parts[i] in ['#', '##']:
                        break
                    current_content += parts[i]
                    i += 1
            else:
                i += 1

        # Add last section
        if current_title and current_content:
            filename = f"{section_num:02d}-{self._slugify(current_title)}.md"
            sections.append((current_title, current_content.strip(), filename))

        # If we didn't get any sections, create one
        if not sections:
            sections.append(("Overview", content, "01-overview.md"))

        return sections

    def _slugify(self, text: str) -> str:
        """Convert text to URL-friendly slug."""
        # Convert to lowercase
        text = text.lower()
        # Replace spaces and special chars with hyphens
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[-\s]+', '-', text)
        # Remove leading/trailing hyphens
        text = text.strip('-')
        # Limit length
        return text[:50]

    def create_frontmatter(self, title: str, description: str, source_url: str) -> str:
        """Create YAML frontmatter."""
        return f"""---
title: "{title}"
description: "{description}"
source: "{source_url}"
last_updated: "{datetime.now().strftime('%Y-%m-%d')}"
---

"""

    def create_footer_navigation(self, current_section: str, all_sections: List[Tuple[str, str, str]]) -> str:
        """Create footer navigation for section files."""
        footer = "\n\n---\n\n"
        footer += "## Navigation\n\n"

        # Links to index, full documentation, and original
        footer += f"- [📑 Back to Index](./index.md)\n"
        footer += f"- [📄 Full Documentation](./documentation.md)\n"
        footer += f"- [📝 Original Source](../llms-full.txt)\n\n"

        # Previous/Next navigation
        current_idx = next((i for i, (_, _, fname) in enumerate(all_sections) if fname == current_section), -1)

        if current_idx > 0:
            prev_title, _, prev_file = all_sections[current_idx - 1]
            footer += f"**Previous:** [← {prev_title}](./{prev_file})\n\n"

        if current_idx < len(all_sections) - 1:
            next_title, _, next_file = all_sections[current_idx + 1]
            footer += f"**Next:** [{next_title} →](./{next_file})\n"

        return footer

    def create_index(self, sections: List[Tuple[str, str, str]], source_url: str) -> str:
        """Create index.md file."""
        content = self.create_frontmatter(
            f"{self.framework_name} Documentation Index",
            f"Navigation hub for {self.framework_name} formatted documentation",
            source_url
        )

        content += f"# {self.framework_name} Documentation\n\n"
        content += f"Welcome to the formatted {self.framework_name} documentation. This documentation is organized into sections for easy navigation.\n\n"

        content += "## Available Formats\n\n"
        content += "- **[📄 Full Documentation](./documentation.md)** - Complete documentation in one file\n"
        content += "- **[📝 Original Source](../llms-full.txt)** - Original llms-full.txt file\n"
        content += "- **[📦 Chunked Version](../chunked/index.md)** - Optimized chunks for LLM context\n\n"

        content += "---\n\n"
        content += "## Documentation Sections\n\n"

        for title, _, filename in sections:
            content += f"### [{title}](./{filename})\n\n"

        content += "---\n\n"
        content += f"*Documentation formatted on {datetime.now().strftime('%Y-%m-%d')}*\n"

        return content

    def process(self) -> Dict[str, int]:
        """Process the documentation and create formatted files."""
        print(f"\n{'='*60}")
        print(f"Processing {self.framework_name}")
        print(f"{'='*60}")

        # Create formatted directory
        self.formatted_dir.mkdir(exist_ok=True)

        # Read and clean content
        print("Reading source file...")
        raw_content = self.read_source()

        # Extract source URL
        source_url = self.extract_source_url(raw_content)
        print(f"Source URL: {source_url}")

        # Clean HTML if needed
        print("Cleaning and formatting content...")
        content = self.clean_html_content(raw_content)

        # Improve formatting
        content = self.improve_formatting(content)

        # Split into sections
        print("Splitting into sections...")
        sections = self.split_into_sections(content)
        print(f"Found {len(sections)} sections")

        # Create full documentation file
        print("Creating documentation.md...")
        full_doc = self.create_frontmatter(
            f"{self.framework_name} Complete Documentation",
            f"Complete formatted documentation for {self.framework_name}",
            source_url
        )

        full_doc += f"# {self.framework_name} Documentation\n\n"

        # Add table of contents
        full_doc += "## Table of Contents\n\n"
        for title, _, filename in sections:
            anchor = self._slugify(title)
            full_doc += f"- [{title}](#{anchor})\n"
        full_doc += "\n---\n\n"

        # Add all sections
        for title, section_content, _ in sections:
            full_doc += section_content + "\n\n---\n\n"

        # Write full documentation
        (self.formatted_dir / "documentation.md").write_text(full_doc, encoding='utf-8')

        # Create individual section files
        print("Creating section files...")
        for title, section_content, filename in sections:
            section_file = self.create_frontmatter(
                f"{self.framework_name}: {title}",
                f"{title} section of {self.framework_name} documentation",
                source_url
            )
            section_file += section_content
            section_file += self.create_footer_navigation(filename, sections)

            (self.formatted_dir / filename).write_text(section_file, encoding='utf-8')
            print(f"  ✓ Created {filename}")

        # Create index file
        print("Creating index.md...")
        index_content = self.create_index(sections, source_url)
        (self.formatted_dir / "index.md").write_text(index_content, encoding='utf-8')

        # Update README.md
        print("Updating README.md...")
        self.update_readme()

        stats = {
            'sections': len(sections),
            'files': len(sections) + 2  # sections + index + documentation
        }

        print(f"\n✓ Successfully processed {self.framework_name}")
        print(f"  - Created {stats['files']} files")
        print(f"  - {stats['sections']} sections")

        return stats

    def update_readme(self):
        """Update the framework's README.md with formatted links."""
        readme_path = self.framework_dir / "README.md"

        if not readme_path.exists():
            # Create a basic README
            content = f"# {self.framework_name}\n\n"
            content += f"## Documentation\n\n"
        else:
            content = readme_path.read_text(encoding='utf-8')

        # Check if formatted link already exists
        if '✨ [Formatted]' not in content:
            # Add formatted link to existing navigation or create new one
            nav_line = "📄 [Full Documentation](./llms-full.txt) | 📑 [Chunked](./chunked/index.md) | ✨ [Formatted](./formatted/index.md)"

            # Try to find and replace existing navigation
            nav_pattern = r'📄 \[Full Documentation\].*?(?:\n|$)'
            if re.search(nav_pattern, content):
                content = re.sub(nav_pattern, nav_line + '\n', content)
            else:
                # Add after first heading
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if line.startswith('#'):
                        lines.insert(i + 1, '\n' + nav_line + '\n')
                        break
                content = '\n'.join(lines)

            readme_path.write_text(content, encoding='utf-8')


def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        # Process specific frameworks
        frameworks = sys.argv[1:]
    else:
        # Process all frameworks
        frameworks = ['langchain', 'langgraph', 'crewai', 'llamaindex', 'haystack', 'mcp']

    base_dir = Path(__file__).parent
    total_stats = {
        'frameworks': 0,
        'sections': 0,
        'files': 0
    }

    print("\n" + "="*60)
    print("AI Framework Documentation Formatter")
    print("="*60)

    for framework in frameworks:
        framework_dir = base_dir / framework

        if not framework_dir.exists():
            print(f"\n⚠ Skipping {framework}: Directory not found")
            continue

        if not (framework_dir / "llms-full.txt").exists():
            print(f"\n⚠ Skipping {framework}: llms-full.txt not found")
            continue

        try:
            formatter = DocumentFormatter(framework_dir)
            stats = formatter.process()

            total_stats['frameworks'] += 1
            total_stats['sections'] += stats['sections']
            total_stats['files'] += stats['files']

        except Exception as e:
            print(f"\n✗ Error processing {framework}: {e}")
            import traceback
            traceback.print_exc()

    # Print summary
    print("\n" + "="*60)
    print("Summary")
    print("="*60)
    print(f"Frameworks processed: {total_stats['frameworks']}")
    print(f"Total sections: {total_stats['sections']}")
    print(f"Total files created: {total_stats['files']}")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
