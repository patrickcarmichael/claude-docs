#!/usr/bin/env python3
"""
Script to parse and format llms-full.txt files into structured markdown documentation.
"""

import re
import os
from pathlib import Path
from typing import List, Dict, Tuple


def parse_nextjs_vercel_format(content: str) -> List[Dict]:
    """Parse Next.js and Vercel format with --- separators and metadata."""
    sections = []

    # Split by the separator pattern (80+ dashes)
    parts = re.split(r'\n-{80,}\n', content)

    current_metadata = {}
    for i, part in enumerate(parts):
        if not part.strip():
            continue

        lines = part.strip().split('\n')

        # Check if this part contains metadata (title:, description:, etc.)
        if i > 0 and ':' in lines[0] and not lines[0].startswith('#'):
            # This is a metadata block
            metadata = {}
            content_start = 0
            for j, line in enumerate(lines):
                if ':' in line and not line.startswith('#'):
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip().strip('"')
                else:
                    content_start = j
                    break

            # The rest is the content
            section_content = '\n'.join(lines[content_start:]).strip()
            if section_content:
                sections.append({
                    'metadata': metadata,
                    'content': section_content
                })
        else:
            # This is content without preceding metadata
            if part.strip():
                sections.append({
                    'metadata': current_metadata.copy() if i > 0 else {},
                    'content': part.strip()
                })

    return sections


def parse_astro_format(content: str) -> List[Dict]:
    """Parse Astro format with simple section headers."""
    sections = []

    # Split by top-level headers (single #)
    parts = re.split(r'\n(?=# [^#])', content)

    for part in parts:
        if not part.strip():
            continue

        lines = part.strip().split('\n')
        if lines[0].startswith('# '):
            title = lines[0].replace('# ', '').strip()

            # Check for system message
            if '<SYSTEM>' in title:
                continue

            sections.append({
                'metadata': {'title': title},
                'content': part.strip()
            })

    return sections


def parse_streamlit_format(content: str) -> List[Dict]:
    """Parse Streamlit format with # Title followed by Source: URL."""
    sections = []

    # Split by --- separators
    parts = content.split('\n---\n')

    for part in parts:
        if not part.strip():
            continue

        lines = part.strip().split('\n')
        metadata = {}

        # Extract title and source
        if lines[0].startswith('# '):
            metadata['title'] = lines[0].replace('# ', '').strip()

            # Look for Source: line
            for i, line in enumerate(lines[1:4], 1):  # Check first few lines
                if line.startswith('Source:'):
                    metadata['source'] = line.replace('Source:', '').strip()
                    break

        sections.append({
            'metadata': metadata,
            'content': part.strip()
        })

    return sections


