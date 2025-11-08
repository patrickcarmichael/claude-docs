#!/bin/bash

##############################################################################
# Script: search-docs.sh
# Description: Search across all documentation files with grep
# Usage: ./search-docs.sh <search-term> [options]
# Examples:
#   ./search-docs.sh "Claude Code"
#   ./search-docs.sh "hooks" -i  (case-insensitive)
#   ./search-docs.sh "API" -l    (list files only)
##############################################################################

# Exit on error
set -e

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Script directory and repo root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
DOCS_DIR="$REPO_ROOT/docs"

# Display usage information
usage() {
    echo -e "${BLUE}Usage:${NC} $(basename "$0") <search-term> [grep-options]"
    echo ""
    echo -e "${BLUE}Search across all markdown and text files in docs/${NC}"
    echo ""
    echo -e "${YELLOW}Arguments:${NC}"
    echo "  <search-term>    The text to search for (required)"
    echo "  [grep-options]   Optional grep flags (-i for case-insensitive, -l for files only, etc.)"
    echo ""
    echo -e "${YELLOW}Examples:${NC}"
    echo "  $(basename "$0") 'Claude Code'"
    echo "  $(basename "$0") 'hooks' -i"
    echo "  $(basename "$0") 'configuration' -l"
    echo "  $(basename "$0") '^##' -r              # Search headings"
    echo ""
    exit 1
}

# Validate input
if [ $# -lt 1 ]; then
    echo -e "${RED}Error: Search term required${NC}"
    usage
fi

SEARCH_TERM="$1"
shift

# Verify docs directory exists
if [ ! -d "$DOCS_DIR" ]; then
    echo -e "${RED}Error: Documentation directory not found at $DOCS_DIR${NC}"
    exit 1
fi

echo -e "${BLUE}Searching for:${NC} '${SEARCH_TERM}' in $DOCS_DIR"
echo -e "${BLUE}Files searched:${NC}"

# Count total files
TOTAL_FILES=$(find "$DOCS_DIR" \( -name "*.md" -o -name "*.txt" \) | wc -l)
echo "  - Found $TOTAL_FILES documentation files"
echo ""

# Perform search
SEARCH_RESULTS=$(grep -r "$SEARCH_TERM" "$DOCS_DIR" \
    --include="*.md" \
    --include="*.txt" \
    --exclude-dir=".git" \
    "$@" 2>/dev/null || true)

# Handle search results
if [ -z "$SEARCH_RESULTS" ]; then
    echo -e "${YELLOW}No matches found for:${NC} '${SEARCH_TERM}'"
    exit 0
fi

# Count and display results
MATCH_COUNT=$(echo "$SEARCH_RESULTS" | grep -c . || echo 0)
echo -e "${GREEN}Found $MATCH_COUNT match(es):${NC}"
echo ""
echo "$SEARCH_RESULTS"
echo ""
echo -e "${GREEN}Search complete${NC}"
