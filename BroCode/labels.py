from tkinter import *

window = Tk()

label1 = Label(text="Label1",
               font=('Arial', 40, 'bold'), 
               fg="green", 
               background='black',
               relief=RAISED,
               bd=10
               )
label1.place(x= 15, y=10) # Place the created label
#label.grid(padx=10, pady=10)
#label1.pack()

label2 = Label(text="Label2",
               font=('Arial', 40, 'bold'), 
               fg="green", 
               background='black',
               relief=RAISED,
               bd=10
               ).place(x=220, y=10)

label3 = Label(text="Label3",
               font=('Arial', 40, 'bold'), 
               fg="green", 
               background='black',
               relief=RAISED,
               bd=10
               ).place(x=425, y=10)
label4 = Label(text="Label4",
               font=('Arial', 40, 'bold'), 
               fg="green", 
               background='black',
               relief=RAISED,
               bd=10
               ).place(x=630, y=10)
# We could create that with  a for loop
labels = ["Label1", "Label2", "Label3", "Label4" ]
for i in range(len(labels)):
    label = Label(text=labels[i],
               font=('Arial', 40, 'bold'), 
               fg="green", 
               background='black',
               relief=RAISED,
               bd=10
               ).place(x=15+i*205, y=100)
    
# We could even use this concept to have labels on both x and y
labels = ["Label1", "Label2", "Label3", "Label4" ]
for i in range(len(labels)):
    for j in range(len(labels)):

        label = Label(text=labels[j],
               font=('Arial', 35+j*2, 'bold'), #increase the font size
               fg="green", 
               background='#2D2528',  # Change the background
               relief=SUNKEN,
               bd=10,
               padx= j+5 , # addd space between the border and the text according to j
               pady= j+5,
             #  image=photo
               )
        label.place(x=15+j*205, y=200+i*100)

    # We could also create many labeles in pictures if we are using the same label or photo
    photo = PhotoImage(file = 'icon.png')
    for i in range(3):
        label = Label( text="Photo",
               font=('Arial', 40, 'bold'), 
               fg="green", 
               background='black',
               relief=RAISED,
               bd=10,
               image= photo,
               compound='top'
               ).place(x=15+i*205, y=610)
    
window.mainloop()