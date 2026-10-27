import webbrowser
import time
import random       
from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Button, Controller as MouseController
keyboard = KeyboardController()
mouse = MouseController()

def suggested():
    webbrowser.open(f"https://www.instagram.com/explore/people/")
    time.sleep(17)
    for _ in range(14):   
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.3)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)
    for _ in range(16):   
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.3)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.3)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.3)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(3)
    keyboard.press(Key.ctrl)
    keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl)
    time.sleep(7)
    print("Followed suggested people finished!\n")     

suggested()




                        