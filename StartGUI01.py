# StartGUI01.py

from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.geometry('500x300') # 500=แนวนอน , 300=แนวตั้ง

GUI.title('โปรแกรมหน้าแมวเดอะซี่รี่ย์')

# L = Label(GUI, text='หน้าแมว', font=('Angsana', 30, 'bold'), fg='green')
L = Label(GUI, text='หน้าแมว', font=(None, 30))
# ต้องมีเสมอ เป็นคำสั่งให้ label ติดหน้าโปรแกรมหลัก
# อีกคำสั่งคือ .place(x,y) หรือ .grid(row=0, column=0) สามารถกำหนดพิกัดได้
L.pack()

# การสร้างกล่องเขียนข้อความ
#-------------------------------------
# ถ้ามีหลายกล่องข้อความก็ต้องสร้างที่เก็บไว้ตามข้อความด้วย ถ้าไม่สร้างข้อความจะซ้ำกัน
v_quantity = StringVar()    # ตำแหน่งตัวแปรที่ใช้เก็บข้อมูลช่องกรอก

# แบบเก่า หน้าตาจะไม่ค่อยสวย
E1 = Entry(GUI, textvariable=v_quantity, font=('impact', 10))  # สร้างกล่องไว้เขียนข้อความ
E1.pack()

# แบบใหม่ ใช้ ttk หน้าตาจะสวยขึ้น
E2 = ttk.Entry(GUI, textvariable=v_quantity, font=('impact', 10))  # สร้างกล่องไว้เขียนข้อความ
E2.pack()

v_quantity1 = StringVar()
E3 = ttk.Entry(GUI, textvariable=v_quantity1, font=('impact', 20))  # สร้างกล่องไว้เขียนข้อความ
E3.pack()
#-------------------------------------

# การสร้างปุ่มกด
#-------------------------------------
B = Button(GUI, text='เมี๊ยววว')
B.place(x=600, y=300)

#-------------------------------------
# ปุ่มแบบเดิม
B2 = Button(GUI, text='หง่าววว')
B2.pack(ipadx=30, ipady=20)

# ปุ่มแบบใหม่ ใช้ package ttk 
B2 = ttk.Button(GUI, text='เมี๊ยววว')
B2.pack(ipadx=30, ipady=20)
#-------------------------------------

# เพื่อให้ GUI ของเรารันตลอด
GUI.mainloop()