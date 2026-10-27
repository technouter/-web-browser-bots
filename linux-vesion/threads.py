import webbrowser
import time
import random       
from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Button, Controller as MouseController
keyboard = KeyboardController()
mouse = MouseController()

def threads():
    webbrowser.open(f"https://www.threads.com/")
    time.sleep(7)
    mouse.position = (100, 250)
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(3)

    #Read first line of threads.txt
    with open("threads.txt", "r", encoding="utf-8") as post:
        thread = post.readline()
    print(thread)
    for char in thread:
        keyboard.type(char)
        time.sleep(0.3)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    for i in range(2):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(7)
    #Clear first line of threads.txt
    with open("threads.txt", "r", encoding="utf-8") as text:
        firstline = text.read().splitlines(True)
    with open("threads.txt", "w", encoding="utf-8") as text:
        text.writelines(firstline[1:])
    with open("threads.txt", "r", encoding="utf-8") as text:
        thread = text.read()

   #Read second line of threads.txt
    with open("threads.txt", "r", encoding="utf-8") as post:
        thread = post.readline()
    print(thread)
    for char in thread:
        keyboard.type(char)
        time.sleep(0.3)
    time.sleep(7)
    for i in range(2):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.5)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(7)
    for i in range(8):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(17)
    keyboard.press(Key.ctrl)
    keyboard.release(Key.ctrl)
    time.sleep(3)
    #Clear second line of threads.txt
    with open("threads.txt", "r", encoding="utf-8") as text:
        firstline = text.read().splitlines(True)
    with open("threads.txt", "w", encoding="utf-8") as text:
        text.writelines(firstline[1:])
    with open("threads.txt", "r", encoding="utf-8") as text:
        thread = text.read()
    keyboard.press(Key.ctrl)
    keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl)
        
    print("Posted successfully!")

threads()                 




                        