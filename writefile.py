# writefile.py

# Example of write data in txt file
# 'w' =  replace current data, 'a' = append data
# filename = 'data.txt'
# with open(filename, 'a') as file:
#     file.write('\n' + 'Durian: 45')

from datetime import datetime

# ฟังชั่นบันทึกข้อมูลลงไฟล์ txt แบบง่าย, ถ้าใส่ภาษาไทยต้องใส่ encoding = 'utf-8' ด้วย
def writetext(quantity, total):
    stamp = datetime.now()
    stamp = stamp.replace(year=stamp.year+543) # บวกเป็น พ.ศ.
    stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
    filename = 'data.txt'
    with open(filename, 'a', encoding = 'utf-8') as file:
        file.write('\n' + 'วัน-เวลา: {} ทุเรียน: {} กก. รวมยอดทั้งหมด: {:,.2f} บาท'.format(stamp,quantity,total))
        
# writetext(90, 9000)
# writetext(91, 9100)
# writetext(92, 9200)
# writetext(93, 9300)