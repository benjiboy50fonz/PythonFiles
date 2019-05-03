import turtle
from random import randint

colors = ['red', 'white', 'blue', 'red', 'white', 'blue',]


tim = turtle.Pen()
tim.speed(0)
turtle.bgcolor('black')
for i in range(720):
    tim.pencolor(colors[i % 6])
    tim.width(i / 100 + 1)
    tim.forward(i)
    tim.left(59)
    
