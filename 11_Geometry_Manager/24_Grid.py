# 1
from tkinter import *
from tkinter import ttk


# 1
root = Tk()

# 2
label_1 = Label(root, text='Label 1', bg='Red')
label_1.grid(row=0, column=0)
# 3
label_2 = Label(root, text='Label 2', bg='Green')
label_2.grid(row=0, column=1)
# 4
label_3 = Label(root, text='Label 3', bg='Pink')
label_3.grid(row=1, column=0)
# 5
label_4 = Label(root, text='Label 4', bg='Blue')
label_4.grid(row=1, column=1)

# 1
root.mainloop()
