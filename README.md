# 🔍 InternetProtocol - FS
Ferramenta avançada para coleta de informações, análise de IP, WHOIS, traceroute, ping e port scanning, criada para testes éticos e ambientes controlados.
Desenvolvida por K1r4_Fr13nd5 - Sociedade Fr13nd5.

# 🖤 Recursos Principais
✔ Coleta de informações de IP usando múltiplas APIs (ip-api, ipinfo, ipwhois)
✔ Consulta WHOIS
✔ Teste de conectividade com Ping
✔ Traceroute para mapear o caminho até o alvo
✔ Port Scan básico (21, 22, 80, 443, 3306, 8080)
✔ Execução completa com --all (todas as verificações)
✔ Saída colorida estilo Hacker com Colorama
✔ Modo CLI com argumentos e exemplos de uso

# ⚠ Aviso Legal
Esta ferramenta é destinada exclusivamente para testes éticos, auditoria e aprendizado.
O uso indevido para atividades ilícitas é estritamente proibido e de sua inteira responsabilidade.

# 📌 Instalação
✅ Requisitos
Python 3.x
Módulos: requests, colorama

# Instale as dependências:
pip install requests colorama

# Clone o repositório:

git clone https://github.com/K1r4Fr13nd5/InternetProtocol-FS.git

cd InternetProtocol-FS

# 🚀 Modo de Uso
Exibir ajuda e opções disponíveis:
python3 ip-mod.py --help
Exemplos:
bash
Copiar
Editar
# Buscar informações completas do IP
python3 InternetProtocol-FS.py -v 8.8.8.8 --all

# Consultar WHOIS
python3 InternetProtocol-FS.py -v exemplo.com --whois

# Realizar traceroute
python3 InternetProtocol-FS.py -v 8.8.8.8 --traceroute

# Testar conectividade com ping
python3 InternetProtocol-FS.py -v 8.8.8.8 --ping

# Escanear portas comuns
python3 InternetProtocol-FS.py -v 8.8.8.8 --scan-ports

# 🔧 Opções Disponíveis
Opção	        Descrição
-v, --victim	Define o IP ou domínio alvo
--whois	Executa consulta WHOIS no alvo
--traceroute	Executa traceroute até o alvo
--ping	        Testa conectividade com ping
--scan-ports	Escaneia portas comuns
--all	Executa todas as verificações

# 🖥 Demonstração do Banner

.___        __                              __ __________                __                      .__            ____________________
|   | _____/  |_  ___________  ____   _____/  |\______   \_______  _____/  |_  ____   ____  ____ |  |           \_   _____/   _____/
|   |/    \   __\/ __ \_  __ \/    \_/ __ \   __\     ___/\_  __ \/  _ \   __\/  _ \_/ ___\/  _ \|  |     ______ |    __) \_____  \ 
|   |   |  \  | \  ___/|  | \/   |  \  ___/|  | |    |     |  | \(  <_> )  | (  <_> )  \__(  <_> )  |__  /_____/ |     \  /        \
|___|___|  /__|  \___  >__|  |___|  /\___  >__| |____|     |__|   \____/|__|  \____/ \___  >____/|____/          \___  / /_______  /
         \/          \/           \/     \/                                              \/                          \/          \/ 
                                                      v 2.0
# 🏴 Créditos
Ferramenta: InternetProtocol - FS

Desenvolvido por: K1r4_Fr13nd5

Grupo: ☠ Sociedade Fr13nd5 ☠

# ✅ Quer evoluir a ferramenta?
Podemos adicionar:
✔ Menu interativo estilo terminal hacker
✔ Integração com Nmap para scans avançados
✔ Exportar resultados para arquivos TXT/JSON
✔ Modo stealth para bypass de firewall