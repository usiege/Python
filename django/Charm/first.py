#函数多参数
def printinfo(arg1, *vartuple):
	"打印任何传入的参数"
	print("输出")
	print(arg1)
	for var in vartuple:
		print(var)
	return;

printinfo(10)
printinfo(2, 10, "1111", [1,2,(1,2)])

#匿名函数
sum = lambda arg1, arg2: arg1 + arg2;
print("相加后的值：", sum(10, 20))

#作用域
x = int(2.9) #内建作用域

g_ount = 0 #全局作用域

def outer():
	o_count = 1 #闭包函数外的函数中
	def inner():
		i_ount = 2 #局部作用域

#global nonlocal
print("global ------> ")

num = 1
def func1():
	global num
	print(num)
	num = 123
	print(num)

func1()
print(num)

#要修改嵌套作用域，外层非全局作用域变量
def outer():
	num = 10
	def inner():
		nonlocal num
		print(num)

	inner()
	print(num)
outer()
print(num)

#遍历
knight = {"a":"jjj","e":"iii", "d":"lll", "c":"ccc", "b":"xxx"}
for k, v in knight.items():
	print(k, v)

for i, v in enumerate(knight):
	print(i, v)
	print(knight[v])

import sys
print(dir())

with open("foo.txt", "r") as f:
	read_data = f.read()
f.close()


