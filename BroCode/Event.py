from tkinter import *

def on_key_press(event):
    print(f"Pressed key: {event.char}")

def on_mouse_click(event):
    print(f"Mouse clicked at: ({event.x}, {event.y})")

window = Tk()
window.bind("<KeyPress>", on_key_press)
window.bind("<Button-1>", on_mouse_click)

window.mainloop()