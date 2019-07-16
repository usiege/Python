#!/usr/bin/python3
#-*-encoding=utf-8-*-

a,b = 0,1
while b < 10:
	print(b)
	a,b = b,a+b
	pass

import sys
def fibonacci(n):
	a, b, counter = 0, 1, 0
	while True:
		if (counter > n):
			return
		yield a
		a, b = b, a+b
		counter += 1
		pass
f = fibonacci(10)
while True:
	try:
		print(next(f), end=" ")
	except StopIteration:
		sys.exit()
		raise
	pass


