import sys
import os

def signature():
    red = "\033[31m"
    reset = "\033[0m"
    string = f"{red}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{reset}"
    signature = """
    ██████╗ ██╗   ██╗    ██╗   ██╗ █████╗ ██╗   ██╗
    ██╔══██╗╚██╗ ██╔╝    ╚██╗ ██╔╝██╔══██╗╚██╗ ██╔╝
    ██████╔╝ ╚████╔╝      ╚████╔╝ ███████║ ╚████╔╝ 
    ██╔══██╗  ╚██╔╝        ╚██╔╝  ██╔══██║  ╚██╔╝  
    ██████╔╝   ██║          ██║   ██║  ██║   ██║   
    ╚═════╝    ╚═╝          ╚═╝   ╚═╝  ╚═╝   ╚═╝  

      YaySCN v1.0 - Offensive Security Toolkit
    """
    print(string)
    print(signature)
    print(string)
    print()

def control():
    os.system("python Control_Tools/control.py")
    with open("Options/control.txt", "r") as file:
        result = file.read()
    if result == "0":
        return True    
    else:
        return False

def clear():
    os.system("clear")
    
def menu_vuln():
    menu = """
    - run          : Analyze NMAP results for vulnerabilities
    - show vuln    : Display vulnerability analysis
    - clear        : Clean the terminal
    - back         : Return to the main menu
    - help         : List commands
"""
    print(menu)

def menu_attack():
    menu = """
    - xss            : Launch Cross-Site Scripting Attack
    - discovery      : Launch directory and file discovery on a target
    - sql            : Launch SQL Injection Attack
    - mitm           : Launch Man-in-the-Middle Attack
    - dos            : Launch Denial of Service Attack
    - cd bruteforce  : Launch a brute force attack with Hydra
    - clear          : Clean the terminal
    - back           : Return to the main menu
    - help           : List commands
""" 
    print(menu)

def menu_network():
    menu = """
    - scan         : Start scanning
    - run nmap     : Start an NMAP scan
    - show nmap    : Show NMAP scan
    - clear        : Clean the terminal
    - back         : Return to the main menu
    - help         : List commands
"""
    print(menu)

def menu():
    menu = """
    - use network   : Launch Network Scanning Module
    - use vuln      : Launch Vulnerability Analysis Module
    - use attack    : Launch Attack Module
    - set target    : Set Manuel Target Ip Address
    - create report : Read all log files and generate a visual HTML report in the 'Reports' directory.
    - clear logs    : Delete all log files' content and reset them with a 'null' value.
    - clear         : Clean the terminal
    - exit          : Exit the Program
    - help          : List commands
"""
    print(menu)

def menu_bruteforce():
    menu = """
    - url          : Launch a brute force attack on a URL you specify
    - ftp          : Launch a brute force attack on FTP
    - ssh          : Launch a brute force attack on SSH
    - clear        : Clean the terminal
    - back         : Return to the main menu
    - help         : List commands
"""
    print(menu)

def white_list(command, list):
    for data in list:
        if data == command:
            return True
    return False

def clear_log():
    with open("Options/target_ip.txt", "w") as file:
        file.write("null")
    with open("Options/target_port.txt", "w") as file:
        file.write("null")
    with open("Log/nmap_log.txt", "w") as file:
        file.write("null")
    with open("Log/vuln_log.txt", "w") as file:
        file.write("null")
    with open("Log/discovery_log.txt", "w") as file:
        file.write("null")
    with open("Log/sql_log.txt", "w") as file:
        file.write("null")
    with open("Log/xss_log.txt", "w") as file:
        file.write("null")
    with open("Log/ftp_log.txt", "w") as file:
        file.write("null")
    with open("Log/ssh_log.txt", "w") as file:
        file.write("null")
    with open("Log/url_log.txt", "w") as file:
        file.write("null")
    with open("Log/TempLog/ssh_log.txt", "w") as file:
        file.write("")
    with open("Log/TempLog/ftp_log.txt", "w") as file:
        file.write("")
    with open("Log/TempLog/xss_log.txt", "w") as file:
        file.write("")
    with open("Log/TempLog/sql_log.txt", "w") as file:
        file.write("")
    with open("Log/TempLog/discovery_log.txt", "w") as file:
        file.write("")
    with open("Log/TempLog/vuln_log.txt", "w") as file:
        file.write("")
    with open("Log/TempLog/nmap_log.txt", "w") as file:
        file.write("")
    with open("Log/TempLog/url_log.txt", "w") as file:
        file.write("")

