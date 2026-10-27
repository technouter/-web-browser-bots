import webbrowser
import time
import random
from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()

def rewards():
    webbrowser.open("https://rewards.bing.com/dashboard")
    time.sleep(17)
    
    #Daily Set
    for i in range(9):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.3)
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(57)
    keyboard.press(Key.ctrl)
    keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl)
    time.sleep(7)
    keyboard.press(Key.f5)
    keyboard.release(Key.f5)
    time.sleep(7)
    for i in range(10):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)                                           

        time.sleep(0.3)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(37)
    keyboard.press(Key.ctrl)
    keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl)
    time.sleep(7)
    keyboard.press(Key.f5)
    keyboard.release(Key.f5)
    time.sleep(7)
    for i in range(11):             
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.3)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(77)
    keyboard.press(Key.ctrl)
    keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl)
    time.sleep(3)
    print("Daily Set finished!")                            

    #Claim Rewards
    keyboard.press(Key.f5)
    keyboard.release(Key.f5)
    time.sleep(7)
    for i in range(4):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.3)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(7)
    for i in range(2):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.3)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(7)
    
    #Close Browser
    keyboard.press(Key.ctrl)
    keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl)  
    print("Rewards claimed!")   

def search():
    topics = [
    "artificial intelligence", "machine learning", "deep learning", "neural network",
    "cloud computing", "big data", "cybersecurity", "blockchain", "virtual reality",
    "augmented reality", "internet of things", "5G", "quantum computing", "data mining",
    "open source", "API", "framework", "algorithm", "encryption", "serverless",
    "microservices", "DevOps", "containerization", "Kubernetes", "Docker",
    "edge computing", "digital twin", "metaverse", "smart contract", "NFT",
    "data science", "robotics", "autonomous vehicle", "wearable tech", "smartphone",
    "semiconductor", "GPU", "CPU", "cloud storage", "database", "SQL", "NoSQL",
    "virtual machine", "operating system", "Linux", "Windows", "macOS",
    "RPG", "MMORPG", "FPS", "battle royale", "sandbox", "open world", "quest",
    "loot box", "multiplayer", "single player", "co-op", "PvP", "PvE",
    "level up", "boss fight", "checkpoint", "save point", "respawn", "DLC",
    "expansion pack", "season pass", "modding", "speedrun", "console", "PC gaming",
    "PlayStation", "Xbox", "Nintendo Switch", "Steam", "Epic Games", "Game Pass",
    "controller", "joystick", "VR headset", "gamer tag", "leaderboard", "tournament",
    "eSports", "LAN party", "questline", "skill tree", "inventory", "crafting",
    "character customization", "skins", "battle pass", "guild", "clan",
    "blockbuster", "box office", "trailer", "director", "screenwriter", "cinematography",
    "special effects", "CGI", "soundtrack", "score", "sequel", "prequel", "reboot",
    "remake", "franchise", "adaptation", "biopic", "documentary", "short film",
    "feature film", "indie film", "film festival", "Oscar", "Academy Awards",
    "Golden Globe", "Cannes", "Sundance", "red carpet", "premiere", "casting",
    "screenplay", "script", "storyboard", "production", "post-production",
    "editing", "voice acting", "motion capture", "cinema", "IMAX",
    "pilot episode", "season finale", "cliffhanger", "spin-off", "crossover",
    "sitcom", "drama", "thriller", "sci-fi", "fantasy", "crime series",
    "soap opera", "mini-series", "limited series", "anthology", "streaming",
    "binge-watching", "Netflix", "HBO", "Disney Plus", "Prime Video", "Hulu",
    "Apple TV+", "Peacock", "Paramount+", "episode arc", "character development",
    "plot twist", "flashback", "flashforward", "cold open", "credits",
    "opening theme", "soundtrack", "showrunner", "production company",
    "shonen", "shojo", "isekai", "mecha", "slice of life", "fantasy anime",
    "manga", "light novel", "OVA", "OP", "ED", "filler episode", "canon",
    "arc", "power-up", "transformation", "sensei", "senpai", "kawaii",
    "tsundere", "yandere", "otaku", "cosplay", "anime convention",
    "fan service", "subbed", "dubbed", "anime studio", "Shonen Jump",
    "Crunchyroll", "Funimation", "Aniplex", "Studio Ghibli", "Toei Animation",
    "Madhouse", "Bones", "MAPPA", "Kyoto Animation", "Gainax"
    ]

    for i in range(21):
        webbrowser.open("https://www.bing.com/")
        time.sleep(7)
        keyword = random.choice(topics)
        for char in keyword:
            keyboard.type(char)
            time.sleep(0.3)
        time.sleep(1)
        keyword = random.choice(topics)
        time.sleep(1)
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        for char in keyword:
                keyboard.type(char)
                time.sleep(0.3)
        time.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(17)
        keyboard.press(Key.ctrl)
        keyboard.press('w')
        keyboard.release('w')
        keyboard.release(Key.ctrl)
        print(keyword + " searched!")
        time.sleep(17)  

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

def threads():
    webbrowser.open(f"https://www.threads.com/")
    time.sleep(17)
    
    #Read first line of quote.txt
    with open("quote.txt", "r", encoding="utf-8") as post:
        thread = post.readline()
    print(thread)
    for i in range(4):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)
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
    #Clear first line of quote.txt
    with open("quote.txt", "r", encoding="utf-8") as text:
        firstline = text.read().splitlines(True)
    with open("quote.txt", "w", encoding="utf-8") as text:
        text.writelines(firstline[1:])
    with open("quote.txt", "r", encoding="utf-8") as text:
        thread = text.read()

   #Read second line of quote.txt
    with open("quote.txt", "r", encoding="utf-8") as post:
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
    #Clear second line of quote.txt
    with open("quote.txt", "r", encoding="utf-8") as text:
        firstline = text.read().splitlines(True)
    with open("quote.txt", "w", encoding="utf-8") as text:
        text.writelines(firstline[1:])
    with open("quote.txt", "r", encoding="utf-8") as text:
        thread = text.read()
    keyboard.press(Key.ctrl)
    keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl)
        
    print("Quote posted successfully!")

def follow():
    for i in range(17):
        #Read first line of followtxt
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

        #Clear first line of follow.txt
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

rewards()
threads()                 
suggested()
#follow()
search()