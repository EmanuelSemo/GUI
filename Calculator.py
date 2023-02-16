from tkinter import *
import tkinter.font as font
import math

root = Tk()
root.geometry("360x400")

numOne = Label(root, text = "Enter First Number:", font = ( "Serif", 12))
enterOne = Entry(root)
numTwo = Label(root, text = "Enter Second Number:", font = ("Serif", 12))
enterTwo = Entry(root)

def add():
    x = int(enterOne.get())
    y = int(enterTwo.get())
    result["text"] = str(x + y)

def sub():
    x = int(enterOne.get())
    y = int(enterTwo.get())
    result["text"] = str(x - y)

def div():
    x = int(enterOne.get())
    y = int(enterTwo.get())
    result["text"] = str(x / y)

def mul():
    x = int(enterOne.get())
    y = int(enterTwo.get())
    result["text"] = str(x * y)

def sqrt():
    x = int(enterOne.get())
    result["text"] = math.sqrt(x)
    
add = Button(root, text = "+", width = 10, command = add)
sub = Button(root, text = "-", width = 10, command = sub)
div = Button(root, text = "/", width = 10, command = div)
mul = Button(root, text = "x", width = 10, command = mul)
sqr = Button(root, text = "√", width = 10, command = sqrt)


result = Label(root)
numOne.grid( row = 0, column = 0)
enterOne.grid( row = 0, column = 1)
numTwo.grid( row = 1, column = 0)
enterTwo.grid( row = 1, column = 1)
add.grid( row = 2, column = 0)
sub.grid( row = 2, column = 1)
div.grid( row = 3, column = 0)
mul.grid( row = 3, column = 1)
sqr. grid( row = 4, column = 0  )
result.grid( row = 3, column = 2)

root.mainloop()
    
