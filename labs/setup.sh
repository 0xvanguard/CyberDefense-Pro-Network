#!/bin/bash
# ══════════════════════════════════════════════════════════════
# CDPN Lab Setup Script — Universal launcher for all labs
# ══════════════════════════════════════════════════════════════
#
# Usage:
#   ./setup.sh <lab-path>          # Start a lab
#   ./setup.sh <lab-path> --stop   # Stop a lab
#   ./setup.sh <lab-path> --status # Check lab status
#   ./setup.sh --list              # List all available labs
#   ./setup.sh --validate          # Validate all docker-compose files
#
# Examples:
#   ./setup.sh intermedio/pentest-01
#   ./setup.sh avanzado/redteam-c2-01
#   ./setup.sh --list
# ══════════════════════════════════════════════════════════════

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LABS_DIR="$SCRIPT_DIR"

# ── Colors ──
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# ── Functions ──

print_banner() {
    echo -e "${CYAN}"
    echo "  ╔══════════════════════════════════════════╗"
    echo "  ║   🛡️  CDPN Lab Launcher                  ║"
    echo "  ║   CyberDefense Pro Network                ║"
    echo "  ╚══════════════════════════════════════════╝"
    echo -e "${NC}"
}

list_labs() {
    echo -e "${BLUE}Available Labs:${NC}"
    echo ""
    
    for level in fundamentos intermedio avanzado expert; do
        if [ -d "$LABS_DIR/$level" ]; then
            echo -e "${YELLOW}━━━ $(echo $level | tr '[:lower:]' '[:upper:]') ━━━${NC}"
            for lab in "$LABS_DIR/$level"/*/; do
                if [ -d "$lab" ]; then
                    lab_name=$(basename "$lab")
                    has_docker="❌"
                    has_readme="❌"
                    has_setup="❌"
                    
                    [ -f "$lab/docker-compose.yml" ] && has_docker="✅"
                    [ -f "$lab/README.md" ] && has_readme="✅"
                    [ -f "$lab/setup.sh" ] && has_setup="✅"
                    
                    echo -e "  ${GREEN}$lab_name${NC}  Docker:$has_docker  README:$has_readme  Setup:$has_setup"
                fi
            done
            echo ""
        fi
    done
}

validate_labs() {
    echo -e "${BLUE}Validating all docker-compose files...${NC}"
    echo ""
    
    errors=0
    for f in $(find "$LABS_DIR" -name "docker-compose.yml" | sort); do
        dir=$(dirname "$f")
        lab_name=$(echo "$dir" | sed "s|$LABS_DIR/||")
        
        if docker compose -f "$f" config --quiet 2>/dev/null; then
            echo -e "  ${GREEN}✅${NC} $lab_name"
        else
            echo -e "  ${RED}❌${NC} $lab_name — INVALID compose file"
            errors=$((errors + 1))
        fi
    done
    
    echo ""
    if [ $errors -eq 0 ]; then
        echo -e "${GREEN}All docker-compose files are valid!${NC}"
    else
        echo -e "${RED}$errors compose files have errors${NC}"
    fi
}

start_lab() {
    local lab_path="$1"
    local full_path="$LABS_DIR/$lab_path"
    
    if [ ! -d "$full_path" ]; then
        echo -e "${RED}Error: Lab '$lab_path' not found${NC}"
        echo "Use --list to see available labs"
        exit 1
    fi
    
    if [ ! -f "$full_path/docker-compose.yml" ]; then
        echo -e "${RED}Error: No docker-compose.yml found in $lab_path${NC}"
        exit 1
    fi
    
    echo -e "${CYAN}Starting lab: $lab_path${NC}"
    echo ""
    
    # Check if Docker is running
    if ! docker info > /dev/null 2>&1; then
        echo -e "${RED}Error: Docker is not running${NC}"
        echo "Start Docker Desktop or run: sudo systemctl start docker"
        exit 1
    fi
    
    cd "$full_path"
    
    # Build and start
    echo -e "${YELLOW}Building and starting containers...${NC}"
    docker compose up -d --build
    
    echo ""
    echo -e "${GREEN}✅ Lab started successfully!${NC}"
    echo ""
    
    # Show service status
    echo -e "${BLUE}Service Status:${NC}"
    docker compose ps
    
    # Show access info
    echo ""
    echo -e "${YELLOW}Access Info:${NC}"
    docker compose ps --format "table {{.Name}}\t{{.Ports}}" | grep -v "NAME"
    
    echo ""
    echo -e "${CYAN}To stop: ./setup.sh $lab_path --stop${NC}"
    echo -e "${CYAN}To view logs: cd $lab_path && docker compose logs -f${NC}"
}

stop_lab() {
    local lab_path="$1"
    local full_path="$LABS_DIR/$lab_path"
    
    if [ ! -f "$full_path/docker-compose.yml" ]; then
        echo -e "${RED}Error: No docker-compose.yml found in $lab_path${NC}"
        exit 1
    fi
    
    echo -e "${YELLOW}Stopping lab: $lab_path${NC}"
    cd "$full_path"
    docker compose down -v
    
    echo -e "${GREEN}✅ Lab stopped${NC}"
}

status_lab() {
    local lab_path="$1"
    local full_path="$LABS_DIR/$lab_path"
    
    if [ ! -f "$full_path/docker-compose.yml" ]; then
        echo -e "${RED}Error: No docker-compose.yml found in $lab_path${NC}"
        exit 1
    fi
    
    cd "$full_path"
    docker compose ps
}

# ── Main ──

print_banner

case "${1:-}" in
    --list|-l)
        list_labs
        ;;
    --validate|-v)
        validate_labs
        ;;
    --stop|-s)
        if [ -z "${2:-}" ]; then
            echo -e "${RED}Usage: ./setup.sh <lab-path> --stop${NC}"
            exit 1
        fi
        stop_lab "$2"
        ;;
    --status)
        if [ -z "${2:-}" ]; then
            echo -e "${RED}Usage: ./setup.sh <lab-path> --status${NC}"
            exit 1
        fi
        status_lab "$2"
        ;;
    "")
        echo -e "${YELLOW}Usage:${NC}"
        echo "  ./setup.sh <lab-path>          # Start a lab"
        echo "  ./setup.sh <lab-path> --stop   # Stop a lab"
        echo "  ./setup.sh <lab-path> --status # Check status"
        echo "  ./setup.sh --list              # List all labs"
        echo "  ./setup.sh --validate          # Validate compose files"
        echo ""
        echo -e "${YELLOW}Examples:${NC}"
        echo "  ./setup.sh intermedio/pentest-01"
        echo "  ./setup.sh avanzado/redteam-c2-01"
        echo "  ./setup.sh --list"
        ;;
    *)
        if [ "${2:-}" = "--stop" ]; then
            stop_lab "$1"
        elif [ "${2:-}" = "--status" ]; then
            status_lab "$1"
        else
            start_lab "$1"
        fi
        ;;
esac
