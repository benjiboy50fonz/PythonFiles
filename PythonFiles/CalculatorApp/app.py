#!/usr/bin/env python3

'''
A calculator app for my Arch raspberry pi, even though it definitley has one!
'''

import math

import re

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
        
        self.operators = ['+', '-', '*', '/', '=']
        
        self.equation = ''
        
        self.equationTerms = {}
        
        self.variables = []
        
        self.leftSideTerms = []
        self.rightSideTerms = []
        self.terms = []
        
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
        self.cc = 1 # Starts with one for the equal sign
        self.reset()
        eq = str(self.eqEntry.get()).lower()
                
        self.equation = eq
        
        for char in eq:
            if char in self.legalAlphabet:
                if char not in self.variables:
                    self.variables.append(char)
                            
            # Removes white space that the strip() could not clear.
            elif char == ' ':
                self.equation = self.equation[:(self.equation.index(' '))] + self.equation[(self.equation.index(' ') + 1):]
                
            elif char in self.operators:
                self.cc += 1
                    
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
        
    def findVarEnd(self, term, startWith=-1):
        try:
            while term[startWith] in self.legalAlphabet:
                startWith -= 1
            return startWith + 1
        except(IndexError):
            return startWith + 1
        
    def getEntries(self):
        signCount = 0
        for char in self.equation:
            if char == '=':
                signCount += 1
            
        if signCount > 1:
            return False
                
        separatedLeft = re.split('[+*/-]', self.equation.split('=')[0]) # This was NOT fun.
        separatedRight = re.split('[+*/-]', self.equation.split('=')[1])
        
        termID = 0
        
        for term in separatedLeft:
            gotit = False
            if term[-1] in self.legalAlphabet: # Makes sure its a variable
                i = self.findVarEnd(term)
                
                obj = Term(str(term)[:i], False, termID, str(term)[i:])
                
                self.equationTerms[termID] = obj 
                
                self.terms.append(obj)
                self.leftSideTerms.append(obj)
                gotit = True
                
            try:
                if not gotit and math.isfinite(int(term[-1])): # No variable, does not need i because they would all be nums. 3x4 is not a thing, but 34 is lol
                    obj = Term(str(term), False, termID)

                    self.equationTerms[termID] = obj 
                    
                    self.terms.append(obj)
                    self.leftSideTerms.append(obj)
                
            except(TypeError):
                print('Error line 347')
                
            termID += 1
        
        #termID = 0
        for term in separatedRight:
            gotit = False
            if term[-1] in self.legalAlphabet: # Makes sure its a variable
                i = self.findVarEnd(term)
                
                obj = Term(str(term)[:i], True, termID, str(term)[i:])
                    
                self.equationTerms[str('-' + str(termID))] = obj 
                
                self.terms.append(obj)
                self.rightSideTerms.append(obj)
                gotit = True
                
            try:
                if not gotit and math.isfinite(int(term[-1])): # No variable
                    obj = Term(str(term), True, termID)
                    
                    self.equationTerms[str('-' + str(termID))] = obj 
                    
                    self.terms.append(obj)
                    self.rightSideTerms.append(obj)
                
            except(TypeError):
                print('Error line 360')
                
            termID += 1
                
        self.combineLikeTerms()
        
    def makeFloatsInts(self):
        for term in self.terms:
            if int(term.coefficient) == term.coefficient:
                term.coefficient = int(term.coefficient)
                
    def getOpBetween(self, term, other):
        goalOne = term.getTermID()
        goalTwo = other.getTermID()
        
        termCount = -1
        same = False
        possibleOpFound = False
        operator = 'temp'
        
        for char in self.equation:
            if char in self.legalAlphabet and not same:
                same = True
                termCount += 1
                if termCount == goalOne or termCount == goalTwo:
                    if not possibleOpFound:
                        possibleOpFound = True
                    else:
                        return operator
            
            try:
                if math.isfinite(float(char)) and not same:
                    same = True
                    termCount += 1
                    if termCount == goalOne or termCount == goalTwo:
                        if not possibleOpFound:
                            possibleOpFound = True # Works here
                        else:
                            return operator
                
            except(ValueError):
                pass
            
            if char in self.operators and not possibleOpFound:
                same = False
                
            elif char in self.operators and possibleOpFound:
                operator = char
                same = False
                        
        return False # Did not succeed if it went through every character.
    
                
    def combineLikeTerms(self):
        
        '''
        We have to be careful with this because we can't just willy-nilly combine like terms; instead, we must find the like terms on each side, then perform valid operations between them.
        '''
        
        newEq = self.equation
        
        duplicate = self.terms
        for term in self.terms:
            for termTwo in duplicate:
                if term is termTwo:
                    pass
                else:

                    if term.equalSignSide == termTwo.equalSignSide and term.termType == termTwo.termType and abs(term.termID - termTwo.termID) == 1: # Term ID is used to find out if the terms are next to each other. Look at constructor for more info.
                        operator = self.getOpBetween(termTwo, term)
                        
                        if term.termID > termTwo.termID:
                            finalTerm = termTwo.op(term, operator)
                        else:
                            finalTerm = term.op(termTwo, operator)
                        
                        newEq = newEq.replace(term.stringId + operator + termTwo.stringId, finalTerm, 1)
                        if newEq == self.equation: # If the last one did not change anything, then the variables must need to be reversed. 
                            newEq = newEq.replace(termTwo.stringId + operator + term.stringId, finalTerm, 1)
                
            
        print('f ' + str(newEq))
            