def main():
    with open("Options/control.txt", "w") as file:
        file.write("1")

    yellow = "\033[33m"
    reset = "\033[0m"
    green = "\033[32m"
    red = "\033[31m"    

    with open("Options/target_ip.txt", "r") as file:
        target_ip = file.read()

    clear()
    signature()
    print(f"{yellow}TARGET IP: {target_ip}{reset}\n")

    commands = []
    with open("Options/Commands.txt", "r") as file:
        for data in file:
            commands.append(data.strip())
    
    while True:
        with open("Options/target_ip.txt", "r") as file:
            target_ip = file.read()
        command = input(f"{red}YaySCN >{reset} ")
        if white_list(command, commands):
            if command == "exit":
                print("Bye!")
                sys.exit()
            elif command == "help":
                menu()
            elif command == "clear":
                clear()
                signature()
                print(f"{yellow}TARGET IP: {target_ip}{reset}\n")
            elif command == "back":
                print(f"{red}[!] You are already in the main menu.{reset}\n")
            elif command == "use network":
                print(f"{yellow}[*] Network Scanning Module Selected.{reset}")
                while True:
                    command_network = input(f"{red}YaySCN (network) >{reset} ")
                    if command_network == "back":
                        break
                    elif command_network == "scan":
                        os.system("python Modules/network_scan.py")
                        with open("Options/target_ip.txt", "r") as file:
                            target_ip = file.read()
                        clear()
                        signature()
                        print(f"{yellow}TARGET IP: {target_ip}{reset}\n")
                    elif command_network == "help":
                        menu_network()
                    elif command_network == "show nmap":
                        with open("Log/nmap_log.txt", "r") as file:
                            data_nmap = file.read()
                        print(data_nmap)    
                    elif command_network == "run nmap":
                        if target_ip != "null":
                            os.system("python Modules/port.py")
                            clear()
                            signature()
                            print(f"{yellow}TARGET IP: {target_ip}{reset}\n")
                        else:
                            print(f"{red}[!] Firstly, scan the network and select the target IP address.{reset}")                     
                    elif command_network == "clear":
                        with open("Options/target_ip.txt", "r") as file:
                            target_ip = file.read()
                        clear()
                        signature()
                        print(f"{yellow}TARGET IP: {target_ip}{reset}\n")
                    else:
                        print(f"{red}[!] Invalid command. Type 'help' for available commands.{reset}")
            elif command == "use vuln":
                with open("Log/nmap_log.txt", "r") as file:
                    data_vuln = file.read()
                if data_vuln != "null":
                    print(f"{yellow}[*] Vuln Module Selected.{reset}")
                    while True:
                        command_vuln = input(f"{red}YaySCN (vuln) >{reset} ")
                        if command_vuln == "back":
                            break
                        elif command_vuln == "run":
                            os.system("python Modules/vuln_analysis.py")
                            clear()
                            signature()
                            print(f"{yellow}TARGET IP: {target_ip}{reset}\n")
                        elif command_vuln == "help":
                            menu_vuln()
                        elif command_vuln == "clear":
                            clear()
                            signature()
                            print(f"{yellow}TARGET IP: {target_ip}{reset}\n")
                        elif command_vuln == "show vuln":
                            with open("Log/vuln_log.txt", "r") as file:
                                data_vuln = file.read()
                                print(data_vuln)
                        else:
                            print(f"{red}[!] Invalid command. Type 'help' for available commands.{reset}")
                else:
                    print(f"{red}[!] NMAP scan results not found.{reset}")
                    print(f"{yellow}[*] Please perform an NMAP scan first using the 'run nmap' command in the network module.{reset}")
            elif command == "use attack":
                if target_ip != "null":
                    print(f"{yellow}[*] Attack Module Selected.{reset}")
                    while True:
                        command_attack = input(f"{red}YaySCN (attack) >{reset} ")
                        if command_attack == "back":
                            break
                        elif command_attack == "dos":
                            os.system("python Modules/Attack/dos.py")
                            clear()
                            signature()
                            print(f"{yellow}TARGET IP: {target_ip}{reset}\n")
                        elif command_attack == "help":
                            menu_attack()
                        elif command_attack == "clear":
                            clear()
                            signature()
                            print(f"{yellow}TARGET IP: {target_ip}{reset}\n")
                        elif command_attack == "mitm":
                            os.system("python Modules/Attack/mitm.py")
                            clear()
                            signature()
                            print(f"{yellow}TARGET IP: {target_ip}{reset}\n")
                        elif command_attack == "discovery":
                            os.system("python Modules/Attack/discovery.py")
                            clear()
                            signature()
                            print(f"{yellow}TARGET IP: {target_ip}{reset}\n")
                        elif command_attack == "xss":
                            os.system("python Modules/Attack/xss.py")
                            clear()
                            signature()
                            print(f"{yellow}TARGET IP: {target_ip}{reset}\n")
                        elif command_attack == "sql":
                            os.system("python Modules/Attack/sql.py")
                            clear()
                            signature()
                            print(f"{yellow}TARGET IP: {target_ip}{reset}\n")
                        elif command_attack == "cd bruteforce":
                            print(f"{yellow}[*] Attack/BruteForce Module Selected.{reset}")
                            while True:
                                command_attack_brutefroce = input(f"{red}YaySCN (attack/bruteforce) >{reset} ")
                                if command_attack_brutefroce == "back":
                                    break
                                elif command_attack_brutefroce == "help":
                                    menu_bruteforce()
                                elif command_attack_brutefroce == "clear":
                                    clear()
                                    signature()
                                    print(f"{yellow}TARGET IP: {target_ip}{reset}\n")
                                elif command_attack_brutefroce == "ftp":
                                    os.system("python Modules/Attack/Bruteforce/ftp.py")
                                    clear()
                                    signature()
                                    print(f"{yellow}TARGET IP: {target_ip}{reset}\n")
                                elif command_attack_brutefroce == "ssh":
                                    os.system("python Modules/Attack/Bruteforce/ssh.py")
                                    clear()
                                    signature()
                                    print(f"{yellow}TARGET IP: {target_ip}{reset}\n")
                                elif command_attack_brutefroce == "url":
                                    os.system("python Modules/Attack/Bruteforce/url.py")
                                    clear()
                                    signature()
                                    print(f"{yellow}TARGET IP: {target_ip}{reset}\n")
                                else:
                                    print(f"{red}[!] Invalid command. Type 'help' for available commands.{reset}")
                        else:
                            print(f"{red}[!] Invalid command. Type 'help' for available commands.{reset}")
                else:
                    print(f"{red}[!] Please determine the target IP address with the 'run' command in the network module and try again.{reset}")
            elif command == "clear logs":
                clear_log()
                with open("Options/target_ip.txt", "r") as file:
                    target_ip = file.read()
                clear()
                signature()
                print(f"{yellow}TARGET IP: {target_ip}{reset}\n")
                print(f"{green}[*] Logs have been successfully cleared.\n{reset}")
            elif command == "create report":
                os.system("python log.py")
            elif command == "set target":
                os.system("python Options/ip_control.py")
                with open("Options/target_ip.txt", "r") as file:
                    target_ip = file.read()
                clear()
                signature()
                print(f"{yellow}TARGET IP: {target_ip}{reset}\n")
        else:
            print(f"{red}[!] Invalid command. Type 'help' for available commands.{reset}")

if __name__ == "__main__":
    if control() == False:
        exit()
    yellow = "\033[33m"
    reset = "\033[0m"
    green = "\033[32m"
    red = "\033[31m"
    
    while True:        
        try:        
            main()
        except KeyboardInterrupt:
            print(f"\n\n{yellow}[*] Are you sure you want to exit? To exit the program, please click 'ctrl+c'.{reset}")
            input()