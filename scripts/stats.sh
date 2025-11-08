#!/bin/bash

##############################################################################
# Script: stats.sh
# Description: Show collection statistics (file count, sizes, categories)
# Usage: ./stats.sh [--json] [--category <name>]
#
# This script displays:
# 1. Total file counts by type (markdown, text, etc.)
# 2. Total size of documentation
# 3. Breakdown by category (subdirectory)
# 4. Average file size
# 5. Largest/smallest files
##############################################################################

# Exit on error
set -e

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

# Script directory and repo root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
DOCS_DIR="$REPO_ROOT/docs"

# Parse arguments
JSON_OUTPUT=false
FILTER_CATEGORY=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --json)
            JSON_OUTPUT=true
            shift
            ;;
        --category)
            FILTER_CATEGORY="$2"
            shift 2
            ;;
        --help|-h)
            echo "Usage: $(basename "$0") [--json] [--category <name>]"
            echo ""
            echo "Show documentation collection statistics"
            echo ""
            echo "Options:"
            echo "  --json              Output in JSON format"
            echo "  --category <name>   Show stats for specific category"
            echo "  --help              Show this help message"
            exit 0
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            exit 1
            ;;
    esac
done

# Helper function: convert bytes to human-readable format
format_bytes() {
    local bytes=$1
    if [ "$bytes" -lt 1024 ]; then
        echo "${bytes}B"
    elif [ "$bytes" -lt 1048576 ]; then
        echo "$(echo "scale=1; $bytes / 1024" | bc)KB"
    else
        echo "$(echo "scale=1; $bytes / 1048576" | bc)MB"
    fi
}

# Collect statistics
if [ -z "$FILTER_CATEGORY" ]; then
    STATS_DIR="$DOCS_DIR"
else
    STATS_DIR="$DOCS_DIR/$FILTER_CATEGORY"
fi

if [ ! -d "$STATS_DIR" ]; then
    echo -e "${RED}Error: Directory not found: $STATS_DIR${NC}"
    exit 1
fi

# Count files by type
MD_COUNT=$(find "$STATS_DIR" -name "*.md" -type f 2>/dev/null | wc -l)
TXT_COUNT=$(find "$STATS_DIR" -name "*.txt" -type f 2>/dev/null | wc -l)
OTHER_COUNT=$(find "$STATS_DIR" -type f ! -name "*.md" ! -name "*.txt" ! -name ".*" 2>/dev/null | wc -l)
TOTAL_FILES=$((MD_COUNT + TXT_COUNT + OTHER_COUNT))

# Calculate sizes
TOTAL_SIZE=$(find "$STATS_DIR" -type f \( -name "*.md" -o -name "*.txt" \) -exec du -cb {} + 2>/dev/null | tail -1 | awk '{print $1}')
[ -z "$TOTAL_SIZE" ] && TOTAL_SIZE=0

MD_SIZE=$(find "$STATS_DIR" -name "*.md" -type f -exec du -cb {} + 2>/dev/null | tail -1 | awk '{print $1}')
[ -z "$MD_SIZE" ] && MD_SIZE=0

TXT_SIZE=$(find "$STATS_DIR" -name "*.txt" -type f -exec du -cb {} + 2>/dev/null | tail -1 | awk '{print $1}')
[ -z "$TXT_SIZE" ] && TXT_SIZE=0

# Calculate averages
if [ $MD_COUNT -gt 0 ]; then
    AVG_MD_SIZE=$((MD_SIZE / MD_COUNT))
else
    AVG_MD_SIZE=0
fi

if [ $TOTAL_FILES -gt 0 ]; then
    AVG_FILE_SIZE=$((TOTAL_SIZE / TOTAL_FILES))
else
    AVG_FILE_SIZE=0
fi

# Find directory count
DIR_COUNT=$(find "$STATS_DIR" -mindepth 1 -maxdepth 1 -type d ! -name ".*" 2>/dev/null | wc -l)

# Get largest files
mapfile -t LARGEST_FILES < <(find "$STATS_DIR" -type f \( -name "*.md" -o -name "*.txt" \) -printf '%s %p\n' 2>/dev/null | sort -rn | head -3 | awk '{print $2}')

# Get smallest non-empty files
mapfile -t SMALLEST_FILES < <(find "$STATS_DIR" -type f \( -name "*.md" -o -name "*.txt" \) -size +0 -printf '%s %p\n' 2>/dev/null | sort -n | head -3 | awk '{print $2}')

