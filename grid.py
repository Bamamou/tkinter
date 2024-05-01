from tkinter import *
root = Tk()
#create a label
mylabel1 = Label(root, text = "Hello there!")
mylabel2 = Label(root, text = "My name is Nicolas and youn?")
# Display with a grid
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=0)  # second row 

root.mainloop()