from tkinter import *        # to get the GUI module of Pyhton
import serial
import serial.tools.list_ports
import tkinter.ttk as ttk
from guiLoop import guiLoop # https://gist.github.com/niccokunzmann/8673951
from tkinter import filedialog  # To get the file dialogue in order to save, open, read files.

@guiLoop
def Connection(argument):
    if(argument ==""):
        print("no port selected ")
    else:
    #ser.port =  str(on_select())
        ser = serial.Serial(argument, 115200) 
    #er.baudrate = 19200
    #ser.open()
        print("connected")
    while 1:
        line = ser.readline()
        print(line)
        yield 1 # time to wait

# Opening the binary file in binary mode as rb(read binary)
#filepath = filedialog.askopenfilename(title="Open file",
#                                          filetypes=(("text files", "*.txt"), ("Plain files", "*.txt")))
    #To catch exception errors in case the path is empty

window = Tk()
window.title("Bin")
window.iconphoto(True, PhotoImage(file='RedRose.png'))   # Icon of the window    
def serial_ports():    
    return serial.tools.list_ports.comports()

def on_select(event =None):

    # get selection from event    
  #  print("event.widget:", event.widget.get())

    # or get selection directly from combobox
    #print("comboboxes: ", cb.get())
    com =cb.get() # get the combox port
    # The below is not the correct way we need a delimiter to have the port name
    return com[0: 5]

cb = ttk.Combobox(window, values=serial_ports())  # Combobox dropdown button
cb.set("COM12")          # Not needed and it has to be set to Port or Com
cb.pack()

# assign function to combobox
cb.bind('<<ComboboxSelected>>', on_select)                 # to set the value of the port gotten from the fuction

Button(window, command = Connection, text = 'Connect').pack()

Connection(window, str(on_select()))  # Call the function to run the infinte loop

window.mainloop()