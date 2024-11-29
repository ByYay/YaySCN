import aiohttp
import asyncio
import os

async def fetch_url(session, url, data, green, yellow, red, reset, sem):
    async with sem:
        try:
            async with session.get(url, timeout=5) as response:
                if response.status == 200:
                    print(f"{green}[200] Found: The directory or file exists:{reset} {url}")
                    data.append(f"[200] Found: The directory or file exists: {url}")
                elif response.status in [301, 302]:
                    print(f"{yellow}[{response.status}] Redirect: The directory or file redirects to another location:{reset} {url}")
                    data.append(f"[{response.status}] Redirect: The directory or file redirects to another location: {url}")
                elif response.status == 403:
                    print(f"{red}[{response.status}] Forbidden: Access to this directory or file is restricted:{reset} {url}")
                    data.append(f"[{response.status}] Forbidden: Access to this directory or file is restricted: {url}")
        except Exception as e:
            print(f"{red}[!] Error occurred while requesting {url}:{reset} {e}")


async def discovery(protocol, target_url, port, wordlist_path):
    yellow = "\033[33m"
    reset = "\033[0m"
    green = "\033[32m"
    red = "\033[31m"

    data = []
    protocol = "http" if protocol == 1 else "https"

    sem = asyncio.Semaphore(2)

    async with aiohttp.ClientSession() as session:
        tasks = []
        with open(wordlist_path, "r") as wordlist:
            for file in wordlist:
                file = file.strip()
                url = f"{protocol}://{target_url}:{port}/{file}"
                tasks.append(fetch_url(session, url, data, green, yellow, red, reset, sem))

        await asyncio.gather(*tasks)
    
    return data


def main():
    try:
        yellow = "\033[33m"
        reset = "\033[0m"
        green = "\033[32m"
        red = "\033[31m"

        os.system("clear")
        string = f"{red}≿━━━━━━━━━━━━━━━━━━━━━━━━━━༺❀{reset} By YAY {red}❀༻━━━━━━━━━━━━━━━━━━━━━━━━━━≾{reset}"
        print(string)

        string = """
       1 - http       : Start scanning for http site
       2 - https      : Start scanning for https site
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

        default_path = "/usr/share/dirb/wordlists/common.txt"
        while True:
            path_input = input(f"{yellow}[?] Please enter the worldlist (or press Enter to use default '/usr/share/dirb/wordlists/common.txt'): {reset}")
            if path_input.strip() == "":
                path = default_path
                break
            else:
                if not os.path.exists(path_input):
                    print(f"{red}[!] Error: The specified wordlist file '{path_input}' does not exist. Please check the path and try again.{reset}")
                else:
                    path = path_input
                    break

        default_port = 80
        while True:
            port_input = input(f"{yellow}[?] Please enter the target PORT (or press Enter to use default 80): {reset}")
            if port_input.strip() == "":
                port = default_port
                break
            elif port_input.isdigit():
                port = int(port_input)
                break
            else:
                print(f"{red}[!] Invalid input. Please enter a valid port number.{reset}")
        
        with open("Options/target_ip.txt", "r") as file:
            target_ip = file.read()
        
        target_ip = target_ip.strip()
        
        print()
        data_discovery = asyncio.run(discovery(mod, target_ip, port, path))
        
        with open("Log/discovery_log.txt", "w") as file:
            for data in data_discovery:
                file.write(data + '\n')

        print()
        input("Press enter to continue")
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    main()
