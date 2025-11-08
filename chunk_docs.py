#!/usr/bin/env python3
"""
Split large llms-full.txt files into manageable chunks with navigation.
"""

import os
import re
from pathlib import Path
from typing import List, Tuple, Dict
from dataclasses import dataclass


@dataclass
class Section:
    title: str
    content: str
    level: int  # 1 for #, 2 for ##
    start_line: int


@dataclass
class Chunk:
    filename: str
    title: str
    content: str
    sections: List[str]


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug."""
    # Remove special characters and convert to lowercase
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def parse_markdown_sections(content: str) -> List[Section]:
    """Parse markdown content and extract sections based on # and ## headers."""
    sections = []
    lines = content.split('\n')

    for i, line in enumerate(lines):
        # Match # or ## headers (but not ###, ####, etc.)
        match = re.match(r'^(#{1,2})\s+(.+)$', line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            sections.append(Section(title=title, content='', level=level, start_line=i))

    # Now extract content for each section
    for i, section in enumerate(sections):
        start = section.start_line
        end = sections[i+1].start_line if i+1 < len(sections) else len(lines)
        section.content = '\n'.join(lines[start:end])

    return sections


def parse_plain_text_sections(content: str) -> List[Section]:
    """Parse plain text with section headers (like haystack/llamaindex format)."""
    sections = []
    lines = content.split('\n')

    # Look for section headers (uppercase lines followed by separator lines)
    for i, line in enumerate(lines):
        # Pattern 1: Lines with === separators (major sections)
        if i > 0 and re.match(r'^={20,}$', line):
            prev_line = lines[i-1].strip()
            if prev_line:
                sections.append(Section(title=prev_line, content='', level=1, start_line=i-1))

    # If no major sections found, try looking for numbered sections or other patterns
    if not sections:
        for i, line in enumerate(lines):
            # Pattern 2: All uppercase headers with sufficient length
            if line.strip() and line.strip().isupper() and len(line.strip()) > 5:
                # Make sure it's not just a separator line
                if not re.match(r'^[=\-\*]+$', line.strip()):
                    sections.append(Section(title=line.strip(), content='', level=1, start_line=i))

    # Extract content for each section
    for i, section in enumerate(sections):
        start = section.start_line
        end = sections[i+1].start_line if i+1 < len(sections) else len(lines)
        section.content = '\n'.join(lines[start:end]).strip()

    # Filter out empty sections
    sections = [s for s in sections if s.content and len(s.content) > 50]

    return sections


def detect_format(content: str) -> str:
    """Detect the format of the content."""
    if content.strip().startswith('<!DOCTYPE html') or content.strip().startswith('<html'):
        return 'html'
    elif re.search(r'^#{1,2}\s+.+$', content[:1000], re.MULTILINE):
        return 'markdown'
    else:
        return 'plaintext'


def split_into_chunks(sections: List[Section], target_size: int = 150000, min_size: int = 50000) -> List[Chunk]:
    """Split sections into logical chunks."""
    chunks = []
    current_chunk_sections = []
    current_size = 0
    chunk_num = 1

    h1_sections = [s for s in sections if s.level == 1]

    # If file is small, split by h2 or group smaller sections
    if sum(len(s.content) for s in sections) < min_size * 2:
        # For small files, create chunks based on major sections
        for section in sections:
            if section.level == 1:
                if current_chunk_sections:
                    # Save previous chunk
                    title = current_chunk_sections[0].title
                    content = '\n\n'.join(s.content for s in current_chunk_sections)
                    chunks.append(Chunk(
                        filename=f"{chunk_num:02d}-{slugify(title)}.md",
                        title=title,
                        content=content,
                        sections=[s.title for s in current_chunk_sections]
                    ))
                    chunk_num += 1
                current_chunk_sections = [section]
                current_size = len(section.content)
            else:
                current_chunk_sections.append(section)
                current_size += len(section.content)

        # Don't forget the last chunk
        if current_chunk_sections:
            title = current_chunk_sections[0].title
            content = '\n\n'.join(s.content for s in current_chunk_sections)
            chunks.append(Chunk(
                filename=f"{chunk_num:02d}-{slugify(title)}.md",
                title=title,
                content=content,
                sections=[s.title for s in current_chunk_sections]
            ))
    else:
        # For large files, split by h1 or target size
        for section in sections:
            if section.level == 1 and current_size > target_size and current_chunk_sections:
                # Save current chunk and start new one
                title = current_chunk_sections[0].title
                content = '\n\n'.join(s.content for s in current_chunk_sections)
                chunks.append(Chunk(
                    filename=f"{chunk_num:02d}-{slugify(title)}.md",
                    title=title,
                    content=content,
                    sections=[s.title for s in current_chunk_sections]
                ))
                chunk_num += 1
                current_chunk_sections = [section]
                current_size = len(section.content)
            else:
                current_chunk_sections.append(section)
                current_size += len(section.content)

        # Don't forget the last chunk
        if current_chunk_sections:
            title = current_chunk_sections[0].title
            content = '\n\n'.join(s.content for s in current_chunk_sections)
            chunks.append(Chunk(
                filename=f"{chunk_num:02d}-{slugify(title)}.md",
                title=title,
                content=content,
                sections=[s.title for s in current_chunk_sections]
            ))

    return chunks


def create_chunk_file(chunk: Chunk, chunk_idx: int, total_chunks: int, prev_filename: str = None, next_filename: str = None) -> str:
    """Create content for a chunk file with navigation."""
    prev_link = f"[← Previous](./{prev_filename})" if prev_filename else ""
    next_link = f"[Next →](./{next_filename})" if next_filename else ""

    nav_parts = [p for p in [prev_link, "[Index](./index.md)", next_link] if p or p == "[Index](./index.md)"]
    navigation = " | ".join(nav_parts)

    content = f"""# {chunk.title}

**Navigation:** {navigation}

---

{chunk.content}

---

**Navigation:** {navigation}
"""
    return content


def create_index(chunks: List[Chunk], framework_name: str) -> str:
    """Create index.md file content."""
    toc_items = []
    for i, chunk in enumerate(chunks):
        toc_items.append(f"{i+1}. [{chunk.title}](./{chunk.filename})")
        # Add subsections if available
        if len(chunk.sections) > 1:
            for section in chunk.sections[1:]:
                toc_items.append(f"   - {section}")

    toc = '\n'.join(toc_items)

    content = f"""# {framework_name} Documentation - Chunked Version

This is the chunked version of the {framework_name} documentation for easier navigation and reading.

## Table of Contents

{toc}

---

[← Back to {framework_name} README](../README.md)
"""
    return content


def process_framework(framework_path: Path, framework_name: str):
    """Process a single framework's documentation."""
    print(f"\nProcessing {framework_name}...")

    # Read the full documentation file
    full_doc_path = framework_path / 'llms-full.txt'
    if not full_doc_path.exists():
        print(f"  ⚠ Warning: {full_doc_path} not found, skipping...")
        return None

    with open(full_doc_path, 'r', encoding='utf-8') as f:
        content = f.read()

    file_size = len(content)
    print(f"  File size: {file_size / 1024:.1f} KB")

    # Detect format and parse sections
    fmt = detect_format(content)
    print(f"  Format detected: {fmt}")

    if fmt == 'html':
        print(f"  ⚠ Warning: HTML format detected, treating as single chunk")
        # For HTML, we'll just create a simple reference
        sections = [Section(title=f"{framework_name} Documentation", content=content, level=1, start_line=0)]
    elif fmt == 'markdown':
        sections = parse_markdown_sections(content)
    else:
        sections = parse_plain_text_sections(content)

    print(f"  Sections found: {len(sections)}")

    if not sections:
        print(f"  ⚠ Warning: No sections found, creating single chunk")
        sections = [Section(title=f"{framework_name} Documentation", content=content, level=1, start_line=0)]

    # Split into chunks
    chunks = split_into_chunks(sections)
    print(f"  Chunks created: {len(chunks)}")

    # Create chunked directory
    chunked_dir = framework_path / 'chunked'
    chunked_dir.mkdir(exist_ok=True)

    # Write chunk files with proper navigation
    for i, chunk in enumerate(chunks):
        prev_filename = chunks[i-1].filename if i > 0 else None
        next_filename = chunks[i+1].filename if i < len(chunks) - 1 else None
        chunk_content = create_chunk_file(chunk, i, len(chunks), prev_filename, next_filename)
        chunk_path = chunked_dir / chunk.filename
        with open(chunk_path, 'w', encoding='utf-8') as f:
            f.write(chunk_content)
        print(f"    Created: {chunk.filename}")

    # Create index file
    index_content = create_index(chunks, framework_name)
    index_path = chunked_dir / 'index.md'
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    print(f"    Created: index.md")

    return len(chunks)


def main():
    """Main function to process all frameworks."""
    frameworks = {
        'langchain': 'LangChain',
        'langgraph': 'LangGraph',
        'crewai': 'CrewAI',
        'llamaindex': 'LlamaIndex',
        'haystack': 'Haystack',
        'mcp': 'Model Context Protocol (MCP)',
    }

    base_path = Path('/home/user/claude-docs/docs/ai-frameworks')
    results = {}

    print("=" * 60)
    print("Documentation Chunking Tool")
    print("=" * 60)

    for folder, name in frameworks.items():
        framework_path = base_path / folder
        chunk_count = process_framework(framework_path, name)
        if chunk_count:
            results[name] = chunk_count

    # Print summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    total_chunks = sum(results.values())
    for name, count in results.items():
        print(f"  {name}: {count} chunks")
    print(f"\n  TOTAL: {total_chunks} chunks created")
    print("=" * 60)


if __name__ == '__main__':
    main()
