from tkinter import *
from tkinter import ttk
from unicodedata import name

wah = Tk()
wah.title('ARISEn')

def adddetails():
    global count

    name = nameinput.get()
    gender = genderinput.get()
    age = ageinput.get()

    datalist.clear() 
    datalist.append((name, gender, age)) 

    for item in datalist:
        datatable.insert(parent='', index='end',iid=count, text=f'{count + 1}', values=(item))

    nameinput.delete(0, END)
    genderinput.delete(0, END)
    ageinput.delete(0, END)
    count += 1

    print(datalist)

def delete():
    selected_item = datatable.selection()[0] 
    datatable.delete(selected_item)

datatable = ttk.Treeview(wah)
global count
count = 0

datalist = []
datatable['columns'] = ("Name", "Gender", "Age")

datatable.column("#0", width=30)
datatable.column("Name", width=120, anchor=W)
datatable.column("Gender", width=120, anchor=W)
datatable.column("Age", width=120, anchor=W)


headings = ["#0", "Name", "Gender", "Age"]
txtheadings = ["No.", "Name", "Gender", "Age"]
for x in range(len(headings)):
    datatable.heading(headings[x], text=txtheadings[x], anchor=W)

frameinput = Frame(wah)
frameinput.grid()

namelabel = Label(frameinput, text ="Name:")
namelabel.grid(row = 0, column = 1)
genderlabel = Label(frameinput, text ="Gender:")
genderlabel.grid(row = 1, column = 1)
agelabel = Label(frameinput, text ="Age:")
agelabel.grid(row = 2, column = 1)

nameinput = Entry(frameinput, width=20)
nameinput.grid(row = 0, column = 2)
genderinput = Entry(frameinput, width=20)
genderinput.grid(row = 1, column = 2)
ageinput = Entry(frameinput, width=20)
ageinput.grid(row = 2, column = 2)

addbut = Button(frameinput, text="Add Line", width=20, command=adddetails)
addbut.grid(row = 1, column = 4)

deletelabel = Label(frameinput, text="Select line to delete: ")
deletelabel.grid(row = 3, column = 2)
deletebut = Button(frameinput, text="Delete Line", command=delete)
deletebut.grid(row = 3, column = 4)

datatable.grid()
wah.mainloop()

