import webbrowser
import keyboard
import time
import random

def search():
    topics = [
    # Technology
    "artificial intelligence", "machine learning", "deep learning", "neural network",
    "cloud computing", "big data", "cybersecurity", "blockchain", "virtual reality",
    "augmented reality", "internet of things", "5G", "quantum computing", "data mining",
    "open source", "API", "framework", "algorithm", "encryption", "serverless",
    "microservices", "DevOps", "containerization", "Kubernetes", "Docker",
    "edge computing", "digital twin", "metaverse", "smart contract", "NFT",
    "data science", "robotics", "autonomous vehicle", "wearable tech", "smartphone",
    "semiconductor", "GPU", "CPU", "cloud storage", "database", "SQL", "NoSQL",
    "virtual machine", "operating system", "Linux", "Windows", "macOS",

    # Games
    "RPG", "MMORPG", "FPS", "battle royale", "sandbox", "open world", "quest",
    "loot box", "multiplayer", "single player", "co-op", "PvP", "PvE",
    "level up", "boss fight", "checkpoint", "save point", "respawn", "DLC",
    "expansion pack", "season pass", "modding", "speedrun", "console", "PC gaming",
    "PlayStation", "Xbox", "Nintendo Switch", "Steam", "Epic Games", "Game Pass",
    "controller", "joystick", "VR headset", "gamer tag", "leaderboard", "tournament",
    "eSports", "LAN party", "questline", "skill tree", "inventory", "crafting",
    "character customization", "skins", "battle pass", "guild", "clan",

    # Movies
    "blockbuster", "box office", "trailer", "director", "screenwriter", "cinematography",
    "special effects", "CGI", "soundtrack", "score", "sequel", "prequel", "reboot",
    "remake", "franchise", "adaptation", "biopic", "documentary", "short film",
    "feature film", "indie film", "film festival", "Oscar", "Academy Awards",
    "Golden Globe", "Cannes", "Sundance", "red carpet", "premiere", "casting",
    "screenplay", "script", "storyboard", "production", "post-production",
    "editing", "voice acting", "motion capture", "cinema", "IMAX",

    # Series
    "pilot episode", "season finale", "cliffhanger", "spin-off", "crossover",
    "sitcom", "drama", "thriller", "sci-fi", "fantasy", "crime series",
    "soap opera", "mini-series", "limited series", "anthology", "streaming",
    "binge-watching", "Netflix", "HBO", "Disney Plus", "Prime Video", "Hulu",
    "Apple TV+", "Peacock", "Paramount+", "episode arc", "character development",
    "plot twist", "flashback", "flashforward", "cold open", "credits",
    "opening theme", "soundtrack", "showrunner", "production company",

    # Anime
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
        time.sleep(17)
        keyword = random.choice(topics)
        keyboard.write(keyword, delay=0.1)
        keyboard.send("Enter")
        num = random.randint(17, 71)
        print(keyword + " searched! Waiting " + str(num) + " seconds for next search...")
        time.sleep(num)
        keyboard.send("ctrl+w")
        
    print("Searches finished!")
    
search()