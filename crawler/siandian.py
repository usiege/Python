#!/usr/bin/python
# coding:utf-8

import urllib2 
import re 
from bs4 import BeautifulSoup
from distutils.filelist import findall
 
import time
import sys
import os

import socket

second_out = 200
socket.setdefaulttimeout(second_out) 

reload(sys)
sys.setdefaultencoding('utf-8')
 
web = "http://www.siandian.com/yulu/"

def get_page(index):
	url = web + "{}.html".format(index)
	request = urllib2.Request(url)
	page = urllib2.urlopen(request, timeout=second_out) 

	return page

def get_sentence(index, index_path):
	pass

if __name__ == '__main__':

	global index
	index = 1351

	index_path = os.path.join(os.getcwd(), 'index.txt')
	if not os.path.exists(index_path):
		with open(index_path, 'w') as f:
			s = str(index)
			f.write(s)

	with open(index_path, 'r') as f:
		s = f.read()
		print s
		index = int(s)
	
	

	while True:
		
		page = get_page(index)
		time.sleep(1)

		try:
			if page != None:
				contents = page.read()
				# print contents
				soup = BeautifulSoup(contents, "html.parser", fromEncoding="gb18030")
				soup.originalEncoding
				soup.prettify()
				# print soup.prettify()
				print "当前索引：{}".format(index)

				# print soup.title
				# print soup.head
				# print soup.p
				# print soup.a
				ppps = soup.find_all('p')

				path_dir = os.path.join(os.getcwd(), "txt")
				if not os.path.exists(path_dir):
					os.mkdir(path_dir)

				if len(ppps) > 10:

					file_path = "{}/{}.txt".format(path_dir,index)
					if os.path.exists(file_path):
						index += 1
						continue

					with open(file_path, 'w') as f:
						for cont in soup.find_all('p'):
							# print type(cont) # bs4.element.Tag
							text = cont.text.encode('utf-8').decode('utf-8')
							f.write(text + '\n')

					with open(index_path, 'w') as f:
						f.write("{}".format(index))
				else:
					print "无信息可保存！！！"
					index += 1
					continue
			else:
				print "index: {} ----> None".format(index)

		except Exception as e:

			print "处理网址异常！！！"
			print e
			index += 1

			continue
		finally:

			print "finally"
			with open(index_path, 'w') as f:
				f.write("{}".format(index))
			pass	

