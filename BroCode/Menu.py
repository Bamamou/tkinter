from tkinter import *
from tkinter import ttk

#create the main window
window = Tk()
window.title("Menu tutorial")
window.geometry("500x500")

#Create a menu
menubar  = Menu(window, activebackground ='black', 	activeforeground ="black",bg='black', )
#Create sub menus
file_menu = Menu(menubar , tearoff= False, relief =FLAT, )
edit_menu  = Menu(menubar ,tearoff= False,  relief=RAISED)
view_menu  = Menu(menubar ,tearoff= False,  relief=RAISED)
help_menu = Menu(menubar ,tearoff= False, relief=GROOVE)

#Functinon to call 
def dosomething():
   filewin = Toplevel(window)
   button = Button(filewin, text="Do nothing button")
   button.pack()

#file menu
file_menu.add_command(label='New File', command=lambda: print("New file created"))
file_menu.add_separator()
file_menu.add_command(label='Open File', command=lambda: print("File Opened"))
file_menu.add_separator()
file_menu.add_command(label='Save File', command=lambda: print("File saved"))
file_menu.add_separator()
file_menu.add_command(label='Save as', command=lambda: print("File save as"))
file_menu.add_separator()
file_menu.add_command(label="Close", foreground= "red", command= dosomething)
file_menu.add_separator()
file_menu.add_command(label="Exit", foreground= "red", command=window.quit)
#Edit menu
edit_menu.add_command(label="Undo", command=dosomething)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=dosomething)
edit_menu.add_command(label="Copy", command=dosomething)
edit_menu.add_command(label="Paste", command=dosomething)
edit_menu.add_command(label="Delete", command=dosomething)
edit_menu.add_command(label="Select All", command=dosomething)
#Help menu
help_menu.add_command(label="Help Index", command=dosomething)
help_menu.add_command(label="About...", command=dosomething)



menubar .add_cascade(label='File', menu=file_menu)
menubar .add_cascade(label='Edit', menu=edit_menu)
menubar .add_cascade(label='View', menu=view_menu)
menubar .add_cascade(label='help', menu=help_menu)



window.config(menu=menubar)
window.mainloop()