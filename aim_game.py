# 움직이는 버튼 클릭해서 맞추는 게임

from tkinter import *
import random

num_targets = 0
now_target = 0

win = Tk()
win.title("aim_game")
win.geometry("550x150")
win.option_add("*Font", "궁서 20")
 
# Label
lab = Label(win)
lab.config(text="표적 개수")
lab.grid(column=0, row=0, padx=20, pady=20)

#Entry
ent = Entry(win)
ent.grid(column=1, row=0, padx=20, pady=20)

def destroy_grid():
    for wedget in win.grid_slaves():
        wedget.destroy()

def destroy_place():
    for wedget in win.place_slaves():
        wedget.destroy()

def finish():
    destroy_place()
    lab = Label(win)
    lab.config(text="clear")
    lab.pack(side="top")

    exit_button = Button(win, text="Exit", command=win.destroy)
    exit_button.pack(side="top")

    

def create_target():
    global now_target

    destroy_place()
    now_target += 1
    target = Button(win)
    target.config(bg="red")
    target.config(text=now_target)


    if now_target == num_targets: target.config(command=finish)
    else: target.config(command=create_target)
    target.place(relx=random.random(), rely=random.random())

def start():
    global num_targets

    num_targets = int(ent.get())
    destroy_grid()
    win.geometry('500x500')
    create_target()

#Button
btn = Button(win)
btn.config(text="시작")
btn.config(command=start)
btn.grid(column=0, row=1, columnspan=2)


win.mainloop()