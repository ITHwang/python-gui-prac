from tkinter import *

win = Tk()
win.geometry("400x200")
win.title("pack")
win.option_add("*Font", "궁서 20")

ent = Entry(win)
ent.pack(side="top")

btn = Button(win)
btn.config(text="버튼")
def move_btn():
    btn.pack(side=ent.get())
    # btn.pack(pady=ent.get())
btn.config(command=move_btn)
btn.pack(side="top")

win.mainloop()

