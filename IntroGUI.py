#-*- coding: utf-8 -*-
# IntroGUI.py

from tkinter import *
from tkinter import ttk, messagebox

friend = {'somchai':'สมชาย ดีมาก',
          'somsak':'สมศักดิ์ เก่งมาก',
          'somsri':'สมศรี เยี่ยมมาก'}

GUI = Tk()
GUI.title('โปรแกรมของฉัน')
GUI.geometry('500x300')

L = Label(GUI,text='กรุณากรอกรหัสชื่อ',font=('Angsana New', 20)).pack(pady=20)

v_text = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_text,font=('Angsana New', 20))
E1.pack()

def Click():
    text = v_text.get() #ดึงข้อความที่ พิมพ์ออกมา
    print('Text: ', text)
    if text in friend:
        result = friend[text]
        print(friend[text])
        messagebox.showinfo('Result','รหัส: {} คือชื่อ: {}'.format(text,result))
    else:
        print('ไม่มีข้อมูลของคนนี้')
        messagebox.showwarning('Result: Error', 'ไม่มีข้อมูลในระบบ กรุณากรอกใหม่ หรือเพิ่มข้อมูลในระบบ')

B1 = ttk.Button(GUI, text='Click me!', command=Click)
B1.pack(ipadx=50, ipady=30, pady=30)

GUI.mainloop()