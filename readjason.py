# readjson.py
# json = JavaScript Object Notation

import json

def readjson():
	with open('data.json', encoding='utf-8') as file:
		data = json.load(file)
		print(data)
		print(data[0])
		# print(type(data)) # เรียกดูชนิดของข้อมูลว่าเป็น list ไหม
  		# print(data[0]['point']) # สามารถ Reference index ด้วยชื่อ key ได้
	return data

# Google search: json write utf-8 python
# 'w' เขียนทับข้อมูลในไฟล์เดิม 'fruit.json'
def writejson(data):
	jsonobject = json.dumps(data, ensure_ascii=False, indent=4)
	with open('fruit.json', 'w', encoding='utf-8') as file:
		file.write(jsonobject)


data = {'112341234':['Banana', 100, 5],
		'112341235':['Durian', 150, 99],
		'112341236':['Apple', 200, 10],
		'112341237':['แก้วมังกร', 300, 20]}

writejson(data)

# สรุปการเขียนไฟล์ Json
#############################################################

# เก็บไฟล์ json แบบ List ใช้ [] เป็นแบบ array
#-------------------------------------------------
'''
[
	{"id":1001, "name":"Loong Wissawakorn", "point": 100},
	{"id":1002, "name":"Somsak Deemak", "point": 200},
	{"id":1003, "name":"Somsri Jaidee", "point": 150}
]
'''
# เก็บไฟล์ json แบบ Dictionary ใช้ {} ต้องมี key กับ value เสมอ
#-------------------------------------------------
'''
{
	"101": {"id":1001, "name":"Loong Wissawakorn", "point": 100},
	"102": {"id":1002, "name":"Somsak Deemak", "point": 200},
	"103": {"id":1003, "name":"Somsri Jaidee", "point": 150}
}
'''
#############################################################