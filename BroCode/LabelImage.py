
from tkinter import *

window = Tk()
window.config(background="black")
window.title('Album') #this is how to create a title
window.iconbitmap('evokem.ico')  #This is how to add an icon

photoes = ['Roses.png', 'Orange.png', 'table.png']
images=[] # create an empty list
for img in range(len(photoes)):
    images.append(PhotoImage(file = photoes[img]))   #Store all the png images in the images list
#photoes = ['Roses.png', 'Wedding.png', 'table.png'] #, 'Purple.png','Yellow.png', 'Orange.png'

num = 0
var = IntVar()
# Next function
def Next():
   global label
   global num
   if (num>=len(photoes)-1):
        next_button.config(state=DISABLED)
        var.set(num)

   else:
        num = num+1
        back_button.config(state=NORMAL)
        label.grid_forget()
        label = Label(text=photoes[num],
                        font=('Arial', 40, 'bold'), 
                        fg="green", 
                        background='black',
                        relief=RAISED,
                        bd=10,
                        compound='top',
                        image= images[num] )
        label.grid(row=0, column=0, columnspan=3)
        var.set(num)
                
#back function
def back():
   global label
   global num
   if (num<=0):
        back_button.config(state=DISABLED)
        var.set(num)
   else:
        num -=1
        label.grid_forget()
        next_button.config(state=NORMAL)
        label = Label(  text=photoes[num],
                        font=('Arial', 40, 'bold'), 
                        fg="green", 
                        background='black',
                        relief=RAISED,
                        bd=10,
                        compound='top',
                        image= images[num] )
        label.grid(row=0, column=0, columnspan=3)
        var.set(num)


label = Label( text="Roses",
               font=('Arial', 40, 'bold'), 
               fg="green", 
               background='black',
               relief=RAISED,
               bd=10,
               image= images[num],
               compound='top'
               )
label.grid(column=0, row=0, columnspan=3)

    
next_button  = Button(window, 
                text="next>>",
                font=('Comic Sans', 15, 'italic'),
                fg='green',
                bg= "black",
                activebackground="black",
                activeforeground="black",
                command= Next)
next_button.grid(column=2, row=1)

quit_button  = Button(window, 
                text="quit",
                font=('Comic Sans', 15, 'italic'),
                fg='green',
                bg= "black",
                activebackground="black",
                activeforeground="black",
                command= quit)
quit_button.grid(column=1, row=1)

back_button  = Button(window, 
                text="back<<",
                font=('Comic Sans', 15, 'italic'),
                fg='green',
                bg= "black",
                activebackground="black",
                activeforeground="black",
                command= back)
back_button.grid(column=0, row=1)

window.mainloop()