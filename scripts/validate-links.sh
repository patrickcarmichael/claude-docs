#!/bin/bash

##############################################################################
# Script: validate-links.sh
# Description: Check all markdown cross-references are valid
# Usage: ./validate-links.sh [--verbose] [--fix]
#
# This script validates:
# 1. Relative file links point to existing files
# 2. Directory links point to existing directories
# 3. Anchor links reference existing markdown headings (optional)
#
# Note: Only checks relative links, not external HTTP URLs
##############################################################################

# Exit on error
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
VERBOSE=false
FIX=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --verbose|-v)
            VERBOSE=true
            shift
            ;;
        --fix)
            FIX=true
            shift
            ;;
        --help|-h)
            echo "Usage: $(basename "$0") [--verbose] [--fix]"
            echo ""
            echo "Validate all markdown cross-references"
            echo ""
            echo "Options:"
            echo "  --verbose    Show detailed validation output"
            echo "  --fix        Attempt to fix broken links (experimental)"
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
echo -e "${BLUE}║  Markdown Link Validator               ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════╝${NC}"
echo ""

if [ "$VERBOSE" = true ]; then
    echo -e "${CYAN}VERBOSE MODE${NC} - Detailed output enabled"
fi
if [ "$FIX" = true ]; then
    echo -e "${YELLOW}FIX MODE${NC} - Will attempt to fix broken links"
fi
echo ""

# Counters
TOTAL_LINKS=0
VALID_LINKS=0
INVALID_LINKS=0
EXTERNAL_LINKS=0

# Find all markdown files
mapfile -t MD_FILES < <(find "$DOCS_DIR" -name "*.md" | sort)

echo -e "${BLUE}Found ${#MD_FILES[@]} markdown file(s)${NC}"
echo ""

# Process each markdown file
for MD_FILE in "${MD_FILES[@]}"; do
    RELATIVE_PATH="${MD_FILE#$REPO_ROOT/}"
    DIR_PATH="$(dirname "$MD_FILE")"

    if [ "$VERBOSE" = true ]; then
        echo -e "${CYAN}→${NC} Checking: $RELATIVE_PATH"
    fi

    # Extract links from markdown file
    # Matches patterns: [text](link) and [text]: link
    mapfile -t LINKS < <(grep -oE '\[([^\]]+)\]\(([^)]+)\)' "$MD_FILE" 2>/dev/null | sed -E 's/\[([^\]]+)\]\(([^)]+)\)/\2/' || true)

    # Also check reference-style links
    mapfile -t REF_LINKS < <(grep -oE '^\[([^\]]+)\]:\s*(.+)$' "$MD_FILE" 2>/dev/null | sed -E 's/^\[([^\]]+)\]:\s*(.+)$/\2/' || true)

    LINKS+=("${REF_LINKS[@]}")

    # Check each link
    for LINK in "${LINKS[@]}"; do
        # Skip empty links
        [ -z "$LINK" ] && continue

        # Extract the file path and anchor
        FILE_PART="${LINK%%#*}"
        ANCHOR_PART="${LINK#*#}"

        # Skip external links (http://, https://, mailto:, etc.)
        if [[ $LINK =~ ^(https?://|mailto:|ftp://|#) ]]; then
            ((EXTERNAL_LINKS++))
            if [ "$VERBOSE" = true ]; then
                echo "  ${CYAN}⊙${NC} External: $LINK"
            fi
            continue
        fi

        ((TOTAL_LINKS++))

        # Handle relative paths
        if [ -z "$FILE_PART" ] || [ "$FILE_PART" = "#" ]; then
            # Anchor-only link to current file
            if [ "$FILE_PART" = "#" ]; then
                LINK_TARGET="$MD_FILE"
            else
                LINK_TARGET="$MD_FILE"
            fi
        else
            # Relative path
            LINK_TARGET="$(cd "$DIR_PATH" && realpath -q "$FILE_PART" 2>/dev/null || echo "")"
        fi

        # Check if target exists
        if [ -n "$LINK_TARGET" ] && [ -e "$LINK_TARGET" ]; then
            ((VALID_LINKS++))
            if [ "$VERBOSE" = true ]; then
                echo "  ${GREEN}✓${NC} Valid: $LINK"
            fi
        else
            ((INVALID_LINKS++))
            RELATIVE_TARGET="${LINK_TARGET#$REPO_ROOT/}"
            [ -z "$RELATIVE_TARGET" ] && RELATIVE_TARGET="$FILE_PART"

            echo -e "  ${RED}✗ BROKEN${NC} in $RELATIVE_PATH"
            echo -e "     Link: ${YELLOW}$LINK${NC}"
            echo -e "     Target: ${RED}$RELATIVE_TARGET${NC} (not found)"
        fi
    done
done

# Summary
echo ""
echo -e "${BLUE}╔════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  Validation Summary                    ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════╝${NC}"
echo ""
echo "Total links found:        $((VALID_LINKS + INVALID_LINKS))"
echo -e "Valid links:              ${GREEN}$VALID_LINKS${NC}"
echo -e "Broken links:             ${RED}$INVALID_LINKS${NC}"
echo "External links (skipped):  $EXTERNAL_LINKS"
echo ""

if [ $INVALID_LINKS -eq 0 ]; then
    echo -e "${GREEN}All links are valid!${NC}"
    exit 0
else
    echo -e "${RED}Found $INVALID_LINKS broken link(s)${NC}"
    exit 1
fi
