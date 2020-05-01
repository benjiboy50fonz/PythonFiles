#!/usr/bin/env python3

import pygame

from pygame import joystick

import tkinter as tk

import time

window = tk.Tk()

label = tk.Label(window, text='')
label.pack()

pygame.init()

buttonCount = None

if joystick.get_count() == 0:
    print("Please plug in a controller!")
    exit()
    
print('Taking joystick id 0')

myStick = joystick.Joystick(0)
myStick.init()

print('Initializing ' + str(myStick.get_name()))

buttonCount = myStick.get_numbuttons()

colors = {0 : 'green',
          1 : 'red',
          2 : 'blue',
          3 : 'yellow',
          4 : 'orange',
          5 : 'pink',
          6 : 'brown',
          7 : 'gray',
          8 : 'gold',
          9 : 'lime',
          10 : 'purple'
        }

if len(colors) < buttonCount: # Less colors than buttons
    for i in range(buttonCount - len(colors)):
        colors[i + 1] = 'black' # Black is unknown

def update(new):
    label.config(text=new)
    window.config(bg=colors[new])

count = 0

class notThisAgain:
    def __init__(self):
        self.count = 0
        self.recent = -1
        
    def runAlongSide(self):
        if self.count == 10: 
            pygame.event.pump()
            for id_ in range(buttonCount):
                if myStick.get_button(id_):
                    self.recent = id_
    #        pressed = [id_ if myStick.get_button(id_) else None for id_ in range(buttonCount)]
            self.count = 10
            
        else: 
            self.count += 1
            
        if self.recent != -1:
            update(self.recent)
    
        print(myStick.get_axis(5))
    
        window.after(100, self.runAlongSide)
    
why = notThisAgain()
    
window.after(100, why.runAlongSide)
window.mainloop()       
