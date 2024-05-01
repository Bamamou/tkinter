from tkinter import *
root =Tk()
# A simple function to be called when the button is pressed
def myClick():
    myLabel = Label(root, text ="You clicke me!")
    myLabel.pack()

# Create the button
myButton = Button(root, text ="Click me!", state="normal", padx=50, pady=10, command=myClick, fg="red", bg="orange") # Do not call the function myClick() because it will execute it even without clicking
# display the button with a packing method
myButton.pack()

root.mainloop()