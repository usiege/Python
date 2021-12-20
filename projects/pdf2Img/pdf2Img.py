#!/usr/bin/python
# -*- coding: utf-8 -*-
# made by Tseng

import os
import sys

from wand.image import Image

 
# 解决转码
reload(sys)
sys.setdefaultencoding('utf8')


pdfSrc = './pdf'
imageDst = './images'


# 将pdf转化为image
def pdfToImage(src):
  for root, dirs, files in src:
    for name in files:
      if name.endswith(".pdf"):
        dirPath = imageDst + '/' + name[:-4]
        if not os.path.exists(dirPath):
          os.mkdir(dirPath)
        
        f = root + '/' + name
        with(Image(filename=f, resolution=120)) as source: 
          for i, image in enumerate(source.sequence):
            newfilename = dirPath + '/' + name[:-4] + '_page' + str(i + 1) + '.png'
            Image(image).save(filename=newfilename)
        print(name + '  >>>>>>>  pdfToImage转化完成')
  print('pdfToImage全部转化完成')

gp = os.walk(pdfSrc)
pdfToImage(gp)




