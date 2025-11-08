#!/usr/bin/env python3
"""
Single Query Execution Script

Query the RAG system with a single question.

Usage:
    python query.py "What is Claude Code?"
    python query.py "How do I use RAG?" --show-sources
"""

import argparse
import logging
import sys

import config
from retriever import RAGRetriever

logging.basicConfig(
    level=config.LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def format_result(result: dict, show_sources: bool = True) -> str:
    """
    Format the result for display.

    Args:
        result: Result dictionary from query
        show_sources: Whether to show source documents

    Returns:
        Formatted string
    """
    output = []

    # Main answer
    output.append("=" * 70)
    output.append("ANSWER")
    output.append("=" * 70)
    output.append(result.get("result", "No answer generated"))

    # Sources
    if show_sources and result.get("source_documents"):
        output.append("\n" + "=" * 70)
        output.append("SOURCES")
        output.append("=" * 70)

        for i, doc in enumerate(result["source_documents"], 1):
            source = doc.metadata.get("source", "Unknown")
            page = doc.metadata.get("page", "N/A")
            output.append(f"\n[{i}] {source}")
            if page != "N/A":
                output.append(f"    Page: {page}")
            output.append(f"    Content: {doc.page_content[:200]}...")

    output.append("\n" + "=" * 70)
    return "\n".join(output)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Query the RAG system"
    )
    parser.add_argument(
        "question",
        help="Question to ask"
    )
    parser.add_argument(
        "--show-sources",
        action="store_true",
        help="Display source documents"
    )
    parser.add_argument(
        "--num-sources",
        type=int,
        default=config.MAX_RETRIEVED_DOCS,
        help=f"Number of sources to retrieve (default: {config.MAX_RETRIEVED_DOCS})"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    parser.add_argument(
        "--show-index-stats",
        action="store_true",
        help="Show Pinecone index statistics"
    )

    args = parser.parse_args()

    # Validate question
    if not args.question.strip():
        logger.error("Question cannot be empty")
        sys.exit(1)

    logger.info("=" * 70)
    logger.info("RAG Query System")
    logger.info("=" * 70)
    logger.info(f"Question: {args.question}")
    logger.info(f"Show Sources: {args.show_sources}")
    logger.info(f"Num Sources: {args.num_sources}")
    logger.info("=" * 70)

    try:
        # Initialize retriever
        logger.info("Initializing RAG Retriever...")
        retriever = RAGRetriever()

        # Show index stats if requested
        if args.show_index_stats:
            stats = retriever.get_index_stats()
            logger.info(f"Index Statistics: {stats}")

        # Execute query
        logger.info(f"Executing query...")
        result = retriever.query(
            args.question,
            return_source_documents=args.show_sources,
            verbose=args.verbose
        )

        # Display result
        print(format_result(result, show_sources=args.show_sources))

    except Exception as e:
        logger.error(f"Query failed: {e}", exc_info=args.verbose)
        sys.exit(1)


if __name__ == "__main__":
    main()
