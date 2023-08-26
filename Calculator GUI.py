from tkinter import *
from tkinter import ttk
import numpy as np

class Calc_GUI():
    def __init__(self):
        self.root =  Tk()
        self.Bg_Colour = 'grey40'
        self.calculation = ''
        self.var = StringVar()
        self.var.set('0')
        self.root.title('Calcuator')
        self.root.geometry('240x360')
        self.root.configure(background = self.Bg_Colour)
        self.root.resizable(width = False, height = False)

        #Sets up number display
        Label(self.root, textvariable=self.var, bg=self.Bg_Colour, anchor='w', 
            font=("Lucida Grande", 50, "italic"), fg='white').place(x=0, y=0)
   
    def Reset(self):
        self.calculation = ''
        self.var.set('0')

    def Input(self, i):
        if i == '=':
            self.calculation = str(self.Calculate())
            self.var.set(self.calculation)

        else:
            self.calculation += str(i)
            self.var.set(self.calculation)

    def Decimal(self):
        self.Input('=')
        self.calculation = int(self.calculation) / 100
        self.var.set(self.calculation)

    def PlusMinus(self):
        try:
            self.calculation = str(int(self.calculation) * -1)
            print(self.calculation)
            self.var.set(self.calculation)
        except:
            pass
   
    def Calculate(self):
        self.calculation = eval(self.calculation)
        return self.calculation

    def Calc_Buttons(self):
        counter = 0

        for num in range(1,10):
            x = counter*60
            y = 240 - 60*((num-1)//3) #3 numbers on each row

            #Produces button where if clicked will pass num to Input function
            Button(self.root, command=lambda num=num:self.Input(str(num)),
                text=str(num), width=6, height=3).place(x=x, y=y)
            counter += 1
            if counter == 3:
                counter = 0

        #Set up of function buttons not easily looped over
        Button(self.root, command=lambda:self.Input('0'), text='0', width=13,
            height=3).place(x=-3, y=300)
        Button(self.root, text='C', highlightbackground='Gray60',
            command=self.Reset, width=6, height=3).place(x=0, y=60)
        Button(self.root, command=self.Decimal, text='%', highlightbackground='Gray60', width=6,
            height=3).place(x=60, y=60)
        Button(self.root, command=self.PlusMinus, text='+\-', highlightbackground='Gray60', width=6,
            height=3).place(x=120, y=60)
        Button(self.root, command=lambda:self.Input('/'),
            highlightbackground='darkgoldenrod1', text='/', width=6,
            height=3).place(x=180, y=60)
        Button(self.root, command=lambda:self.Input('*'),
            highlightbackground='darkgoldenrod1',text='x', width=6,
            height=3).place(x=180, y=120)
        Button(self.root, command=lambda:self.Input('-'),
            highlightbackground='darkgoldenrod1', text='-', width=6,
            height=3).place(x=180, y=180)
        Button(self.root, command=lambda:self.Input('+'),
            highlightbackground='darkgoldenrod1', text='+', width=6,
            height=3).place(x=180,y=240)
        Button(self.root, command=lambda:self.Input('.'), text='.', width=6,
            height=3).place(x=120, y=300)
        Button(self.root, command=lambda:self.Input('='),
            highlightbackground='darkgoldenrod1', text='=', width=6,
            height=3).place(x=180, y=300)

if __name__ == "__main__":
    calc = Calc_GUI()
    calc.Calc_Buttons()
    calc.root.mainloop()
