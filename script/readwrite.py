
path = "/Users/xianfeng/Downloads/"
name = '3fdf8288-3a0d-4b1b-8800-e8ac56731682.txt'
file = open(path+name)
all_the_text = file.read()
file.close()

outPath = path+"3f.txt"
output = open(outPath,'w')
output.write(all_the_text)
output.close()