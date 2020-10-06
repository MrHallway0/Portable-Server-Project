'''
Portable Server Project
https://github.com/MrHallway0/Portable-Server-Project

Programed by: Mr. Hallway
'''

# Load
import os getpass time

username = str(getpass.getuser())
maxOptions = 5

# Package definations
webServer = []

# Wizard

while True:
  os.system("clear")
  try:
    print('''
Setup wizard
Welcome to the setup wizard. First let's get what you wish use your server for!

  1. Web Server
  2. Samba Server
  3. Minecraft Server
  5. SSH Server

    ''')
    serverPurpuse = int(input("Select an option: "))
    
    if serverPurpuse == serverPurpuse < maxOptions + 1:
      break
      if serverPurpuse == serverPurpuse >= maxOptions + 1:
      print("Invalid option")
  
  else:
    print("Invalid option")
    time.sleep(0.5)
os.system("clear")

