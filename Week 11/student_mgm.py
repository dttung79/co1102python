from tkinter import *
import tkinter.messagebox as msgbox
from tkinter import filedialog

##### CREATE WINDOW #####
window = Tk()
window.title("Student Management System")
window.geometry("700x500")

students = []
##### EVENT HANDLER #####
def btnLoad_clicked():
    students.clear()
    # open file dialog to get file path
    file_path = filedialog.askopenfilename(title="Open file", 
                            filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if file_path == '':
        msgbox.showerror("Error", "Please select a file", icon='error')
        return

    with open(file_path, 'r') as f:
        lines = f.readlines()
        for row in lines:
            name = row.split(',')[0].strip()
            age = row.split(',')[1].strip()
            grade = row.split(',')[2].strip()
            students.append([name, int(age), float(grade)])

    # clear listbox
    lstBoxAllStudents.delete(0, END)
    # load data from list students to listbox
    for row in students:
        lstBoxAllStudents.insert(END, row[0])

def btnSave_clicked():
    file_path = filedialog.askopenfilename(title="Open file", 
                            filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if file_path == '':
        msgbox.showerror("Error", "Please select a file", icon='error')
        return
    
    with open(file_path, 'w') as f:
        for row in students:
            f.write(f'{row[0]},{row[1]},{row[2]}\n')
    
    msgbox.showinfo("Save", "Data saved successfully", icon='info')

def lstBoxAllStudents_clicked(event):
    # in case of unselect listbox
    if lstBoxAllStudents.curselection() == ():
        return
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
    try:
        students.append([name, int(age), float(grade)])     # add new student to list students
        lstBoxAllStudents.insert(END, name)     # add new student to listbox
        msgbox.showinfo("Add", "Student added successfully", icon='info')
    except ValueError:
        msgbox.showerror("Error", "Invalid number age or grade. Please try again.", icon='error')

def btnUpdate_clicked():
    # check if listbox is selected
    if lstBoxAllStudents.curselection() == ():
        msgbox.showerror("Error", "Please select a student", icon='error')
        return
    
    index = lstBoxAllStudents.curselection()[0]     # get selected index
    name, age, grade = get_info_textboxes()         # get student info from textboxes

    try:
        # update student in list students
        students[index] = [name, int(age), float(grade)]
        # update student name in listbox
        lstBoxAllStudents.delete(index)         # delete name at current index
        lstBoxAllStudents.insert(index, name)   # insert new name at current index
        
        msgbox.showinfo("Update", "Student updated successfully", icon='info')
    except ValueError:
        msgbox.showerror("Error", "Invalid number age or grade. Please try again.", icon='error')

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

def btnSearch_clicked():
    # get search text
    name = txtSearch.get()
    for i in range(len(students)):
        if name.lower() in students[i][0].lower():
            # clear old selection
            lstBoxAllStudents.selection_clear(0, END)
            # set listbox is selected at position i
            lstBoxAllStudents.selection_set(i)
            lstBoxAllStudents_clicked(None)
            break

##### CREATE WIDGETS #####
lblSearch = Label(window, text="Search:")
lblSearch.grid(row=0, column=0, sticky='e', pady=10)

txtSearch = Entry(window)
txtSearch.grid(row=0, column=1, sticky='w', columnspan=2)

btnSearch = Button(window, text="Search", command=btnSearch_clicked)
btnSearch.grid(row=0, column=2, sticky='w')

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

btnSave = Button(window, text="Save", command=btnSave_clicked)
btnSave.grid(row=5, column=2, pady=5)
##### START GUI #####
window.mainloop()