# writecsv.py
import csv
from types import DynamicClassAttribute

def writecsv(data):
    # data = ['Time','quantity','total']
    with open('data.csv', 'a', newline='', encoding='utf-8') as file:
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)
    print('Success')

# d = ['2021-05-11 10:15:10', 50, 5000]
# writecsv(d)

def readcsv():
    with open('data.csv', newline='', encoding='utf-8') as file:
        fr = csv.reader(file) # file reader
        # print(list(fr))
        data = list(fr)
    return data
        
result = readcsv()
print(result)

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

sumresult = sumdata()
print(sumresult)

'''
# การเรียกข้อมูลใน List ต้องกำหนด index
print(result[3])

# การเรียกข้อมูลใน List ซ้อน List ต้องระบุ index ที่ต้องการต่อท้าย
print(result[3][2])

# ถ้าต้องการผลรวมของตำแหน่งสุดท้าย * 10 ต้องใส่ float ครอบไว้
print(float(result[3][2]) * 10)
'''

# ทำ For Loop
# วิธีที่ 1 ทำแบบยาว
# ต้องแปลงให้เป็นตัวเลข float เพื่อให้ sum ได้
# หลังจากนั้นสามารถใช้ sum ได้ เพื่อแสดงผลลัพท์ด้านหลัง
#-----------------------------------
sumlist_quan1 = []
for total in result:
    sumlist_quan1.append(float(total[1]))
print(sumlist_quan1, sum(sumlist_quan1))

#-----------------------------------
# วิธีที่ 2 ทำแบบย่อให้สั้น
sumlist_quan2 = [float(total[1]) for total in result]
print(sumlist_quan2, sum(sumlist_quan2))

#-----------------------------------
# ถ้าอยากได้แค่ผลรวม ทำแบบย่อให้สั้น
sumlist_quan = sum([float(total[1]) for total in result])
print(sumlist_quan)