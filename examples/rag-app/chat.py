#!/usr/bin/env python3
"""
Interactive Chat Interface for RAG System

Multi-turn conversation with memory and document retrieval.

Usage:
    python chat.py
    python chat.py --verbose
"""

import argparse
import logging
import sys
from typing import Optional

import config
from retriever import RAGRetriever

logging.basicConfig(
    level=config.LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ChatInterface:
    """Interactive chat interface for RAG system."""

    def __init__(self, verbose: bool = False, show_sources: bool = True):
        """
        Initialize chat interface.

        Args:
            verbose: Enable verbose output
            show_sources: Show source documents in responses
        """
        self.verbose = verbose
        self.show_sources = show_sources
        self.retriever = None
        self.conversation_chain = None

        logger.info("Initializing Chat Interface...")

    def initialize(self):
        """Initialize the RAG retriever and conversation chain."""
        try:
            self.retriever = RAGRetriever()
            self.conversation_chain = self.retriever.create_conversation_chain()
            logger.info("Chat interface initialized successfully")
            return True
        except Exception as e:
            logger.error(f"Failed to initialize: {e}")
            return False

    def display_welcome_message(self):
        """Display welcome message and instructions."""
        print("\n" + "=" * 70)
        print("RAG Interactive Chat System")
        print("=" * 70)
        print(f"Model: {config.CLAUDE_MODEL}")
        print(f"Temperature: {config.TEMPERATURE}")
        print(f"Max Retrieved Docs: {config.MAX_RETRIEVED_DOCS}")
        print("\nCommands:")
        print("  /help      - Show this help message")
        print("  /stats     - Show index statistics")
        print("  /sources   - Toggle showing sources")
        print("  /clear     - Clear conversation history")
        print("  /exit      - Exit the chat")
        print("\nType your question and press Enter to get a response.")
        print("=" * 70 + "\n")

    def show_help(self):
        """Display help message."""
        print("\nAvailable Commands:")
        print("  /help      - Show this help message")
        print("  /stats     - Show Pinecone index statistics")
        print("  /sources   - Toggle source document display")
        print("  /clear     - Clear conversation history")
        print("  /exit      - Exit the chat")
        print("\nFor regular queries, just type your question.\n")

    def show_stats(self):
        """Display index statistics."""
        try:
            stats = self.retriever.get_index_stats()
            print("\nIndex Statistics:")
            for key, value in stats.items():
                print(f"  {key}: {value}")
            print()
        except Exception as e:
            logger.error(f"Failed to get stats: {e}")

    def toggle_sources(self):
        """Toggle source document display."""
        self.show_sources = not self.show_sources
        status = "enabled" if self.show_sources else "disabled"
        print(f"\nSource display: {status}\n")

    def process_command(self, user_input: str) -> bool:
        """
        Process special commands.

        Args:
            user_input: User input to process

        Returns:
            True if a command was processed, False otherwise
        """
        command = user_input.strip().lower()

        if command == "/help":
            self.show_help()
            return True
        elif command == "/stats":
            self.show_stats()
            return True
        elif command == "/sources":
            self.toggle_sources()
            return True
        elif command == "/clear":
            self.conversation_chain.memory.clear()
            print("\nConversation history cleared.\n")
            return True
        elif command in ["/exit", "/quit", "exit", "quit"]:
            print("\nGoodbye!\n")
            return False  # Signal to exit

        return False

    def process_query(self, question: str):
        """
        Process a user query.

        Args:
            question: User's question
        """
        try:
            # Log query
            logger.info(f"Processing query: {question}")

            # Use QA chain for single query (simpler than conversation)
            result = self.retriever.query(
                question,
                return_source_documents=self.show_sources,
                verbose=self.verbose
            )

            # Display answer
            print(f"\nAssistant: {result['result']}\n")

            # Display sources if enabled
            if self.show_sources and result.get("source_documents"):
                print("Sources:")
                for i, doc in enumerate(result["source_documents"], 1):
                    source = doc.metadata.get("source", "Unknown")
                    print(f"  [{i}] {source}")
                print()

        except Exception as e:
            logger.error(f"Error processing query: {e}")
            print(f"\nError: Failed to process query. Please try again.\n")

    def run(self):
        """Run the interactive chat loop."""
        # Initialize
        if not self.initialize():
            print("Failed to initialize chat interface")
            sys.exit(1)

        # Display welcome
        self.display_welcome_message()

        # Chat loop
        try:
            while True:
                try:
                    user_input = input("You: ").strip()

                    if not user_input:
                        continue

                    # Check for commands
                    if user_input.startswith("/"):
                        if not self.process_command(user_input):
                            break  # Exit if command returns False
                    else:
                        # Process regular query
                        self.process_query(user_input)

                except KeyboardInterrupt:
                    print("\n\nInterrupted by user. Goodbye!\n")
                    break

        except EOFError:
            print("\n\nEnd of input. Goodbye!\n")
        except Exception as e:
            logger.error(f"Unexpected error: {e}", exc_info=True)
            print(f"\nUnexpected error occurred: {e}\n")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Interactive RAG Chat Interface"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    parser.add_argument(
        "--no-sources",
        action="store_true",
        help="Don't show source documents by default"
    )

    args = parser.parse_args()

    # Create and run chat interface
    chat = ChatInterface(
        verbose=args.verbose,
        show_sources=not args.no_sources
    )
    chat.run()


if __name__ == "__main__":
    main()
