import os

os.getcwd() #返回当前目录
print(os.getcwd())

'''
import shutil

shutil.copyfile("src.f", "des.f")
shutil.move("src.f", "des.f")

'''
import glob

print(glob.glob("*.py")) #文件通配符

import sys

print(sys.argv)

sys.stderr.write("Warning, log file not found starting a new one\n")

#正则匹配
import re

print(re.findall(r'\bf[a-z]*]', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the hat'))

print('tea and too'.replace('too', 'two'))

import math

print(math.cos(math.pi / 4))
print(math.log(1024, 2))

import random

print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))
# SyntaxError: unexpected EOF while parsing 少打了个括号
print(random.random())
print(random.randrange(6))


#互联网
from urllib.request import urlopen

for line in urlopen('http://www.runoob.com/python3/python3-examples.html'):
    line = line.decode('utf-8')
    if 'EST' in line or 'EDT' in line:
        print(line)


from datetime import date

now = date.today()
print(now)

import doctest
doctest.testmod()

# http://www.runoob.com/python3/python3-examples.html