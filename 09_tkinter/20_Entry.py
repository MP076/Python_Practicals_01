# 1.
# from tkinter import *
#
# root = Tk()
#
# entry = Entry(root)
# entry.pack()
#
# root.mainloop()


# 2.
# from tkinter import *
#
# root = Tk()
#
# entry = Entry(root, bg='Red', fg='Yellow')
# entry.pack()
#
# root.mainloop()


# 3.
# from tkinter import *
#
#
# def clear_text():
#     entry.delete(0, END)
#
#
# root = Tk()
#
# entry = Entry(root, bg='Red', fg='Yellow')
# entry.pack()
#
# Button(root, text="Clear Entry Box", command=clear_text).pack()
#
# root.mainloop()


# 4.
from tkinter import *


def show_on_label():
    labelText.set(entry.get())


root = Tk()

entry = Entry(root, bg='Black', fg='White')
entry.pack()

Button(root, text='Show text on label', command=show_on_label).pack()

labelText = StringVar()
labelText.set("=====")

label = Label(root, textvariable=labelText)
label.pack()

root.mainloop()
