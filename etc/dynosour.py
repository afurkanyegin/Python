#import numpy as np
import pyautogui
import time
from PIL import ImageGrab,ImageOps
from numpy import *


class Coordinates():
    replayButton=(410,365)
    dinosaur=(176,370)
    halfdino=(166,393)
    ssarea=(dinosaur[0]+70,dinosaur[1],halfdino[0]+124,halfdino[1])
    
def restartGame():
    pyautogui.click(Coordinates.replayButton)

def Jumping():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')

def areacontrol():
    box=Coordinates.ssarea
    image=ImageGrab.grab(box)
    grayImage= ImageOps.grayscale(image)
    a=array(grayImage.getcolors())
    return a.sum()

def main():
    s=0
    restartGame()
    while True:
        if(areacontrol()!=1259):
            Jumping()
            print(s)
            s=s+1 
            time.sleep(0.05)
main()

