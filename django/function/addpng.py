#!usr/bin/python
#-*-encoding:utf-8-*-

import sys
import os

def add_pathname_2x(pathname):
	if os.path.isdir(pathname):
		filelist = os.listdir(pathname)
		print("子文件：")
		print(filelist)
		for file in filelist:
			if file.endswith(".png"):
				if not file.endswith("@2x.png"):
					oldpath = pathname + "/" + file
					newname = file[:-4] + "@2x.png"
					print("当前文件：" + oldpath)
					if os.path.isfile(oldpath):
						print("新文件：" + newname)
						os.rename(oldpath, pathname + "/" + newname)
				

add_pathname_2x(sys.argv[1])