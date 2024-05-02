from tkinter import *
Window =Tk()
Window.title("CheckButton")
Window.iconphoto(True, PhotoImage(file='table.png'))
Window.config(background="black")

f = IntVar()  # save the checkbox variables
m = IntVar()

def gender_display():
    global gender
    if (m.get()==1 and f.get()==0):
        gender = "Male"
    else:
        gender ="Female"

def delete():
    first_nameEntry.delete(0, END)
def delete1():
    lastname_Entry.delete(0, END)
def delete2():
    password_Entry.delete(0, END)
# Dubmit function not yet define
def submit():
      pass


def check():
    first_name = first_nameEntry.get()
    last_name = lastname_Entry.get()
    password = password_Entry.get()
    fLabel = Label(Window, text="First name: "+ first_name, font=("times new roman", 10, 'bold'),fg = "green", bg ="black")
    lLabel = Label(Window, text="First name: "+ last_name, font=("times new roman", 10, 'bold'),fg = "green", bg ="black")
    gLabel = Label(Window, text="First name: "+ gender, font=("times new roman", 10, 'bold'),fg = "green", bg ="black")
    pLabel = Label(Window, text="First name: "+ password, font=("times new roman", 10, 'bold'),fg = "green", bg ="black")
    fLabel.grid(row=5, column=1)
    lLabel.grid(row=6, column=1)
    gLabel.grid(row=7, column=1)
    pLabel.grid(row=8, column=1)

#e1 = Entry(Window,textvariable = mystring,width=100,fg="blue",bd=3,selectbackground='violet').pack()
Male_button = Checkbutton(Window, 
                text='Male',
                variable=m,
                onvalue=1,
                offvalue=0, 
                command=gender_display,
                font=("times new roman", 10, 'bold'),
                fg = "green",
                bg = "black" 
                )
Female_button = Checkbutton(Window, 
                text='Female',
                variable=f,
                onvalue=1,
                offvalue=0,
                command=gender_display,
                font=("times new roman", 10, 'bold'),
                fg = "green",
                bg = "black"
                )
Gender_label = Label(Window, 
              text= "Gender:    ",
              font=("times new roman", 10, 'bold'),
              fg = "green",
              bg = "black")
first_namelabel = Label(Window, 
              text= "First name",
              font=("times new roman", 10, 'bold'),
              fg = "green",
              bg = "black")
first_nameEntry = Entry(Window,
                        width=50, 
                        bg="black", 
                        fg="green",
                        borderwidth=5,
                        font=('times new roman', 15, 'bold')
                        )
first_nameEntry.insert(0,"Enter your first name")


lastname_label = Label(Window, 
              text= "Last name:    ",
              font=("times new roman", 10, 'bold'),
              fg = "green",
              bg = "black")

lastname_Entry = Entry(Window,
                        width=50, 
                        bg="black", 
                        fg="green",
                        borderwidth=5,
                        font=('times new roman', 15, 'bold')
                        )
lastname_Entry.insert(0,"Enter your last name")

password_label = Label(Window, 
                       font=("times new roman", 10, 'bold'),
                        fg = "green",
                        bg = "black",
                        text= "Password:    ")

password_Entry = Entry(Window,
                        width=50, 
                        bg="black", 
                        fg="green",
                        borderwidth=5,
                        font=('times new roman', 15, 'bold'),
                        show="*"
                        )
password_Entry.insert(0,"Enter your password")


password_DeleteButton = Button(Window,
                               text="delete",
                               command=delete2,
                               font=("times new roman", 10, 'bold'),
                                fg = "green",
                                bg = "black"
                                )

last_nameDeleteButton = Button(Window, 
                                text="delete",
                                command=delete1,
                                font=("times new roman", 10, 'bold'),
                                fg = "green",
                                bg = "black"
                                )
first_nameDeleteButton = Button(Window, 
                                text="delete",
                                font=("times new roman", 10, 'bold'),
                                fg = "green",
                                bg = "black",
                                command=delete)
                              
submit =Button(Window,
               text="submit",
                font=("times new roman", 10, 'bold'),
                fg = "green",
                bg = "black",
               command=submit)
quit_button = Button(Window,
                     text= "quit",
                    font=("times new roman", 10, 'bold'),
                    fg = "green",
                    bg = "black",
                    command=quit)
check_button = Button(Window,
                      text = "check entered information",
                      font=("times new roman", 10, 'bold'),
                      fg = "green",
                      bg = "black",
                      command=check)

first_namelabel.grid(row=0, column=0)
first_nameEntry.grid(row=0, column=1)
first_nameDeleteButton.grid(row=0, column=2)

lastname_label.grid(row=1, column=0)
lastname_Entry.grid(row=1, column=1)
last_nameDeleteButton.grid(row=1, column=2)
                                
password_label.grid(row=2, column=0)
password_Entry.grid(row=2, column=1)
password_DeleteButton.grid(row=2, column=2)

Gender_label.grid(row =3, column=0)
Male_button.grid(row =3, column=1)
Female_button.grid(row =3, column=2)

submit.place(x=150, y=130)
quit_button.place(x=500, y=130)
check_button.grid(row=4, column=1)

Window.mainloop()