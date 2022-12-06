from tkinter import *
import tkinter.messagebox as msgbox

##### CREATE WINDOW #####
window = Tk()
window.title("Student Management System")
window.geometry("700x500")

##### EVENT HANDLER #####


##### CREATE WIDGETS #####
lblSearch = Label(window, text="Search:")
lblSearch.grid(row=0, column=0, sticky='e', pady=10)

txtSearch = Entry(window)
txtSearch.grid(row=0, column=1, sticky='w', columnspan=2)

lblAllStudents = Label(window, text="All Students:")
lblAllStudents.grid(row=1, column=0, sticky='ne')

lstBoxAllStudents = Listbox(window, width=30, height=10)
lstBoxAllStudents.grid(row=1, column=1, sticky='w', columnspan=2, rowspan=4)

# create schrollbar for listbox
schrollbar = Scrollbar(window)
schrollbar.grid(row=1, column=3, sticky='nsew', rowspan=4)
# attach schrollbar to listbox
lstBoxAllStudents.config(yscrollcommand=schrollbar.set)
schrollbar.config(command=lstBoxAllStudents.yview)

lblName = Label(window, text="Name:")
lblName.grid(row=1, column=4, sticky='ne')
txtName = Entry(window)
txtName.grid(row=1, column=5, sticky='nw', columnspan=3)

lblAge = Label(window, text="Age:")
lblAge.grid(row=2, column=4, sticky='ne')
txtAge = Entry(window)
txtAge.grid(row=2, column=5, sticky='nw', columnspan=3)

lblGrade = Label(window, text="Grade:")
lblGrade.grid(row=3, column=4, sticky='ne')
txtGrade = Entry(window)
txtGrade.grid(row=3, column=5, sticky='nw', columnspan=3)

##### START GUI #####
window.mainloop()