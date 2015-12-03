import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint



################################################################

# This program is an interactive simulation/game. A cat starts
# to move across the screen. The direction of movement is reversed
# on each "mouse down" event.
#
# The state of the cat is represented by a tuple (pos, delta-pos).
# The first element, pos, represents the x-coordinate of the cat.
# The second element, delta-pos, represents the amount that the
# position changes on each iteration of the simulation loop.
#
# For example, the tuple (7,1) would represent the cat at x-coord,
# 7, and moving to the right by 1 pixel per "clock tick."
# 
# The initial state of the cat in this program is (0,1), meaning that the cat
# starts at the left of the screen and moves right one pixel per tick.
#
# Pressing a mouse button down while this simulation run updates the cat state
# by leaving pos unchanged but reversing delta-pos (changing 1 to -1 and vice
# versa). That is, pressing a mouse key reverses the direction of the
# cat.
#
# The simulation ends when the cat is allowed to reach either the left
# or the right edge of the screen.

################################################################

# Initialize world
name = "Click to Move! Get the Cheese! Avoid the Cat!"
width = 500
height = 500
rw.newDisplay(width, height, name)

################################################################


# Display the state by drawing a cat at that x coordinate
myimage = dw.loadImage("level1.jpeg")
mymouse = dw.loadImage("mouse.jpeg")
mycheese = dw.loadImage("cheese.jpeg")
#fonts for words
font = pg.font.Font(None, 60)
dangerText = font.render("DANGER!", 1, (255, 255, 0))

# state -> image (IO)
# draw the cat halfway up the screen (height/2) and at the x
# coordinate given by the first component of the state tuple
'''this code shows the user how close the mouse is from the cat by turning the screen red and displaying danger when they are close'''
def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(myimage, (state.cat.xcord, state.cat.ycord))
    dw.draw(mymouse, (state.mouse.xcord, state.mouse.ycord))
    dw.draw(mycheese, (state.cheese.xcord,state.cheese.ycord))
    if ((state.cheese.xcord-75) < state.mouse.xcord and state.mouse.xcord < (state.cat.xcord+105) and (state.cat.ycord-75) <state.mouse.ycord and state.mouse.ycord < (state.cat.ycord+105)):
        dw.fill(dw.red)
        dw.draw(myimage, (state.cat.xcord, state.cat.ycord))
        dw.draw(mymouse, (state.mouse.xcord, state.mouse.ycord))
        dw.draw(mycheese, (state.cheese.xcord,state.cheese.ycord))
        dw.draw(dangerText, (state.mouse.xcord - 70 , state.mouse.ycord + 70))
        


################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# Note that pos is accessed as state[0], and delta-pos
# as state[1]. Later on we'll see how to access state
# components by name (as we saw with records in Idris).
#
# state -> state

"""states 0-3 define respectively the x,delta x, y, delta y of cat 1. states 4-7 define the x, delta x, y, delta y of the user controlled mouse, states 8-9 define the x, y of the cheese"""
    
