import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from tkinter import  *
Window =Tk()
Window.title("CheckButton")
Window.iconphoto(True, PhotoImage(file='table.png'))
Window.config(background="black")
def graph():
    # This is a sample of gouhnut pot in pyhton using the matplolib librairy
    labels = ['Category A', 'Category B', 'Category C', 'Category D']
    sizes = [20, 30, 40, 10]
    explode = (0, 0.1, 0, 0)  # explode the 2nd slice
    # now create the doughnut plot
    fig,ax = plt.subplots()
    ax.pie(sizes, explode = explode, labels = labels, autopct = '%1.1f%%', startangle = 90, shadow = True, colors = plt.cm.tab20.colors)
    ax.axis('equal')
 
    #Draw the plot
    centre_circle = plt.Circle((0,0), 0.7, color = 'white', fc ='white', linewidth = 1.25)
    fig.gca().add_artist(centre_circle)
    #Title
    plt.title('Doughnut Plot with Explode feature')
    #Show 
    plt.show()

def piegraphpt():
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    plt.stackplot(x, y1, y2, baseline ="wiggle")
    plt.title("Stream")
    plt.xlabel("x")
    plt.ylabel("Sin(x), Cos(s)")
    plt.show()


def TwoDThreeD():
# Set up a figure twice as tall as it is wide
    fig = plt.figure(figsize=plt.figaspect(2.5))
    fig.suptitle('A tale of 2 subplots')
# First subplot
    ax = fig.add_subplot(2, 1, 1)

    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)
    t3 = np.arange(0.0, 2.0, 0.01)
    f1=  np.cos(2*np.pi*t1) * np.exp(-t1)
    f2=  np.cos(2*np.pi*t2) * np.exp(-t2)
    ax.plot(t1, f1, 'bo',
        t2, f2, 'k--', markerfacecolor='green')
    ax.grid(True)
    ax.set_ylabel('Damped oscillation')
# Second subplot
    ax = fig.add_subplot(2, 1, 2, projection='3d')

    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
    ax.set_zlim(-1, 1)
    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()


button1 = Button(Window,text="Doughnut Explode  plot", fg="green", font=('times new roman', 20, 'bold'), relief=RAISED, bd=8, command=graph)
button2 = Button(Window, text="Sin & Cos Stream plot", fg="green", font=('times new roman', 20, 'bold'), relief=RAISED, bd=8,command=piegraphpt)
button3 = Button(Window, text="Damped oscillation 2D&3D", fg="green", font=('times new roman', 20, 'bold'), relief=RAISED, bd=8,command=TwoDThreeD)
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)
Window.mainloop()