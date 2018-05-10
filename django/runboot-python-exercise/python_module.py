#模块名
#!/usr/bin/python3
# Filename: support.py
#如想要导入模块 support，需要把命令放在脚本的顶端


if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')

# 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入

#将输出的值转成字符串，可以使用repr() 或 str() 来实现
# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。

#File

f = open("foo.txt", "w")
f.write("python 是一个非常好的语言")
f.close()

f = open("foo.txt", "r")
str = f.read()
print(str)
f.close()

f.readline()
f.readlines(sizehint)

for line in f:
	print(line, end = "")

#返回文件对象当前所处的位置，从文件开头开始算起字节数
f.tell()

#如果要改变文件当前位置
# from_what 0表示开头 1表示当前 2表示文件结尾
f.seek(offset, from_what)

'''
当处理一个文件对象时, 使用 with 关键字是非常好的方式。
在结束后, 它会帮你正确的关闭文件。 
而且写起来也比 try - finally 语句块要简短
'''
with open("foo.txt", "r") as f:
	read_data = f.read()
f.close()



