# Contributing to Claude Docs

Thank you for your interest in contributing to the Claude documentation repository! This guide will help you understand how to add new platforms, update existing documentation, and submit your contributions.

## Table of Contents

- [Getting Started](#getting-started)
- [Adding New Platforms](#adding-new-platforms)
- [Updating Existing Documentation](#updating-existing-documentation)
- [Format Requirements](#format-requirements)
- [Pull Request Process](#pull-request-process)
- [Naming Conventions](#naming-conventions)
- [Code of Conduct](#code-of-conduct)

## Getting Started

1. **Fork the Repository**: Create a personal fork of the repository
2. **Clone Your Fork**: `git clone https://github.com/your-username/claude-docs.git`
3. **Create a Branch**: `git checkout -b docs/add-platform-name` or `git checkout -b docs/update-topic-name`
4. **Make Your Changes**: Follow the guidelines below
5. **Test Your Changes**: Verify markdown syntax and links
6. **Submit a Pull Request**: Follow the PR process below

## Adding New Platforms

### Step 1: Verify Platform Category

Determine which category your platform belongs to:

- **`docs/ai-platforms/`** - AI and machine learning platforms (OpenAI, Anthropic, etc.)
- **`docs/ai-frameworks/`** - ML frameworks and libraries (TensorFlow, PyTorch, etc.)
- **`docs/infrastructure/`** - Cloud providers and DevOps tools (AWS, GCP, Azure, Kubernetes, Docker, etc.)
- **`docs/claude-code/`** - Claude Code IDE configuration and administration

### Step 2: Create Platform Directory

Create a new directory in the appropriate category:

```bash
mkdir -p docs/{category}/{platform-name}
```

Examples:
- `docs/infrastructure/aws/`
- `docs/ai-platforms/openai/`
- `docs/ai-frameworks/tensorflow/`

### Step 3: Create Documentation Files

Minimum required files for a new platform:

```
docs/{category}/{platform-name}/
├── README.md                 # Overview and getting started
├── installation.md          # Installation and setup instructions
└── integration.md           # Integration with Claude Code
```

Optional but recommended files:

```
├── configuration.md         # Configuration options
├── troubleshooting.md      # Common issues and solutions
├── examples.md             # Code examples and use cases
├── api-reference.md        # API endpoints and methods
└── faq.md                  # Frequently asked questions
```

### Step 4: Create README in Category

If the category doesn't have a README.md, create one:

```bash
touch docs/{category}/README.md
```

Include:
- Category overview
- List of all platforms in category
- How to get started
- Links to platform documentation

### Step 5: Update Main README

Update `/home/user/claude-docs/README.md` to include your new platform.

## Updating Existing Documentation

### Step 1: Identify Outdated Content

- Check timestamps in documentation
- Review platform's official documentation for changes
- Look for broken links or outdated examples

### Step 2: Make Updates

- Update content with new information
- Verify all links are working
- Test any code examples
- Update version numbers if applicable

### Step 3: Update CHANGELOG

Add your changes to `CHANGELOG.md` under the `[Unreleased]` section:

```markdown
## [Unreleased]

### Changed
- Updated AWS documentation with new EC2 instance types
- Fixed broken links in Kubernetes configuration guide

### Fixed
- Corrected Terraform syntax examples in infrastructure docs
```

## Format Requirements

### File Structure

All documentation files must follow this structure:

```markdown
# Main Title

Brief introduction (1-2 sentences).

## Table of Contents

- [Section 1](#section-1)
- [Section 2](#section-2)
- [See Also](#see-also)

## Section 1

Content with proper markdown formatting.

### Subsection 1.1

Additional details.

## Section 2

More content.

## See Also

- [Related Documentation](./path-to-docs)
- [External Resource](https://example.com)
```

### Markdown Style

- **Headings**: Use `#` for main title (h1), `##` for sections (h2), `###` for subsections (h3)
- **Code Blocks**: Use triple backticks with language identifier
  ```python
  # Example code
  print("hello")
  ```
- **Lists**: Use `-` for unordered, `1.` for ordered
- **Links**: Use `[text](url)` format
- **Line Length**: Keep lines under 100 characters when possible
- **Spacing**: Use blank lines between sections

### Content Requirements

Each platform documentation must include:

- **Overview**: What is this platform and why use it?
- **Prerequisites**: System requirements and dependencies
- **Installation/Setup**: Step-by-step setup instructions
- **Configuration**: How to configure with Claude Code
- **Examples**: Practical code examples
- **Troubleshooting**: Common issues and solutions
- **References**: Links to official documentation and resources

### Front Matter (Optional)

Add metadata to the top of files for better organization:

```markdown
---
title: Platform Name
description: Brief description of the platform
category: ai-platforms
tags: [ai, ml, platform]
last_updated: 2025-11-08
---

# Platform Name

Content starts here...
```

## Pull Request Process

### Before Submitting

1. **Test Your Changes**
   - Verify all markdown syntax is correct
   - Check that all links work
   - Test any code examples provided
   - Run spell check

2. **Update Documentation**
   - Update CHANGELOG.md
   - Update relevant README.md files
   - Update main README.md if platform is new

3. **Self Review**
   - Review your own PR
   - Ensure consistency with existing documentation
   - Check for clarity and readability

### Submitting Your PR

1. **Push Your Branch**
   ```bash
   git add .
   git commit -m "docs: add/update [platform-name]"
   git push origin docs/branch-name
   ```

2. **Create Pull Request**
   - Use the provided PR template
   - Link any related issues
   - Provide clear description of changes
   - Add screenshots or examples if helpful

3. **PR Template Fields**
   - **Type**: New Platform / Update / Bug Fix / Enhancement
   - **Platform(s)**: Affected platform names
   - **Summary**: Brief description of changes
   - **Testing**: What was tested and how
   - **Checklist**: Confirm all requirements met

### PR Requirements

- [ ] CHANGELOG.md has been updated
- [ ] Markdown syntax is valid
- [ ] All links are working
- [ ] Code examples have been tested
- [ ] Content follows style guidelines
- [ ] No spelling or grammar errors
- [ ] Documentation is clear and well-organized

### Review Process

1. **Automated Checks**
   - Markdown linting
   - Link validation
   - Spell checking

2. **Manual Review**
   - Content accuracy
   - Style consistency
   - Completeness

3. **Approval and Merge**
   - Minimum 1 approval required
   - Maintainer merges to main branch

## Naming Conventions

### Directory Names

- Use lowercase
- Use hyphens for spaces (not underscores)
- Keep names concise
- Examples: `aws`, `google-cloud`, `azure`, `docker`, `kubernetes`

### File Names

- Use lowercase
- Use hyphens for spaces
- Be descriptive
- Examples: `installation.md`, `configuration.md`, `troubleshooting.md`

### Branch Names

- Format: `docs/type-description`
- Examples:
  - `docs/add-aws-rds`
  - `docs/update-docker`
  - `docs/fix-broken-links`

### Commit Messages

Follow conventional commits format:

```
docs: add/update/fix [description]

- Detailed explanation of changes
- Why this change was made
- Any related issues (#123)
```

Examples:
- `docs: add AWS documentation with RDS guide`
- `docs: update Docker configuration for latest version`
- `docs: fix broken links in Kubernetes guide`

## Naming Conventions for Platforms

When adding a new platform, use the official name:

- Official name: "Amazon Web Services" → Directory: `aws`
- Official name: "Google Cloud Platform" → Directory: `google-cloud`
- Official name: "Microsoft Azure" → Directory: `azure`
- Official name: "OpenAI" → Directory: `openai`
- Official name: "Kubernetes" → Directory: `kubernetes`

Check the platform's official documentation for the standard abbreviated name.

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors.

### Expected Behavior

- Be respectful and professional
- Welcome different perspectives and experiences
- Give credit where credit is due
- Provide constructive feedback
- Focus on what is best for the community

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insults
- Unprofessional conduct
- Disrespect of differing opinions

### Reporting Issues

If you witness or experience unacceptable behavior, please report it to the maintainers.

## Questions?

If you have questions about contributing:

1. Check existing documentation
2. Search for similar issues in the repository
3. Open a new issue with the label `question`
4. Contact the maintainers

## License

By contributing to this repository, you agree that your contributions will be licensed under the same license as the project.

---

**Thank you for contributing to Claude Docs!**

For more information, see:
- [README.md](./README.md) - Project overview
- [CHANGELOG.md](./CHANGELOG.md) - Version history
