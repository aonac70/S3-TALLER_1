import os

reset_color = "\033[0m"
red_color = "\033[91m"
green_color = "\033[92m"
yellow_color = "\033[93m"
blue_color = "\033[94m"
purple_color = "\033[95m"
cyan_color = "\033[96m"

def gotoxy(x, y):
    print(f"\033[{y};{x}H", end="")

def BorrarPantalla():
    os.system("cls") 

def linea(longitud, color):
    print(f"{color}{longitud * '-'}{reset_color}")

