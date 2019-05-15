#!/usr/bin/python
#coding=utf-8
#-*- coding:utf-8 -*-

# https://zhuanlan.zhihu.com/p/20878530?refer=intelligentunit

def quicksort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[len(arr) / 2]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	return quicksort(left) + middle + quicksort(right)

print(quicksort([3, 6, 9, 10, 11, 8, 0]))


'''
Python中没有 x++ 和 x-- 的操作符。

'''
hello = 'hello'   # String literals can use single quotes
world = "world"  
hw12 = '%s %s %d' % (hello, world, 12)  # sprintf style string formatting
print hw12

xs = [3, 1, 2]
print xs, xs[2]
print xs[-1]

# 和列表最重要的不同在于，元组可以在字典中用作键，还可以作为集合的元素，而列表不行。

def sign(x):
	if x > 0:
		return 'positive'
	elif x < 0:
		return 'negative'
	else:
		return 'zero'
for x in [-1, 0, 1]:
	print sign(x):

def hello(name, loud = False):
	if loud:
		print 'HELLO, %s' % name.upper()
	else:
		print 'HELLO, %s' % name

hello('Bob')
hello('Fred', loud = True)

class Creeter(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
	def greet(self, loud = False):
		if loud:
			print 'HELLO, %s!' % self.name.upper()
		else:
			print 'hello, %s' % self.name

g = Greet('Fred')
g.greet()

		
import numpy as np




