from tkinter import *
from tkinter import *
from PIL import ImageTk
from flames import *
start = timer()
from Welcome_screen import *
img = PhotoImage(file="worldmap.png")

Welcome()
def t():
    Tutorial()
top.after(4000, t)

def map():
    myCanvas.create_image(525,400, image=img)

top.after(8000, map)

F = flames()
x = 1

for n in range(30):
    top.after(int(8000* x), F.flame_appears)
    x += 0.09375

for n in range(40):
    top.after(int(8000* x), F.flame_appears)
    x += 0.0625

myCanvas.pack()



top.after(35000,lambda:top.destroy())
top.mainloop()

L = Tk()
mycanvas = Canvas(L, bg="white", height=1100, width=1500)

splash_label = Label(L, text="YOU FOOL! YOU CAN'T SOLVE ", font=("Garamond", 75), fg="red")
splash_label.place(x=100, y=250)
splash_label = Label(L, text="GLOBAL WARMING BY CLICKING!", font=("Garamond", 75), fg="red")
splash_label.place(x=100, y=350)
splash_label = Label(L, text=" GET UP ACTUALLY DO SOMETHING USEFUL!", font=("Garamond", 55), fg="red")
splash_label.place(x=90, y=450)
mycanvas.pack()
L.mainloop()







