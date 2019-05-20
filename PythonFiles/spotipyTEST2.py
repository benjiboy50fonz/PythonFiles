from tkinter import *

master = Tk()

e = Entry(master)

lbl = Label(master, width=10)

def clicked():
    lbl.configure(text='hahahshahha')    

master.mainloop()

btn = Button(master, text='this is stupid', command=clicked)
