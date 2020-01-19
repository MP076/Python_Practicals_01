from tkinter import *


def showValue():
    print(radio_button_value.get())


root = Tk()

radio_button_value = StringVar()

Label(root, text="What is your favorite weather?").pack()
Radiobutton(root, text='Sunny', value='sunny', variable=radio_button_value).pack()
Radiobutton(root, text='Rainy', value='rainy', variable=radio_button_value).pack()
Radiobutton(root, text='Wet', value='wet', variable=radio_button_value).pack()
Radiobutton(root, text='Dry', value='dry', variable=radio_button_value).pack()
Radiobutton(root, text='Cloudy', value='cloudy', variable=radio_button_value).pack()

Button(root, text="Show radio button value", command=showValue).pack()

root.mainloop()

# Click buttons
# wet
# rainy
# sunny
# cloudy
# dry
