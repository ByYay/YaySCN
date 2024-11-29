import os

def hydra(target_ip, wordlist, username):
    command = f"hydra -l {username} -P {wordlist} ftp://{target_ip} -o Log/ftp_log.txt"
    os.system(command)        

def main():
    yellow = "\033[33m"
    reset = "\033[0m"
    green = "\033[32m"
    red = "\033[31m"

    os.system("clear")
    string = f"{red}≿━━━━━━━━━━━━━━━━━━━━━━━━━━༺❀{reset} By YAY {red}❀༻━━━━━━━━━━━━━━━━━━━━━━━━━━≾{reset}"
    print(string)

    default_path = "/usr/share/wordlists/rockyou.txt"
    while True:
        path_input = input(f"{yellow}[?] Please enter the worldlist (or press Enter to use default '/usr/share/wordlists/rockyou.txt'): {reset}")
        if path_input.strip() == "":
            if os.path.exists(default_path):
                path = default_path
                break
            else:
                print(f"{red}[!] File 'rockyou.txt' not found in default directory. (/usr/share/wordlists/rockyou.txt) {reset}")
        else:
            if not os.path.exists(path_input):
                print(f"{red}[!] Error: The specified wordlist file '{path_input}' does not exist. Please check the path and try again.{reset}")
            else:
                path = path_input
                break
    
    
    while True:
        temp_username = input(f"{yellow}[?] Specify the username for the target system: {reset}")
        mod = input(f"{yellow}[?] Username = {temp_username} , are you sure: (Y/n){reset}").lower()
        if mod.strip() == "" or mod == "y":
            username = temp_username
            break
    with open("Options/target_ip.txt", "r") as file:
        target = file.read()

    hydra(target, path, username)

    with open("Log/ftp_log.txt", "r") as file:
        data = file.read()
    print(data)

    input("\n\n\nPress Enter to contiune...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()