from tkinter import *
window = Tk()
window.geometry("300x100")

# This function enable or disable the button based on the state
def switchButtonState():
    if (button1['state'] == NORMAL):
        button1['state'] = DISABLED
    else:
        button1['state'] = NORMAL
button1 = Button(window, text="Python Button 1",
                    state=DISABLED)
button2 = Button(window, text="EN/DISABLE Button 1",
                    command = switchButtonState)
button1.pack(side=LEFT)
button2.pack(side=RIGHT)

window.mainloop()