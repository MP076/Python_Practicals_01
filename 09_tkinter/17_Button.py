from tkinter import *
from tkinter import messagebox


def button_tapped():
    messagebox._show("Message", "Button Clicked")


root = Tk()

Button(root, text="Click Me", command=button_tapped).pack()

root.mainloop()
