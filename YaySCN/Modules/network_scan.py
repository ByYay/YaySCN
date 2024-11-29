import scapy.all as scapy
import os

try:
    reset = "\033[0m"
    green = "\033[32m"
    red = "\033[31m"
    yellow = "\033[33m"

    os.system("clear")
    string = f"{red}≿━━━━━━━━━━━━━━━━━━━━━━━━━━༺❀{reset} By YAY {red}❀༻━━━━━━━━━━━━━━━━━━━━━━━━━━≾{reset}"
    print(string)

    packet = scapy.ARP(pdst="192.168.2.0/24")
    packet2 = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    last_packet = packet2 / packet

    (ip, noip) = scapy.srp(last_packet, timeout=1, verbose=False)

    temp = 1
    devices = []
    for sent, received in ip:
        print(f"{green}{temp}.      Ip Address: {received.psrc} - MAC Address: {received.hwsrc}{reset}")
        devices.append(received.psrc)
        temp += 1

    len = len(devices)

    while True:
        if len != 0:
            try:
                target_id = int(input(f"{yellow}[?] Please select the target IP address by entering its number (1-{len}): {reset}"))
                if target_id < 1 or target_id > len:  
                    print(f"{red}[!] Invalid selection. Please enter a valid number (1-{len}).{reset}")
                else:
                    print(f"{yellow}[+] Target IP set to: {devices[target_id-1]}{reset}")
                    with open("Options/target_ip.txt", "w") as file:
                        file.write(str(devices[target_id-1]))
                    break
            except ValueError:  
                print(f"{red}[!] Invalid character.{reset}")
        else:
            print(f"{yellow}[*] No device found on local network.{reset}")
            break

except KeyboardInterrupt:
    exit()