import pyautogui as gui
from time import sleep

def fish():
    while(True):
        position = gui.locateOnScreen('detect-img.png', confidence=0.8)
        if position:
            sleep(0.1)
            gui.rightClick()
            sleep(0.5)
            gui.rightClick()
            sleep(2)

def main():
    fish()

main()