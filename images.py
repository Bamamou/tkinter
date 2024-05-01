from tkinter import *
from PIL import ImageTk, Image

root =Tk()
root.title('Image_viwer')
root.iconbitmap('evokem.ico')  #This is how to add an icon
mybutton= Button(root, text='Exit', command=root.quit) # this is how to create an exit button
my_img = ImageTk.PhotoImage(Image.open("flower1.jpg"))
my_label = Label(image=my_img)
flowers = ["flower1.jpg","flower2.jpg","flower3.jpg","flower4.jpg","flower5.jpg"]


def forward_fun():
    global my_label
    global number
    global flowers
    number = 0
    my_label.grid_forget()
    images =ImageTk.PhotoImage(Image.open(flowers[number]))
    my_label = Label(image= images)
    my_label.grid(row=0, column=0, columnspan=3)
    number = number+1
    #number += number
            

def backward_fun():
    return

forward = Button(root, text=">>", command= lambda: forward_fun())
backward = Button(root, text="<<", command= lambda: backward_fun())


my_label.grid(row=0, column=0, columnspan=3)
mybutton.grid(row=1,column=1)
backward.grid(row=1, column=0)
forward.grid(row=1,column=2)

root.mainloop()