class Term:
        
    def __init__(self, coefficient, sideOfSign, termID, variable=None):
        
        self.opToFunc = {'+' : self.addTerms,
                         '-' : self.subTerms,
                         '*' : self.multTerms,
                         '/' : self.divTerms,
                         }
        
        self.coefficient = coefficient # coefficient can be a constant; just leave the variable argument as default!
        
        self.equalSignSide = sideOfSign # Left is False, and right is True
        
        self.termID = termID # the position of this term, relative to the others on that side, starting at zero.
        
        if variable is None:
            self.variableString = ''
            self.termType = 'constant'
            
        else:
            self.variableString, self.termType = str(variable), str(variable)
            
        self.stringId = str(self.coefficient) + str(self.variableString)
        
    def op(self, otherTerm, operator):
        return self.opToFunc[str(operator)](otherTerm)
        
    def getTermID(self):
        return self.termID
        
    def addTerms(self, other):
        if self.termType == other.termType:
            finalCoef = float(self.coefficient) + float(other.coefficient)
            finalVar = self.variableString
                    
            if str(self.coefficient).isdigit() and str(other.coefficient).isdigit():
                return str(int(finalCoef)) + finalVar
            return str(finalCoef) + finalVar
        
    def subTerms(self, other):
        if self.termType == other.termType:
            finalCoef = float(self.coefficient) - float(other.coefficient)
            finalVar = self.variableString
            
            if str(self.coefficient).isdigit() and str(other.coefficient).isdigit():
                return str(int(finalCoef)) + finalVar
            return str(finalCoef) + finalVar
        
    def divTerms(self, other):
        if self.termType == other.termType:
            finalCoef = float(self.coefficient) / float(other.coefficient)
            finalVar = self.variableString
            
            if str(self.coefficient).isdigit() and str(other.coefficient).isdigit():
                return str(int(finalCoef)) + finalVar
            return str(finalCoef) + finalVar

    def multTerms(self, other):
        if self.termType == other.termType:
            finalCoef = float(self.coefficient) * float(other.coefficient)
            finalVar = self.variableString
            
            if str(self.coefficient).isdigit() and str(other.coefficient).isdigit():
                return str(int(finalCoef)) + finalVar
            return str(finalCoef) + finalVar
        
    def getCoef(self):
        return self.coefficient
    
    def getVar(self):
        return self.variableString
    
    def getTermType(self):
        return self.termType

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
        
