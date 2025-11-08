#!/usr/bin/env python3
"""
Content Creation Crew

A multi-agent system for creating high-quality content:
1. Researcher Agent: Gathers information
2. Writer Agent: Creates content
3. Editor Agent: Reviews and refines

Usage:
    python content_crew.py --topic "Claude Code Fundamentals"
    python content_crew.py --topic "RAG Applications" --verbose
"""

import argparse
import logging
from typing import Optional

from crewai import Agent, Task, Crew
from langchain_anthropic import ChatAnthropic

import config

logging.basicConfig(
    level=config.LOG_LEVEL,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def create_researcher_agent() -> Agent:
    """Create a research agent for gathering information."""
    return Agent(
        role="Research Analyst",
        goal="Find accurate, comprehensive information on any topic",
        backstory="""You are an expert researcher with deep knowledge across many domains.
        You excel at finding reliable sources, extracting key information,
        and presenting findings in a structured way.
        You have access to web search capabilities and can analyze documents.""",
        tools=[],  # Would add search_tool, read_file_tool in production
        llm=ChatAnthropic(
            model=config.CLAUDE_MODEL,
            temperature=config.TEMPERATURE,
            max_tokens=config.MAX_TOKENS,
            api_key=config.ANTHROPIC_API_KEY,
        ),
        verbose=config.VERBOSE,
        allow_delegation=False,
    )


def create_writer_agent() -> Agent:
    """Create a writer agent for content creation."""
    return Agent(
        role="Content Writer",
        goal="Write clear, engaging, and well-structured content",
        backstory="""You are an accomplished content writer with expertise in various genres.
        You create compelling narratives, explain complex topics clearly,
        and adapt your writing style to different audiences.
        You follow best practices in content organization and formatting.""",
        tools=[],
        llm=ChatAnthropic(
            model=config.CLAUDE_MODEL,
            temperature=config.TEMPERATURE,
            max_tokens=config.MAX_TOKENS,
            api_key=config.ANTHROPIC_API_KEY,
        ),
        verbose=config.VERBOSE,
        allow_delegation=False,
    )


def create_editor_agent() -> Agent:
    """Create an editor agent for content review."""
    return Agent(
        role="Content Editor",
        goal="Review and refine content for quality, clarity, and impact",
        backstory="""You are an experienced editor with a keen eye for detail.
        You improve clarity, fix grammatical issues, ensure consistency,
        and enhance overall readability.
        You provide constructive feedback and maintain the author's voice.""",
        tools=[],
        llm=ChatAnthropic(
            model=config.CLAUDE_MODEL,
            temperature=config.TEMPERATURE - 0.1,  # Slightly lower temp for editing
            max_tokens=config.MAX_TOKENS,
            api_key=config.ANTHROPIC_API_KEY,
        ),
        verbose=config.VERBOSE,
        allow_delegation=False,
    )


def create_research_task(agent: Agent, topic: str) -> Task:
    """Create a research task."""
    return Task(
        description=f"""Research comprehensive information about the topic: {topic}

        Your research should include:
        1. Key concepts and definitions
        2. Important facts and statistics
        3. Real-world applications
        4. Current trends and developments
        5. Notable experts or resources

        Organize your findings in a clear, structured format that can be used as input for writing.""",
        expected_output="A comprehensive research document with well-organized findings",
        agent=agent,
        max_iter=3,
    )


def create_writing_task(agent: Agent, topic: str) -> Task:
    """Create a writing task."""
    return Task(
        description=f"""Write high-quality content about {topic} based on the research findings.

        The content should:
        1. Have a compelling introduction that hooks the reader
        2. Be well-organized with clear sections and headers
        3. Use concrete examples and analogies
        4. Include actionable takeaways or insights
        5. Have a strong conclusion
        6. Be approximately 1000-1500 words

        Use professional but accessible language suitable for both beginners and experts.""",
        expected_output="A well-written article about the topic with proper structure and formatting",
        agent=agent,
        max_iter=3,
    )


def create_editing_task(agent: Agent) -> Task:
    """Create an editing task."""
    return Task(
        description="""Review the written content and provide detailed feedback.

        Focus on:
        1. Grammar, spelling, and punctuation
        2. Clarity and readability
        3. Flow and logical progression
        4. Consistency in tone and style
        5. Accuracy of information
        6. Engagement and impact

        Provide specific suggestions for improvement and a final polished version.""",
        expected_output="An edited version of the article with suggestions and improvements",
        agent=agent,
        max_iter=2,
    )


def run_content_creation_crew(topic: str, verbose: bool = False) -> str:
    """
    Run the content creation crew.

    Args:
        topic: Topic for content creation
        verbose: Enable verbose output

    Returns:
        Final content
    """
    logger.info(f"Starting content creation crew for topic: {topic}")
    logger.info("=" * 70)

    # Create agents
    researcher = create_researcher_agent()
    writer = create_writer_agent()
    editor = create_editor_agent()

    # Create tasks
    research_task = create_research_task(researcher, topic)
    writing_task = create_writing_task(writer, topic)
    editing_task = create_editing_task(editor)

    # Create crew
    crew = Crew(
        agents=[researcher, writer, editor],
        tasks=[research_task, writing_task, editing_task],
        verbose=verbose or config.VERBOSE,
    )

    # Execute crew
    try:
        result = crew.kickoff(inputs={"topic": topic})
        logger.info("Content creation completed successfully")
        return result
    except Exception as e:
        logger.error(f"Error during crew execution: {e}")
        raise


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Content Creation Multi-Agent System"
    )
    parser.add_argument(
        "--topic",
        required=True,
        help="Topic for content creation"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )

    args = parser.parse_args()

    logger.info("=" * 70)
    logger.info("Content Creation Crew")
    logger.info("=" * 70)
    logger.info(f"Topic: {args.topic}")
    logger.info(f"Model: {config.CLAUDE_MODEL}")
    logger.info(f"Verbose: {args.verbose}")
    logger.info("=" * 70)

    try:
        result = run_content_creation_crew(args.topic, verbose=args.verbose)
        print("\n" + "=" * 70)
        print("GENERATED CONTENT")
        print("=" * 70)
        print(result)
        print("=" * 70)
    except Exception as e:
        logger.error(f"Failed to create content: {e}")
        exit(1)


if __name__ == "__main__":
    main()
