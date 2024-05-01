
from tkinter import *

window = Tk()

photoes = ['Roses.png', 'Wedding.png', 'table.png'] #, 'Purple.png','Yellow.png', 'Orange.png'
images=[]
for img in range(len(photoes)):
    images.append(PhotoImage(file = photoes[img]))    
for i in range(len(photoes)):
    label = Label(
               font=('Arial', 40, 'bold'), 
               fg="green", 
               background='black',
               relief=RAISED,
               bd=10,
               image= images[i]
              # compound='top'
               ).pack()
    #place(x=15+i*205, y=600)
    
window.mainloop()

window.mainloop()