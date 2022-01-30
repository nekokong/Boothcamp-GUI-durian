# BasicGUI.py

from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import csv

#######################################################################

# วิธีเขียน Timestamp สามารถทำได้หลายแบบ
#------------------------------------------------------------------
# วิธีที่ 1 เอา stamp ไว้ใน if
def timestamp(thai=True):
    if thai == True:
        stamp = datetime.now()
        stamp = stamp.replace(year=stamp.year+543) # บวกเป็น พ.ศ.
        stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
    else:
        stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return stamp
'''
# วิธีที่ 2 เอา stamp ไว้นอก if
def timestamp(thai=True):
    stamp = datetime.now()
    if thai == True:
        stamp = stamp.replace(year=stamp.year+543) # บวกเป็น พ.ศ.
        stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
    else:
        stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
    return stamp
'''
#------------------------------------------------------------------

def writetext(quantity, total):
    # stamp = datetime.now()
    # stamp = stamp.replace(year=stamp.year+543) # บวกเป็น พ.ศ.
    # stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
    stamp = timestamp()
    filename = 'data.txt'
    with open(filename, 'a', encoding = 'utf-8') as file:
        file.write('\n' + 'วัน-เวลา: {} ทุเรียน: {} กก. รวมยอดทั้งหมด: {:,.2f} บาท'.format(stamp,quantity,total))

def writecsv(data):
    # data = ['Time','quantity','total']
    with open('data.csv', 'a', newline='', encoding='utf-8') as file:
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)
    print('Success')

def readcsv():
    with open('data.csv', newline='', encoding='utf-8') as file:
        fr = csv.reader(file) # file reader
        # print(list(fr))
        data = list(fr)
    return data

def sumdata():
    # ฟังชั่นนี้ใช้สำหรับรวมค่าที่ได้จาก csv ไฟล์สรุปออกมาเป็น 2 อย่าง
    result = readcsv()
    sumlist_quan1 = []
    sumlist_total = []
    for total in result:
        sumlist_quan1.append(float(total[1]))
        sumlist_total.append(float(total[2]))
    sumquan = sum(sumlist_quan1)
    sumtotal = sum(sumlist_total)
    
    return(sumquan, sumtotal)

#######################################################################

GUI = Tk()
GUI.geometry('600x700') # Size of GUI
GUI.title('โปรแกรมของก้องเอง v.0.0.1')

file = PhotoImage(file='durian.png')
IMG = Label(GUI, image=file, text='')
IMG.pack()

L1 = Label(GUI, text='โปรแกรมคำนวณทุเรียน', font=('Angsana New', 30, 'bold'), fg='green')
L1.pack() # .place(x,y) , .grid(row=0,column=0)

L2 = Label(GUI, text='กรุณากรอกจำนวนทุเรียน (กิโลกรัม)', font=('Angsana New', 20))
L2.pack() # .place(x,y) , .grid(row=0,column=0)

v_quantity = StringVar() #ตำแหน่งตัวแปรที่ใช้เก็บข้อมูลช่องกรอก

E1 = ttk.Entry(GUI,textvariable=v_quantity, font=('impact', 30))
E1.pack()

def Calculate(event=None):
    quantity = v_quantity.get()
    price = 100
    print('จำนวน', float(quantity) * price)
    cal = float(quantity) * price
    # EN DATE
    # stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
 
    # --------------------------------------------------------------------------
    # THAI DATE
    # stamp = datetime.now()
    # stamp = stamp.replace(year=stamp.year+543) # บวกเป็น พ.ศ.
    # stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
    
    # ฟังชั่นบันทึกข้อมูลลงไฟล์ txt แบบง่าย, ถ้าใส่ภาษาไทยต้องใส่ encoding = 'utf-8' ด้วย
    # filename = 'data.txt'
    # with open(filename, 'a', encoding = 'utf-8') as file:
    #     file.write('\n' + 'วัน-เวลา: {} ทุเรียน: {} กก. รวมยอดทั้งหมด: {:,.2f} บาท'.format(stamp,quantity,cal))
    #---------------------------------------------------------------------------

    # การบันทึกแบบ txt
    # writetext(quantity,cal)
    
    # การบันทึกแบบ csv
    # ถ้าอยากได้ปีเป็นแบบสากล ให้กำหนด thai=False เพราะเราใส่ในฟังชั่นไว้
    #data = [timestamp(thai=False), quantity, cal]
    data = [timestamp(), quantity, cal]
    writecsv(data)

    #messagebox.showinfo('ยอดที่ลูกค้าต้องจ่าย' , 'ทุเรียนจำนวน {} กิโลกรัม ราคาทั้งหมด: {:,.2f} บาท'.format(quantity,cal))

    # pop up
    sm = sumdata()
    title = 'ยอดที่ลูกค้าต้องจ่าย'
    text = 'ทุเรียนจำนวน {} กิโลกรัม ราคาทั้งหมด: {:,.2f} บาท'.format(quantity, cal)
    messagebox.showinfo(title,text)

    v_quantity.set('') # clear data
    E1.focus()


B1 = ttk.Button(GUI, text='คำนวณ', command=Calculate)
B1.pack(ipadx=30, ipady=20, pady=20)

E1.bind('<Return>', Calculate)

def SummaryData(event):
    # pop up
    sm = sumdata()
    title = 'ยอดสรุปรวมท้งหมด'
    text = 'จำนวนที่ขายได้: {} กก.\nยอดขาย {:,.2f} บาท'.format(sm[0],sm[1])
    messagebox.showinfo(title,text)

# สร้างคำสั่ง กดปุ่ม F1 เพื่อสรุปยอด
GUI.bind('<F1>', SummaryData)
GUI.bind('<F2>', SummaryData)

E1.focus() # ให้ cursor ไปยังตำแหน่งของ E1
GUI.mainloop()