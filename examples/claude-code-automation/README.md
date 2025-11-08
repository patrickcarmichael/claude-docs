# Claude Code Automation Scripts

Automation and productivity scripts using Claude Code, the Anthropic AI coding assistant.

This example demonstrates:
- Using Claude Code via CLI for project automation
- Scripting with AI-powered code generation
- Batch processing with Claude
- Multi-file project management
- AI-assisted development workflows

## Overview

Claude Code is Anthropic's official CLI tool that brings AI-powered code assistance to your terminal. This example shows:
- Installing and configuring Claude Code
- Using Claude Code in automation scripts
- Integrating with existing development workflows
- Building AI-powered development tools
- Batch processing documents and code

### Features

- CLI-based AI coding assistance
- Multi-file project analysis
- Code generation and refactoring
- Documentation generation
- Test writing assistance
- Bug detection and fixing
- API integration examples
- Parallel processing with AI

## Requirements

### System Requirements
- Claude Code CLI installed
- Python 3.9+ (for automation scripts)
- Anthropic API key
- Basic command-line knowledge

### Installation

#### 1. Install Claude Code CLI

```bash
# Using npm (recommended)
npm install -g @anthropic-ai/claude-code

# Or using the official installer
curl https://code.claude.com/install.sh | bash
```

#### 2. Authenticate

```bash
# Set API key
export ANTHROPIC_API_KEY=sk-ant-...

# Or create ~/.anthropic/config
mkdir -p ~/.anthropic
echo "api_key=sk-ant-..." > ~/.anthropic/config
```

#### 3. Verify Installation

```bash
claude --version
# Output: Claude Code v1.0.0
```

## File Structure

```
claude-code-automation/
├── README.md                           # This file
├── requirements.txt                    # Python dependencies
│
├── scripts/
│   ├── generate_docs.py               # Generate documentation
│   ├── batch_refactor.py              # Refactor multiple files
│   ├── test_generator.py              # Generate tests
│   ├── code_review.py                 # AI code review
│   └── setup_project.py               # Project initialization
│
├── templates/
│   ├── claude_prompt.txt              # Standard prompt template
│   ├── project_structure.txt          # Project template
│   └── commit_message.txt             # Git commit template
│
├── examples/
│   ├── batch_refactor_example.sh     # Shell script example
│   ├── automated_testing.sh          # Testing automation
│   └── doc_generation.sh             # Doc generation example
│
└── utils/
    ├── claude_wrapper.py              # Claude Code wrapper
    └── batch_processor.py             # Batch processing utilities
```

## Quick Start

### 1. Simple Code Generation

```bash
# Generate a Python function
claude "Generate a Python function that validates email addresses"

# Generate with context
claude --project /path/to/project "Add error handling to this module"
```

### 2. Batch Document Generation

```bash
python scripts/generate_docs.py \
  --project /path/to/project \
  --output ./docs
```

### 3. Automated Code Review

```bash
python scripts/code_review.py \
  --files src/**/*.py \
  --output review.md
```

## Usage Examples

### Example 1: Generate Project Documentation

```bash
python scripts/generate_docs.py \
  --project ./my_app \
  --format markdown \
  --include-examples
```

Generates:
- README.md
- API documentation
- Setup instructions
- Examples

### Example 2: Batch Refactor Code

```bash
python scripts/batch_refactor.py \
  --pattern "*.py" \
  --target-dir ./src \
  --improvements modernize,type-hints
```

Refactors code for:
- Modern Python practices
- Type hints
- Better readability
- Performance improvements

### Example 3: Generate Unit Tests

```bash
python scripts/test_generator.py \
  --source src/app.py \
  --coverage 80 \
  --output tests/test_app.py
```

Creates:
- Unit tests for each function
- Edge case tests
- Integration tests
- Mocking setup

### Example 4: Code Review and Suggestions

```bash
python scripts/code_review.py \
  --files src/**/*.py \
  --report review.html \
  --check-patterns best-practices,security
```

Checks for:
- Best practices
- Security issues
- Performance problems
- Code smells

## Script Examples

### generate_docs.py

Generate comprehensive documentation for your project:

```python
from utils import claude_wrapper

def generate_project_docs(project_path, output_dir):
    """Generate documentation for entire project."""

    # Analyze project structure
    files = list_project_files(project_path)

    # Generate main README
    readme = claude_wrapper.generate(
        f"""Generate a comprehensive README.md for this project:
        {project_files_summary}

        Include:
        1. Project overview
        2. Installation instructions
        3. Usage examples
        4. API documentation
        5. Contributing guidelines""",
        output_tokens=2000
    )

    write_file(f"{output_dir}/README.md", readme)

    # Generate API docs
    api_docs = claude_wrapper.generate(
        f"""Generate API documentation for:
        {get_public_apis(project_path)}""",
        output_tokens=1500
    )

    write_file(f"{output_dir}/API.md", api_docs)

if __name__ == "__main__":
    generate_project_docs("./src", "./docs")
```

### batch_refactor.py

Refactor multiple files with AI assistance:

```python
from utils import batch_processor, claude_wrapper

def refactor_codebase(pattern, improvements):
    """Refactor files matching pattern."""

    files = find_files(pattern)

    for file_path in files:
        code = read_file(file_path)

        refactored = claude_wrapper.refactor(
            code=code,
            improvements=improvements,
            language="python"
        )

        write_file(file_path, refactored)
        print(f"✓ Refactored {file_path}")

if __name__ == "__main__":
    refactor_codebase("src/**/*.py", ["modernize", "type-hints"])
```

### test_generator.py

Generate comprehensive tests:

