"""#!usr/bin/python3"""

#!usr/bin/env python3
#-*- encoding=utf-8 -*-

#保留字
'''
['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 
'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 
'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 
'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''

counter = 100
miles = 1000.0
name = 'runoob'

#允许进行多个变量赋值
a = b = c = 1
print(id(a),id(b),id(c))

a,b,c = 1, 2, 'runoob'

#数字类型
a,b,c,d = 1, 20.0, True, 4+3j
print(type(a),type(b),type(c),type(d))

if isinstance(a,int):
	print("a是数字类型")

class A:
	pass

class B(A):
	pass

bool_res1 = isinstance(B(),A)  #return True
bool_res2 = type(B()) == A 	#return False

print('bool res1:', bool_res1)
print('bool res2:', bool_res2)

#删除对象引用
del a,b,c,d

#混合计算时，python会把整形转换为浮点型
#/为浮点除，//为整除

str = 'Runoob'

print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + "TEST")

print("添加反斜杠发生转义，添加r显示原始字符")
print(r"r\kkkoob")
print("python没有单独的字符类型，字符是长度为1的字符串")

#列表
list = ['123', 24, 2.0, 'runoob']
print(list)

#元组
tuple = ('123', 24, 2.0, 'runoob')
print(tuple)

#集合
set = {'Tom','Jim','Mary','Jack','Rose'}
print(set)

#set()用来创建空集合 ，{}用来创建空字典

#字典
dict = {'name':'runoob', 'code':1, 'site':'www.runoob.com'}
print(dict)
print('keys:', dict.keys())
print('values:', dict.values())

chr(1)		#整数转字符
ord('1') 	#字符转整数
hex(100)	#整数转十六进制
oct(100)	#整数转八进制


















