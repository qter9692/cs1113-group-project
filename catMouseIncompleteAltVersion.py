import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint



################################################################


################################################################

# Initialize world
name = "Click to Move! Get the Cheese! Avoid the Cat!"
width = 500
height = 500
rw.newDisplay(width, height, name)

################################################################


# Display the state by drawing a cat at that x coordinate
myimage = dw.loadImage("level1.jpeg")
myimage2 = dw.loadImage("level2.jpeg")
myimage3 = dw.loadImage("level3.jpeg")
myimage4 = dw.loadImage("level4.jpeg")
myimage5 = dw.loadImage("level5.jpeg")
mymouse = dw.loadImage("mouse.jpeg")
mycheese = dw.loadImage("cheese.jpeg")

# state -> image (IO)

def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(myimage, (state[0], state[2]))
    dw.draw(mymouse, (state[4], state[6]))
    dw.draw(mycheese,(state[8],state[9]))
    dw.draw(myimage2, (state[10],state[12]))

################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# Note that pos is accessed as state[0], and delta-pos
# as state[1]. Later on we'll see how to access state
# components by name (as we saw with records in Idris).
#
# state -> state
def updateState(state):

    #causes cat1 to bounce off sides of window
    if state[0] == (width - 80) or state [0] == 0:
        return (state[0] - state[1], -1 * state[1], state[2]-state[3], state[3], state[4]+state[5],state[5],state[6]+state[7],state[7],state[8],state[9],state[10]+state[11],state[11],state[12]+state[13],state[13])
    if state[2] == (height - 80) or state[2] == 0:
        return (state[0] - state[1],state[1],state[2]-state[3], -1 * state[3],state[4]+state[5],state[5],state[6]+state[7],state[7],state[8],state[9],state[10]+state[11],state[11],state[12]+state[13],state[13])

    #causes mouse to bounce off sides of window
    if state[4] == (width - 50) or state [4] == 0:
        return (state[0]+state[1],state [1],state[2]+state[3],state[3],state[4] - state[5], -1 * state[5],state[6]-state[7],state[7],state[8],state[9],state[10]+state[11],state[11],state[12]+state[13],state[13])
    if state[6] == (height - 50) or state[6] == 0:
        return (state[0]+state[1],state [1],state[2]+state[3],state[3],state[4] - state[5],state[5],state[6]-state[7], -1 * state[7],state[8],state[9],state[10]+state[11],state[11],state[12]+state[13],state[13])

    #hitbox detection for cheese and summoner of cat 2
    if ((state[4]-50) < state[8]  < (state[4]+50) and (state[6]-50) < state[9] < (state[6]+50)):
        return (state[0]+state[1],state[1],state[2]+state[3],state[3],state[4]+state[5],state[5],state[6]+state[7],state[7],randint(0,420),randint(0,420),randint(0,420),x2,randint(0,420),y2)
    if state[10] == (width - 80) or state [10] == 0:
        return (state[0] + state[1], state[1], state[2]+state[3], state[3], state[4]+state[5],state[5],state[6]+state[7],state[7],state[8],state[9],state[10]-state[11],-1*state[11],state[12]-state[13],state[13])

    #causes cat 2 to bounce off sides of window
    if state[12] == (height - 80) or state[12] == 0:
        return (state[0] + state[1],state[1],state[2]+state[3], state[3],state[4]+state[5],state[5],state[6]+state[7],state[7],state[8],state[9],state[10]-state[11],state[11],state[12]-state[13],-1*state[13])    
    else:
        return(state[0] + state[1], state[1], state[2] + state[3], state[3],state[4]+state[5],state[5],state[6]+state[7],state[7],state[8],state[9],state[10]+state[11],state[11],state[12]+state[13],state[13])

#states 0-3 define respectively the x,delta x, y, delta y of cat 1. states #4-7 define the x, delta x, y, delta y of the user controlled mouse, states #8-9 define the x, y of the cheese, states 10 - 13 define respectively  the #x,delta x, y, delta y of cat 2 





################################################################

# Terminate the simulation when the mouse hits either cat
def endState(state):
    if ((state[0]-50) < state[4] and state[4] < (state[0]+80) and (state[2]-50) <state[6] and state[6] < (state[2]+80)):
        return True
    if  ((state[10]-50) < state[4] and state[4] < (state[10]+80) and (state[12]-50) <state[6] and state[6] < (state[12]+80)):
        return True
    else:
        return False 


################################################################
#Whenever we click the mouse, mouse would change velocity randomly
#
# state -> event -> state
#
def handleEvent(state, event):  
#    print("Handling event: " + str(event))
    if (event.type == pg.MOUSEBUTTONDOWN):
        if (state[5],state[7]) == (state[5],state[7]):
            newState = (randint(-1,1),randint(-1,1))            
        else:
            newState = (randint(-1,1),randint(-1,1))
        return( state[0], state[1], state[2], state[3], state[4], newState[0], state[6], newState[1], state[8], state[9], state[10], state[11], state[12], state[13])
    else:
        return(state)

################################################################

#cat's velocity can't be (0,0)

x1 = randint(-1,1)
y1 = randint(-1,1)
while (x1 == 0 and y1 == 0):
    x1 == randint (-1,1) and y1 == randint (-1,1)

x2 = randint(-1,1)
y2 = randint(-1,1)
while (x2 == 0 and y2 == 0):
    x2 == randint (-1,1) and y2 == randint (-1,1)
  
    
initState = (randint(250,350), x1, randint(250,350), y1, 50, randint(-1,1), 50, randint(-1,1), randint(0,450), randint(0,450), -100, 0, -100, 0 )


# Run the simulation no faster than 60 frames per second
frameRate = 30

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
