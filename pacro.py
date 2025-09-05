import pyautogui
import time
import os
import sys

def getpath(relativePath):
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relativePath)
signLunchImage = getpath("pictures/sign.png")
nextWeekImage = getpath("pictures/nextWeek.png")
def click(obrazok, confidence):
    try:
        pyautogui.click(pyautogui.locateCenterOnScreen(obrazok, confidence=confidence))
        return True
    except Exception as e:
        return False
while True:
    if click(signLunchImage, 0.7):
        print("signed lunch")
    else:
        print("couldn't find sign button: skipping to next week")
        click(nextWeekImage, 0.8)
    time.sleep(0.5)
