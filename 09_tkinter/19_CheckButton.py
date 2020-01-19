from tkinter import *

root = Tk()

Label(root, text="Which one is your favorite?").pack()
Checkbutton(root, text="Milk").pack()
Checkbutton(root, text="Apple juice").pack()
Checkbutton(root, text="Mango shake").pack()

root.mainloop()
