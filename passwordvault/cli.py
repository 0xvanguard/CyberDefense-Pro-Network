#!/usr/bin/env python3
"""
PasswordVault CLI — Password manager from the command line.

Usage:
    python cli.py add --service github.com --username user@email.com --password mypass
    python cli.py get --service github.com
    python cli.py generate --length 20
    python cli.py passphrase --words 5
    python cli.py strength --password mypassword
    python cli.py list
    python cli.py search "github"
    python cli.py delete ENTRY-0001
    python cli.py stats
"""

import argparse
import getpass
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from vault import PasswordVault


def get_vault():
    password = os.environ.get("VAULT_PASSWORD")
    if not password:
        password = getpass.getpass("Master password: ")
    return PasswordVault(master_password=password)


def cmd_add(args):
    """Add a password entry."""
    vault = get_vault()

    password = args.password
    if not password:
        import secrets
        import string
        charset = string.ascii_letters + string.digits + "!@#$%^&*"
        password = "".join(secrets.choice(charset) for _ in range(args.length))

    entry = vault.add(
        service=args.service, username=args.username,
        password=password, url=args.url, notes=args.notes,
        category=args.category, favorite=args.favorite,
    )

    strength = vault.analyze_password(password)

    print(f"\n🔐 Entry Added\n{'='*40}")
    print(f"  ID:       {entry.id}")
    print(f"  Service:  {entry.service}")
    print(f"  Username: {entry.username}")
    print(f"  Category: {entry.category}")
    print(f"  Strength: {entry.strength_score}/100 ({strength.label})")
    print(f"  Crack Time: {strength.crack_time}")


def cmd_get(args):
    """Get a password entry."""
    vault = get_vault()

    if args.id:
        entry = vault.get_by_id(args.id)
    else:
        entry = vault.get(args.service)

    if not entry:
        print(f"\n❌ Entry not found")
        return

    password = vault.get_password(entry.id)

    print(f"\n🔑 {entry.service}\n{'='*40}")
    print(f"  ID:       {entry.id}")
    print(f"  Service:  {entry.service}")
    print(f"  Username: {entry.username}")
    print(f"  Password: {'*' * len(password)}")
    print(f"  URL:      {entry.url or 'N/A'}")
    print(f"  Notes:    {entry.notes or 'N/A'}")
    print(f"  Category: {entry.category}")
    print(f"  Strength: {entry.strength_score}/100")
    print(f"  Created:  {entry.created[:19]}")

    if args.show:
        print(f"\n  📋 Password: {password}")


def cmd_generate(args):
    """Generate a secure password."""
    vault = get_vault()

    passwords = []
    for _ in range(args.count):
        pw = vault.generate_password(
            length=args.length,
            uppercase=not args.no_upper,
            digits=not args.no_digits,
            symbols=not args.no_symbols,
        )
        passwords.append(pw)

    print(f"\n🎲 Generated Passwords\n{'='*40}")
    for i, pw in enumerate(passwords, 1):
        strength = vault.analyze_password(pw)
        print(f"  {i}. {pw}")
        print(f"     Strength: {strength.score}/100 ({strength.label})")


def cmd_passphrase(args):
    """Generate a passphrase."""
    vault = get_vault()

    passphrases = []
    for _ in range(args.count):
        pp = vault.generate_passphrase(words=args.words, separator=args.separator)
        passphrases.append(pp)

    print(f"\n🎲 Generated Passphrases\n{'='*40}")
    for i, pp in enumerate(passphrases, 1):
        strength = vault.analyze_password(pp)
        print(f"  {i}. {pp}")
        print(f"     Strength: {strength.score}/100 ({strength.label})")


