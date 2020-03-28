#!/usr/bin/env python3

'''
A calculator app for my Arch raspberry pi, even though it definitley has one!
'''

import math

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
        self._leave = tk.Button(self, text='Quit', fg='black', command=self.leave, width=3, height=1)
        
        self.gridIt()
        
    def gridIt(self):
        self.display.grid(row=0, column=0, columnspan=2)
        self.entryBox.grid(row=1, column=0, columnspan=2)
        self.submitButton.grid(row=2, column=0, columnspan=2)
        self._leave.grid(row=3, column=0, columnspan=2)
            
        self.master.grid_columnconfigure(0, minsize=100)
            
    def enter(self):
        self.entryString = self.entryBox.get()
        
        self.calculateBasics()
        
        if '==' in self.entryString:
            if self.recentResult == True:
                self.recentResult = 'True'
            else:
                self.recentResult = 'False'
                
        self.displayResult()
        
        self.recentResult = '' # Re-updates it after display
        
    def calculateBasics(self):
        self.recentResult = eval(self.entryString)
            
    def displayResult(self):
        self.display.config(text=self.recentResult)
        
class EquationSolver(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.master = master
        
        self.legalAlphabet = ['a',
                              'b',
                              'c',
                              'd',
                              'e',
                              'f',
                              'g',
                              'h',
                              'i',
                              'j',
                              'k',
                              'l',
                              'm',
                              'n',
                              'o',
                              'p',
                              'q',
                              'r',
                              's',
                              't',
                              'u',
                              'v',
                              'w',
                              'x',
                              'y',
                              'z']
        
        self.operators = ['+', '-', '*', '/']
        
        self.operatorFunctions = {'+' : self.add,
                                  '-' : self.sub,
                                  '*' : self.mult,
                                  '/' : self.div}
        
        self.equation = ''
        self.variables = []
        
        self.customLabels = []
        self.customEntries = []
        
        self.varsAndEnties = []
        
        self.buildStandardWidgets()
    def reset(self):
        self.equation = ''
        self.variables = []
        
        self.customLabels = []
        self.customEntries = []
        
        self.varsAndEnties = []
        
    def buildStandardWidgets(self):
        self.eqEntry = tk.Entry(self, bg='white')
        
        self.submitEq = tk.Button(self, text='Enter Equation', fg='blue', command=self.configureStuff)
        
        self.submitVars = tk.Button(self, text='Enter Variables', fg='blue', command=self.getEntries)
        
        self.resultLabel = tk.Label(self, text='', fg='blue')
        
        self.clearButton = tk.Button(self, text='Clear All', fg='red', command=self.reset)
        
        self.gridStandards()
        
    def gridStandards(self):
        self.eqEntry.grid(row=1, column=0)
        
        self.submitEq.grid(row=2, column=0)
        
        self.clearButton.grid(row=1, column=1)
        
    def configureStuff(self):
        self.reset()
        eq = str(self.eqEntry.get()).lower()
        
        self.equation = eq
        
        for char in eq:
            if char in self.legalAlphabet:
                if char not in self.variables:
                    self.variables.append(char)
                            
        for char in self.equation: # Removes white space that the strip() could not clear.
            if char == ' ':
                self.equation = self.equation[:(self.equation.index(' '))] + self.equation[(self.equation.index(' ') + 1):]
                print(self.equation)
                    
        self.buildCustomInputs()
                    
    def buildCustomInputs(self):
        rowCount = 3
        for var in self.variables:
            str_ = var + ' = '
            self.customLabels.append(tk.Label(self, text=str_, fg='green'))
            self.customEntries.append(tk.Entry(self, bg='white'))
                                     
            self.customLabels[rowCount - 3].grid(row=rowCount, column=0)
            self.customEntries[rowCount - 3].grid(row=rowCount, column=1)
            
            rowCount += 1
            
        self.submitVars.grid(row=rowCount, column=0)
        self.resultLabel.grid(row=rowCount + 1, column=0)
            
    def getEntries(self):
        for var, entrySpace in zip(self.variables, self.customEntries):
            self.replace(var)
                        
    def replace(self, variable):
        count = 0
        for char in str(self.equation):
            if char == str(variable):
                print('here')
                index = self.equation.index(char, count)
                
                
                
                
                # This mumbled shit fucking sucks. Going to rewrite
                
                #try:
                    #if self.equation[index - 1] in self.legalAlphabet:
                        #if self.equation[index - 1] == char: # Check variables to square itself.
                            #self.equation = self.equation[:(index - 1)] + str(char) + '**2' + self.equation[(index + 1):] # Up to, but not including!
                #except(IndexError):
                    #pass
                                    
                
                #try:
                    #print('index = ' + str(index))
                    #if (self.equation[index - 1] not in self.legalAlphabet and self.equation[index + 1] not in self.legalAlphabet) and self.equation[index - 2] == char: # Looks to combine like terms between the current character and ones two spaces behind itself.
                        #print('wellll')
                        #operator = self.equation[index - 1]
                        #other = self.equation[index - 2]
                    
                        #coefs = False
                    
                        #if self.equation[index - 3] not in self.legalAlphabet or self.equation[index - 3] not in self.operators: # Looks to see if the like term has a coefficient
                            #digitIndexer = 3
                            #digitCount = 1
                            #try:
                                #checking = True
                                #while checking:
                                    #if self.equation[index - digitIndexer] not in self.legalAlphabet or self.equation[index - digitIndexer] not in self.operators:
                                        #digitIndexer += 1
                                        #digitCount += 1
                                    #else:
                                        #checking = False
                            #except(IndexError, TypeError):
                                #checking = False
                                #digitIndexer -= 1 
                                        
                            #other = self.equation[(index - digitIndexer):((index - digitIndexer) + digitCount)]
                            #coefs = True
                            
                        #final = self.operatorFunctions[self.equation[index - 1]](char, other, coefs, True)
                        
                        #self.equation = self.equation[:(index - digitIndexer) + 1] + '+' + final + '+' + self.equation[(index + 1):]
                                                        
                #except(IndexError):
                    #print('FUCK')
                    #pass

            #print(self.equation)
            #count += 1


    def add(self, main, other, coefs=False, invert=False):
        oldMain = main
        if not coefs:
            return '2' + str(main)
        else:
            if len(other) == 1:
                other = '1 '
            
            if len(main) == 1:
                main = '1 ' 
        
            var = float(main[:-1]) + float(other[:-1])
            
            if int(var) == var:
                var = int(var)
            
            return str(var) + oldMain[-1]
        
    def sub(self, main, other, coefs=False, invert=False):
        oldMain = main
        if not coefs:
            return  '' # They cancel out!
        else: 
            if len(other) == 1:
                other = '1 '
            
            if len(main) == 1:
                main = '1 ' 
                
            if not invert:
                var = float(main[:-1]) - float(other[:-1])
            
            else:
                var = float(other[:-1]) - float(main[:-1])
                
            if int(var) == var:
                var = int(var)
            
            return str(var) + oldMain[-1]

            
    def mult(self, main, other, coefs=False, invert=False):
        pass

    def div(self, main, other, coefs=False, invert=False):
        pass

root = tk.Tk()
root.title('Calculator')

tabControl = ttk.Notebook(root) # Establishes tab control

main = App(root)
manual = ManualInput(root)
eqSolver = EquationSolver(root)

tabControl.add(main, text='Main')
tabControl.add(manual, text='Manual')
tabControl.add(eqSolver, text='Equation Solver')

tabControl.grid()

main.mainloop() # Calls the parent method
        
