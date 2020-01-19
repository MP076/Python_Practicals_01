# 1
from tkinter import *


# 5
def showTable():
    table = entry.get()

    two = int(table) * 2
    three = int(table) * 3
    four = int(table) * 4
    five = int(table) * 5

    label_text_1.set(table + ' x ' + '1 = ' + table)
    # 10
    label_text_2.set(table + ' x ' + '2 = ' + str(two))
    label_text_3.set(table + ' x ' + '3 = ' + str(three))
    label_text_4.set(table + ' x ' + '4 = ' + str(four))
    label_text_5.set(table + ' x ' + '5 = ' + str(five))


# 1
root = Tk()

# 2
entry = Entry(root)
entry.pack()

# 3
Button(root, text="Show Table", command=showTable).pack()

# 4
label_text_1 = StringVar()
label_text_1.set("=====")
Label(root, textvariable=label_text_1, bg='Green').pack()

# 6
label_text_2 = StringVar()
label_text_2.set("=====")
Label(root, textvariable=label_text_2, bg='Yellow').pack()

# 7
label_text_3 = StringVar()
label_text_3.set("=====")
Label(root, textvariable=label_text_3, bg='Pink').pack()

# 8
label_text_4 = StringVar()
label_text_4.set("=====")
Label(root, textvariable=label_text_4, bg='Brown').pack()

# 9
label_text_5 = StringVar()
label_text_5.set("=====")
Label(root, textvariable=label_text_5, bg='Blue').pack()

# 1
root.mainloop()
