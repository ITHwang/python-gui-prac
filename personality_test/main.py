from tkinter import Label, Tk, font, PhotoImage, Button
from question import question_list
from util import start
import os

root = Tk()
root.title("TOST 성향 테스트")
root.geometry("400x300")
root.configure(bg='white')
font20 = font.Font(family='Noto Sans KR', size=20)

file_path = os.path.join(os.getcwd(), 'personality_test/img/logo.png')
img = PhotoImage(file=file_path, master=root).subsample(8)
lab_d = Label(root)
lab_d.config(image=img)
lab_d.pack(pady=20)

btn = Button(root)
btn.config(text="시작하기", font=font20, command=start)
btn.pack(pady=20)

root.mainloop()


