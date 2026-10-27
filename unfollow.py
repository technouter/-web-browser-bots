import webbrowser
import time

for i in range(7):
    #Open many browser tabs windows of unfollows for you unfollow manualy, read and delete ids of unfollow.txt
    with open("instabot/unfollow.txt", "r", encoding="utf-8") as text:
        idname = text.readline()
    print(idname)
    webbrowser.open(f"https://www.instagram.com/{idname}/")
    time.sleep(1.7)
    with open("instabot/unfollow.txt", "r", encoding="utf-8") as text:
        firstline = text.read().splitlines(True)
    with open("instabot/unfollow.txt", "w", encoding="utf-8") as text:
        text.writelines(firstline[1:])
    with open("instabot/unfollow.txt", "r", encoding="utf-8") as text:
        thread = text.read()

print("Open all unfollow pages, now you can unfollow them manually.")

