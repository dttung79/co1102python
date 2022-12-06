from tkinter import *
from tkinter import messagebox as msgbox
PYTHON_PRICE = 100
JAVA_PRICE = 120
C_SHARP_PRICE = 90
NEW_STUDENT = 1
OLD_STUDENT = 2
DISCOUNT = 0.9
##### CREATE WINDOW #####
window = Tk()
window.title("DEMO OPTIONS")
window.geometry("500x300")

##### EVENT HANDLERS #####
def chk_language_clicked():
    payment = get_payment()
    # set text for lblPayment
    lblPayment["text"] = f'Payment: ${payment}'
    
    if student_state.get() == OLD_STUDENT:
        payment = payment * DISCOUNT
    lblFinalPayment["text"] = f'Final payment: ${payment}'

def rd_student_clicked():
    payment = get_payment()
    if student_state.get() == OLD_STUDENT:
        payment = payment * DISCOUNT
    lblFinalPayment["text"] = f'Final payment: ${payment}'

def get_payment():
    payment = 0
    payment += PYTHON_PRICE if python_state.get() else 0
    payment += JAVA_PRICE if java_state.get() else 0
    payment += C_SHARP_PRICE if csharp_state.get() else 0
    return payment

##### CREATE WIDGETS #####
lblChooseCourses = Label(window, text="Choose courses:")
lblChooseCourses.grid(column=0, row=0)

python_state = BooleanVar()
python_state.set(False) 
chkPython = Checkbutton(window, text="Python ($100)", var=python_state, command=chk_language_clicked)
chkPython.grid(column=1, row=1, sticky='w')

java_state = BooleanVar()
java_state.set(False)
chkJava = Checkbutton(window, text="Java ($120)", var=java_state, command=chk_language_clicked)
chkJava.grid(column=1, row=2, sticky='w')

csharp_state = BooleanVar()
csharp_state.set(False)
chkCSharp = Checkbutton(window, text="C# ($90)", var=csharp_state, command=chk_language_clicked)
chkCSharp.grid(column=1, row=3, sticky='w')

lblPayment = Label(window, text="Payment: $0")
lblPayment.grid(column=0, row=4, sticky='w')

lblStudent = Label(window, text="Student type:")
lblStudent.grid(column=0, row=5, sticky='w')

student_state = IntVar()
student_state.set(1)
radNewStudent = Radiobutton(window, text="New student (no discount)", 
                            value=NEW_STUDENT, var=student_state, command=rd_student_clicked)
radNewStudent.grid(column=1, row=6, sticky='w')

radOldStudent = Radiobutton(window, text="Old student (10% discount)", 
                            value=OLD_STUDENT, var=student_state, command=rd_student_clicked)
radOldStudent.grid(column=1, row=7, sticky='w')

lblFinalPayment = Label(window, text="Final payment: $0")
lblFinalPayment.grid(column=0, row=8, sticky='w')

##### START GUI PROGRAM #####
window.mainloop()   # window waiting for any events (click, keypress, etc.)