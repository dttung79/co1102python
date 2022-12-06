from tkinter import *
import tkinter.messagebox as msgbox

##### CREATE WINDOW #####
window = Tk()
window.title("Student Management System")
window.geometry("700x500")

students = [['Le Minh Phuong', 20, 9.5],
            ['Nguyen Thi Thuy', 19, 8.5],
            ['Nguyen Van Minh', 20, 7.0],
            ['Nguyen Thi Thu', 19, 8.0],
            ['Do Thanh Hung', 19, 9.5],
            ['Ha Dang Chinh', 21, 5.0],
            ['Tran Dang Tu', 20, 10.0]]
##### EVENT HANDLER #####
def btnLoad_clicked():
    # clear listbox
    lstBoxAllStudents.delete(0, END)
    # load data from list students to listbox
    for row in students:
        lstBoxAllStudents.insert(END, row[0])
    
def lstBoxAllStudents_clicked(event):
    # get selected index
    index = lstBoxAllStudents.curselection()[0]
    # get selected student
    s = students[index]
    txtName.delete(0, END)
    txtName.insert(0, s[0])
    txtAge.delete(0, END)
    txtAge.insert(0, s[1])
    txtGrade.delete(0, END)
    txtGrade.insert(0, s[2])


##### CREATE WIDGETS #####
lblSearch = Label(window, text="Search:")
lblSearch.grid(row=0, column=0, sticky='e', pady=10)

txtSearch = Entry(window)
txtSearch.grid(row=0, column=1, sticky='w', columnspan=2)

lblAllStudents = Label(window, text="All Students:")
lblAllStudents.grid(row=1, column=0, sticky='ne')

lstBoxAllStudents = Listbox(window, width=30, height=10)
lstBoxAllStudents.grid(row=1, column=1, sticky='w', columnspan=2, rowspan=4)
lstBoxAllStudents.bind('<<ListboxSelect>>', lstBoxAllStudents_clicked)

# create schrollbar for listbox
schrollbar = Scrollbar(window)
schrollbar.grid(row=1, column=3, sticky='nsew', rowspan=4)
# attach schrollbar to listbox
lstBoxAllStudents.config(yscrollcommand=schrollbar.set)
schrollbar.config(command=lstBoxAllStudents.yview)

lblName = Label(window, text="Name:")
lblName.grid(row=1, column=4, sticky='ne')
txtName = Entry(window, width=25)
txtName.grid(row=1, column=5, sticky='nw', columnspan=3)

lblAge = Label(window, text="Age:")
lblAge.grid(row=2, column=4, sticky='ne')
txtAge = Entry(window, width=25)
txtAge.grid(row=2, column=5, sticky='nw', columnspan=3)

lblGrade = Label(window, text="Grade:")
lblGrade.grid(row=3, column=4, sticky='ne')
txtGrade = Entry(window, width=25)
txtGrade.grid(row=3, column=5, sticky='nw', columnspan=3)

btnAdd = Button(window, text="Add", command=btnAdd_clicked)
btnAdd.grid(row=4, column=5, sticky='ne')

btnUpdate = Button(window, text="Update")
btnUpdate.grid(row=4, column=6, sticky='ne')

btnDelete = Button(window, text="Delete")
btnDelete.grid(row=4, column=7, sticky='ne')

btnLoad = Button(window, text="Load", command=btnLoad_clicked)
btnLoad.grid(row=5, column=1, pady=5)

btnSave = Button(window, text="Save")
btnSave.grid(row=5, column=2, pady=5)
##### START GUI #####
window.mainloop()