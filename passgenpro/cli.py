#!/usr/bin/env python3
"""
PassGen Pro CLI — Password Generator from the command line.

Usage:
    python cli.py random --length 20
    python cli.py passphrase --words 6
    python cli.py pin --length 6
    python cli.py check "MyPassword123!"
    python cli.py batch --count 5
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from generator import PassGen


def cmd_random(args):
    """Generate random password."""
    gen = PassGen()
    password = gen.random(
        length=args.length,
        uppercase=not args.no_uppercase,
        lowercase=not args.no_lowercase,
        digits=not args.no_digits,
        symbols=not args.no_symbols,
        exclude_ambiguous=args.exclude_ambiguous,
    )

    print(f"\n🔐 Random Password\n{'='*50}")
    print(f"  Password:    {password.password}")
    print(f"  Length:      {len(password.password)}")
    print(f"  Entropy:     {password.entropy} bits")
    print(f"  Strength:    {password.strength.upper()}")
    print(f"  Bar:         {password.strength_bar}")
    print(f"  Charset:     {password.charset_used}")
    print(f"  Crack Time:  {password.crack_time}")
    print(f"  Unique:      {password.unique_chars} characters")

    if args.output:
        with open(args.output, "w") as f:
            json.dump(password.to_dict(), f, indent=2)
        print(f"\n  ✅ Exported to {args.output}")


def cmd_passphrase(args):
    """Generate passphrase."""
    gen = PassGen()
    password = gen.passphrase(
        words=args.words,
        separator=args.separator,
        capitalize=args.capitalize,
        add_number=args.add_number,
    )

    print(f"\n📝 Passphrase\n{'='*50}")
    print(f"  Passphrase:  {password.password}")
    print(f"  Words:       {args.words}")
    print(f"  Entropy:     {password.entropy} bits")
    print(f"  Strength:    {password.strength.upper()}")
    print(f"  Bar:         {password.strength_bar}")
    print(f"  Crack Time:  {password.crack_time}")


def cmd_pin(args):
    """Generate PIN."""
    gen = PassGen()
    password = gen.pin(length=args.length)

    print(f"\n🔢 PIN Code\n{'='*50}")
    print(f"  PIN:         {password.password}")
    print(f"  Length:      {args.length}")
    print(f"  Entropy:     {password.entropy} bits")
    print(f"  Strength:    {password.strength.upper()}")
    print(f"  Crack Time:  {password.crack_time}")


def cmd_check(args):
    """Check password strength."""
    gen = PassGen()
    password = gen.check_strength(args.password)

    print(f"\n🔍 Password Analysis\n{'='*50}")
    print(f"  Password:    {'*' * len(password.password)} (hidden)")
    print(f"  Length:      {len(password.password)}")
    print(f"  Entropy:     {password.entropy} bits")
    print(f"  Strength:    {password.strength.upper()}")
    print(f"  Bar:         {password.strength_bar}")
    print(f"  Charset:     {password.charset_used}")
    print(f"  Crack Time:  {password.crack_time}")
    print(f"  Has Upper:   {'✅' if password.has_uppercase else '❌'}")
    print(f"  Has Lower:   {'✅' if password.has_lowercase else '❌'}")
    print(f"  Has Digits:  {'✅' if password.has_digits else '❌'}")
    print(f"  Has Symbols: {'✅' if password.has_symbols else '❌'}")
    print(f"  Unique Chars: {password.unique_chars}")


def cmd_batch(args):
    """Generate batch of passwords."""
    gen = PassGen()
    passwords = gen.random_batch(
        count=args.count,
        length=args.length,
    )

    print(f"\n🎲 Batch Generation ({args.count} passwords)\n{'='*50}")

    for i, p in enumerate(passwords, 1):
        print(f"  {i}. {p.password}  [{p.strength.upper()}] {p.entropy} bits")


def main():
    parser = argparse.ArgumentParser(description="🔐 PassGen Pro — Password Generator")
    sub = parser.add_subparsers(dest="command")

    # random
    rand_p = sub.add_parser("random", help="Generate random password")
    rand_p.add_argument("-l", "--length", type=int, default=16)
    rand_p.add_argument("--no-uppercase", action="store_true")
    rand_p.add_argument("--no-lowercase", action="store_true")
    rand_p.add_argument("--no-digits", action="store_true")
    rand_p.add_argument("--no-symbols", action="store_true")
    rand_p.add_argument("--exclude-ambiguous", action="store_true")
    rand_p.add_argument("-o", "--output", help="Export to file")

    # passphrase
    phrase_p = sub.add_parser("passphrase", help="Generate passphrase")
    phrase_p.add_argument("-w", "--words", type=int, default=6)
    phrase_p.add_argument("-s", "--separator", default="-")
    phrase_p.add_argument("--capitalize", action="store_true")
    phrase_p.add_argument("--add-number", action="store_true", default=True)

    # pin
    pin_p = sub.add_parser("pin", help="Generate PIN")
    pin_p.add_argument("-l", "--length", type=int, default=6)

    # check
    check_p = sub.add_parser("check", help="Check password strength")
    check_p.add_argument("password", help="Password to check")

    # batch
    batch_p = sub.add_parser("batch", help="Generate batch")
    batch_p.add_argument("-n", "--count", type=int, default=5)
    batch_p.add_argument("-l", "--length", type=int, default=16)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    commands = {
        "random": cmd_random,
        "passphrase": cmd_passphrase,
        "pin": cmd_pin,
        "check": cmd_check,
        "batch": cmd_batch,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
