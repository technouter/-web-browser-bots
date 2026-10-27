import webbrowser
import time
import random       
from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Button, Controller as MouseController
keyboard = KeyboardController()
mouse = MouseController()

def follow():
    for i in range(17):
        #Read first line of text.txt
        with open("follow.txt", "r", encoding="utf-8") as text:
            idname = text.readline()
        print(idname)
        webbrowser.open(f"https://www.instagram.com/{idname}/")
        time.sleep(7)
        mouse.position = (397, 351)
        time.sleep(1)
        mouse.click(Button.left, 1)
        print("Follow successfully!")
        time.sleep(3)

        #Delete first line of text.txt
        with open("follow.txt", "r", encoding="utf-8") as text:
            firstline = text.read().splitlines(True)
        with open("follow.txt", "w", encoding="utf-8") as text:
            text.writelines(firstline[1:])
        with open("follow.txt", "r", encoding="utf-8") as text:
            thread = text.read()
        keyboard.press(Key.ctrl)
        keyboard.press('w')
        keyboard.release('w')
        keyboard.release(Key.ctrl)
        time.sleep(7)

follow()




                        