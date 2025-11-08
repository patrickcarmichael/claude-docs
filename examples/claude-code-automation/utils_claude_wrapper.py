"""
Claude Code Wrapper Utility

Provides convenient functions for interacting with Claude API
for code generation, refactoring, and analysis tasks.

This file should be placed at: utils/claude_wrapper.py
"""

import os
from typing import Optional, Union, List
from anthropic import Anthropic

# Initialize client
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def generate(
    prompt: str,
    model: str = "claude-3-5-sonnet-20241022",
    output_tokens: int = 2000,
    temperature: float = 0.7,
    system_prompt: Optional[str] = None,
) -> str:
    """
    Generate code or text using Claude.

    Args:
        prompt: The prompt/request
        model: Claude model to use
        output_tokens: Maximum output length
        temperature: Creativity level (0-1)
        system_prompt: Optional system message

    Returns:
        Generated text/code
    """
    system = system_prompt or "You are an expert programmer and code assistant."

    response = client.messages.create(
        model=model,
        max_tokens=output_tokens,
        temperature=temperature,
        system=system,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.content[0].text


def refactor(
    code: str,
    improvements: Union[str, List[str]],
    language: str = "python",
) -> str:
    """
    Refactor code with specified improvements.

    Args:
        code: Source code to refactor
        improvements: List of improvements to apply
        language: Programming language

    Returns:
        Refactored code
    """
    if isinstance(improvements, list):
        improvements = ", ".join(improvements)

    prompt = f"""Refactor the following {language} code with these improvements:
{improvements}

Original code:
```{language}
{code}
```

Return only the refactored code without explanations."""

    system = f"You are an expert {language} programmer. Refactor code for better quality."

    return generate(prompt, system_prompt=system, output_tokens=3000)


def generate_tests(
    code: str,
    language: str = "python",
    framework: str = "pytest",
    coverage: int = 80,
) -> str:
    """
    Generate unit tests for code.

    Args:
        code: Source code
        language: Programming language
        framework: Testing framework
        coverage: Target code coverage percentage

    Returns:
        Generated tests
    """
    prompt = f"""Generate comprehensive unit tests for this {language} code.

Target {coverage}% code coverage using {framework}.

Source code:
```{language}
{code}
```

Requirements:
1. Test all functions and methods
2. Include edge cases and error conditions
3. Use clear test names and docstrings
4. Include setup/teardown if needed
5. Use appropriate mocking

Return only the test code without explanations."""

    system = f"You are an expert {language} test engineer using {framework}."

    return generate(prompt, system_prompt=system, output_tokens=3000)


def analyze_code(
    code: str,
    language: str = "python",
    checks: Optional[List[str]] = None,
) -> str:
    """
    Analyze code for issues and improvements.

    Args:
        code: Source code
        language: Programming language
        checks: List of checks to perform (e.g., security, performance)

    Returns:
        Analysis report
    """
    checks_text = ""
    if checks:
        checks_text = f"\nFocus on: {', '.join(checks)}"

    prompt = f"""Analyze this {language} code and provide detailed feedback.{checks_text}

Code:
```{language}
{code}
```

Provide analysis on:
1. Code quality and readability
2. Best practices compliance
3. Potential bugs or issues
4. Performance considerations
5. Security concerns (if applicable)
6. Suggested improvements"""

    return generate(prompt, output_tokens=2000)


def generate_documentation(
    code: str,
    language: str = "python",
    format: str = "markdown",
) -> str:
    """
    Generate documentation for code.

    Args:
        code: Source code
        language: Programming language
        format: Output format (markdown, rst, html)

    Returns:
        Generated documentation
    """
    prompt = f"""Generate comprehensive documentation for this {language} code.

Code:
```{language}
{code}
```

Requirements:
1. Clear descriptions of what the code does
2. Parameter and return value documentation
3. Usage examples
4. Edge cases and limitations
5. Related functions/classes

Format as {format}."""

    system = f"You are a technical documentation expert for {language}."

    return generate(prompt, system_prompt=system, output_tokens=2000)


def fix_code(
    code: str,
    error_message: str,
    language: str = "python",
) -> str:
    """
    Fix code based on error message.

    Args:
        code: Broken code
        error_message: Error message or description
        language: Programming language

    Returns:
        Fixed code
    """
    prompt = f"""Fix this {language} code:

Error: {error_message}

Broken code:
```{language}
{code}
```

Return only the fixed code without explanations."""

    system = f"You are an expert {language} debugger. Fix code based on errors."

    return generate(prompt, system_prompt=system, output_tokens=2000)


def explain_code(
    code: str,
    language: str = "python",
    detail_level: str = "medium",
) -> str:
    """
    Generate explanation of code.

    Args:
        code: Source code
        language: Programming language
        detail_level: "brief", "medium", or "detailed"

    Returns:
        Code explanation
    """
    detail_instructions = {
        "brief": "Provide a 1-2 sentence summary.",
        "medium": "Explain what the code does, key logic, and why.",
        "detailed": "Thoroughly explain every part, logic flow, and design decisions."
    }

    prompt = f"""Explain this {language} code in {detail_level} detail.

{detail_instructions.get(detail_level, detail_instructions['medium'])}

Code:
```{language}
{code}
```"""

    return generate(prompt, output_tokens=1500)


def review_code(
    code: str,
    language: str = "python",
    review_type: str = "general",
) -> str:
    """
    Perform code review.

    Args:
        code: Source code to review
        language: Programming language
        review_type: "general", "security", "performance", "style"

    Returns:
        Code review with suggestions
    """
    review_prompts = {
        "security": "Focus on security vulnerabilities and best practices.",
        "performance": "Focus on performance optimization and efficiency.",
        "style": "Focus on code style, naming conventions, and readability.",
        "general": "Provide comprehensive feedback on quality, style, and best practices."
    }

    prompt = f"""Review this {language} code.

{review_prompts.get(review_type, review_prompts['general'])}

Code:
```{language}
{code}
```

Provide structured feedback with:
1. Issues found
2. Specific suggestions
3. Severity levels
4. Examples of fixes"""

    system = f"You are an experienced {language} code reviewer."

    return generate(prompt, system_prompt=system, output_tokens=2000)


def convert_code(
    code: str,
    from_language: str,
    to_language: str,
) -> str:
    """
    Convert code from one language to another.

    Args:
        code: Source code
        from_language: Source language
        to_language: Target language

    Returns:
        Converted code
    """
    prompt = f"""Convert this {from_language} code to {to_language}.

Original code:
```{from_language}
{code}
```

Return only the converted code maintaining the same functionality.
Adapt to {to_language} idioms and best practices."""

    system = f"You are an expert polyglot programmer skilled in both {from_language} and {to_language}."

    return generate(prompt, system_prompt=system, output_tokens=3000)


if __name__ == "__main__":
    # Example usage
    sample_code = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
"""

    print("Analysis:")
    print(analyze_code(sample_code))
    print("\n" + "="*60 + "\n")

    print("Refactored:")
    print(refactor(sample_code, improvements=["optimize", "add-type-hints"]))
    print("\n" + "="*60 + "\n")

    print("Tests:")
    print(generate_tests(sample_code, coverage=90))
