from tkinter import *
root = Tk()
root.title('icons') #this is how to create a title
root.iconbitmap('evokem.ico')  #This is how to add an icon

mybuttonquitt= Button(root, text='Exit', command=root.quit) # this is how to create an exit button

mybuttonquitt.pack()

root.mainloop()