from tkinter import *

root = Tk()
root.title("Calculator")
entry =Entry(root, width=35, borderwidth=5)
entry.grid(row=0,column=0, columnspan=3, padx=10,pady=20)
# Create an addition button

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current)+ str(number))
    return
#clear the screen
def button_clear():
    entry.delete(0, END)

# Create an addition button
def button_add():
    first_number = entry.get()
    global f_num 
    global operation
    operation = "plus"
    f_num = float(first_number)
    entry.delete(0, END)

    return

def button_substract():
    first_number = entry.get()
    global f_num 
    global operation
    operation = "minus"

    f_num = float(first_number)
    entry.delete(0, END)
    return

def button_division():
    first_number = entry.get()
    global f_num 
    global operation
    operation = "division"
    f_num = float(first_number)
    entry.delete(0, END)
    return

def button_multiplication():
    first_number = entry.get()
    global f_num 
    global operation
    operation = "multiplication"
    f_num = float(first_number)
    entry.delete(0, END)
    return

def button_modulo():
    first_number = entry.get()
    global f_num 
    global operation
    operation = "modulo"
    f_num = float(first_number)
    entry.delete(0, END)
    return

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if(operation == "plus"):
        entry.insert(0, f_num + int(second_number))
    elif (operation == "minus"):
        entry.insert(0, f_num - int(second_number))
    elif (operation == "multiplication"):
        entry.insert(0, f_num * int(second_number))
    elif (operation == "division"):
        entry.insert(0, f_num / int(second_number))
    elif (operation == "modulo"):
        entry.insert(0, f_num % int(second_number))
    return



#create butthon
button_1 =Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 =Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 =Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 =Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 =Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 =Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 =Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 =Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 =Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 =Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_d =Button(root, text=".", padx=40, pady=20, command=lambda: button_click("."))
button_e =Button(root, text="=", padx=40, pady=20, command=lambda: button_equal())
button_c =Button(root, text="C", padx=40, pady=20, command=lambda: button_clear())
button_pl =Button(root, text="+", padx=40, pady=20, command=lambda: button_add())
button_mn =Button(root, text="-", padx=40, pady=20, command=lambda: button_substract())
button_di =Button(root, text="/", padx=40, pady=20, command=lambda: button_division())
button_mu =Button(root, text="*", padx=40, pady=20, command=lambda: button_multiplication())
button_mo =Button(root, text="%", padx=40, pady=20, command=lambda: button_modulo())

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_d.grid(row=4, column=1)
button_c.grid(row=4, column=2)

button_pl.grid(row=5, column=0)
button_mu.grid( row=5, column=1)
button_mn.grid(row=5, column=2)

button_di.grid(row=6, column=0)
button_mo.grid(row=6, column=1)
button_e.grid(row=6, column=2)

root.mainloop()