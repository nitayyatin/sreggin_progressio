from flames import *
from tkinter import font


def Welcome():
    splash_label = Label(top, text="Welcome to Burning World!", font=("Garamond", 75), fg="red")
    splash_label.place(x=150, y=250)
    def main():
        splash_label.destroy()
    top.after(4000, main)

def Tutorial():
    splash_label = Label(top, text="How to play:", font=("Garamond", 50), fg="red")
    f = font.Font(splash_label, splash_label.cget("font"))
    f.configure(underline=True)
    splash_label.configure(font=f)
    splash_label.place(x=400, y=150)
    text = Label(top, text="It is the year 2050, global warming has gone out of control.", font=("Garamond", 50), fg="red")
    text.place(x=0, y=250)
    text2 = Label(top, text="Save the world! Douse the sun's flames by clicking on them", font=("Garamond", 50),fg="red")
    text2.place(x=0, y=350)
    def main():
        splash_label.destroy()
        text.destroy()
        text2.destroy()
    top.after(4000, main)


