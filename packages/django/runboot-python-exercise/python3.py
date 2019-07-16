#!/usr/bin/env python3
#-*-encoding=utf-8-*-
 
import keyword

print(keyword.kwlist)
#注释
'''
多行注释
'''

"""
多行注释
"""

#多行语句
item1 = item2 = item3 = 1
total = item1 + \
item2 + \
item3

#用户输入
input("\n按下 enter 键后退出\n")

print("print 默认输出换行，如需要不换行，则如下")
print("不换行要加end", end = " ")

import sys
for i in sys.argv:
	print(i)
from sys import argv,path
print('path:', path)

#python -h 可以使用该参数查看各参数帮助信息；


