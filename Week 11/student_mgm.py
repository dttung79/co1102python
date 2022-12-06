from tkinter import *
import tkinter.messagebox as msgbox

##### CREATE WINDOW #####
window = Tk()
window.title("Student Management System")
window.geometry("700x500")

students = []
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

def btnAdd_clicked():
    name, age, grade = get_info_textboxes() # get student info from textboxes
    students.append([name, age, grade])     # add new student to list students
    lstBoxAllStudents.insert(END, name)     # add new student to listbox

def btnUpdate_clicked():
    # check if listbox is selected
    if lstBoxAllStudents.curselection() == ():
        msgbox.showerror("Error", "Please select a student", icon='error')
        return
    
    index = lstBoxAllStudents.curselection()[0]     # get selected index
    name, age, grade = get_info_textboxes()         # get student info from textboxes

    # update student in list students
    students[index] = [name, age, grade]
    # update student name in listbox
    lstBoxAllStudents.delete(index)         # delete name at current index
    lstBoxAllStudents.insert(index, name)   # insert new name at current index
    
    msgbox.showinfo("Update", "Student updated successfully", icon='info')

def btnDelete_clicked():
    # check if listbox is selected
    if lstBoxAllStudents.curselection() == ():
        msgbox.showerror("Error", "Please select a student", icon='error')
        return
    
    index = lstBoxAllStudents.curselection()[0]     # get selected index

    # delete student in list students
    students.pop(index)
    # delete student name in listbox
    lstBoxAllStudents.delete(index)

    msgbox.showinfo("Delete", "Student deleted successfully", icon='info')

def get_info_textboxes():
    name = txtName.get()    # get name from textbox
    age = txtAge.get()      # get age from textbox
    grade = txtGrade.get()  # get grade from textbox
    return name, age, grade

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

btnUpdate = Button(window, text="Update", command=btnUpdate_clicked)
btnUpdate.grid(row=4, column=6, sticky='ne')

btnDelete = Button(window, text="Delete", command=btnDelete_clicked)
btnDelete.grid(row=4, column=7, sticky='ne')

btnLoad = Button(window, text="Load", command=btnLoad_clicked)
btnLoad.grid(row=5, column=1, pady=5)

btnSave = Button(window, text="Save")
btnSave.grid(row=5, column=2, pady=5)
##### START GUI #####
window.mainloop()