#!/usr/bin/env python3
"""
alerta_telegram.py — Envío de alertas de seguridad a Telegram

Ideal para notificar eventos de tu SOC simulado (Wazuh, scripts de monitoreo)
o resultados de tus labs. Solo usa la librería estándar (urllib).

Configuración (variables de entorno, evita hardcodear secretos):
    export TELEGRAM_BOT_TOKEN="123456:ABC-DEF..."
    export TELEGRAM_CHAT_ID="123456789"

Uso:
    ./alerta_telegram.py -m "ALERTA: intento de login fallido en 192.168.1.10"
    ./alerta_telegram.py -m "Evento crítico" --parse /var/log/syslog --grep "Failed password"
"""

import argparse
import json
import os
import subprocess
import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import URLError


def send_message(token: str, chat_id: str, text: str, silent: bool = False) -> bool:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text[:4000], "disable_notification": "true" if silent else "false"}
    req = Request(url, data=urlencode(payload).encode(), method="POST")
    try:
        with urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            return bool(data.get("ok"))
    except URLError as e:
        print(f"[!] Error enviando a Telegram: {e}", file=sys.stderr)
        return False


def extract_logs(path: str, grep: str, max_lines: int = 20) -> str:
    """Extrae las últimas líneas relevantes de un log (uso con --grep)."""
    try:
        out = subprocess.run(
            ["grep", grep, path], capture_output=True, text=True, timeout=30
        ).stdout.splitlines()
        return "\n".join(out[-max_lines:])
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        return f"[!] No se pudo leer el log: {e}"


def main():
    parser = argparse.ArgumentParser(description="Envía alertas de seguridad a Telegram")
    parser.add_argument("-m", "--message", required=True, help="Texto del mensaje")
    parser.add_argument("--parse", help="Archivo de log a leer (requiere --grep)")
    parser.add_argument("--grep", default="", help="Patrón de búsqueda en el log")
    parser.add_argument("--silent", action="store_true", help="Desactivar notificación sonora")
    args = parser.parse_args()

    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("[!] Faltan TELEGRAM_BOT_TOKEN o TELEGRAM_CHAT_ID (variables de entorno)")
        sys.exit(1)

    if args.parse:
        snippet = extract_logs(args.parse, args.grep) if args.grep else ""
        if snippet:
            args.message += f"\n\n--- Log ({args.parse}) ---\n{snippet}"

    if send_message(token, chat_id, args.message, args.silent):
        print("[+] Alerta enviada correctamente")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
