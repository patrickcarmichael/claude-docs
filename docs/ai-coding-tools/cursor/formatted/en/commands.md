---
title: "Commands"
source: "https://docs.cursor.com/en/agent/chat/commands"
language: "en"
language_name: "English"
---

# Commands
Source: https://docs.cursor.com/en/agent/chat/commands

Define commands for reusable workflows

Custom commands allow you to create reusable workflows that can be triggered with a simple `/` prefix in the chat input box. These commands help standardize processes across your team and make common tasks more efficient.

<Frame>
    <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0d25ac517b091210da1c6eff4c8e3098" alt="Commands input example" data-og-width="1689" width="1689" data-og-height="1079" height="1079" data-path="images/chat/commands/input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=680f0cbf1491ef1303171dbd18115288 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d6a5397e565ab2c90435e6fdd2b7b27a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ae074e2f2b26741544fd8c8ecfa529e3 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=564aad432affcc04e51b624725f386ad 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5c1bd5d49babc2f08eb0efcd24ba7783 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3244c3be31c9bc704468a706c6e6b38e 2500w" />
</Frame>

<Info>
  Commands are currently in beta. The feature and syntax may change as we continue to improve it.
</Info>

## How commands work

Commands are defined as plain Markdown files that can be stored in two locations:

1. **Project commands**: Stored in the `.cursor/commands` directory of your project
2. **Global commands**: Stored in the `~/.cursor/commands` directory in your home directory

When you type `/` in the chat input box, Cursor will automatically detect and display available commands from both directories, making them instantly accessible across your workflow.

## Creating commands

1. Create a `.cursor/commands` directory in your project root
2. Add `.md` files with descriptive names (e.g., `review-code.md`, `write-tests.md`)
3. Write plain Markdown content describing what the command should do
4. Commands will automatically appear in the chat when you type `/`

Here's an example of how your commands directory structure might look:

```
.cursor/
└── commands/
    ├── address-github-pr-comments.md
    ├── code-review-checklist.md
    ├── create-pr.md
    ├── light-review-existing-diffs.md
    ├── onboard-new-developer.md
    ├── run-all-tests-and-fix.md
    ├── security-audit.md
    └── setup-new-feature.md
```

## Examples

Try these commands in your projects to get a feel for how they work.

<AccordionGroup>
  <Accordion title="Code review checklist">
    ```markdown  theme={null}
    # Code Review Checklist

    ## Overview
    Comprehensive checklist for conducting thorough code reviews to ensure quality, security, and maintainability.

    ## Review Categories

    ### Functionality
    - [ ] Code does what it's supposed to do
    - [ ] Edge cases are handled
    - [ ] Error handling is appropriate
    - [ ] No obvious bugs or logic errors

    ### Code Quality
    - [ ] Code is readable and well-structured
    - [ ] Functions are small and focused
    - [ ] Variable names are descriptive
    - [ ] No code duplication
    - [ ] Follows project conventions

    ### Security
    - [ ] No obvious security vulnerabilities
    - [ ] Input validation is present
    - [ ] Sensitive data is handled properly
    - [ ] No hardcoded secrets
    ```
  </Accordion>

  <Accordion title="Security audit">
    ```markdown  theme={null}
    # Security Audit

    ## Overview
    Comprehensive security review to identify and fix vulnerabilities in the codebase.

    ## Steps
    1. **Dependency audit**
       - Check for known vulnerabilities
       - Update outdated packages
       - Review third-party dependencies

    2. **Code security review**
       - Check for common vulnerabilities
       - Review authentication/authorization
       - Audit data handling practices

    3. **Infrastructure security**
       - Review environment variables
       - Check access controls
       - Audit network security

    ## Security Checklist
    - [ ] Dependencies updated and secure
    - [ ] No hardcoded secrets
    - [ ] Input validation implemented
    - [ ] Authentication secure
    - [ ] Authorization properly configured
    ```
  </Accordion>

  <Accordion title="Setup new feature">
    ```markdown  theme={null}
    # Setup New Feature

    ## Overview
    Systematically set up a new feature from initial planning through to implementation structure.

    ## Steps
    1. **Define requirements**
       - Clarify feature scope and goals
       - Identify user stories and acceptance criteria
       - Plan technical approach

    2. **Create feature branch**
       - Branch from main/develop
       - Set up local development environment
       - Configure any new dependencies

    3. **Plan architecture**
       - Design data models and APIs
       - Plan UI components and flow
       - Consider testing strategy

    ## Feature Setup Checklist
    - [ ] Requirements documented
    - [ ] User stories written
    - [ ] Technical approach planned
    - [ ] Feature branch created
    - [ ] Development environment ready
    ```
  </Accordion>

  <Accordion title="Create pull request">
    ```markdown  theme={null}
    # Create PR

    ## Overview
    Create a well-structured pull request with proper description, labels, and reviewers.

    ## Steps
    1. **Prepare branch**
       - Ensure all changes are committed
       - Push branch to remote
       - Verify branch is up to date with main

    2. **Write PR description**
       - Summarize changes clearly
       - Include context and motivation
       - List any breaking changes
       - Add screenshots if UI changes

    3. **Set up PR**
       - Create PR with descriptive title
       - Add appropriate labels
       - Assign reviewers
       - Link related issues

    ## PR Template
    - [ ] Feature A
    - [ ] Bug fix B
    - [ ] Unit tests pass
    - [ ] Manual testing completed
    ```
  </Accordion>

  <Accordion title="Run tests and fix failures">
    ```markdown  theme={null}
    # Run All Tests and Fix Failures

    ## Overview
    Execute the full test suite and systematically fix any failures, ensuring code quality and functionality.

    ## Steps
    1. **Run test suite**
       - Execute all tests in the project
       - Capture output and identify failures
       - Check both unit and integration tests

    2. **Analyze failures**
       - Categorize by type: flaky, broken, new failures
       - Prioritize fixes based on impact
       - Check if failures are related to recent changes

    3. **Fix issues systematically**
       - Start with the most critical failures
       - Fix one issue at a time
       - Re-run tests after each fix
    ```
  </Accordion>

  <Accordion title="Onboard new developer">
    ```markdown  theme={null}
    # Onboard New Developer

    ## Overview
    Comprehensive onboarding process to get a new developer up and running quickly.

    ## Steps
    1. **Environment setup**
       - Install required tools
       - Set up development environment
       - Configure IDE and extensions
       - Set up git and SSH keys

    2. **Project familiarization**
       - Review project structure
       - Understand architecture
       - Read key documentation
       - Set up local database

    ## Onboarding Checklist
    - [ ] Development environment ready
    - [ ] All tests passing
    - [ ] Can run application locally
    - [ ] Database set up and working
    - [ ] First PR submitted
    ```
  </Accordion>
</AccordionGroup>

---

← Previous: [Checkpoints](./checkpoints.md) | [Index](./index.md) | Next: [Compact](./compact.md) →