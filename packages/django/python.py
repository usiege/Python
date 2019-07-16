#!/usr/bin/env python3
#-*-encoding:utf-8-*-
# chmod +x python.py


var = 100
if var:
	print("var")
elif var == 1:
	print("var == 1")
else:
	print("var other")


#def functionname([formal_args,] *var_args_tuple):

def printinfo(arg1, *vartuple):
	"打印任何传入的参数"
	print("输出")
	print(arg1)
	for var in vartuple:
		print(var)
	return;

printinfo(10)
printinfo(1, 10, "1111", [1,2,(1,2)])