```python
from utils import claude_wrapper

def generate_tests(source_file, output_file, coverage=80):
    """Generate tests for source file."""

    code = read_file(source_file)

    tests = claude_wrapper.generate(
        f"""Generate comprehensive unit tests for this code:

        {code}

        Requirements:
        1. Target {coverage}% code coverage
        2. Test all functions and edge cases
        3. Use pytest framework
        4. Include mocking where needed
        5. Clear test names and docstrings""",
        output_tokens=3000
    )

    write_file(output_file, tests)
    print(f"✓ Generated tests to {output_file}")

if __name__ == "__main__":
    generate_tests("src/app.py", "tests/test_app.py", coverage=85)
```

## Advanced Usage

### 1. Multi-File Context

Provide multiple files as context:

```bash
claude --files src/main.py src/utils.py src/config.py \
       "Refactor these modules for better separation of concerns"
```

### 2. Streaming Output

Process large outputs:

```bash
claude --stream "Generate 1000 lines of documentation" | \
  tee output.txt | \
  head -100
```

### 3. Structured Output

Request specific formats:

```bash
claude --output json \
       "Analyze this code and return metrics as JSON"

claude --output markdown \
       "Generate documentation in markdown format"
```

### 4. Integration with Git

Automate commits with AI:

```bash
# Generate commit message from changes
git diff | claude "Generate a concise commit message" > /tmp/msg

git commit -F /tmp/msg
```

### 5. Parallel Processing

Process multiple files in parallel:

```bash
python scripts/batch_processor.py \
  --input-dir ./files \
  --output-dir ./processed \
  --workers 4 \
  --prompt "Optimize this code for performance"
```

## Real-World Workflow

### Complete Development Automation

```bash
# 1. Initialize project with Claude Code
python scripts/setup_project.py --template=nextjs-api

# 2. Generate initial documentation
python scripts/generate_docs.py --project ./src

# 3. Add comprehensive tests
python scripts/test_generator.py --coverage=85

# 4. Refactor for best practices
python scripts/batch_refactor.py --improvements=all

# 5. Review and suggest improvements
python scripts/code_review.py --report=html

# 6. Commit with AI-generated message
git add .
git diff --cached | claude "Generate git commit message" | \
  xargs git commit -m
```

## Best Practices

### 1. Provide Context

```bash
# Good: Include relevant context
claude --files app.py config.py --project-root ./src \
       "Add logging to all functions"

# Less effective: No context
claude "Add logging to the app"
```

### 2. Use Specific Prompts

```bash
# Good: Clear, specific requirements
claude """Generate a function that:
- Takes a list of URLs
- Fetches content in parallel
- Returns dict with URLs as keys
- Handles timeout/errors gracefully"""

# Vague: Too broad
claude "Make a web scraper"
```

### 3. Iterative Refinement

```bash
# First pass: Generate code
result=$(claude "Generate a sorting algorithm")

# Second pass: Improve
claude "Optimize this for performance: $result"

# Third pass: Document
claude "Add comprehensive docstrings: $result"
```

### 4. Error Handling

```bash
python scripts/batch_processor.py \
  --error-handling retry \
  --max-retries 3 \
  --timeout 30
```

## Integration Examples

### With GitHub Actions

```yaml
name: AI-Assisted Code Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Code Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          python scripts/code_review.py \
            --files "src/**/*.py" \
            --output review.md
      - name: Comment on PR
        uses: actions/github-script@v6
        with:
          script: |
            const review = fs.readFileSync('review.md', 'utf8');
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: review
            });
```

### With Pre-commit Hooks

```bash
# .git/hooks/pre-commit
#!/bin/bash
python scripts/code_review.py --files $(git diff --cached --name-only) \
  && echo "✓ Code review passed"
```

## Troubleshooting

### "API key not found"
```bash
# Check API key is set
echo $ANTHROPIC_API_KEY

# Set if missing
export ANTHROPIC_API_KEY=sk-ant-...
```

### Rate Limiting
```bash
# Add delays between requests
python scripts/batch_processor.py \
  --delay 2 \
  --max-requests-per-minute 30
```

### Memory Issues with Large Files
```bash
# Split large files or use streaming
python scripts/batch_processor.py \
  --chunk-size 5000 \
  --stream-output
```

## Performance Tips

1. **Batch Processing**: Process multiple files together when context allows
2. **Caching**: Cache Claude Code responses for identical requests
3. **Streaming**: Use streaming for large outputs to avoid memory issues
4. **Parallel Processing**: Use multiple workers for independent tasks
5. **Incremental**: Process only changed files to save API usage

## Related Examples

- [RAG Application](../rag-app/) - Use RAG with Claude Code integration
- [Multi-Agent System](../multi-agent/) - Orchestrate Claude Code tasks with CrewAI
- [Chat Interface](../chat-interface/) - Web interface for Claude Code features

## Resources

- Claude Code Official: https://code.claude.com/
- Claude Code GitHub: https://github.com/anthropics/claude-code
- Anthropic API Docs: https://docs.anthropic.com/
- Claude Code CLI Reference: https://code.claude.com/docs/cli/

## Environment Variables

```bash
# API Configuration
ANTHROPIC_API_KEY          # Your Anthropic API key
ANTHROPIC_ORG_ID          # Organization ID (optional)

# Behavior Configuration
CLAUDE_MODEL              # Model to use (default: claude-3-5-sonnet-20241022)
CLAUDE_TEMPERATURE        # Response temperature (0-1)
CLAUDE_MAX_TOKENS         # Maximum output tokens
CLAUDE_TIMEOUT            # Request timeout in seconds

# Feature Flags
CLAUDE_CACHE_RESPONSES    # Enable response caching
CLAUDE_PARALLEL_WORKERS   # Number of parallel workers
CLAUDE_VERBOSE_LOGGING    # Enable detailed logs
```

---

*Practical automation scripts demonstrating Claude Code's power for AI-assisted development and project automation.*
