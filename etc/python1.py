import pyautogui
import sys
import time

for i in range (0,5):
    print(i)
    time.sleep(1)
print("Go")

q=1
#while(True):
#    pyautogui.press('a')
#    q+=1
#    print(q)
#    if(q==22):
#        break
    

pyautogui.keyDown('up')
#pyautogui.press('b')
print("pressing up ")
time.sleep(2)
pyautogui.keyUp('up')
#pyautogui.keyUp('b')
print("pressing finished")