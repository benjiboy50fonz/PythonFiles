import turtle
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'pink', 'orange', 'indigo']
import random

t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
for i in range(360):
    t.pencolor(colors[i % 6])
    t.width(i / 100 + 1)
    v1 =  random.randint(0, i)
    add = i - v1
    v2 = add
    t.forward(v1)
    t.pencolor(random.choice(colors))
    t.forward(v2)
    t.left(59)
