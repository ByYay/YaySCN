import socket
import threading
import os

open_ports = []

def scan(ip, port):
    global open_ports

    yellow = "\033[33m"
    reset = "\033[0m"
    green = "\033[32m"
    red = "\033[31m"

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"{green}[+] Port {port} is OPEN{reset}")
            open_ports.append(port)

        sock.close()
    except Exception as e:
        pass


def main():
    yellow = "\033[33m"
    reset = "\033[0m"
    green = "\033[32m"
    red = "\033[31m"

    os.system("clear")
    string = f"{red}≿━━━━━━━━━━━━━━━━━━━━━━━━━━༺❀{reset} By YAY {red}❀༻━━━━━━━━━━━━━━━━━━━━━━━━━━≾{reset}"
    print(string)

    global open_ports

    with open("Options/target_ip.txt") as file:
        target_ip = file.read().strip()

    ports = range(1, 65536)

    threads = []
    for port in ports:
        thread = threading.Thread(target=scan, args=(target_ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    string_ports = ",".join(map(str, open_ports))

    print(f"\n{yellow}[*] Nmap scan has started... (Launched with: nmap -Pn -n -T4 -p {string_ports} -sV -sC -O {target_ip}){reset}")

    os.system(f"nmap -Pn -n -T4 -p {string_ports} -sV -sC -O {target_ip} -oN Log/nmap_log.txt")

    input("\n\n\nPress enter to contiune...")

try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    exit()
