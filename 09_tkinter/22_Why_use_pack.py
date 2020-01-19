# Check 18
from tkinter import *


def change_to_red():
    labelText.set('Red Color')
    label.config(bg='Red')


def change_to_green():
    labelText.set('Green Color')
    label.config(bg='Green')


def change_to_blue():
    labelText.set('Blue Color')
    label.config(bg='Blue')


root = Tk()

labelText = StringVar()
labelText.set('label')

label = Label(root, textvariable=labelText).pack()

Button(root, text="Click Red", command=change_to_red).pack()
Button(root, text="Click Green", command=change_to_green).pack()
Button(root, text="Click Blue", command=change_to_blue).pack()

root.mainloop()

# AttributeError: 'NoneType' object has no attribute 'config'
# Text displayed but color doesn't change
