#!/usr/bin/env python3
from time import sleep
import random

Master = "5152"
xo = ("X","O")
from console import clear
from getpass import getpass
clear()
clear()

def Credit_Start():
    Winrow = 0
    
    WonTickets = 0
    
    input("Geben sie irgenwas ein zum Starten")
    print("Sie gewinnen, wenn in einer Reihe 4 X vorkommen!")
    print("Es geht in 3 Sekunden los.")
    sleep(3) 
    for i in range(3):
        print("")
    
    print("Ihr Los ist:") 
     
    print("==============")
    
    XorO = random.choice(xo)
    if XorO == "X":
            Winrow += 1
    print("|",XorO,end="")
    XorO = random.choice(xo)
    if XorO == "X":
            Winrow += 1
    print("|",XorO,end="")
    XorO = random.choice(xo)
    if XorO == "X":
            Winrow += 1
    print("|",XorO,end="")
    XorO = random.choice(xo)
    if XorO == "X":
            Winrow += 1
    print("|",XorO,"|",end="")
    print("  5T",end="")
    if Winrow == 4:
        print("  GEWONNEN!")
        WonTickets += 5
    else:
        print("")
    print("==============")
    
    Winrow = 0
    XorO = random.choice(xo)
    if XorO == "X":
            Winrow += 1
    print("|",XorO,end="")
    XorO = random.choice(xo)
    if XorO == "X":
            Winrow += 1
    print("|",XorO,end="")
    XorO = random.choice(xo)
    if XorO == "X":
            Winrow += 1
    print("|",XorO,end="")
    XorO = random.choice(xo)
    if XorO == "X":
            Winrow += 1
    print("|",XorO,"|",end="")
    print("  10T",end="")
    if Winrow == 4:
        print("  GEWONNEN!")
        WonTickets += 10
    else:
        print("")
    print("==============")
    
    Winrow = 0
    XorO = random.choice(xo)
    if XorO == "X":
            Winrow += 1
    print("|",XorO,end="")
    XorO = random.choice(xo)
    if XorO == "X":
            Winrow += 1
    print("|",XorO,end="")
    XorO = random.choice(xo)
    if XorO == "X":
            Winrow += 1
    print("|",XorO,end="")
    XorO = random.choice(xo)
    if XorO == "X":
            Winrow += 1
    print("|",XorO,"|",end="")
    print("  15T",end="")
    if Winrow == 4:
        print("  GEWONNEN!")
        WonTickets += 15
    else:
        print("")
    print("==============")
    
    Winrow = 0
    XorO = random.choice(xo)
    if XorO == "X":
            Winrow += 1
    print("|",XorO,end="")
    XorO = random.choice(xo)
    if XorO == "X":
            Winrow += 1
    print("|",XorO,end="")
    XorO = random.choice(xo)
    if XorO == "X":
            Winrow += 1
    print("|",XorO,end="")
    XorO = random.choice(xo)
    if XorO == "X":
            Winrow += 1
    print("|",XorO,"|",end="")
    print("  20T",end="")
    if Winrow == 4:
        print("  GEWONNEN!")
        WonTickets += 20
    else:
        print("")
    print("==============")
    print("")
    
    print("Gewonnene Tickets: ",WonTickets)
    
    Winrow = 0
    
        
        
        
    

        
while True:
    WonTickets = 0
    print("Wilkommen beim Los Generator!")
    print("Zum beginnen Credits an der Kasse kaufen!")
    

    password = getpass("Password: ")
    if password == Master:
        print("Sie sind Als Administator Angemeldet!")
        Kr = input("Credits: ")
        clear()
        Credits = 0
        if Kr == "1":
            Credits = 1
        if Kr == "2":
            Credits = 2
        if Kr == "3":
            Credits = 3
        if Kr == "4":
            Credits = 4
        if Kr == "5":
            Credits = 5 
        if Kr == "6":
            Credits = 6
        if Kr == "7":
            Credits = 7
        if Kr == "8":
            Credits = 8
        while Credits != 0:
            print("")
            print("Wilkommen beim Los Generator!")
            print("Sie haben",Credits,"Credits")
            Credits -= 1
            Credit_Start()
        
             
    else:
        print("Falsches Administrator Passwort!")
        sleep(2)
        clear()
