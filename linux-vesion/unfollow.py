import webbrowser
import time
import random       
from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Button, Controller as MouseController
keyboard = KeyboardController()
mouse = MouseController()


for i in range(37):
    #Read first line of text.txt
    with open("unfollow.txt", "r", encoding="utf-8") as text:
        idname = text.readline()
    print(idname)
    webbrowser.open(f"https://www.instagram.com/{idname}/")
    time.sleep(1.7)
    
    #Delete first line of text.txt
    with open("unfollow.txt", "r", encoding="utf-8") as text:
        firstline = text.read().splitlines(True)
    with open("unfollow.txt", "w", encoding="utf-8") as text:
        text.writelines(firstline[1:])
    with open("unfollow.txt", "r", encoding="utf-8") as text:
        thread = text.read()

print("Open all unfollow pages, now you can unfollow them manually.")

