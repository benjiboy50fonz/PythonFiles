from turtle import *

import turtle

from random import *
def health(health):
    print('HEALTH = ' + str(health))

setup( width = 800, height = 500, startx = None, starty = None)

turtle.screensize(800, 500)

color('green', 'yellow')

turtle.bgcolor('black')

turtle.hideturtle()

i = turtle.Turtle()

i.penup()

i.speed(0)

i.back(250)

i.pensize(5)

i.speed(0)

i.hideturtle()

i.color('green', 'yellow')

i.pencolor("green")

i.fillcolor('green')

i.begin_fill()

i.penup()

i.back(30)

i.right(110)

i.pendown()

i.forward(150)

i.left(110)

i.forward(40)

i.left(70)

i.forward(210)

i.left(110)

i.forward(40)

i.left(70)

i.forward(60)

i.end_fill()

o = turtle.Turtle()

o.fillcolor('green')

o.speed(0)

o.penup()

o.back(250)

o.pensize(5)

o.speed(0)

o.hideturtle()

o.pencolor("green")

o.penup()

o.forward(45)

o.right(90)

o.forward(25)

o.right(200)

o.pendown()

o.begin_fill()

for x in range(10):

    o.forward(18)

    o.right(18)

o.forward(55)

for x in range(10):

    o.forward(18)

    o.right(18)

o.forward(60)

o.penup()

o.right(90)

o.forward(24)

o.left(90)

o.end_fill()

o.pendown()

o.fillcolor('black')

o.begin_fill()

for x in range(8):

    o.forward(6)

    o.right(9)

o.forward(1)

for x in range(8):

    o.forward(6)

    o.right(13)

o.forward(55)

for x in range(8):

    o.forward(6)

    o.right(9)

o.forward(1)

for x in range(8):

    o.forward(7)

    o.right(14)

o.left(2)

o.forward(55)

o.penup()



o.end_fill()

s = turtle.Turtle()

s.fillcolor('green')

s.speed(0)

s.penup()

s.back(250)

s.hideturtle()

s.pencolor('green')

s.penup()

s.pensize(5)

s.speed(0)

s.forward(200)

s.forward(90)

s.left(90)

s.forward(20)

s.right(90)

s.right(180)

s.right(20)

s.pendown()

s.begin_fill()

s.forward(10)

for x in range(9):

    s.forward(11)

    s.left(12)

for x in range(6):

    s.forward(9)

    s.left(14)

for x in range(7):

    s.forward(15)

    s.right(18)

for x in range(6):

    s.forward(14)

    s.right(15)

s.forward(30)

###---------

s.right(90)

s.forward(20)

s.right(90)

s.forward(25)

for x in range(12):

    s.forward(9)

    s.left(17)

s.forward(1)

s.left(1)

s.forward(14)

for x in range(6):

    s.forward(18)

    s.right(18)

for x in range(2):

    s.forward(28)

    s.right(18)

    s.right(10)

s.forward(2)

s.left(10)

s.forward(5)

s.right(5)

s.forward(30)

s.right(20)

s.forward(27)

s.right(99)

s.forward(16)

s.end_fill()

i2 = turtle.Turtle()

i2.speed(0)

i2.penup()

i2.back(250)

i2.penup()

i2.hideturtle()

i2.pensize(5)

i2.speed(0)

i2.color('green', 'yellow')

i2.pencolor("green")

i2.fillcolor("green")

i2.forward(380)

i2.pendown()

i2.begin_fill()

i2.circle(25)

i2.end_fill()

i2.penup()

i2.back(27)

i2.right(110)

i2.forward(20)

i2.pendown()

i2.begin_fill()

i2.forward(140)

i2.left(110)

i2.forward(40)

i2.left(70)

i2.forward(140)

i2.left(110)

i2.forward(40)

i2.end_fill()

ss = turtle.Turtle()

ss.fillcolor('green')

ss.speed(0)

ss.penup()

ss.back(250)

ss.hideturtle()

ss.pencolor('green')

ss.penup()

ss.pensize(5)

ss.speed(0)

ss.forward(445)

ss.forward(90)

ss.left(90)

ss.forward(20)

ss.right(90)

ss.right(180)

ss.right(20)

ss.pendown()

ss.begin_fill()

ss.forward(10)

for x in range(9):

    ss.forward(11)

    ss.left(12)

for x in range(6):

    ss.forward(9)

    ss.left(14)

for x in range(7):

    ss.forward(15)

    ss.right(18)

for x in range(6):

    ss.forward(14)

    ss.right(15)

ss.forward(30)

ss.right(90)

ss.forward(20)

ss.right(90)

ss.forward(25)

for x in range(12):

    ss.forward(9)

    ss.left(17)

ss.forward(1)

ss.left(1)

ss.forward(14)

for x in range(6):

    ss.forward(18)

    ss.right(18)

for x in range(2):

    ss.forward(28)

    ss.right(18)

    ss.right(10)

ss.forward(2)

ss.left(10)

ss.forward(5)

ss.right(5)

ss.forward(30)

ss.right(20)

ss.forward(27)

ss.right(99)

ss.forward(16)

ss.end_fill()

print('Welcome to Iosis! The game of skills and strategies! This game takes place in a galaxy 399 light years away, and the exact location is unknown. You are part of the Katarsis military group of the        crashing nation, known as Andeya, and you have been battling the Zortecs, an unknown alien from another galaxy. Your nation is falling to the Zortecs, and you are aboard a starship, which has    gone missing. You have been put into hyper sleep in order to conserve your body and skills. You are reactivated by an unknown source. You remember three things:')

print('    ')

print('You have one objective: support your falling nation')

print('You have been put into hyper sleep in the year of 3056')

print('You are never alone, even in the darkest corners of space')

print(' ')

print('----------------------------------------------------------------------------------------------------------------------------------------------')

print(' ')

