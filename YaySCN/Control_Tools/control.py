import subprocess
import os
import sys
import time

def string(mod, tool):
    red = "\033[31m"
    green = "\033[32m"
    reset = "\033[0m"

    if mod == 1:
        print(f"{green}[+] Tool detected: {tool}{reset}")
    elif mod == 0:
        print(f"{red}[!] Missing tool detected: {tool}{reset}")

def control(tool):
    try:
        subprocess.run(["which", tool], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(0.3)
        return True
    except subprocess.CalledProcessError:
        return False

def file_control():
    red = "\033[31m"
    green = "\033[32m"
    reset = "\033[0m"

    paths = [
    "Options/Commands.txt",
    "Options/control.txt",
    "Options/ip_control.py",
    "Options/sql_payloads.txt",
    "Options/target_ip.txt",
    "Options/target_port.txt",
    "Options/xss_payloads.txt",
    "Modules/network_scan.py",
    "Modules/port.py",
    "Modules/vuln_analysis.py",
    "Modules/Attack/discovery.py",
    "Modules/Attack/dos.py",
    "Modules/Attack/mitm.py",
    "Modules/Attack/sql.py",
    "Modules/Attack/xss.py",
    "Modules/Attack/Bruteforce/url.py",
    "Modules/Attack/Bruteforce/ftp.py",
    "Modules/Attack/Bruteforce/ssh.py",
    "Log/discovery_log.txt",
    "Log/nmap_log.txt",
    "Log/sql_log.txt",
    "Log/vuln_log.txt",
    "Log/xss_log.txt",
    "Log/url_log.txt",
    "Log/ftp_log.txt",
    "Log/ssh_log.txt",
    "Log/TempLog/discovery_log.txt",
    "Log/TempLog/ftp_log.txt",
    "Log/TempLog/nmap_log.txt",
    "Log/TempLog/sql_log.txt",
    "Log/TempLog/ssh_log.txt",
    "Log/TempLog/url_log.txt",
    "Log/TempLog/vuln_log.txt",
    "Log/TempLog/xss_log.txt",
    "log.py"
]

    
    for temp in paths:
        if not os.path.exists(temp):
            print(f"{red}[!] Missing files detected. Please delete the tool and download it again!{reset}")
            exit()
        else:
            print(f"{green}[+] '{temp}' is present.{reset}")
            time.sleep(0.2)
    print(f"{green}[+] All files are present.{reset}")

def loading(duration=5):  
    start_time = time.time()  
    loading_text = "loading"
    
    while time.time() - start_time < duration:  
        for dots in range(4): 
            if time.time() - start_time >= duration:  
                break
            sys.stdout.write("\r" + loading_text + "." * dots + " " * (3 - dots))  
            sys.stdout.flush()  
            time.sleep(0.5)

def main():
    yellow = "\033[33m"
    reset = "\033[0m"
    green = "\033[32m"
    red = "\033[31m"

    print(f"{yellow}[*] Let's ensure everything is ready! Checking the required tools...{reset}\n")

    file_control()
    print()

    tools = []
    missing_tools = []
    with open("Control_Tools/Tools.txt" ,"r") as file:
        for data in file:
            tools.append(data.strip())

    for tool in tools:
        if control(tool):
            string(1,tool)
        else:
            string(0, tool)
            missing_tools.append(tool)

    if len(missing_tools) != 0:
        print(f"{yellow}\n[*] How would you like to install the missing tools?{reset}")
        print(f"{yellow}    1. Automatic Installation (Program will install the tools for you){reset}")
        print(f"{yellow}    2. Manual Installation (You will install the tools yourself){reset}\n")
        print(f"{yellow}[*] Note: If you choose manual installation, you need to install the tools before restarting the program. If you choose not to install the missing tools, the program will exit.{reset}\n")
                      
        while True:
            result = input(f"{yellow}[?] Please select an option (1/2): {reset}")
            if result == "2":
                print("bye")
                exit()
            elif result == "1":
                for tool in missing_tools:
                    subprocess.run(["sudo","apt", "install", "-y", tool], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"{green}[+] All missing tools have been successfully installed!{reset}")
                print(f"{green}[+] Your system is ready. Proceeding with the program...{reset}")
                break
            else:
                print(f"{red}[+] Invalid Selection!{reset}")

    else:
        print(f"{green}[+] Your system is ready. Proceeding with the program...{reset}")
    
    with open("Options/control.txt", "w") as file:
            file.write("0")
    print()
    loading()

if __name__ == "__main__":
    main()
