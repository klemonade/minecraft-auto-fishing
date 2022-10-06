import pyautogui as gui
from time import sleep

from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

def fish():
    counter = 0
    index = 4
    while(True):
        position = gui.locateOnScreen('detect-img.png', confidence=0.8)
        # if counter % 63 == 0 and counter != 0:
        #     counter = 0
        #     index += 1
        #     gui.keyDown(str(index))
        #     gui.keyUp(str(index))
        #     sleep(1)
        #     gui.rightClick()
        if position:
            sleep(0.1)
            gui.rightClick()
            sleep(2)
            gui.rightClick()
            # gui.keyDown('a')
            # gui.keyUp('a')
            # gui.keyDown('d')
            # gui.keyUp('d')
            sleep(2)
            counter += 1

def main():
    fish()

main()