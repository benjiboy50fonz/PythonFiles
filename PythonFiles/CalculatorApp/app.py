#!/usr/bin/env python3

'''
A calculator app for my Arch raspberry pi, even though it definitley has one!
'''

import tkinter as tk

from tkinter import ttk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=400, height=700)
        
        self.buttons = {}
        self.entryString = ''
        self.recentResult = ''
        self.operators = ['+', '-', 'x', '/', '.', '^', '(', ')']
                
        self.master = master
        
        self.buildwidgets()
        self.grid()
        
    def exit(self):
        self.master.quit()
        
    def insertAns(self):
        if self.recentResult == 'Try Again':
            pass
        else:
            self.entryString += self.recentResult
            self.updateLabel()
    
    def calculateBasics(self):
        try:
            self.recentResult = str(eval(self.entryString))
            
        except(SyntaxError):
            self.recentResult = 'Try Again'
        self.displayResult()
        self.entryString = ''
    
    def delete(self):
        self.entryString = self.entryString[:-1]
        self.updateLabel()
        
    def clear(self):
        self.entryString = ''
        self.updateLabel()
    
    def gridIt(self):     
        self.leave.grid(row=7, column=0)
        self._delete.grid(row=7, column=1)
        self._clear.grid(row=7, column=2)
        self.enter.grid(row=7, column=3)
        
        self.buttons['0'].grid(row=6, column=0)
        self.buttons['.'].grid(row=6, column=1)
        self.buttons['Ans'].grid(row=6, column=2)
        self.buttons['+'].grid(row=6, column=3)
            
        self.buttons['1'].grid(row=5, column=0)
        self.buttons['2'].grid(row=5, column=1)
        self.buttons['3'].grid(row=5, column=2)
        self.buttons['-'].grid(row=5, column=3)
        
        self.buttons['4'].grid(row=4, column=0)
        self.buttons['5'].grid(row=4, column=1)
        self.buttons['6'].grid(row=4, column=2)
        self.buttons['x'].grid(row=4, column=3)
        
        self.buttons['7'].grid(row=3, column=0)
        self.buttons['8'].grid(row=3, column=1)
        self.buttons['9'].grid(row=3, column=2)
        self.buttons['/'].grid(row=3, column=3)
        
        self.buttons['^'].grid(row=2, column=3)
        self.buttons[')'].grid(row=2, column=2)
        self.buttons['('].grid(row=2, column=1)
        
        self.display.grid(row=1, column=0, columnspan=4)
                
    def buildwidgets(self):
        self.leave = tk.Button(self, text='Quit', width=3, height=1, command=self.exit)
        
        self.enter = tk.Button(self, text='Enter', width=5, height=2, command=self.calculateBasics, fg='green')
        
        self._delete = tk.Button(self, text='Delete', width=5, height=2, command=self.delete, fg='red')
                
        self._clear = tk.Button(self, text='Clear', width=5, height=2, command=self.clear, fg='red')
                
        self.buttons['Ans'] = tk.Button(self, text='Ans', width=5, height=2, command=self.insertAns, fg='blue')
        
        self.display = tk.Label(self, text=self.entryString, fg='blue')
                
        self.buttonMachine('0')
        self.buttonMachine('1')
        self.buttonMachine('2')
        self.buttonMachine('3')
        self.buttonMachine('4')
        self.buttonMachine('5')
        self.buttonMachine('6')
        self.buttonMachine('7')
        self.buttonMachine('8')
        self.buttonMachine('9')
        
        self.buttonMachine('.')
        self.buttonMachine('(')
        self.buttonMachine(')')
        
        self.buttonMachine('+')
        self.buttonMachine('-')
        self.buttonMachine('x')
        self.buttonMachine('/')
        self.buttonMachine('^')
        
        self.gridIt()
        
    def buttonMachine(self, name):
        def doYoThang():
            self.entryString += overriden
            self.updateLabel()
        
        # Add things here that will instantiate at creation
        
        if name == 'x':
            overriden = '*'
        elif name == '^':
            overriden = '**'
        else:
            overriden = name
            
        if name in self.operators:
            color = 'blue'
        else:
            color = 'black'
                
        button = tk.Button(self, text=name, width=5, height=2, command=doYoThang, fg=color)
                
        self.buttons[name] = button
        
    def updateLabel(self):
        self.display.config(text=self.entryString)
        
    def displayResult(self):
        self.display.config(text=self.recentResult)
        
class ManualInput(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        
        self.master = master
        
        self.entryString = ''
        self.recentResult = ''
        
        self.buildWidgets()
        
        self.grid()
        
    def leave(self):
        self.master.quit()
        
    def buildWidgets(self):
        self.display = tk.Label(self, fg='blue')
        self.entryBox = tk.Entry(self, bg='white')
        self.submitButton = tk.Button(self, text='Enter', fg='green', command=self.enter, width=5, height=2)
        self.clearButton = tk.Button(self, text='Clear', fg='red', command=self.clear, width=3, height=1)
        self._leave = tk.Button(self, text='Quit', fg='black', command=self.leave, width=3, height=1)
        
        self.gridIt()
        
    def gridIt(self):
        self.display.grid(row=0, column=0, columnspan=2)
        self.entryBox.grid(row=1, column=0, columnspan=2)
        self.submitButton.grid(row=2, column=0, columnspan=2)
        self.clearButton.grid(row=3, column=1)
        self._leave.grid(row=3, column=0)
        
    def enter(self):
        self.entryString = self.entryBox.get()
        self.calculateBasics()
        self.displayResult()
        
    def clear(self):
        self.entryBox.config(text='')
        
    def calculateBasics(self):
        self.recentResult = eval(self.entryString)
            
    def displayResult(self):
        self.display.config(text=self.recentResult)
        
        
root = tk.Tk()
root.title('Calculator')

tabControl = ttk.Notebook(root) # Establishes tab control

main = App(root)
manual = ManualInput(root)

tabControl.add(main, text='Main')
tabControl.add(manual, text='Manual')

#tabControl.add(main, text='Main')
tabControl.grid()

main.mainloop() # Calls the parent method

        
