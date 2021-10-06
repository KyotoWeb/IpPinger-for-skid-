import os
from os import name, system
from terminaltables import DoubleTable
from pystyle import *
import time

def clear():
    system("cls" if name == 'nt' else "clear")


if name == 'nt':
     system("title Darling & mode 150, 50 ")



banner = """
·▄▄▄▄   ▄▄▄· ▄▄▄  ▄▄▌  ▪   ▐ ▄  ▄▄ • 
██▪ ██ ▐█ ▀█ ▀▄ █·██•  ██ •█▌▐█▐█ ▀ ▪
▐█· ▐█▌▄█▀▀█ ▐▀▀▄ ██▪  ▐█·▐█▐▐▌▄█ ▀█▄
██. ██ ▐█ ▪▐▌▐█•█▌▐█▌▐▌▐█▌██▐█▌▐█▄▪▐█
▀▀▀▀▀•  ▀  ▀ .▀  ▀.▀▀▀ ▀▀▀▀▀ █▪·▀▀▀▀ 
"""

Anime.Fade(Center.Center(banner), Colors.red_to_purple, Colorate.Vertical, interval=0.025, enter=True)
def ipping():
    os.system("cls")
    count = 1
    System.Size(130, 30)
    e = Write.Input("Enter Ip Adress: ", Colors.red_to_blue,interval=0.005)
    replies = 0
    replies += 1
    hostname = e
    os.system("cls")
    print("_"*100)
    print("="*100)
    print("_"*100)
    while True:
        response = os.system("ping -n 1" + hostname + ">nul")
        if response == 0:
            print("\033[1;32;40m" + hostname + " is online!" + "[" + str(count) + "]" + "\033[0m")
        else:
            print("\033[31m" + hostname + " is offline" + "[" + str(count) + "]" + "\033[0m") 
        count += 1
        time.sleep(.2)
             
   
ipping() 