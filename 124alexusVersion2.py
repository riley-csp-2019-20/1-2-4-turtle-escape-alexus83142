import turtle as trtl
import random


drawBot = trtl.Turtle()
drawBot.ht()
drawBot.speed(0)

player = trtl.Turtle()


wall_width = 10
door_width = 15
wall_length = 30

def drawBarrier():
    drawBot.left(90)
    drawBot.forward(wall_width*2)
    drawBot.backward(wall_width*2)
    drawBot.right(90)

def drawDoor():
    drawBot.penup()
    drawBot.forward(door_width)
    drawBot.pendown()

for i in range(25):

    if i > 4:
        #random door location
        door = random.randint(door_width, wall_length - door_width)
        barrier = random.randint(door_width, wall_length - door_width)
        #random barrier location   
        
        if door < barrier:
            drawBot.forward(door)
            drawDoor()
            drawBot.forward(barrier-door-door_width)
            drawBarrier()
            drawBot.forward(wall_length-barrier)
            
        else: 
            drawBot.forward(barrier)
            drawBarrier()
            drawBot.forward(door-barrier)
            drawDoor()
            drawBot.forward(wall_length-door-door_width)    
        


    drawBot.left(90)
    wall_length += wall_width
    
    
def up():
    player.setheading(90)
    player.forward(10)


def down():
    player.setheading(270)
    player.forward(10)


def right():
    player.setheading(0)
    player.forward(10)

def left():
    player.setheading(180)
    player.forward(10)

wn = trtl.Screen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")

wn.listen()
wn.mainloop()