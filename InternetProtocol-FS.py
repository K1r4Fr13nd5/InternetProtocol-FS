#!/usr/bin/env python3
import argparse
import requests
import sys
import os
import socket
import subprocess
from colorama import Fore, Style, init

# Inicializa cores
init(autoreset=True)

# Cores
red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
cyan = Fore.CYAN
magenta = Fore.MAGENTA
bold = Style.BRIGHT
reset = Style.RESET_ALL

# Banner
print(red + r"""
.___        __                              __ __________                __                      .__            ____________________
|   | _____/  |_  ___________  ____   _____/  |\______   \_______  _____/  |_  ____   ____  ____ |  |           \_   _____/   _____/
|   |/    \   __\/ __ \_  __ \/    \_/ __ \   __\     ___/\_  __ \/  _ \   __\/  _ \_/ ___\/  _ \|  |     ______ |    __) \_____  \ 
|   |   |  \  | \  ___/|  | \/   |  \  ___/|  | |    |     |  | \(  <_> )  | (  <_> )  \__(  <_> )  |__  /_____/ |     \  /        \
|___|___|  /__|  \___  >__|  |___|  /\___  >__| |____|     |__|   \____/|__|  \____/ \___  >____/|____/          \___  / /_______  /
         \/          \/           \/     \/                                              \/                          \/          \/ 
                                                      v 2.0
""" + reset)

# Créditos
def creditos():
    print(green + "═══════════════════════════════════════════════════════════════════════")
    print(green + "           ✦✦  Ferramenta: " + cyan + "InternetProtocol - FS" + green + "  ✦✦")
    print(green + "           ✦✦  Desenvolvido por: " + magenta + "K1r4_Fr13nd5" + green + "  ✦✦")
    print(yellow + "                  ☠  Sociedade Fr13nd5  ☠")
    print(green + "═══════════════════════════════════════════════════════════════════════")
    print(cyan + "   [✓] GitHub: " + Fore.WHITE + "https://github.com/K1r4-Fr13nd5")
    print(yellow + "   [⚠] Uso autorizado somente para testes éticos e ambientes controlados.")
    print(green + "═══════════════════════════════════════════════════════════════════════\n" + reset)

creditos()

# Parser com subcomandos
class ColorHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def add_usage(self, usage, actions, groups, prefix=None):
        if prefix is None:
            prefix = f"{cyan}{bold}[*] Modo de uso: {reset}"
        return super().add_usage(usage, actions, groups, prefix)

parser = argparse.ArgumentParser(
    description=f"""{yellow}{bold}
Ferramenta de Coleta de Informações e Testes de IP
Exemplos de uso:{reset}

  {green}python3 InternetProtocol-FS.py -v 8.8.8.8 --all{reset}
  {green}python3 InternetProtocol-FS.py -v exemplo.com --whois{reset}
  {green}python3 InternetProtocol-FS.py -v 8.8.8.8 --scan-ports{reset}
""",
    formatter_class=ColorHelpFormatter
)

parser.add_argument("-v", "--victim", help=f"{cyan}Endereço IP ou Host de destino{reset}", type=str, dest='target', required=True)
parser.add_argument("--whois", help=f"{green}Executa consulta WHOIS no alvo{reset}", action="store_true")
parser.add_argument("--traceroute", help=f"{green}Executa traceroute até o alvo{reset}", action="store_true")
parser.add_argument("--ping", help=f"{green}Faz teste de conectividade (ping){reset}", action="store_true")
parser.add_argument("--scan-ports", help=f"{green}Escaneia portas comuns (21,22,80,443,3306){reset}", action="store_true")
parser.add_argument("--all", help=f"{green}Executa todas as verificações{reset}", action="store_true")

args = parser.parse_args()

ip = args.target

# Funções adicionais
def fetch_data(api_url):
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None

def whois_lookup(host):
    print(cyan + "\n[+] Executando WHOIS..." + reset)
    os.system(f"whois {host}")

def traceroute(host):
    print(cyan + "\n[+] Executando Traceroute..." + reset)
    cmd = "tracert" if os.name == "nt" else "traceroute"
    os.system(f"{cmd} {host}")

def ping_test(host):
    print(cyan + "\n[+] Testando conectividade (ping)..." + reset)
    cmd = "ping -n 4" if os.name == "nt" else "ping -c 4"
    os.system(f"{cmd} {host}")

def scan_ports(host):
    print(cyan + "\n[+] Escaneando portas comuns..." + reset)
    ports = [21,22,80,443,3306,8080]
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((host, port))
        if result == 0:
            print(green + f"[OPEN] Porta {port}" + reset)
        else:
            print(red + f"[CLOSED] Porta {port}" + reset)
        s.close()

# Execução principal
if args.all or not any([args.whois, args.traceroute, args.ping, args.scan_ports]):
    print(cyan + bold + "\n[+] Coletando informações do IP..." + reset)
    apis = {
        "ip-api": f"http://ip-api.com/json/{ip}",
        "ipinfo.io": f"https://ipinfo.io/{ip}/json",
        "ipwhois.io": f"https://ipwhois.app/json/{ip}",
    }
    for service, url in apis.items():
        print(yellow + f"\n--- {service.upper()} ---" + reset)
        data = fetch_data(url)
        if data:
            for key, value in data.items():
                print(f"{green}{key.capitalize()}: {value}{reset}")
        else:
            print(red + f"[!] Falha ao obter dados de {service}" + reset)

if args.whois or args.all:
    whois_lookup(ip)
if args.traceroute or args.all:
    traceroute(ip)
if args.ping or args.all:
    ping_test(ip)
if args.scan_ports or args.all:
    scan_ports(ip)

print(green + bold + "\n[✔] Execução do script concluída." + reset)
