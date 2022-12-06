from tkinter import *
from tkinter import messagebox as msgbox
window = Tk()
window.title("DEMO TKINTER")
window.geometry("500x300")

##### EVENT HANDLERS #####
def btnHelo_clicked():
    # get text from txtName
    name = txtName.get()
    msgbox.showinfo("Hello", "Hello " + name)

def btnLang_clicked():
    # get text from txtLanguage
    language = txtLanguage.get()
    # set text for lblWelcomeLanguage
    lblWelcomeLanguage["text"] = "Welcome to " + language

##### CREATE WIDGETS #####

lblName = Label(window, text="Enter your name:")
lblName.grid(column=0, row=0)

txtName = Entry(window, width=20)
txtName.grid(column=1, row=0)

btnHello = Button(window, text="Say Hello", command=btnHelo_clicked)
btnHello.grid(column=2, row=0)

lblLanguage = Label(window, text="Enter language:")
lblLanguage.grid(column=0, row=1)

txtLanguage = Entry(window, width=20)
txtLanguage.grid(column=1, row=1)

btnLanguage = Button(window, text="Say language", command=btnLang_clicked)
btnLanguage.grid(column=2, row=1)

lblWelcomeLanguage = Label(window, text="Welcom language")
lblWelcomeLanguage.grid(column=1, row=2)


##### START GUI PROGRAM #####
window.mainloop()   # window waiting for any events (click, keypress, etc.)
