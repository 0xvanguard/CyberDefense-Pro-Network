#!/usr/bin/env python3
"""
nmap_parser.py — Parseo y reporte de escaneos Nmap (salida XML)

Convierte un escaneo `nmap -oX salida.xml` en un informe legible por consola
y en un archivo Markdown listo para tu portafolio.

Uso:
    nmap -sV -oX scan.xml <objetivo>
    python3 nmap_parser.py -f scan.xml
    python3 nmap_parser.py -f scan.xml -o informe.md
"""

import argparse
import xml.etree.ElementTree as ET
from datetime import datetime


def parse_nmap(xml_path: str) -> dict:
    tree = ET.parse(xml_path)
    root = tree.getroot()

    scan = {
        "scan_name": root.get("scanner", "nmap"),
        "args": root.get("args", ""),
        "start": datetime.fromtimestamp(int(root.get("start", 0))).isoformat() if root.get("start") else "",
        "hosts": [],
    }

    for host in root.findall("host"):
        addresses = {a.get("addrtype"): a.get("addr") for a in host.findall("address")}
        hostname = ""
        hn = host.find("hostnames/hostname")
        if hn is not None:
            hostname = hn.get("name", "")

        entry = {"ip": addresses.get("ipv4", addresses.get("ipv6", "")), "hostname": hostname, "ports": []}

        status = host.find("status")
        if status is not None:
            entry["state"] = status.get("state")

        for port in host.findall("ports/port"):
            state = port.find("state")
            if state is None or state.get("state") != "open":
                continue
            service = port.find("service")
            port_entry = {
                "port": port.get("portid"),
                "protocol": port.get("protocol"),
                "service": service.get("name", "") if service is not None else "",
                "product": service.get("product", "") if service is not None else "",
                "version": service.get("version", "") if service is not None else "",
                "cpe": service.get("cpe", "") if service is not None else "",
            }
            entry["ports"].append(port_entry)

        scan["hosts"].append(entry)

    return scan


def format_console(scan: dict) -> str:
    lines = [f"Nmap scan: {scan['scan_name']}", f"Args: {scan['args']}", f"Start: {scan['start']}", "=" * 60]
    for host in scan["hosts"]:
        lines.append(f"\nHost {host['ip']} ({host['hostname']}) [{host.get('state','?')}]")
        if not host["ports"]:
            lines.append("  (sin puertos abiertos)")
        for p in host["ports"]:
            product = " ".join(x for x in (p["product"], p["version"]) if x)
            lines.append(f"  {p['port']}/{p['protocol']:<3} {p['service']:<20} {product}")
            if p["cpe"]:
                lines.append(f"      cpe: {p['cpe']}")
    return "\n".join(lines)


def format_markdown(scan: dict) -> str:
    md = ["# Informe de Escaneo Nmap", "",
          f"- **Comando:** `{scan['args']}`", f"- **Fecha:** {scan['start']}", ""]
    for host in scan["hosts"]:
        md.append(f"## Host {host['ip']} ({host['hostname']})")
        md.append("| Puerto | Servicio | Producto | Versión |")
        md.append("|---|---|---|---|")
        for p in host["ports"]:
            md.append(f"| {p['port']}/{p['protocol']} | {p['service']} | {p['product']} | {p['version']} |")
        md.append("")
    md.append("*Generado con nmap_parser.py — Plataforma de Estudio de Ciberseguridad*")
    return "\n".join(md)


def main():
    parser = argparse.ArgumentParser(description="Parser de resultados Nmap XML")
    parser.add_argument("-f", "--file", required=True, help="Archivo XML de Nmap (-oX)")
    parser.add_argument("-o", "--output", help="Archivo Markdown de salida (opcional)")
    args = parser.parse_args()

    try:
        scan = parse_nmap(args.file)
    except ET.ParseError as e:
        print(f"[!] No se pudo parsear el XML: {e}")
        print("    Asegúrate de generar el scan con: nmap -oX archivo.xml <objetivo>")
        raise SystemExit(1)

    print(format_console(scan))

    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(format_markdown(scan))
        print(f"\n[+] Informe Markdown guardado en {args.output}")


if __name__ == "__main__":
    main()
