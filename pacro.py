import pyautogui
import time
import os
import sys

def getpath(relativePath):
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_path, relativePath)
    if not os.path.exists(path):
        print(f"ERROR: File '{path}' does not exist!")
        sys.exit(1)
    return path
signLunchImage = getpath("pictures/sign.png")
nextWeekImage = getpath("pictures/nextWeek.png")
def click(obrazok, confidence):
    pozicia = pyautogui.locateCenterOnScreen(obrazok, confidence=confidence)
    if pozicia:
        pyautogui.click(pozicia)
        return True
    return False
while True:
    if click(signLunchImage, 0.7):
        print("signed lunch")
    else:
        print("couldn't find sign button: skipping to next week")
        click(nextWeekImage, 0.8)
    time.sleep(0.5)