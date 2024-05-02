from tkinter import *
Window =Tk()
Window.title("CheckButton")
Window.iconphoto(True, PhotoImage(file='table.png'))
Window.config(background="white")

x = IntVar()

foods = ["Pizza", "Salad", "Noodle", "Fried-rice", "Hamburder", "Soup"]
for food in range(len(foods)):
    radioButton = Radiobutton(Window, 
                              text=foods[food],
                              variable=x,
                              value=food,
                              font=("times new roman", 15, 'bold'))
    radioButton.pack(anchor=W)

Window.mainloop()