def updateState(state):

    #causes cat1 to bounce off x defined boundries of window 
    if state.cat.xcord == (width - 80) or state.cat.xcord == 0:
        return (state.cat.xcord - state.cat.xvelocity, -1 * state.cat.xvelocity ,state.cat.ycord - state.cat.yvelocity, state.cat.yvelocity , state.mouse.xcord + state.mouse.xvelocity, state.mouse.xvelocity, state.mouse.ycord+state.mouse.yvelocity, state.mouse.yvelocity ,state.cheese.xcord,state.cheese.ycord)

    #causes cat1 to bounce off y defined boundries of window 
    if state.cat.ycord == (height - 80) or state.cat.ycord == 0:
        return (state.cat.xcord - stat.cat.xvelocity,state.cat.xvelocity,state.cat.ycord-state.cat.yvelocity, -1 * state.cat.yvelocity, state.mouse.xcord + state.mouse.xvelocity, state.mouse.xvelocity, state.mouse.ycord+state.mouse.yvelocity, state.mouse.yvelocity ,state.cheese.xcord,state.cheese.ycord)

    #causes mouse to bounce off x defined boundries of window 
    if state.mouse.xcord == (width - 50) or state.mouse.xcord == 0:
        return (state.cat.xcord + state.cat.xvelocity,  state.cat.xvelocity ,state.cat.ycord + state.cat.yvelocity, state.cat.yvelocity , state.mouse.xcord - state.mouse.xvelocity, -1 *state.mouse.xvelocity, state.mouse.ycord - state.mouse.yvelocity, state.mouse.yvelocity ,state.cheese.xcord,state.cheese.ycord)

    #causes cat1 to bounce off y defined boundries of window
    if state.mouse.xcord == (width - 50) or state.mouse.xcord == 0:
        return (state.cat.xcord + state.cat.xvelocity,  state.cat.xvelocity ,state.cat.ycord + state.cat.yvelocity, state.cat.yvelocity , state.mouse.xcord - state.mouse.xvelocity, -state.mouse.xvelocity, state.mouse.ycord - state.mouse.yvelocity,-1 * state.mouse.yvelocity ,state.cheese.xcord,state.cheese.ycord)
    #hitbox detection for cheese
    if ((state.mouse.xcord-50) < state.cheese.xcord  < (state.mouse.xcord+50) and (state.mouse.ycord-50) < state.cheese.ycord < (state.mouse.ycord+50)):
        return (state.cat.xcord + state.cat.xvelocity,  state.cat.xvelocity ,state.cat.ycord + state.cat.yvelocity, state.cat.yvelocity , state.mouse.xcord + state.mouse.xvelocity, state.mouse.xvelocity, state.mouse.ycord + state.mouse.yvelocity, state.mouse.yvelocity ,(randint(0,420)),randint(0,420))
    else:
        return(state.cat.xcord + state.cat.xvelocity,  state.cat.xvelocity ,state.cat.ycord + state.cat.yvelocity, state.cat.yvelocity , state.mouse.xcord + state.mouse.xvelocity, state.mouse.xvelocity, state.mouse.ycord + state.mouse.yvelocity, state.mouse.yvelocity ,state.cheese.xcord , state.cheese.ycord)

################################################################

# Terminate the simulation when the x coord reaches the screen edge,
# that is, when pos is less then zero or greater than the screen width
# state -> bool

#Terminate the simulation when the mouse hits the cat
def endState(state):
    if ((state[0]-50) < state[4] and state[4] < (state[0]+80) and (state[2]-50) <state[6] and state[6] < (state[2]+80)):
        return True
    else:
        return False 


################################################################

# We handle each event by printing (a serialized version of) it on the console
# and by then responding to the event. If the event is not a "mouse button down
# event" we ignore it by just returning the current state unchanged. Otherwise
# we return a new state, with pos the same as in the original state, but
# delta-pos reversed: if the cat was moving right, we update delta-pos so that
# it moves left, and vice versa. Each mouse down event changes the cat
# direction. The game is to keep the cat alive by not letting it run off the
# edge of the screen.
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
        return((state[0],state[1],state[2],state[3],state[4],newState[0],state[6],newState[1],state[8],state[9]))
    else:
        return(state)

################################################################

# World state will be single x coordinate at left edge of world

# The cat starts at the left, moving right
# The mouse starts in the bottom right of the screen

#defining x and y makes sure cats velocity cant be (0,0)
x = randint(-1,1)
y = randint(-1,1)
while (x == 0 and y == 0):
    x = randint (-1,1)
    y = randint (-1,1)
   
initstate = {
    'catxcord': randint(250,350)
    'catxvelocity': x
    'catycord': randint(250,350)
    'catyvelocity': y
    'mousexcord': 50
    'mousexvelocity': randint(-1,1)
    'mouseycord': 50
    'mouseyvelocity': randint(-1,1)
    'cheesexcord': randint(0,450)
    'cheeseycord': randint(0,450)
    }

class State:
    def mouse(self,integer):
        self.xcord = integer
        self.xvelocity = integer
        self.ycord = integer
        self.yvelocity = integer
    def cat(self,integer):
        self.xcord = integer
        self.xvelocity = integer
        self.ycord = integer
        self.yvelocity = integer
    def cheese(self,integer):
        self.xcord = integer
        self.ycord = integer
        
ooInitState = State()
#initState= (state0=catxcord,state1-catxvelocity,state2-catycord,state3-catyvelocity,state4-mousexcord,state5-mousexvelocity,state6-mouseycord,state7-mouseyvelocity,state8-cheesexcord,state9-cheeseycord)
#initState = (randint(250,350),x,randint(250,350),y,50, randint(-1,1), 50, randint(-1,1),randint(0,450),randint(0,450))


# Run the simulation no faster than 60 frames per second
frameRate = 30

# Run the simulation!
rw.runWorld(ooInitState, updateDisplay, updateState, handleEvent,
            endState, frameRate)


















































