"""
Configuration for Multi-Agent System with CrewAI

Loads settings from environment variables with sensible defaults.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ============================================================================
# API Keys
# ============================================================================

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

if not ANTHROPIC_API_KEY:
    raise ValueError("ANTHROPIC_API_KEY environment variable not set")

# ============================================================================
# LLM Configuration
# ============================================================================

CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-3-5-sonnet-20241022")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2000"))
TOP_P = float(os.getenv("TOP_P", "1.0"))

# ============================================================================
# CrewAI Configuration
# ============================================================================

VERBOSE = os.getenv("VERBOSE", "false").lower() == "true"
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# Agent memory settings
MEMORY_BUFFER_SIZE = int(os.getenv("MEMORY_BUFFER_SIZE", "10"))
ENABLE_MEMORY = os.getenv("ENABLE_MEMORY", "true").lower() == "true"

# Task settings
MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", "10"))
TASK_TIMEOUT = int(os.getenv("TASK_TIMEOUT", "300"))  # seconds

# ============================================================================
# Paths
# ============================================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)

# ============================================================================
# Logging
# ============================================================================

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.path.join(LOGS_DIR, "crew.log")


def print_config():
    """Print configuration for debugging."""
    print("=" * 60)
    print("CrewAI Multi-Agent Configuration")
    print("=" * 60)
    print(f"Model: {CLAUDE_MODEL}")
    print(f"Temperature: {TEMPERATURE}")
    print(f"Max Tokens: {MAX_TOKENS}")
    print(f"Verbose: {VERBOSE}")
    print(f"Debug: {DEBUG}")
    print(f"Max Iterations: {MAX_ITERATIONS}")
    print("=" * 60)


if __name__ == "__main__":
    print_config()
