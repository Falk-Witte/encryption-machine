#!/usr/bin/python3
import time
from database import pass_data
from passlib.hash import pbkdf2_sha256
import colorama
from colorama import Back, Fore, init
from rich.progress import track

init(autoreset=True)

def encryption_machine():
  import pyfiglet

  banner = pyfiglet.figlet_format("Encryption Machine")
  print(banner)

    #just a variable
  alph = "abcdefghijklmnopqrstuvwxyz"

  f = input("Enter to encode word=> ")

  rot13 = lambda x: "".join([alph[(alph.find(c) + 13) %len(f)] for c in x])

  i = rot13(f)

  for _ in track(range(50), description="Encrypting..."):
      time.sleep(0.02)

  print("Output of rot13=>", i)

  a = pyfiglet.figlet_format(i, font='hex')

  print("Encoded text=> ", Back.WHITE+Fore.BLACK+a)


#password authentication
try:
  i = input("Please enter password to continue=> ")

  #print(pbkdf2_sha256.verify(i, pass_data()))
except:
  print('\n')
  print(Back.RED+Fore.BLACK+"An error has occured")
  exit(0)

#the .sleep is just there to make it look like the programm is actually doing something that take a second instead of just
#checking if two values are the same

#initialization loop
try:
  if pbkdf2_sha256.verify(i, pass_data()) == True:
    print(Back.GREEN+ Fore.BLACK+"Correct")
    print("Starting Process...")
    time.sleep(1)
    encryption_machine()

  else:
    print(Back.RED+Fore.BLACK+"Incorrect")
    time.sleep(1)
    print("Cancelling Process...")
    time.sleep(1)
except:
  print('\n')
  print(Back.RED+Fore.BLACK+"An error has occured")
  time.sleep(1)
  print("Cancelling Process...")
  time.sleep(1)
  exit(0)
