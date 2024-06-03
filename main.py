# github.com/0x077-thm
# guns.lol/r0ck450

import requests
from colorama import Fore, init

init()
w = Fore.WHITE
lg = Fore.LIGHTGREEN_EX
lr = Fore.LIGHTRED_EX
mg = Fore.MAGENTA

def check_http(proxy):
    urltest = "https://www.google.com/"  # Do not edit this please.
    proxies = {
        "https": f"http://{proxy}" # if you are askin why is there https and scheme http? cuz this will check if http proxies can handle https connection :)
    }
    try:
        r = requests.get(urltest, proxies=proxies, timeout=10)
        if r.status_code == 200:
            return True
    except requests.RequestException:
        return False
    return False

def checker():
    print("Please input Proxy list file")
    proxieslist = input("> ")
    with open(proxieslist, "r") as file:
        http_proxies = file.read().splitlines()
    
    valid_http = []
    
    for proxy in http_proxies:
        if check_http(proxy):
            print(f"{lg}Proxy: {w}[{proxy}]{lg} Working")
            valid_http.append(proxy)
        else:
            print(f"{lr}Proxy: {w}[{proxy}]{lr} Not Working")
    
    with open("valid_http.txt", "w") as valid_file:
        for valid_proxy in valid_http:
            valid_file.write(f"{valid_proxy}\n")

if __name__ == "__main__":
    checker()
