from tkinter import Label, PhotoImage, Button, font
from util import *
import os

root = init()
noto_sans_20 = font.Font(family='Noto Sans KR', size=20)

file_path = os.path.join(os.getcwd(), 'personality_test/img/logo.png')
img = PhotoImage(file=file_path, master=root).subsample(8)
lab = Label(root, image=img, bg='white')
lab.pack(pady=20)

btn = Button(root, bg='white', text="시작하기", font=noto_sans_20, command=lambda: start(root))
btn.pack(pady=20)

root.mainloop()


