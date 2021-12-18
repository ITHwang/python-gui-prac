from tkinter import *
from selenium import webdriver
import os

def login():
    driver = webdriver.Chrome("./chromedriver")
    url = "https://accounts.kakao.com/login?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net%252F"
    driver.get(url)
    driver.implicitly_wait(5)

    xpathId = "//input[@name='email']"
    driver.find_element_by_xpath(xpathId).send_keys(ent1.get())
    xpathPw = "//input[@name='password']"
    driver.find_element_by_xpath(xpathPw).send_keys(ent2.get())
    xpathBtn = "//button[@class='btn_g btn_confirm submit']"
    driver.find_element_by_xpath(xpathBtn).click()

win = Tk()
win.title("Daum Log-In")
win.geometry("400x300")
win.option_add("*Font", "궁서 20")

lab_d = Label(win)
img = PhotoImage(file="/Users/kangchangmin/Desktop/daum.png", master=win).subsample(8)
lab_d.config(image=img)
lab_d.pack()

lab1 = Label(win)
lab1.config(text="ID")
lab1.pack()

ent1 = Entry(win)
ent1.insert(0, "temp@temp.com")
def clear(event):
    if ent1.get() == "temp@temp.com":
        print("delete")
        ent1.delete(0, len(ent1.get()))
ent1.bind("<Button-1>", clear)
ent1.pack()

lab2 = Label(win)
lab2.config(text="Password")
lab2.pack()
ent2 = Entry(win)
ent2.config(show="*") 
ent2.pack()

btn = Button(win)
btn.config(text="로그인")
btn.config(command=login)
btn.pack()

# 메시지 라벨
lab3 = Label(win)
lab3.pack()


win.mainloop()

