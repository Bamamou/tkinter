from tkinter import *

# instantiate create a window
window = Tk()
window.geometry("420x420")  # size the windwo
window.title("HOME")
window.iconphoto(True,PhotoImage(file='icon.png'))  # Create an image object and use it as the icon
window.config(background="black") # change the bakground of the windowS




#display the window
window.mainloop()