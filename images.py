from tkinter import *
from PIL import ImageTk, Image

root =Tk()
root.title('Image_viwer')
root.iconbitmap('evokem.ico')  #This is how to add an icon
mybutton= Button(root, text='Exit', command=root.quit) # this is how to create an exit button
my_img = ImageTk.PhotoImage(Image.open("flower1.jpg"))
my_label = Label(image=my_img)
flowers = ["flower1.jpg","flower2.jpg","flower3.jpg","flower4.jpg","flower5.jpg"]

images = [ImageTk.PhotoImage(Image.open(flowers[0])), ImageTk.PhotoImage(Image.open(flowers[1])), ImageTk.PhotoImage(Image.open(flowers[2])), ImageTk.PhotoImage(Image.open(flowers[1])), ImageTk.PhotoImage(Image.open(flowers[3]))]
varLabel2 = IntVar()
number = 0
def forward_fun():
    global my_label
    global number
    global flowers
    number += 1
    if(number>=5):
        #number -=number (To loop over)
        number=4
        varLabel2.set(number)
    else:
        my_label.grid_forget()
        my_label = Label(image= images[number])
        my_label.grid(row=0, column=0, columnspan=3)
        varLabel2.set(number)
        print(number)
            

def backward_fun():
    global my_label
    global number
    global flowers
    number -= 1
    if(number<=0):
        #number +=number  (To loop over)
        number=1
        varLabel2.set(number)
    else:
        my_label.grid_forget()
        my_label = Label(image= images[number])
        my_label.grid(row=0, column=0, columnspan=3)
        varLabel2.set(number)
        print(number)


forward = Button(root, text=">>", command= lambda: forward_fun())
backward = Button(root, text="<<", command= lambda: backward_fun())


my_label.grid(row=0, column=0, columnspan=3)
mybutton.grid(row=1,column=1)
backward.grid(row=1, column=0)
forward.grid(row=1,column=2)

root.mainloop()