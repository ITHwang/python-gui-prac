from tkinter import *

win = Tk()
win.geometry("400x200")
win.title("place")
win.option_add("*Font", "궁서 20")

btn = Button(win)
btn.config(text="place")
# btn.place(x=30, y=50)
btn.place(relx=0.5, rely=0.5)


win.mainloop()