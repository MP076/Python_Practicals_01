# 1.
# from tkinter import *
#
#
# def on_button_click():
#     labelText.set("Text changed on button click")
#
#
# root = Tk()
#
# labelText = StringVar()
# labelText.set('label')
#
# label = Label(root, textvariable = labelText)
# label.pack()
#
# Button(root, text="Click", command=on_button_click).pack()
#
# root.mainloop()


# 2.
# from tkinter import *
#
#
# def on_button_click():
#     labelText.set('Red Color')
#     label.config(bg='Red')
#
#
# root = Tk()
#
# labelText = StringVar()
# labelText.set('label')
#
# label = Label(root, textvariable=labelText)
# label.pack()
#
# Button(root, text="Click", command=on_button_click).pack()
#
# root.mainloop()


# 3.
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

label = Label(root, textvariable=labelText)
label.pack()

Button(root, text="Click Red", command=change_to_red).pack()
Button(root, text="Click Green", command=change_to_green).pack()
Button(root, text="Click Blue", command=change_to_blue).pack()

root.mainloop()
