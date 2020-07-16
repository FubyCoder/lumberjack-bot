import numpy as np
from PIL import ImageGrab
from directKeys import click , queryMousePosition
import cv2 
import time


START_DELAY = 5 # in seconds



btn = {
    "left" :{
        "x" : 880,
        "y" : 760
    },
    "right" :{
        "x" : 1040,
        "y" : 760
    }
}

treesY = {
    0 : 322,
    1 : 272,
    2 : 222,
    3 : 172,
    4 : 122,
    5 : 72,
    6 : 22,
}
    
treesX = {
    "left" : 28,
    "right" : 155
}

last = ""

def getDirection(screen) :
    if screen [LEFT_TREE[1]][LEFT_TREE[0]] < screen [RIGHT_TREE[1]][RIGHT_TREE[0]] :
        return RIGHT_BTN;
    return LEFT_BTN


# Return [number,direction]
def clicks(screen) : 
    left = checkBest(treesX["left"],treesY)
    right = checkBest(treesX["right"],treesY)

    if left !=0  :
        return [left,"left"]
    else :
        return [right,"right"]


def checkBest(x , array) :
    maxTimes = 6
    for y in array : 
        if screen[treesY[y]][x] == 89 :
            return y
    return maxTimes


    
time.sleep(START_DELAY)
    
    
for i in range(10000) : 
    mousePos = queryMousePosition()
    screen = np.array(ImageGrab.grab(bbox =(863, 145, 1073, 602)))
    screen = cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
    val = clicks(screen)
    print("==========================================================================")
    print("Times : ",val[0])
    print("Direction : ",val[1])
    print("==========================================================================")
    
    direction = btn[val[1]]["x"];
    times = val[0]

    for i in range (times):
        click(direction,btn[val[1]]["y"])
        time.sleep(.05)

    time.sleep(.03)
