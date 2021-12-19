from tkinter import *

win = Tk()
win.geometry("400x200")
win.title("grid")
win.option_add("*Font", "궁서 20")

btn1 = Button(win)
btn1.config(text="(0, 0)")
btn1.grid(column=0, row=0)

btn2 = Button(win)
btn2.config(text="(1, 0)")
btn2.grid(column=1, row=0)

btn3 = Button(win)
btn3.config(text="(0, 1)")
btn3.grid(column=0, row=1)

btn4 = Button(win)
btn4.config(text="new")
btn4.grid(column=0, row=0, columnspan=2)

win.mainloop()