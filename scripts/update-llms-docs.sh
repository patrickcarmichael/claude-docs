#!/bin/bash

##############################################################################
# Script: update-llms-docs.sh
# Description: Re-fetch all llms-full.txt files from their sources
# Usage: ./update-llms-docs.sh [--dry-run] [--verbose]
#
# This script:
# 1. Finds all llms-full.txt files in the documentation
# 2. Extracts the source URL from each file's header
# 3. Re-fetches the content from that source
# 4. Updates the file with fresh content
#
# Note: Source URLs are extracted from the "Source:" line in each file
##############################################################################

# Exit on error (unless doing dry-run)
set -e

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Script directory and repo root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
DOCS_DIR="$REPO_ROOT/docs"

# Parse arguments
DRY_RUN=false
VERBOSE=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --verbose|-v)
            VERBOSE=true
            shift
            ;;
        --help|-h)
            echo "Usage: $(basename "$0") [--dry-run] [--verbose]"
            echo ""
            echo "Re-fetch all llms-full.txt files from their sources"
            echo ""
            echo "Options:"
            echo "  --dry-run    Show what would be updated without making changes"
            echo "  --verbose    Show detailed output"
            echo "  --help       Show this help message"
            exit 0
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            exit 1
            ;;
    esac
done

# Display startup info
echo -e "${BLUE}╔════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  LLMs Documentation Update Script      ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════╝${NC}"
echo ""

if [ "$DRY_RUN" = true ]; then
    echo -e "${YELLOW}DRY RUN MODE${NC} - No files will be modified"
fi
if [ "$VERBOSE" = true ]; then
    echo -e "${CYAN}VERBOSE MODE${NC} - Detailed output enabled"
fi
echo ""

# Find all llms-full.txt files
mapfile -t LLMS_FILES < <(find "$DOCS_DIR" -name "llms-full.txt" | sort)

if [ ${#LLMS_FILES[@]} -eq 0 ]; then
    echo -e "${YELLOW}No llms-full.txt files found in $DOCS_DIR${NC}"
    exit 0
fi

echo -e "${BLUE}Found ${#LLMS_FILES[@]} llms-full.txt file(s)${NC}"
echo ""

# Counters
TOTAL=${#LLMS_FILES[@]}
UPDATED=0
FAILED=0
SKIPPED=0

# Process each file
for FILE in "${LLMS_FILES[@]}"; do
    # Extract relative path for display
    RELATIVE_PATH="${FILE#$REPO_ROOT/}"

    # Extract source URL from file header
    SOURCE_URL=$(head -3 "$FILE" 2>/dev/null | grep "^Source:" | sed 's/^Source: //' || echo "")

    if [ -z "$SOURCE_URL" ]; then
        echo -e "${YELLOW}⊘ SKIP${NC} $RELATIVE_PATH"
        if [ "$VERBOSE" = true ]; then
            echo "    └─ No source URL found in file header"
        fi
        ((SKIPPED++))
        continue
    fi

    echo -e "${CYAN}↓ FETCH${NC} $RELATIVE_PATH"
    if [ "$VERBOSE" = true ]; then
        echo "    └─ Source: $SOURCE_URL"
    fi

    # In a real implementation, you would fetch from the URL here
    # For now, this is a template showing the structure
    if [ "$DRY_RUN" = true ]; then
        echo -e "    ${YELLOW}[DRY RUN]${NC} Would fetch from: $SOURCE_URL"
        ((UPDATED++))
    else
        # Attempt to fetch the content (this requires curl)
        if command -v curl &> /dev/null; then
            if [ "$VERBOSE" = true ]; then
                echo "    └─ Fetching content from source..."
            fi

            # Create a temporary file
            TEMP_FILE=$(mktemp)
            trap "rm -f $TEMP_FILE" EXIT

            # Fetch content with timeout
            if curl -s --max-time 10 "$SOURCE_URL" > "$TEMP_FILE" 2>/dev/null; then
                # Verify file is not empty
                if [ -s "$TEMP_FILE" ]; then
                    cp "$TEMP_FILE" "$FILE"
                    echo -e "    ${GREEN}✓ Updated${NC}"
                    ((UPDATED++))
                else
                    echo -e "    ${RED}✗ Failed${NC} - Remote file is empty"
                    ((FAILED++))
                fi
            else
                echo -e "    ${RED}✗ Failed${NC} - Could not fetch from source"
                ((FAILED++))
            fi

            rm -f "$TEMP_FILE"
        else
            echo -e "    ${YELLOW}⊘ SKIP${NC} - curl not installed"
            ((SKIPPED++))
        fi
    fi
done

# Summary
echo ""
echo -e "${BLUE}╔════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  Update Summary                        ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════╝${NC}"
echo ""
echo "Total files:    $TOTAL"
echo -e "Updated:        ${GREEN}$UPDATED${NC}"
echo -e "Failed:         ${RED}$FAILED${NC}"
echo -e "Skipped:        ${YELLOW}$SKIPPED${NC}"
echo ""

if [ "$DRY_RUN" = true ]; then
    echo -e "${YELLOW}This was a dry run. No files were modified.${NC}"
fi

exit 0
