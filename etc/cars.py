import pyautogui
import time
from PIL import ImageGrab,ImageOps
from numpy import *

class Coordinates():
    controlArealeft=(600,440)
    controlAreaRight=(685,665)
    controlArea=(controlArealeft[0],controlArealeft[1],controlAreaRight[0],controlAreaRight[1])
def imagegrab():
    box=Coordinates.controlArea
    cropimage=ImageGrab.grab(box)
    grayimage=ImageOps.grayscale(cropimage)
    a=array(grayimage.getcolors())
    return a.sum()

def right():
    pyautogui.keyDown('right')
    time.sleep(0.05)
    pyautogui.keyUp('right')

def left():
    pyautogui.keyDown('left')
    time.sleep(0.05)
    pyautogui.keyUp('left')


def main():
    while True:
        if (imagegrab()<42420):
            right()
            printf()
        elif (imagegrab()>44000):
            left()
            printf()
        


def printf():
        print(imagegrab())
        time.sleep(0.05)

main()

