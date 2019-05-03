import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master=None)
        self.master = master
        self.pack()
        self.generateButtonWidget('Hello!', 'red', self.printMessage('Hello!'))

    def generateButtonWidget(self, text, color, command):
        self.command = command
        self.widget = tk.Button(self, text=str(text), fg=str(color), bg='blue', command=self.command)
        self.widget.pack(side='left')
        
        return self.widget
            
    def printMessage(self, message):
        print(str(message))

root = tk.Tk()
app = App(master=root)
app.mainloop()
