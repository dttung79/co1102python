from tkinter import *
from tkinter.ttk import *

from tkinter import messagebox as msgbox

books = {'Harry Potter': ('J.K. Rowling', 50, 800),
         'The Lord of the Rings': ('J.R.R. Tolkien', 80, 1000),
         'The Da Vinci Code': ('Dan Brown', 35, 400),
         'Les Miserables': ('Victor Hugo', 30, 300)}

##### CREATE WINDOW #####
window = Tk()
window.title("BOOKS SHOPS")
window.geometry("500x300")

##### EVENT HANDLERS #####
def cbBooks_changed(event):
    book_name = cbBooks.get()                   # get selected book name
    author, price, pages = books[book_name]     # get author, price, pages from books dictionary
    lblAuthorName["text"] = author              # set text for lblAuthorName
    lblPriceValue["text"] = f'${price}'         # set text for lblPriceValue
    lblPagesValue["text"] = str(pages)          # set text for lblPagesValue

def btnBuy_clicked():
    book_name = cbBooks.get()                  # get selected book name
    _, price, _ = books[book_name]             # get price from books dictionary
    n = txtNumberOfBooks.get()                 # get number of books from txtNumberOfBooks
    try:
        payment = int(n) * price                   # calculate payment
        lblPaymentValue['text'] = f'${payment}'    # set text for lblPayment
    except ValueError:
        msgbox.showerror("Error", "Number of books must be an integer", parent=window, icon='error')
    
##### CREATE WIDGETS #####
lblbChooseBooks = Label(window, text="Choose Books:")
lblbChooseBooks.grid(column=0, row=0, sticky='e')  # right align

cbBooks = Combobox(window)
cbBooks['values'] = ("Harry Potter", "The Lord of the Rings", "The Da Vinci Code", "Les Miserables")
#cbBooks.current(0)  # select first item
cbBooks.grid(column=1, row=0, sticky='w')  # left align
# bind event to cbBooks
cbBooks.bind("<<ComboboxSelected>>", cbBooks_changed)

lblAuthor = Label(window, text="Author:")
lblAuthor.grid(column=0, row=1, sticky='e')  # right align

lblAuthorName = Label(window, text="")
lblAuthorName.grid(column=1, row=1, sticky='w')  # left align

lblPrice = Label(window, text="Price:")
lblPrice.grid(column=0, row=2, sticky='e')  # right align

lblPriceValue = Label(window, text="")
lblPriceValue.grid(column=1, row=2, sticky='w')  # left align

lblPages = Label(window, text="Pages:")
lblPages.grid(column=0, row=3, sticky='e')  # right align

lblPagesValue = Label(window, text="")
lblPagesValue.grid(column=1, row=3, sticky='w')  # left align

lblNumberOfBooks = Label(window, text="Number:")
lblNumberOfBooks.grid(column=0, row=4, sticky='e')  # right align

txtNumberOfBooks = Entry(window, width=20)
txtNumberOfBooks.grid(column=1, row=4, sticky='w')  # left align

btnBuy = Button(window, text="Buy", command=btnBuy_clicked)
btnBuy.grid(column=1, row=5, sticky='w')  # left align

lblPayment = Label(window, text="Payment:")
lblPayment.grid(column=0, row=6, sticky='e')  # right align

lblPaymentValue = Label(window, text="")
lblPaymentValue.grid(column=1, row=6, sticky='w')  # left align




##### START GUI PROGRAM #####
window.mainloop()   # window waiting for any events (click, keypress, etc.)