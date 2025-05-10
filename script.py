import webbrowser
import time
import os

def playRickRoll():
    url = 'https://www.youtube.com/watch?v=q-Y0bnx6Ndw'
    cur = os.getcwd()
    script_path = os.path.join(cur,"script.py")
    image_path = os.path.join(cur,"innocent_CAT.png")
    
    for i in range (10):
        webbrowser.open(url)
        time.sleep(3)
        
        if (os.path.exists(script_path) and os.path.exists(image_path)):
            pass
        
        else:
            break
        
playRickRoll()