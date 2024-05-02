from tkinter import *

window = Tk()
window.title("Entry")
window.iconphoto(True, PhotoImage(file='table.png'))

def submit():
    print(entry.get())
info = ["First name", "Last name", "Gender", "email"]

def delete():
    entry.delete(0, END)
def BackSpace():
    entry.delete(len(entry.get())-1, END)
def check():
    entered_info = entry.get()
    myLabel = Label(window, text=entered_info)
    myLabel.grid_forget()
    myLabel.grid(row=6, column=2)
    

for i in range(len(info)):
    label = Label(window, 
                  text =info[i]
                  )
    entry = Entry(window, 
              width=50, 
              bg="green", 
              fg="white",
              borderwidth=5,
              font=('times new roman', 15, 'bold')
              )
    entry.insert(0, "Enter your "+info[i])
    delte_buttons = Button(window,
                    text="delete",
                    textvariable= i,
                    command=delete)
    backS_button = Button(window,
                          text="<--",
                          command=BackSpace)
    label.grid(row=i,column=0)
    delte_buttons.grid(row=i, column=4)
    backS_button.grid(row=i, column=5)
    entry.grid(row=i, column=1, columnspan=3)


sumbit_button =Button(window,
               text="Submit",
               command=submit)
quit_button =Button(window,
               text="Quit",
               command=quit)
check_button =Button(window,
               text="Check entered info",
               command=check)

sumbit_button.grid(row=5, column=3)
quit_button.grid(row=5, column=1)
check_button.grid(row=5, column=2)
window.mainloop()