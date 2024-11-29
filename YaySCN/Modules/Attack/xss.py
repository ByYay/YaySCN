import os
import requests
import time

try:
    payload_list = []
    with open("Options/xss_payloads.txt", "r", encoding="utf-8") as file:
        payload_list = [line.strip() for line in file]

    with open("Options/target_ip.txt") as file:
        target_ip = file.read().strip()

    yellow = "\033[33m"
    reset = "\033[0m"
    green = "\033[32m"
    red = "\033[31m"

    os.system("clear")
    string = f"{red}≿━━━━━━━━━━━━━━━━━━━━━━━━━━༺❀{reset} By YAY {red}❀༻━━━━━━━━━━━━━━━━━━━━━━━━━━≾{reset}"
    print(string)

    string = """
        - http       : Start scanning for http site
        - https      : Start scanning for https site
    """
    print(string)

    mod = 0
    while True:
        try:
            mod = int(input(f"{yellow}[?] Please enter the site type (1 for HTTP, 2 for HTTPS): {reset}"))
            if mod not in [1, 2]:
                print(f"{red}[!] Invalid choice. Please enter 1 or 2.{reset}")
            else:
                break
        except ValueError:
            print(f"{red}[!] Please enter a valid number.{reset}")


    if mod == 1:
        default_url = f"http://{target_ip}/search?query="
        target_url_input = input(f"{yellow}[?] Please enter the target URL in full format 'e.g., http://example.com/search?query=' (or press Enter to use http://{target_ip}/search?query=): {reset}")
        if target_url_input.strip() == "":
            target_url = default_url
        else:
            target_url = target_url_input
        print(f"{yellow}[*] XSS scanning has started. Requests will be sent every 1 seconds.{reset}")
        for payload in payload_list:
            try:
                response = requests.get(f"{target_url}{payload}")
                if payload in response.text:
                    print(f"{green}[+] XSS vulnerability found! Manual verification is recommended. => {payload}{reset}")
                    with open("../../Log/xss_log.txt", "a") as file:
                        file.write(f"[+] XSS vulnerability found! Manual verification is recommended. => {payload}")
            except requests.exceptions.RequestException as e:
                print(f"{red}[!] An error occurred while sending the request: {reset}{e}")
            time.sleep(1)
    elif mod == 2:
        default_url = f"https://{target_ip}/search?query="
        target_url_input = input(f"{yellow}[?] Please enter the target URL in full format 'e.g., https://example.com/search?query=' (or press Enter to use https://{target_ip}/search?query=): {reset}")
        if target_url_input.strip() == "":
            target_url = default_url
        else:
            target_url = target_url_input
        print(f"{yellow}[*] XSS scanning has started. Requests will be sent every 1 seconds.{reset}")
        for payload in payload_list:
            try:
                response = requests.get(f"{target_url}{payload}")
                if payload in response.text:
                    print(f"{green}[+] XSS vulnerability found! Manual verification is recommended. => {payload}{reset}")
                    with open("../../Log/xss_log.txt", "a") as file:
                        file.write(f"[+] XSS vulnerability found! Manual verification is recommended. => {payload}")
            except requests.exceptions.RequestException as e:
                print(f"{red}[!] An error occurred while sending the request: {reset}{e}")
            time.sleep(1)
    input("Press enter to continue")
except KeyboardInterrupt:
    exit()