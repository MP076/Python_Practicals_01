# 1
from tkinter import *


# 7
def openClicked():
    print("Open was clicked")
# Open was clicked


# 9
def quitApplication():
    quit()


# 1
root = Tk()

# 2
menu1 = Menu(root)
root.config(menu=menu1)

# 3
submenu1 = Menu(menu1, tearoff=0)
menu1.add_cascade(label='File', menu=submenu1)
# submenu1.add_command(label='Open')
# 6
submenu1.add_command(label='Open', command=openClicked)
# 4
submenu1.add_separator()
# submenu1.add_command(label='Quit')
# 8
submenu1.add_command(label='Quit', command=quitApplication)

# 5
submenu2 = Menu(menu1, tearoff=0)
menu1.add_cascade(label='Edit', menu=submenu2)
submenu2.add_command(label='Undo')
submenu2.add_command(label='Redo')

# 1
root.mainloop()