def create_slug(text: str) -> str:
    """Create a URL-friendly slug from text."""
    # Remove special characters and convert to lowercase
    slug = re.sub(r'[^\w\s-]', '', text.lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug.strip('-')


def format_code_blocks(content: str, default_lang: str = 'jsx') -> str:
    """Ensure code blocks have proper language identifiers."""

    # Fix code blocks without language
    content = re.sub(
        r'```\s*\n',
        f'```{default_lang}\n',
        content
    )

    # Fix common language variations
    replacements = {
        '```bash filename=': '```bash\n# ',
        '```txt filename=': '```text\n# ',
        '```json filename=': '```json\n// ',
        '```javascript': '```javascript',
        '```typescript': '```typescript',
        '```tsx': '```tsx',
        '```jsx': '```jsx',
    }

    for old, new in replacements.items():
        content = content.replace(old, new)

    return content


def create_front_matter(metadata: Dict, section_number: int = None) -> str:
    """Create YAML front matter from metadata."""
    front_matter = ['---']

    if 'title' in metadata:
        front_matter.append(f'title: "{metadata["title"]}"')

    if 'description' in metadata:
        front_matter.append(f'description: "{metadata["description"]}"')

    if 'source' in metadata:
        front_matter.append(f'source: {metadata["source"]}')

    if section_number is not None:
        front_matter.append(f'section: {section_number:02d}')

    front_matter.append('---')
    front_matter.append('')

    return '\n'.join(front_matter)


def add_footer_navigation(content: str, prev_link: str = None, next_link: str = None, index_link: str = 'index.md') -> str:
    """Add footer navigation to a section."""
    footer = ['\n\n---\n']

    nav_items = []
    if prev_link:
        nav_items.append(f'[← Previous]({prev_link})')

    nav_items.append(f'[Index]({index_link})')

    if next_link:
        nav_items.append(f'[Next →]({next_link})')

    footer.append(' | '.join(nav_items))
    footer.append('')

    return content + '\n'.join(footer)


def process_framework(framework_name: str, base_path: str):
    """Process a single framework's documentation."""
    framework_dir = Path(base_path) / framework_name
    input_file = framework_dir / 'llms-full.txt'
    output_dir = framework_dir / 'formatted'

    print(f"\n{'='*60}")
    print(f"Processing {framework_name.upper()}")
    print(f"{'='*60}")

    if not input_file.exists():
        print(f"ERROR: {input_file} not found")
        return

    # Create output directory
    output_dir.mkdir(exist_ok=True)

    # Read content
    print(f"Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"  File size: {len(content) / (1024*1024):.2f} MB")

    # Parse based on framework
    print(f"Parsing sections...")
    if framework_name in ['nextjs', 'vercel']:
        sections = parse_nextjs_vercel_format(content)
    elif framework_name == 'astro':
        sections = parse_astro_format(content)
    elif framework_name == 'streamlit':
        sections = parse_streamlit_format(content)
    else:
        print(f"ERROR: Unknown framework format: {framework_name}")
        return

    print(f"  Found {len(sections)} sections")

    # Determine default language for code blocks
    code_lang = 'python' if framework_name == 'streamlit' else 'jsx'

    # Create complete documentation file
    print(f"Creating documentation.md...")
    full_doc = []
    full_doc.append('---')
    full_doc.append(f'title: "{framework_name.title()} Documentation"')
    full_doc.append(f'framework: {framework_name}')
    full_doc.append('type: complete')
    full_doc.append('---')
    full_doc.append('')
    full_doc.append(f'# {framework_name.title()} Documentation')
    full_doc.append('')
    full_doc.append('This is the complete formatted documentation.')
    full_doc.append('')
    full_doc.append('---')
    full_doc.append('')

    for section in sections:
        formatted_content = format_code_blocks(section['content'], code_lang)
        full_doc.append(formatted_content)
        full_doc.append('')
        full_doc.append('---')
        full_doc.append('')

    with open(output_dir / 'documentation.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(full_doc))

    # Create individual section files
    print(f"Creating section files...")
    section_files = []

    for i, section in enumerate(sections, 1):
        if not section['metadata'].get('title'):
            continue

        title = section['metadata']['title']
        slug = create_slug(title)
        filename = f'{i:02d}-{slug}.md'
        section_files.append({'num': i, 'title': title, 'filename': filename})

        # Create section content
        section_content = []
        section_content.append(create_front_matter(section['metadata'], i))

        formatted_content = format_code_blocks(section['content'], code_lang)
        section_content.append(formatted_content)

        # Add navigation
        prev_link = section_files[-2]['filename'] if len(section_files) > 1 else None
        next_link = f'{i+1:02d}-*.md'  # Placeholder, will be fixed

        section_text = '\n'.join(section_content)
        section_text = add_footer_navigation(section_text, prev_link, 'index.md')

        with open(output_dir / filename, 'w', encoding='utf-8') as f:
            f.write(section_text)

    print(f"  Created {len(section_files)} section files")

    # Create index file
    print(f"Creating index.md...")
    index_content = []
    index_content.append('---')
    index_content.append(f'title: "{framework_name.title()} Documentation Index"')
    index_content.append(f'framework: {framework_name}')
    index_content.append('type: index')
    index_content.append('---')
    index_content.append('')
    index_content.append(f'# {framework_name.title()} Documentation Index')
    index_content.append('')
    index_content.append('## Available Formats')
    index_content.append('')
    index_content.append('- [Complete Documentation](documentation.md) - All sections in one file')
    index_content.append('- Individual Sections (below)')
    index_content.append('')
    index_content.append('## Sections')
    index_content.append('')

    for section in section_files:
        index_content.append(f"{section['num']}. [{section['title']}]({section['filename']})")

    index_content.append('')
    index_content.append('---')
    index_content.append('')
    index_content.append(f'Total sections: {len(section_files)}')

    with open(output_dir / 'index.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(index_content))

    # Create/update README.md
    print(f"Creating README.md...")
    readme_content = []
    readme_content.append(f'# {framework_name.title()} Documentation')
    readme_content.append('')
    readme_content.append('This directory contains documentation for ' + framework_name.title() + '.')
    readme_content.append('')
    readme_content.append('## Available Formats')
    readme_content.append('')
    readme_content.append('### Raw Format')
    readme_content.append('- [llms-full.txt](llms-full.txt) - Original concatenated documentation')
    readme_content.append('')
    readme_content.append('### Formatted Markdown')
    readme_content.append('- [Complete Documentation](formatted/documentation.md) - All sections formatted in one file')
    readme_content.append('- [Documentation Index](formatted/index.md) - Navigation hub for individual sections')
    readme_content.append(f'- {len(section_files)} individual section files in `formatted/`')
    readme_content.append('')
    readme_content.append('## Section Overview')
    readme_content.append('')

    # Show first 10 sections as preview
    preview_count = min(10, len(section_files))
    for section in section_files[:preview_count]:
        readme_content.append(f"{section['num']}. [{section['title']}](formatted/{section['filename']})")

    if len(section_files) > preview_count:
        readme_content.append(f'\n...and {len(section_files) - preview_count} more sections. See [index](formatted/index.md) for complete list.')

    readme_content.append('')
    readme_content.append('## Statistics')
    readme_content.append('')
    readme_content.append(f'- Total sections: {len(section_files)}')
    readme_content.append(f'- Original file size: {len(content) / (1024*1024):.2f} MB')
    readme_content.append('')

    with open(framework_dir / 'README.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(readme_content))

    print(f"✓ Completed {framework_name}")
    print(f"  - documentation.md: Complete formatted version")
    print(f"  - index.md: Navigation hub")
    print(f"  - {len(section_files)} section files")
    print(f"  - README.md: Updated with links")

    return {
        'framework': framework_name,
        'sections': len(section_files),
        'files': len(section_files) + 2  # +2 for documentation.md and index.md
    }


if __name__ == '__main__':
    base_path = '/home/user/claude-docs/docs/web-frameworks'

    frameworks = ['nextjs', 'astro', 'streamlit', 'vercel']

    results = []
    for framework in frameworks:
        result = process_framework(framework, base_path)
        if result:
            results.append(result)

    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    for result in results:
        print(f"{result['framework']:12s}: {result['sections']:4d} sections, {result['files']:4d} files created")
    print(f"{'='*60}")