def cmd_strength(args):
    """Analyze password strength."""
    vault = get_vault()
    strength = vault.analyze_password(args.password)

    bar = "█" * (strength.score // 5) + "░" * (20 - strength.score // 5)

    print(f"\n🔐 Password Strength Analysis\n{'='*50}")
    print(f"  Score:      {bar} {strength.score}/100")
    print(f"  Label:      {strength.label}")
    print(f"  Entropy:    {strength.entropy} bits")
    print(f"  Length:     {strength.length} chars")
    print(f"  Charset:    {strength.charset_size} chars")
    print(f"  Crack Time: {strength.crack_time}")
    print(f"\n  Features:")
    print(f"    Uppercase: {'✅' if strength.has_uppercase else '❌'}")
    print(f"    Lowercase: {'✅' if strength.has_lowercase else '❌'}")
    print(f"    Digits:    {'✅' if strength.has_digits else '❌'}")
    print(f"    Symbols:   {'✅' if strength.has_symbols else '❌'}")


def cmd_list(args):
    """List entries."""
    vault = get_vault()
    entries = vault.list_entries(category=args.category, favorite_only=args.favorites)

    label = args.category or ("favorites" if args.favorites else "all")

    print(f"\n📋 Vault ({label}) — {len(entries)}\n{'='*60}")
    print(f"{'ID':<14} {'Service':<20} {'Username':<20} {'Str'}")
    print("-" * 60)

    for e in entries:
        fav = "⭐" if e.favorite else " "
        strength_bar = "█" * (e.strength_score // 20) + "░" * (5 - e.strength_score // 20)
        print(f"{e.id:<14} {fav} {e.service:<18} {e.username:<20} {strength_bar}")


def cmd_search(args):
    """Search entries."""
    vault = get_vault()
    results = vault.search(args.query)

    print(f"\n🔍 Search: '{args.query}' — {len(results)} results\n{'='*60}")
    for e in results:
        print(f"  {e.id} — {e.service} ({e.username})")


def cmd_delete(args):
    """Delete entry."""
    vault = get_vault()
    entry = vault.get_by_id(args.id)

    if not entry:
        print(f"\n❌ Entry not found: {args.id}")
        return

    ok = vault.delete(args.id)
    if ok:
        print(f"\n🗑️  Deleted: {entry.service} ({entry.username})")
    else:
        print(f"\n❌ Failed to delete: {args.id}")


def cmd_stats(args):
    """Show statistics."""
    vault = get_vault()
    stats = vault.get_statistics()

    print(f"\n📊 Vault Statistics\n{'='*40}")
    print(f"  Total Entries: {stats['total_entries']}")
    print(f"  Favorites:     {stats['favorites']}")

    if stats["categories"]:
        print(f"\n  Categories:")
        for cat, count in stats["categories"].items():
            print(f"    {cat:<20} {count}")

    if stats["strength_distribution"]:
        print(f"\n  Strength Distribution:")
        icons = {"Very Strong": "🟢", "Strong": "🟢", "Fair": "🟡", "Weak": "🟠", "Very Weak": "🔴"}
        for label, count in stats["strength_distribution"].items():
            if count > 0:
                print(f"    {icons.get(label, '⚪')} {label:<15} {count}")


def main():
    parser = argparse.ArgumentParser(
        description="🔐 PasswordVault — Password Manager"
    )
    sub = parser.add_subparsers(dest="command")

    # add
    add_p = sub.add_parser("add", help="Add entry")
    add_p.add_argument("--service", "-s", required=True)
    add_p.add_argument("--username", "-u", required=True)
    add_p.add_argument("--password", "-p", default="")
    add_p.add_argument("--url", default="")
    add_p.add_argument("--notes", "-n", default="")
    add_p.add_argument("--category", "-c", default="general")
    add_p.add_argument("--favorite", action="store_true")
    add_p.add_argument("--length", type=int, default=16)

    # get
    get_p = sub.add_parser("get", help="Get entry")
    get_p.add_argument("--service", "-s", default="")
    get_p.add_argument("--id", default="")
    get_p.add_argument("--show", action="store_true")

    # generate
    gen_p = sub.add_parser("generate", help="Generate password")
    gen_p.add_argument("--length", "-l", type=int, default=16)
    gen_p.add_argument("--count", type=int, default=1)
    gen_p.add_argument("--no-upper", action="store_true")
    gen_p.add_argument("--no-digits", action="store_true")
    gen_p.add_argument("--no-symbols", action="store_true")

    # passphrase
    pp_p = sub.add_parser("passphrase", help="Generate passphrase")
    pp_p.add_argument("--words", "-w", type=int, default=4)
    pp_p.add_argument("--separator", default="-")
    pp_p.add_argument("--count", type=int, default=1)

    # strength
    str_p = sub.add_parser("strength", help="Analyze strength")
    str_p.add_argument("--password", "-p", required=True)

    # list
    list_p = sub.add_parser("list", help="List entries")
    list_p.add_argument("--category", "-c", default="")
    list_p.add_argument("--favorites", action="store_true")

    # search
    search_p = sub.add_parser("search", help="Search entries")
    search_p.add_argument("query")

    # delete
    del_p = sub.add_parser("delete", help="Delete entry")
    del_p.add_argument("id")

    # stats
    sub.add_parser("stats", help="Statistics")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    commands = {
        "add": cmd_add, "get": cmd_get, "generate": cmd_generate,
        "passphrase": cmd_passphrase, "strength": cmd_strength,
        "list": cmd_list, "search": cmd_search, "delete": cmd_delete,
        "stats": cmd_stats,
    }
    commands[args.command](args)


if __name__ == "__main__":
    main()
