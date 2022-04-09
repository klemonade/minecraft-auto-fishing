import pyautogui as gui
from time import sleep

from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

def fish():
    while(True):
        position = gui.locateOnScreen('detect-img.png', confidence=0.8)
        if position:
            sleep(0.1)
            gui.rightClick()
            sleep(2)
            gui.rightClick()
            sleep(2)

def main():
    fish()

main()