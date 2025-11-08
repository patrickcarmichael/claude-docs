"""
Configuration for RAG Application

Loads settings from environment variables with sensible defaults.
See .env.example for all available options.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ============================================================================
# API Keys (Required)
# ============================================================================

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# Validate required keys
if not ANTHROPIC_API_KEY:
    raise ValueError("ANTHROPIC_API_KEY environment variable not set")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set")
if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY environment variable not set")

# ============================================================================
# Pinecone Configuration
# ============================================================================

PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT", "us-east1-aws")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "rag-documents")
PINECONE_DIMENSION = 1536  # OpenAI embeddings dimension

# ============================================================================
# Document Processing Configuration
# ============================================================================

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "200"))
SUPPORTED_EXTENSIONS = [".pdf", ".md", ".txt", ".docx"]

# ============================================================================
# Retrieval Configuration
# ============================================================================

MAX_RETRIEVED_DOCS = int(os.getenv("MAX_RETRIEVED_DOCS", "4"))
RETRIEVAL_SEARCH_TYPE = "similarity"  # or "mmr" for maximum marginal relevance

# ============================================================================
# LLM Configuration
# ============================================================================

# Claude model to use
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-3-5-sonnet-20241022")

# Generation parameters
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "1024"))
TOP_P = float(os.getenv("TOP_P", "1.0"))

# ============================================================================
# Embedding Configuration
# ============================================================================

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
EMBEDDING_DIMENSION = 1536  # For text-embedding-3-small and text-embedding-3-large

# ============================================================================
# Data Paths
# ============================================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DOCUMENTS_DIR = os.path.join(DATA_DIR, "documents")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Create directories if they don't exist
os.makedirs(DOCUMENTS_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================================================
# Logging Configuration
# ============================================================================

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.path.join(OUTPUT_DIR, "rag.log")

# ============================================================================
# Feature Flags
# ============================================================================

# Enable debug mode (verbose logging, etc.)
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# Enable caching of embeddings
ENABLE_CACHING = os.getenv("ENABLE_CACHING", "true").lower() == "true"

# Enable prompt caching (for Claude API)
ENABLE_PROMPT_CACHING = os.getenv("ENABLE_PROMPT_CACHING", "false").lower() == "true"


def get_system_prompt():
    """
    Get the system prompt for Claude.

    Can be overridden by SYSTEM_PROMPT environment variable.
    """
    default_prompt = """You are a helpful AI assistant with access to a knowledge base.
Use the provided context to answer user questions accurately and thoroughly.
If the context doesn't contain relevant information, say so explicitly.
Always cite the sources from which you retrieved information."""

    return os.getenv("SYSTEM_PROMPT", default_prompt)


def print_config():
    """Print current configuration (for debugging)."""
    print("=" * 60)
    print("RAG Application Configuration")
    print("=" * 60)
    print(f"Pinecone Index: {PINECONE_INDEX_NAME}")
    print(f"Claude Model: {CLAUDE_MODEL}")
    print(f"Embedding Model: {EMBEDDING_MODEL}")
    print(f"Chunk Size: {CHUNK_SIZE}")
    print(f"Max Retrieved Docs: {MAX_RETRIEVED_DOCS}")
    print(f"Temperature: {TEMPERATURE}")
    print(f"Debug Mode: {DEBUG}")
    print("=" * 60)


if __name__ == "__main__":
    print_config()
