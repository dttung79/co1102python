from tkinter import *
from tkinter import messagebox as msgbox

##### CREATE WINDOW #####
window = Tk()
window.title("DEMO ARITHMETIC OPERATORS")
window.geometry("500x300")

##### EVENT HANDLERS #####
def btnPlus_clicked():
    perform_operator("+")

def btnMinus_clicked():
    perform_operator("-")

def btnMultiply_clicked():
    perform_operator("*")

def btnDivide_clicked():
    perform_operator("/")

def perform_operator(op):
    a = int(txtA.get())     # get number 1 from txtA
    b = int(txtB.get())     # get number 2 from txtB
    c = a + b if op == "+" else a - b if op == "-" else a * b if op == "*" else a / b
    lblResult["text"] = str(c)           # set text for lblResult
    lbl2ops["text"] = "a " + op + " b"   # set operator for lbl2ops

##### CREATE WIDGETS #####
lblA = Label(window, text="a:")
lblA.grid(column=0, row=0)

txtA = Entry(window, width=30)
txtA.grid(column=1, row=0, columnspan=4) # expand txtA to 4 columns
txtA.focus()    # set focus to txtA

lblB = Label(window, text="b:")
lblB.grid(column=0, row=1)

txtB = Entry(window, width=30)
txtB.grid(column=1, row=1, columnspan=4) # expand txtB to 4 columns

btnPlus = Button(window, text="+", command=btnPlus_clicked)
btnPlus.grid(column=1, row=2)

btnMinus = Button(window, text="-", command=btnMinus_clicked)
btnMinus.grid(column=2, row=2)

btnMultiply = Button(window, text="*", command=btnMultiply_clicked)
btnMultiply.grid(column=3, row=2)

btnDivide = Button(window, text="/", command=btnDivide_clicked)
btnDivide.grid(column=4, row=2)

lbl2ops = Label(window, text="a+b")
lbl2ops.grid(column=0, row=3)

lblResult = Label(window, text="")
lblResult.grid(column=1, row=3, columnspan=4, sticky='w') # expand lblResult to 4 columns

##### START GUI PROGRAM #####
window.mainloop()   # window waiting for any events (click, keypress, etc.)