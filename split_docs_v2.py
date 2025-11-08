#!/usr/bin/env python3
"""
Script to split large llms-full.txt files into manageable chunks with navigation.
Version 2: Better chunking logic that groups sections by size, not just by H1.
"""

import os
import re
from pathlib import Path
from typing import List, Tuple

class DocSplitter:
    def __init__(self, file_path: str, target_chunk_size: int):
        self.file_path = Path(file_path)
        self.target_chunk_size = target_chunk_size
        self.service_dir = self.file_path.parent
        self.chunked_dir = self.service_dir / "chunked"

    def read_file(self) -> str:
        """Read the entire file."""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.read()

    def parse_sections(self, content: str) -> List[Tuple[int, str, str, int]]:
        """
        Parse sections based on # and ## headers.
        Returns list of (level, title, content, byte_size) tuples.
        """
        sections = []
        lines = content.split('\n')
        current_section = None
        current_lines = []
        current_title = ""
        current_level = 0

        for i, line in enumerate(lines):
            # Check if this is a header
            h1_match = re.match(r'^# (.+)$', line)
            h2_match = re.match(r'^## (.+)$', line)

            if h1_match or h2_match:
                # Save previous section if it exists
                if current_section is not None:
                    section_content = '\n'.join(current_lines)
                    sections.append((
                        current_level,
                        current_title,
                        section_content,
                        len(section_content.encode('utf-8'))
                    ))

                # Start new section
                if h1_match:
                    current_level = 1
                    current_title = h1_match.group(1)
                else:
                    current_level = 2
                    current_title = h2_match.group(1)

                current_section = i
                current_lines = [line]
            else:
                current_lines.append(line)

        # Add final section
        if current_section is not None:
            section_content = '\n'.join(current_lines)
            sections.append((
                current_level,
                current_title,
                section_content,
                len(section_content.encode('utf-8'))
            ))

        return sections

    def create_chunks(self, sections: List[Tuple[int, str, str, int]]) -> List[Tuple[str, str, str, List[str]]]:
        """
        Group sections into chunks based on target size.
        Combines multiple sections until target size is reached.
        """
        chunks = []
        current_chunk_content = []
        current_chunk_size = 0
        current_chunk_sections = []
        current_chunk_title = None

        for level, title, content, size in sections:
            # Check if adding this section would exceed target
            would_exceed = current_chunk_size + size > self.target_chunk_size
            has_content = len(current_chunk_content) > 0

            # Start new chunk if:
            # 1. We would exceed target size AND we already have content
            # 2. This is a major H1 section AND we would significantly exceed size
            should_start_new = (
                (would_exceed and has_content) or
                (level == 1 and has_content and current_chunk_size > self.target_chunk_size * 0.5)
            )

            if should_start_new:
                # Save current chunk
                if current_chunk_title:
                    chunk_name = self.sanitize_filename(current_chunk_title)
                    chunks.append((
                        chunk_name,
                        current_chunk_title,
                        '\n\n'.join(current_chunk_content),
                        current_chunk_sections.copy()
                    ))
                
                # Start new chunk
                current_chunk_content = []
                current_chunk_size = 0
                current_chunk_sections = []
                current_chunk_title = None

            # Set chunk title if not set (use first H1 or first section)
            if current_chunk_title is None:
                if level == 1:
                    current_chunk_title = title
                elif not current_chunk_title:
                    current_chunk_title = title

            # Add section to current chunk
            current_chunk_content.append(content)
            current_chunk_size += size
            current_chunk_sections.append(title)

        # Add final chunk
        if current_chunk_content and current_chunk_title:
            chunk_name = self.sanitize_filename(current_chunk_title)
            chunks.append((
                chunk_name,
                current_chunk_title,
                '\n\n'.join(current_chunk_content),
                current_chunk_sections
            ))

        return chunks

    def sanitize_filename(self, title: str) -> str:
        """Convert title to a safe filename."""
        # Remove special characters and replace spaces with hyphens
        filename = re.sub(r'[^\w\s-]', '', title.lower())
        filename = re.sub(r'[-\s]+', '-', filename)
        filename = filename.strip('-')
        # Limit length
        return filename[:50]

    def write_chunks(self, chunks: List[Tuple[str, str, str, List[str]]]) -> Tuple[int, List]:
        """Write chunk files with navigation."""
        # Create chunked directory
        self.chunked_dir.mkdir(exist_ok=True)

        # Clean up previous chunk files
        for f in self.chunked_dir.glob("*.md"):
            if f.name != "index.md":
                f.unlink()

        chunk_files = []

        for idx, (chunk_name, chunk_title, content, sections) in enumerate(chunks):
            # Create filename
            filename = f"{idx + 1:02d}-{chunk_name}.md"
            filepath = self.chunked_dir / filename
            chunk_files.append((filename, chunk_title, sections))

            # Create navigation
            nav_parts = []
            if idx > 0:
                prev_name = chunks[idx - 1][0]
                nav_parts.append(f"[← Previous](./{idx:02d}-{prev_name}.md)")
            else:
                nav_parts.append("← Previous")

            nav_parts.append("[Index](./index.md)")

            if idx < len(chunks) - 1:
                next_name = chunks[idx + 1][0]
                nav_parts.append(f"[Next →](./{idx + 2:02d}-{next_name}.md)")
            else:
                nav_parts.append("Next →")

            navigation = " | ".join(nav_parts)

            # Write chunk file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"**Navigation:** {navigation}\n\n")
                f.write(content)
                f.write(f"\n\n---\n**Navigation:** {navigation}\n")

        return len(chunks), chunk_files

    def create_index(self, chunk_files: List[Tuple[str, str, List[str]]]):
        """Create index.md with table of contents."""
        service_name = self.service_dir.name.title()

        index_content = f"# {service_name} Documentation - Chunked Version\n\n"
        index_content += "This documentation has been split into manageable chunks for easier navigation.\n\n"
        index_content += "## Table of Contents\n\n"

        for idx, (filename, title, sections) in enumerate(chunk_files):
            index_content += f"{idx + 1}. [{title}](./{filename})\n"
            if len(sections) > 1:
                for section in sections[:5]:  # Show first 5 sections
                    index_content += f"   - {section}\n"
                if len(sections) > 5:
                    index_content += f"   - ... and {len(sections) - 5} more sections\n"

        index_content += f"\n\n---\n\n[← Back to {service_name} README](../README.md)\n"

        index_path = self.chunked_dir / "index.md"
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)

    def update_readme(self):
        """Update or create README.md with link to chunked version."""
        readme_path = self.service_dir / "README.md"

        # Check if README exists
        if readme_path.exists():
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if it already has the chunked link
            if 'Chunked Version' not in content:
                # Add link at the top after the first header
                lines = content.split('\n')
                new_lines = []
                added = False

                for i, line in enumerate(lines):
                    new_lines.append(line)
                    if line.startswith('#') and not added:
                        # Add after first header
                        new_lines.append('')
                        new_lines.append('📄 [Full Documentation](./llms-full.txt) | 📑 [Chunked Version](./chunked/index.md)')
                        new_lines.append('')
                        added = True

                with open(readme_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(new_lines))
        else:
            # Create new README
            service_name = self.service_dir.name.title()
            content = f"# {service_name}\n\n"
            content += "📄 [Full Documentation](./llms-full.txt) | 📑 [Chunked Version](./chunked/index.md)\n"

            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(content)

    def split(self) -> Tuple[int, int]:
        """Main method to split the file."""
        print(f"Processing {self.file_path.name} in {self.service_dir.name}...")

        # Read file
        content = self.read_file()
        file_size = len(content.encode('utf-8'))
        print(f"  File size: {file_size / 1024 / 1024:.2f} MB")

        # Parse sections
        sections = self.parse_sections(content)
        print(f"  Found {len(sections)} sections")

        # Create chunks
        chunks = self.create_chunks(sections)
        print(f"  Creating {len(chunks)} chunks")

        # Write chunks
        num_chunks, chunk_files = self.write_chunks(chunks)

        # Create index
        self.create_index(chunk_files)

        # Update README
        self.update_readme()

        print(f"  ✓ Successfully split into {num_chunks} chunks")
        return num_chunks, file_size


