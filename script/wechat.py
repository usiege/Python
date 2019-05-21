#-*-coding=utf-8-*-
import itchat
import math
import PIL.Image as Image
import os

itchat.auto_login()
friends = itchat.get_friends(update=True)[0:]
user = friends[0]["UserName"]

dir_path = "./images"
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

num = 0
for i in friends:
    file_path = dir_path + "/" + str(num) + ".jpg"
    num += 1
    if os.path.exists(file_path):
        print(file_path)
        continue
    img = itchat.get_head_img(userName=i["UserName"])
    fileImage = open(file_path,'wb')
    fileImage.write(img)
    fileImage.close()
    

ls = os.listdir(dir_path)
each_size = int(math.sqrt(float(640*640)/len(ls)))
lines = int(640/each_size)
image = Image.new('RGB', (640, 640))
x = 0
y = 0
for i in range(0,len(ls)+1):
    try:
        img = Image.open(dir_path + "/" + str(i) + ".jpg")
    except IOError:
        print("Error")
    else:
        img = img.resize((each_size, each_size), Image.ANTIALIAS)
        image.paste(img, (x * each_size, y * each_size))
        x += 1
        if x == lines:
            x = 0
            y += 1
image.save(dir_path + "/" + "all.jpg")
itchat.send_image(dir_path + "/" + "all.jpg", 'filehelper')
