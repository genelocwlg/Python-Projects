from tkinter import *
from tkinter import messagebox
import math
window = Tk()
window.geometry("500x285")
window.title("Calculator")
window.wm_attributes("-topmost", 1)
number = ""
def add(character):
    global number
    try:
        if character == "√":
            number = str(math.sqrt(float(number)))
            nlabel.config(text= number)
        else:
            if number == "ERROR" or number == "0":
                number = ""
                number += str(character)
                nlabel.configure(text = number)
            else:
                if len(number) <= 25:
                    number += str(character)
                    nlabel.configure(text = number)
                else: 
                    pass
    except:
        number = "ERROR"
        nlabel.configure(text = "ERROR")
        messagebox.showerror("An Error Occured", "Error: Invalid Equation")
def solve():
    global number
    try:
        nlabel.configure(text = str(eval(number)))
        number = str(eval(number))
    except:
        number = "ERROR"
        nlabel.configure(text = "ERROR")
        messagebox.showerror("An Error Occured", "Error: Invalid Equation")
def delete(clear):
    global number
    if nlabel['text'] == "ERROR":
        number = ""
        nlabel.configure(text = "")
    else:
        if clear:
            number = ""
            nlabel.configure(text = "")
        else:
            number = number[:-1]
            nlabel.configure(text = number)
def ab():
    global number
    try:
        if int(number) >= 0:
            number = str(0 - float(number))
        elif int(number) < 0:
            number = str(abs(float(number)))
    except:
        number = "ERROR"
        nlabel.configure(text = "ERROR")
        messagebox.showerror("An Error Occured", "Error: Invalid Equation")
    nlabel.configure(text = number)

nlabel = Label(window, text = number, width = 69, height = 3, bg = "light grey", justify = "right", relief = "sunken", bd = 5)
nlabel.grid(row = 0, column= 0, columnspan = 10)
n1 = Button(window, text = 1, width = 7, height = 3, command = lambda:add("1")).grid(row = 1, column = 0)
n2 = Button(window, text = 2, width = 7, height = 3, command = lambda:add("2")).grid(row = 1, column = 1)
n3 = Button(window, text = 3, width = 7, height = 3, command = lambda:add("3")).grid(row = 1, column = 2)
n4 = Button(window, text = 4, width = 7, height = 3, command = lambda:add("4")).grid(row = 2, column = 0)
n5 = Button(window, text = 5, width = 7, height = 3, command = lambda:add("5")).grid(row = 2, column = 1)
n6 = Button(window, text = 6, width = 7, height = 3, command = lambda:add("6")).grid(row = 2, column = 2)
n7 = Button(window, text = 7, width = 7, height = 3, command = lambda:add("7")).grid(row = 3, column = 0)
n8 = Button(window, text = 8, width = 7, height = 3, command = lambda:add("8")).grid(row = 3, column = 1)
n9= Button(window, text = 9, width = 7, height = 3, command = lambda:add("9")).grid(row = 3, column = 2)
n0= Button(window, text = 0, width = 7, height = 3, command = lambda:add("0")).grid(row = 4, column = 1)
nplus = Button(window, text = "+", width = 7, height = 3, command = lambda:add("+")).grid(row = 1, column = 3)
nmin = Button(window, text = "-", width = 7, height = 3, command = lambda:add("-")).grid(row = 2, column = 3)
ndev = Button(window, text = "/", width = 7, height = 3, command = lambda:add("/")).grid(row = 3, column = 3)
nmul = Button(window, text = "*", width = 7, height = 3, command = lambda:add("*")).grid(row = 2, column = 4)
nsolve = Button(window, text = "=", width = 7, height = 3, command = solve).grid(row = 4, column = 3)
nrad = Button(window, text = "√",width = 7, height = 3, command = lambda:add("√")).grid(row = 1, column = 4)
ndel = Button(window, text = "AC", width = 7, height = 3, command = lambda:delete(True)).grid(row = 4, column = 4)
ndel2 = Button(window, text = " DEL", width = 7, height = 3, command = lambda:delete(False)).grid(row = 3, column = 4)
npoint = Button(window, text = ".", width = 7, height = 3, command = lambda:add(".")).grid(row = 4, column = 0)
nab = Button(window, text = "+/-", width = 7, height = 3, command = ab).grid(row = 4, column = 2)
ntext = Label(window, text = "Write your notes here").grid(row = 1, column = 6, columnspan = 20)
nentry = Text(window, font = 'arial 10',width = 40, height = 10).grid(row =  2, column = 6, columnspan = 100, rowspan = 5)
window.mainloop()
#credits to geneloclwg
