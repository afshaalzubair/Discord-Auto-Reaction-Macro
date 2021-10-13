import pyautogui
import time
import keyboard

time.sleep(5)
# Reaction Button Region: 1423, 144, 200, 800
# Flushed Button Region: 824, 137, 800, 800

while keyboard.is_pressed("q") == False:
    if pyautogui.locateOnScreen("add reaction button image.png", region = (1423, 144, 200, 800), grayscale = True, confidence = 0.8) != None:
        pyautogui.moveTo("add reaction button image.png")
        pyautogui.click()
        time.sleep(0.2)
        flushedImage = pyautogui.locateOnScreen("flushed button.png", region = (824, 137, 800, 800), confidence = 0.7)
        time.sleep(0.05)
        pyautogui.moveTo(flushedImage, None, 0.05)
        pyautogui.click()
        pyautogui.scroll(-200)
        time.sleep(0.2)
        pyautogui.click()
    else:
        pyautogui.scroll(-200)
        time.sleep(0.2)
        pyautogui.click()
