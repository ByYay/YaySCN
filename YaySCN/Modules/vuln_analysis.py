import re
import subprocess
import os

def nmap_data():
    with open("Log/nmap_log.txt", "r") as file:
        data = file.read()

    pattern = r"(\d+/tcp)\s+open\s+\S+\s+(.*)"
    matches = re.findall(pattern, data)
    versions = []
    ports = []

    for match in matches:
        port, version = match
        versions.append(version)
        ports.append(port)
        
    return ports,versions

def searchsploit():
    ports, versions = nmap_data()
    output_exploit = []

    for version in versions:
        result = subprocess.run(["searchsploit", version],stdout=subprocess.PIPE,stderr=subprocess.PIPE)             
        output = result.stdout.decode('utf-8')
        print(f"{version} => {output}")
        output_exploit.append(f"{version} => {output}")

    with open("Log/vuln_log.txt", "w") as file:
        for data in output_exploit:
            file.write(data + "\n")


def main():
    reset = "\033[0m"
    red = "\033[31m"

    os.system("clear")
    string = f"{red}≿━━━━━━━━━━━━━━━━━━━━━━━━━━༺❀{reset} By YAY {red}❀༻━━━━━━━━━━━━━━━━━━━━━━━━━━≾{reset}"
    print(string)

    searchsploit()

try:
    if __name__ == "__main__":
        main()
    input("Press enter to continue")
except KeyboardInterrupt:
    exit()