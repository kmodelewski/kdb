import sys

import colorama
from colorama import Fore, Back, Style
from termcolor import colored
import time

colorama.init(autoreset=True)
print(Fore.LIGHTGREEN_EX + "Welcome colors" + Style.RESET_ALL)
print(f"Hello world")

#TERMCOLOR LIBRARY FOR CHOOSING COLORS ONLY
active_blinker = True
blinker = colored("Hi", color= 'white')
while active_blinker:
    print(blinker)
    sys.stdout.write("\033[F")

    time.sleep(1)


print(blinker) #windows teminal do not support blinking text
