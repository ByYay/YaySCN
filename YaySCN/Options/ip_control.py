import re
import os

def set_target():
    yellow = "\033[33m"
    reset = "\033[0m"
    green = "\033[32m"
    red = "\033[31m"

    target_ip = input(f"{yellow}[*] Enter a target ip address : {reset}")
    
    ip_regex = r'^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'
    
    if re.match(ip_regex, target_ip):
        print(f"{green}[+] Ip format is correct: {target_ip}{reset}")
        if ping_target(target_ip):
            print(f"{green}[+] Target ip is reachable{reset}")
            with open("Options/target_ip.txt", "w") as file:
                file.write(target_ip)         
        else:
            print(f"{red}[!] The target IP address is unreachable.{reset}")
            mod = input(f"{yellow}[?] Do you want to set it up anyway? (y/N): {reset}")
            if mod == "y":
                with open("Options/target_ip.txt", "w") as file:
                    file.write(target_ip)
    else:
        print(f"{red}[!] IP format is wrong: {target_ip}{reset}")

def ping_target(ip):
    command = f"ping {ip} -c 1"
    response = os.system(command)
    return response == 0

try:
    yellow = "\033[33m"
    reset = "\033[0m"
    green = "\033[32m"
    red = "\033[31m"

    os.system("clear")
    string = f"{red}≿━━━━━━━━━━━━━━━━━━━━━━━━━━༺❀{reset} By YAY {red}❀༻━━━━━━━━━━━━━━━━━━━━━━━━━━≾{reset}"
    print(string)
    set_target()
    input("\n\n\nPress enter to contiune...")
except KeyboardInterrupt:
    exit()
