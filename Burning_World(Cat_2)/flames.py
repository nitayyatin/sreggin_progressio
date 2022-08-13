from tkinter import *
from timeit import default_timer as timer
from threading import Timer
from PIL import Image, ImageTk
import time
import random
top = Tk()
myCanvas = Canvas(top, bg="white", height=1000, width=1200)
blaze = Image.open('flame.png')
flame = ImageTk.PhotoImage(blaze)
count = 0
pic = 0
Dict = {}
class flames():
    def flame_appears(self):
        btn = Button(top, text='Click Me', image=flame)
        btn.config(image=flame)
        btn.place(x=random.randint(1, 900), y=random.randint(1, 900))
        def on_click(event):
            global count
            if event.num == 1:
                btn.destroy()
                count += 1
                splash_label = Label(top, text=f"Count: {count}", font=("Garamond", 19), fg="red")
                splash_label.place(x=20,y=20)


        btn.bind('<Any-Button>', on_click)







