from tkinter import *

def on_select(event):
    print("Selected item:", listbox.get(listbox.curselection()))

window = Tk()
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)
# Create a listbox
listbox = Listbox(window, yscrollcommand=scrollbar.set)
# A function to insert the items list
for i in range(100):
    listbox.insert(END, f"Item {i+1}")

listbox.pack(side=LEFT, # alignment on the left of the window
             fill=BOTH, # To fill the screen on Y and X
             expand=True # Can expand the field of listbox when the screen is expanded horizontally
             )  

scrollbar.config(command=listbox.yview)   # configure the srowllbar in the listbox
listbox.bind('<<ListboxSelect>>', on_select)  # bind the on_select function to an event

window.mainloop()