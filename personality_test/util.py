from tkinter import *
from tkinter import font
from tkinter import *
from question import question_list

question_topics = [key for key in question_list.keys()]

def init():
    root = Tk()
    root.title("TOST 성향 테스트")
    root.geometry("600x300")
    root.configure(bg='white')
    return root

def destroy_all(window):
    for wedjet in window.slaves(): wedjet.destroy()

def start(root):
    destroy_all(root)

    question_frame = Frame(root, relief='solid', bd=2, height=200)
    question_frame.pack(pady=20)

    answer_frame = Frame(root, relief='solid', bd=4, height=200)
    answer_frame.pack(pady=20)

    lab = Label(question_frame, bg='white', wraplength=300, font=font.Font(family='Noto Sans KR', size=15), text=question_list[question_topics[0]][0][0])
    lab.pack()

    radio_variety = IntVar()
    Radiobutton(answer_frame, text="진짜진짜 아니다", value=-3, variable=radio_variety).pack(side='left')
    Radiobutton(answer_frame, text="진짜 아니다", value=-2, variable=radio_variety).pack(side='left')
    Radiobutton(answer_frame, text="아니다", value=-1, variable=radio_variety).pack(side='left')
    Radiobutton(answer_frame, text="보통이다", value=0, variable=radio_variety).pack(side='left')
    Radiobutton(answer_frame, text="맞다", value=1, variable=radio_variety).pack(side='left')
    Radiobutton(answer_frame, text="진짜 맞다", value=2, variable=radio_variety).pack(side='left')
    Radiobutton(answer_frame, text="진짜진짜 맞다", value=3, variable=radio_variety).pack(side='left')

        


