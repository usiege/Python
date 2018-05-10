import os
import os.path

l = [ ]

def get_py(path, l):
	filelist = os.listdir(path)
	for filename in filelist:
		pathTmp = os.path.join(path, filename)	#获取path与filename组合后的路径
		if os.path.isdir(pathTmp): 		#是目录
			get_py(pathTmp, l)
		elif filename[-3: ].upper() == '.PY': 	#不是目录，比较后缀名
			l.append(pathTmp)

path = input('请输入路径：').strip()
get_py(path, l)

for fliepath in l:
	print(fliepath + '\n')


