"""
Terminal display utilities — colors, tables, progress.
"""

import sys


# ANSI Colors
class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"


def print_header(text: str, char: str = "═"):
    """Print a formatted header."""
    width = min(60, max(len(text) + 4, 40))
    print(f"\n{C.BOLD}{C.CYAN}{char * width}{C.RESET}")
    print(f"{C.BOLD}{C.CYAN}  {text}{C.RESET}")
    print(f"{C.BOLD}{C.CYAN}{char * width}{C.RESET}\n")


def print_subheader(text: str):
    """Print a formatted subheader."""
    print(f"\n{C.BOLD}{C.BLUE}▸ {text}{C.RESET}")


def print_success(text: str):
    """Print a success message."""
    print(f"  {C.GREEN}✓{C.RESET} {text}")


def print_error(text: str):
    """Print an error message."""
    print(f"  {C.RED}✗{C.RESET} {text}")


def print_warning(text: str):
    """Print a warning message."""
    print(f"  {C.YELLOW}⚠{C.RESET} {text}")


def print_info(text: str):
    """Print an info message."""
    print(f"  {C.DIM}ℹ{C.RESET} {text}")


def print_table(headers: list, rows: list, col_widths: list = None):
    """Print a formatted table."""
    if not col_widths:
        col_widths = []
        for i, header in enumerate(headers):
            max_w = len(header)
            for row in rows:
                if i < len(row):
                    max_w = max(max_w, len(str(row[i])))
            col_widths.append(min(max_w + 2, 40))

    # Header
    header_line = ""
    for i, header in enumerate(headers):
        header_line += f"{C.BOLD}{header:<{col_widths[i]}}{C.RESET}"
    print(f"  {header_line}")
    print(f"  {C.DIM}{'─' * sum(col_widths)}{C.RESET}")

    # Rows
    for row in rows:
        line = ""
        for i in range(len(headers)):
            val = str(row[i]) if i < len(row) else ""
            line += f"{val:<{col_widths[i]}}"
        print(f"  {line}")


def print_repo_card(name: str, data: dict, index: int = None):
    """Print a single repo as a card."""
    prefix = f"#{index} " if index else ""
    print(f"  {C.BOLD}{C.CYAN}{prefix}{data.get('name', name)}{C.RESET}")
    print(f"    {data.get('description', 'No description')}")
    tags = " ".join([f"{C.DIM}[{t}]{C.RESET}" for t in data.get("tags", [])])
    print(f"    {tags}")
    print()


def print_category_card(cat_name: str, cat_data: dict):
    """Print a category header card."""
    color = cat_data.get("color", C.WHITE)
    print(f"\n  {color}{C.BOLD}{'━' * 50}{C.RESET}")
    print(f"  {color}{C.BOLD}  {cat_name}{C.RESET}")
    print(f"  {color}{C.BOLD}{'━' * 50}{C.RESET}\n")


def print_progress(current: int, total: int, text: str = ""):
    """Print a progress bar."""
    pct = int((current / total) * 100) if total > 0 else 0
    filled = int(pct / 5)
    bar = "█" * filled + "░" * (20 - filled)
    print(f"\r  {C.CYAN}{bar}{C.RESET} {pct}% {C.DIM}{text}{C.RESET}", end="", flush=True)
    if current == total:
        print()


def print_banner():
    """Print the CLI banner."""
    banner = f"""
{C.BOLD}{C.CYAN}
  ╔══════════════════════════════════════════╗
  ║                                          ║
  ║    0x{C.PURPLE}vanguard{C.CYAN} — Cybersecurity CLI        ║
  ║                                          ║
  ║    {C.WHITE}35 tools. One empire.                {C.CYAN}║
  ║                                          ║
  ╚══════════════════════════════════════════╝
{C.RESET}"""
    print(banner)
