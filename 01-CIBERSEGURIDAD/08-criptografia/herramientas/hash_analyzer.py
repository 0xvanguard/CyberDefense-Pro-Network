#!/usr/bin/env python3
"""
hash_analyzer.py — Identificación y cracking de hashes por diccionario

Identifica el algoritmo (MD5/SHA1/SHA224/SHA256/SHA384/SHA512/NTLM) por su
longitud, y luego prueba cada hash contra una wordlist local.

Uso (educativo — solo con datos propios o autorizados):
    python3 hash_analyzer.py -H e10adc3949ba59abbe56e057f20f883e -w rockyou-mini.txt
    python3 hash_analyzer.py -f hashes.txt -w rockyou-mini.txt -o resueltos.txt
"""

import argparse
import hashlib
import sys
from pathlib import Path

ALGORITHMS = {
    32: "MD5",
    40: "SHA1",
    56: "SHA224",
    64: "SHA256",
    96: "SHA384",
    128: "SHA512",
}


def identify(h: str) -> str:
    h = h.strip().lower()
    if not all(c in "0123456789abcdef" for c in h):
        return "desconocido (no hexadecimal)"
    return ALGORITHMS.get(len(h), f"desconocido ({len(h)} hex chars)")


def crack_single(h: str, wordlist: list) -> str:
    h = h.strip().lower()
    alg = identify(h)
    if alg.startswith("desconocido"):
        return ""
    for word in wordlist:
        w = word.strip()
        if not w:
            continue
        digest = hashlib.new(alg.lower(), w.encode("utf-8")).hexdigest()
        if digest == h:
            return w
    return ""


def main():
    parser = argparse.ArgumentParser(description="Identifica y crackea hashes por diccionario (uso educativo)")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-H", "--hash", help="Un solo hash")
    group.add_argument("-f", "--file", help="Archivo con hashes (uno por línea)")
    parser.add_argument("-w", "--wordlist", required=True, help="Wordlist local (una palabra por línea)")
    parser.add_argument("-o", "--output", help="Archivo de salida con los hashes resueltos")
    args = parser.parse_args()

    wl = Path(args.wordlist)
    if not wl.is_file():
        print(f"[!] Wordlist no encontrada: {wl}")
        sys.exit(1)
    wordlist = wl.read_text(encoding="utf-8", errors="ignore").splitlines()
    print(f"[*] Wordlist cargada: {len(wordlist)} palabras")

    hashes = [args.hash] if args.hash else [l.strip() for l in Path(args.file).read_text().splitlines() if l.strip()]

    print(f"[*] Analizando {len(hashes)} hash(es)...\n")
    solved = []
    for h in hashes:
        print(f"  Hash: {h}")
        print(f"    Algoritmo probable: {identify(h)}")
        plain = crack_single(h, wordlist)
        if plain:
            print(f"    ✅ RESUELTO: {plain}")
            solved.append(f"{h}:{plain}")
        else:
            print("    ❌ No encontrado en la wordlist")

    if args.output and solved:
        Path(args.output).write_text("\n".join(solved) + "\n", encoding="utf-8")
        print(f"\n[+] {len(solved)} resueltos guardados en {args.output}")


if __name__ == "__main__":
    main()