# JSON Output
if [ "$JSON_OUTPUT" = true ]; then
    cat <<EOF
{
  "directory": "$STATS_DIR",
  "files": {
    "markdown": $MD_COUNT,
    "text": $TXT_COUNT,
    "other": $OTHER_COUNT,
    "total": $TOTAL_FILES
  },
  "directories": $DIR_COUNT,
  "sizes": {
    "markdown_bytes": $MD_SIZE,
    "text_bytes": $TXT_SIZE,
    "total_bytes": $TOTAL_SIZE,
    "markdown_formatted": "$(format_bytes $MD_SIZE)",
    "text_formatted": "$(format_bytes $TXT_SIZE)",
    "total_formatted": "$(format_bytes $TOTAL_SIZE)"
  },
  "averages": {
    "markdown_size_bytes": $AVG_MD_SIZE,
    "file_size_bytes": $AVG_FILE_SIZE,
    "markdown_size_formatted": "$(format_bytes $AVG_MD_SIZE)",
    "file_size_formatted": "$(format_bytes $AVG_FILE_SIZE)"
  }
}
EOF
    exit 0
fi

# Text Output
echo -e "${BLUE}╔════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  Documentation Statistics              ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════╝${NC}"
echo ""

echo -e "${CYAN}Directory:${NC} $STATS_DIR"
echo ""

echo -e "${YELLOW}File Counts:${NC}"
echo "  Markdown files (.md):        $MD_COUNT"
echo "  Text files (.txt):           $TXT_COUNT"
echo "  Other files:                 $OTHER_COUNT"
echo -e "  ${PURPLE}Total files:${NC}                  ${PURPLE}$TOTAL_FILES${NC}"
echo ""

echo -e "${YELLOW}Directory Structure:${NC}"
echo "  Subdirectories:              $DIR_COUNT"
echo ""

echo -e "${YELLOW}Storage Size:${NC}"
echo "  Markdown files:              $(format_bytes $MD_SIZE)"
echo "  Text files:                  $(format_bytes $TXT_SIZE)"
echo -e "  ${PURPLE}Total size:${NC}                   ${PURPLE}$(format_bytes $TOTAL_SIZE)${NC}"
echo ""

echo -e "${YELLOW}Average File Sizes:${NC}"
echo "  Markdown (average):          $(format_bytes $AVG_MD_SIZE)"
echo "  All files (average):         $(format_bytes $AVG_FILE_SIZE)"
echo ""

# Largest files
if [ ${#LARGEST_FILES[@]} -gt 0 ] && [ -n "${LARGEST_FILES[0]}" ]; then
    echo -e "${YELLOW}Largest Files:${NC}"
    for i in "${!LARGEST_FILES[@]}"; do
        FILE="${LARGEST_FILES[$i]}"
        RELATIVE_FILE="${FILE#$REPO_ROOT/}"
        SIZE=$(du -b "$FILE" | awk '{print $1}')
        echo "  $(($i + 1)). $(format_bytes $SIZE) - $RELATIVE_FILE"
    done
    echo ""
fi

# Categories breakdown (if not filtering)
if [ -z "$FILTER_CATEGORY" ]; then
    echo -e "${YELLOW}Categories:${NC}"
    mapfile -t CATEGORIES < <(find "$DOCS_DIR" -mindepth 1 -maxdepth 1 -type d ! -name ".*" | sort)

    for CATEGORY in "${CATEGORIES[@]}"; do
        CAT_NAME=$(basename "$CATEGORY")
        CAT_MD=$(find "$CATEGORY" -name "*.md" -type f 2>/dev/null | wc -l)
        CAT_TXT=$(find "$CATEGORY" -name "*.txt" -type f 2>/dev/null | wc -l)
        CAT_SIZE=$(find "$CATEGORY" -type f \( -name "*.md" -o -name "*.txt" \) -exec du -cb {} + 2>/dev/null | tail -1 | awk '{print $1}')
        [ -z "$CAT_SIZE" ] && CAT_SIZE=0

        if [ $((CAT_MD + CAT_TXT)) -gt 0 ]; then
            printf "  %-25s %3d files  %3d MD  %3d TXT  %8s\n" \
                "$CAT_NAME:" "$((CAT_MD + CAT_TXT))" "$CAT_MD" "$CAT_TXT" "$(format_bytes $CAT_SIZE)"
        fi
    done
    echo ""
fi

echo -e "${GREEN}Statistics complete${NC}"
