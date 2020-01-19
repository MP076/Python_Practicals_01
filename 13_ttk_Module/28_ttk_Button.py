# 1
from tkinter import *
# 2
from tkinter import ttk

# 1
root = Tk()

# 3
Button(root, text='tkinter Button').pack()
ttk.Button(root, text='ttk Button').pack()

# 1
root.mainloop()