def main():
    """Process all services."""
    base_dir = Path("/home/user/claude-docs/docs/infrastructure")

    # Configuration: service -> target chunk size in bytes
    services = {
        "elevenlabs": 180 * 1024,  # 180KB
        "supabase": 180 * 1024,    # 180KB
        "pinecone": 140 * 1024,    # 140KB
        "mintlify": 140 * 1024,    # 140KB
        "gitbook": 140 * 1024,     # 140KB
    }

    results = []
    skipped = []

    # Check which files are too small to split
    small_files = ["qdrant", "weaviate", "chroma", "cloudflare"]

    print("=" * 70)
    print("DOCUMENTATION SPLITTING UTILITY")
    print("=" * 70)
    print("\nSkipping small files (< 30KB):")
    for service in small_files:
        file_path = base_dir / service / "llms-full.txt"
        if file_path.exists():
            size = file_path.stat().st_size
            print(f"  ✓ {service:<15} {size / 1024:>6.1f} KB (kept as-is)")
            skipped.append(service)

    print("\n" + "=" * 70)
    print("Processing large files:\n")

    for service, chunk_size in services.items():
        file_path = base_dir / service / "llms-full.txt"
        if file_path.exists():
            splitter = DocSplitter(str(file_path), chunk_size)
            num_chunks, file_size = splitter.split()
            results.append((service, num_chunks, file_size))
            print()

    print("=" * 70)
    print("\n📊 SUMMARY:\n")
    print(f"  Processed services:  {len(results)}")
    print(f"  Skipped services:    {len(skipped)} (too small)")
    print(f"  Total chunks:        {sum(r[1] for r in results)}")
    print("\n📝 Details:")
    for service, chunks, size in results:
        avg_chunk_kb = (size / chunks) / 1024
        print(f"  • {service:<15} {chunks:>3} chunks  ({size / 1024 / 1024:>5.2f} MB, ~{avg_chunk_kb:.0f}KB/chunk)")
    print(f"\n⏭️  Skipped: {', '.join(skipped)}")
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
