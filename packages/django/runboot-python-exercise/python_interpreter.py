#!usr/bin/env python3
#-*-encoding=utf-8-*-

# 设置环境变量 $PATH=$PATH:/usr/local/python3/bin/python3
# win下 set path=%path%;C:\python34
# $chmod +x python_name.py 增加其执行权限 ./python_name.py 即可运行

a = 4
print(a**2)

b = 60
c = 10
d = 0b00001111
e = 0o47
f = 0xeff

print(a,b,c,d,e,f)

cc = dd = 1000
ee = 1000
print(id(cc),id(dd))
print(id(ee))

'''
楼上的同学所说的在脚本式编程环境中没有问题。但是在交互式环境中，编译器会有一个小整数池的概念，
会把（-5，256）间的数预先创建好，而当a和b超过这个范围的时候，两个变量就会指向不同的对象了，因此地址也会不一样
'''
del ee




