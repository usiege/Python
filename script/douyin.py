# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 18:57:36 2022

@author: Administrator
"""

import pyautogui as ui
import pyperclip as cl
import time
import cv2
import os

ui.PAUSE = 0.5

# print(os.getcwd())
# img = cv2.imread(path, 1)
# cv2.imshow("1", img)
# cv2.waitKey()

Step = 200

def recognize_order():
    
    img = "./copy.png"
    ori_x = 500; ori_y = 1080-Step;
    width = 350; height = Step; 
    region = (ori_x, ori_y, ori_x + width, ori_y + height)
    copy = ui.locateCenterOnScreen(img, confidence=0.7, 
                                   grayscale=True, region=region)
    print(copy)
    # ori_point = (ori_x, ori_y)
    # end_point = (ori_x + width, ori_y + height)
    
    ui.moveTo(copy)
    if copy == None:
        return "", None
    
    ui.click()
    res = cl.paste()
    print('订单号为：' + res)
    
    return res, copy


def recognize_eye():
    img = "./eye.png"
    '''
    必传参数，图片路径；
    confidence, 识别精度，需要安装 opencv 才能使用；
    grayscale, 灰度级别，能够提升识别速度。
    '''
    ori_x = 1000; ori_y = 1080-Step;
    width = 350; height = Step; 
    region = (ori_x, ori_y, ori_x + width, ori_y + height)
    eye = ui.locateCenterOnScreen(img, confidence=0.7, 
                                  grayscale=True,region=region)
    print('locate start')
    print(eye)
    ui.moveTo(eye)
    print('locate end...')

    if eye == None:
        return "", None
        
    ui.click()
    # ui.sleep(2)
    ui.moveRel(0, 10)
    ui.moveRel(-150,0)
    ui.click (clicks=2, interval=0.25)
    print('移动光标并选中内容！')

    ui.hotkey('ctrl','c')
    # print(cl.copy())
    res = cl.paste()
    print('手机号为：' + res)
    print('-----------------')
    
    return res, eye

def recognize_next():
    
    print('next end.')
    

try:
    while True:
        # 识别订单
        order, copy_point = recognize_order()
        # 识别眼睛
        phone, eye_point = recognize_eye()
        
        # 滑动页面
        ui.scroll(-Step)
        ui.sleep(1)
        
except KeyboardInterrupt:
    print('\nExit.')


'''
    if point == None:
        print('结束啦！')
        break;
    if res == None or res == '':
        print('剪贴板内容为空！')
        break;
    
    
    if res == '*':
        ui.scroll(-250)
        # ui.sleep(1)
        continue
  '''  


