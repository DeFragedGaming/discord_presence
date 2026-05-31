import time
import psutil
from pypresence import Presence

client_id = ""  # replace with your Discord app ID
rpc = Presence(client_id)
connected = False

def is_running(name):
    for p in psutil.process_iter(['name']):
        if p.info['name'] and name.lower() in p.info['name'].lower():
            return True
    return False

active = False

while True:
    app = is_running("") # replace with the name of the application you want to track

    if app and not active:
        try:
            if not connected:
                rpc.connect()
                connected = True
            rpc.update(
                state="", # replace with the state you want to display
                details="", # replace with the details you want to display
                large_image="", # replace with the name of the large image you want to display
                small_image="", # replace with the name of the small image you want to display
                small_text="" # replace with the text you want to display next to the small image
            )
            active = True
        except:
            connected = False

    if not app and active:
        try:
            rpc.clear()
        except:
            pass
        active = False

    time.sleep(10)
