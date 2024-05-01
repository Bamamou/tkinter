from tkinter import *
 # create a frame 
root = Tk()

#Create an Entry which ic a kind of an input button    
entry = Entry(root, width=50, bg="green", fg="white",borderwidth=5)
entry.insert(0, "Enter your name")
#Display the entry with the packing method
entry.grid(row=0, column=1)
#create a simple function to the entered text and display it as a label
def myClick():
    hello = "Hello "+ entry.get()
    myLabel = Label(root, text=hello)
    myLabel.grid(row=1, column=0)

#Create a button to display the label when the button is pressed
myButton = Button(root, text= "Check your name", command=myClick)
# display the button
myButton.grid(row=0, column=0)
root.mainloop()
