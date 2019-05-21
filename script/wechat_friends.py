#!/usr/local/bin/python3
#-*-coding=utf-8-*-
import itchat
import math
import PIL.Image as Image
import os

itchat.auto_login()
friends = itchat.get_friends(update=True)[0:]
user = friends[0]["UserName"]

dir_path = "./image"
num = 0
for i in friends:
    img = itchat.get_head_img(userName=i["UserName"])
    fileImage = open(dir_path + "/" + str(num) + ".jpg",'wb')
    fileImage.write(img)
    fileImage.close()
    num += 1

ls = os.listdir(dir_path)
each_size = int(math.sqrt(float(640*640)/len(ls)))
lines = int(640/each_size)
image = Image.new('RGBA', (640, 640))
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
