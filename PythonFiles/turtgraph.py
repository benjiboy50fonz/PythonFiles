import turtle

def start():
    window = turtle.Screen()
    window.screensize(10000,10000)
    grid1 = turtle.Turtle()
    grid1.hideturtle()
    grid1.penup()
    grid1.setposition(-410, 300)
    rowspace = 0
    grid1.speed(0)
    for i in range(25):
        rowspace += 20
        grid1.forward(818)
        grid1.penup()
        grid1.backward(818)
        grid1.sety(rowspace)
        grid1.pendown()




start()
