#Coded by GR1FF1N, use/change/modify as you wish.

#YouTube: https://www.youtube.com/channel/UCPlDVOXFkFpLF1x3lH_B9HQ
#X / Twitter: https://x.com/JohnTech2023
#Github: https://github.com/4R1FF1N


import pyautogui #Screenshot Grabber
import sys
import os #Sending commands
import time #Time for screenshots
import datetime #Save Screenshot as current date

#CREATE DIR IF IT DOESN'T EXIST!
def createDIR():
    dircreate = os.system("mkdir img")
    if dircreate == True:
        dircreate()
    else:
        print("DIR not created since it exists...")
createDIR()

#TAKE_SCREENSHOT
def takess():
    timenow = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S")
    ss = pyautogui.screenshot()
    print("Screenshot taken... ")
    filepath = (f"img/S_{timenow}.png")
    ss.save(filepath)
    print("Screenshot saved... ")

#REPEAT
def main_loop():
    while 1:
        takess()
        time.sleep(10) #It saves a screenshot every 10 seconds.

if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)
