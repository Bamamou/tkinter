from tkinter import *

window =Tk()  # intantiate a window
window.title('Button')   
window.config(background='black')
window.iconphoto(True, PhotoImage(file='Roses.png'))
window.iconname("flower")

buttons = ["button1", "button2", "button3", "button4"]
""" for i in range(len(buttons)):
    button = Button(window, text=buttons[i], font=('times new roman', 10, 'bold'))
    button.grid(row=10, column=0+10* i)
 """
for i in range(len(buttons)):
    for j in range(len(buttons)):
        button2 = Button(window, 
                     text=j+i*4,
                     font=('times new roman', 10, 'bold'),
                     fg= "green",
                     padx=5, 
                     pady=5,
                     background='black',
                     relief=RAISED,
                     bd=5
                     )
        button2.grid(row=0+i*10, column=0+10* j)
    



window.mainloop()