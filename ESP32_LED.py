import serial
import time
import tkinter

3
def quit():
    global tkTop
    ser.write(bytes('L', 'UTF-8'))
    tkTop.destroy()

def set_button1_state():
        global b
        b += 1
        varLabel.set("LED ON ")
        ser.write(bytes('H', 'UTF-8'))
        varLabel2.set(b)
    

def set_button2_state():
        varLabel.set("LED OFF")
        ser.write(bytes('L', 'UTF-8'))
        tkLabel.config(textvariable=0)
        varLabel2.set(0)


ser = serial.Serial('com12', 115200)   # Choose the right port number and baudrate 
print("Reset ESP32")
time.sleep(3)
ser.write(bytes('L', 'UTF-8'))


tkTop = tkinter.Tk()
#tkTop.geometry('300x200')
tkTop.title("IoT24hours")
tkTop.iconbitmap('evokem.ico')  #This is how to add an icon
label3 = tkinter.Label(text = 'ESP32 LED control GUI,',font=("Courier", 12,'bold'), fg='black').pack()
tkTop.counter = 0
b = tkTop.counter

varLabel = tkinter.IntVar()
tkLabel = tkinter.Label(textvariable=varLabel)
tkLabel.pack()

varLabel2 = tkinter.IntVar()
tkLabel2 = tkinter.Label(textvariable=varLabel2, )
tkLabel2.pack()

button1 = tkinter.IntVar()
button1state = tkinter.Button(tkTop,
    text="ON",
    command=set_button1_state,
    height = 4,
    fg = "black",
    width = 8,
    relief= 'raised',
    bd = 5,
    font=('Arial', 35, 'bold'),
    activebackground='green'
)
button1state.pack(side='top', ipadx=10, padx=10, pady=15)

button2 = tkinter.IntVar()
button2state = tkinter.Button(tkTop,
    text="OFF",
    command=set_button2_state,
    height = 4,
    fg = "black",
    width = 8,
    relief= 'raised',
    bd = 5,
    font=('Arial', 35, 'bold')
)
button2state.pack(side='top', ipadx=10, padx=10, pady=15)

tkButtonQuit = tkinter.Button(
    tkTop,
    text="Quit",
    command=quit,
    height = 4,
    fg = "black",
    width = 8,
    bg = 'yellow',
    bd = 5
)
tkButtonQuit.pack(side='top', ipadx=10, padx=10, pady=15)

tkinter.mainloop()