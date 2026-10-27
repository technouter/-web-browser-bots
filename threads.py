import webbrowser
import time     
import keyboard

webbrowser.open(f"https://www.threads.com/")
time.sleep(7)
for i in range(4):
    keyboard.send("tab")
    time.sleep(0.5)
keyboard.send("enter")
time.sleep(1.5)
    
#Read quote, write, post in threads and delete first line of text.txt
with open("threads.txt", "r", encoding="utf-8") as text:
    thread = text.readline()
print(thread)
keyboard.write(thread, delay=0.3)
time.sleep(1)
for i in range(11):
    keyboard.send("tab")
    time.sleep(0.5)
keyboard.send("enter")
time.sleep(7)
with open("threads.txt", "r", encoding="utf-8") as text:
    firstline = text.read().splitlines(True)
with open("threads.txt", "w", encoding="utf-8") as text:
    text.writelines(firstline[1:])
with open("threads.txt", "r", encoding="utf-8") as text:
    thread = text.read()

keyboard.send("ctrl+w")
  
print("Threads posting completed.")

