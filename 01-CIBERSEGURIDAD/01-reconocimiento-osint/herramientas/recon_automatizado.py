#!/usr/bin/env python3
"""
recon_automatizado.py — Reconocimiento OSINT automatizado (fase pasiva/ligera)

Uso educativo y autorizado: solo sobre dominios propios o con permiso escrito.
Realiza: resolución DNS, enumeración de subdominios con wordlist (consulta DNS directa),
revisión de puertos HTTP/HTTPS abiertos y captura de títulos de página.

Requisitos: python3 (sin dependencias externas).
Ejemplo:  python3 recon_automatizado.py -d ejemplo.com -w subdominios.txt
"""

import argparse
import concurrent.futures
import json
import socket
import ssl
import sys
from datetime import datetime
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

BANNER = r"""
  ____  _____ _____ _   _     ____  _   _ _____ ____
 |  _ \| ____| ____| \ | |   / ___|| | | | ____|  _ \
 | |_) |  _| |  _| |  \| |   \___ \| |_| |  _| | |_) |
 |  _ <| |___| |___| |\  |    ___) |  _  | |___|  _ <
 |_| \_\_____|_____|_| \_|   |____/|_| |_|_____|_| \_\
            Reconocimiento OSINT automatizado
"""


def resolve(hostname: str) -> list:
    """Resuelve un hostname a IPv4/IPv6."""
    try:
        infos = socket.getaddrinfo(hostname, None)
        return sorted({info[4][0] for info in infos})
    except socket.gaierror:
        return []


def get_http_title(hostname: str, timeout: int = 5) -> str:
    """Consulta HTTP(S) y extrae el <title> de la página."""
    for scheme in ("https", "http"):
        url = f"{scheme}://{hostname}"
        try:
            req = Request(url, headers={"User-Agent": "recon-osint-educativo/1.0"})
            with urlopen(req, timeout=timeout) as resp:
                body = resp.read(4096).decode("utf-8", errors="ignore").lower()
                if "<title" in body:
                    start = body.find("<title") + len("<title")
                    start = body.find(">", start) + 1
                    end = body.find("</title>", start)
                    if end > start:
                        return body[start:end].strip()[:80]
                return f"{scheme}://{hostname} (sin title)"
        except (URLError, HTTPError, ssl.SSLError):
            continue
    return ""


def enumerate_subdomains(domain: str, wordlist_path: str, workers: int = 50) -> dict:
    """Prueba subdominios contra la wordlist resolviéndolos por DNS."""
    found = {}

    def check(sub: str) -> tuple:
        hostname = f"{sub}.{domain}"
        ips = resolve(hostname)
        if ips:
            return (hostname, ips)
        return (None, None)

    try:
        with open(wordlist_path, encoding="utf-8", errors="ignore") as fh:
            subs = [line.strip().lower() for line in fh if line.strip() and not line.startswith("#")]
    except FileNotFoundError:
        print(f"[!] Wordlist no encontrada: {wordlist_path}")
        sys.exit(1)

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        for hostname, ips in pool.map(check, subs):
            if hostname:
                found[hostname] = ips

    return found


def main():
    parser = argparse.ArgumentParser(description="Reconocimiento OSINT automatizado (uso educativo autorizado)")
    parser.add_argument("-d", "--domain", required=True, help="Dominio objetivo (propio o autorizado)")
    parser.add_argument("-w", "--wordlist", help="Wordlist de subdominios (uno por línea)")
    parser.add_argument("-o", "--output", help="Archivo JSON de salida (opcional)")
    parser.add_argument("-t", "--timeout", type=int, default=5, help="Timeout HTTP en segundos")
    args = parser.parse_args()

    print(BANNER)
    print(f"[*] Inicio: {datetime.now().isoformat()}")
    print(f"[*] Objetivo: {args.domain}")
    print("=" * 60)

    report = {"dominio": args.domain, "timestamp": datetime.now().isoformat(), "subdominios": {}}

    # 1. Resolución base
    ips = resolve(args.domain)
    print(f"[+] {args.domain} -> {', '.join(ips) if ips else 'sin resolución DNS'}")
    report["ip_principal"] = ips

    # 2. Enumeración de subdominios
    if args.wordlist:
        print(f"[*] Enumerando subdominios con {args.wordlist} ...")
        found = enumerate_subdomains(args.domain, args.wordlist)
        print(f"[+] {len(found)} subdominios resueltos")
        for hostname in sorted(found):
            print(f"    {hostname:40s} -> {', '.join(found[hostname])}")
        report["subdominios"] = found

    # 3. Sondeo HTTP en subdominios encontrados
    targets = [args.domain] + list(found.keys())
    print("[*] Consultando títulos HTTP/HTTPS ...")
    for hostname in targets:
        title = get_http_title(hostname, args.timeout)
        if title:
            print(f"    {hostname:40s} | {title}")
            report.setdefault("titles", {})[hostname] = title

    # 4. Salida
    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            json.dump(report, fh, indent=2, ensure_ascii=False)
        print(f"\n[+] Informe guardado en {args.output}")
    print(f"[*] Fin: {datetime.now().isoformat()}")


if __name__ == "__main__":
    main()
