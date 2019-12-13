import turtle as trtl

drawBot = trtl.Turtle()
drawBot.ht()


amount = 15
wall_width = 10

for i in range(25):
    drawBot.forward(amount/3)
    drawBot.penup()
    drawBot.forward(wall_width+5)
    drawBot.pendown()
    drawBot.forward(amount/5)
    if i > 4:
        drawBot.left(90)
        drawBot.forward(wall_width+10)
        drawBot.backward(wall_width+10)
        drawBot.right(90)

    drawBot.forward(2*amount/3)


    drawBot.left(90)
    amount += wall_width



wn = trtl.Screen()
wn.mainloop()