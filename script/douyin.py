# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 18:57:36 2022

@author: Administrator
"""

import pyautogui as ui # 操作UI
import pyperclip as cl # 复制粘贴
import pyscreeze # 屏幕点操作
import time

# import cv2
# print(os.getcwd())
# img = cv2.imread(path, 1)
# cv2.imshow("1", img)
# cv2.waitKey()

# 调用在执行动作后暂停的秒数，只能在执行一些pyautogui动作后才能使用
# 建议用time.sleep
ui.PAUSE = 0.2
# 启用自动防故障功能，左上角的坐标为（0，0）
# 将鼠标移到屏幕的左上角，来抛出failSafeException异常
ui.FAILSAFE = True


PAGE_PER_COUNT = 10 # 每页处理单子数量

SCREEN_WIDTH = 1920  # 屏幕宽度
SCREEN_HEIGHT = 1080 # 屏幕高度
BOTTOM_HEIGHT = 40 # 底部任务栏高度

Step = 200 # 跳到下一步步长
FineTuning = 80 # 页面浏览步长

ResizePhoneStep = 130 # 无法全部看清楚手机号的调整步长
ResizeBackStep = 50 # 识别到的订单高度过长，回调步长

safe_x, safe_y = 10, 500 # 安全点击处


# 识别订单复制
def recognize_order():
    img = "./copy.png"
    # ori_x = 500; ori_y = SCREEN_HEIGHT-Step-BOTTOM_HEIGHT;
    # width = 350; height = Step; 
    # region = (ori_x, ori_y, ori_x + width, ori_y + height)
    
    region = (532, 932, 850, 1040)  
    copy = ui.locateCenterOnScreen(img, confidence=0.7, 
                                   grayscale=True, region=region)
    print(copy)
    # ori_point = (ori_x, ori_y)
    # end_point = (ori_x + width, ori_y + height)
    if copy == None:
        return "", None
    
    ui.moveTo(copy)
    ui.click()
    res = cl.paste()
    print('订单号为：' + res)
    
    return res, copy


# 识别眼睛处点击获取手机号
def recognize_eye():
    img = "./eye.png"
    '''
    必传参数，图片路径；
    confidence, 识别精度，需要安装 opencv 才能使用；
    grayscale, 灰度级别，能够提升识别速度。
    '''
    # relative_height = SCREEN_HEIGHT - copy_point.y - BOTTOM_HEIGHT
    # ori_x = 1000; ori_y = copy_point.y;
    # width = 350; height = relative_height; 
    # region = (ori_x, ori_y, ori_x + width, ori_y + height)
    
    region = (1200, 860, 1380, 1040)
    
    eye = ui.locateCenterOnScreen(img, confidence=0.7, 
                                  grayscale=True,region=region)
    print('locate eye:')
    print(eye)
    if eye == None:
        img_double_check = "./eye2.png"
        eye_double_check = ui.locateCenterOnScreen(img_double_check, 
                                                   confidence=0.7, 
                                      grayscale=True,region=region)
        if eye_double_check == None:
            return "", None
        else:
            eye = eye_double_check
            print('double check eye point:')
            print(eye_double_check)
        
    ui.moveTo(eye)
    ui.moveRel(0, 5)
    ui.click()
    # 点击鼠标后等一下 (眼睛处显示有延迟)
    time.sleep(0.6) # required
    
    # 移动到后双击
    ui.moveRel(0, 15)
    ui.moveRel(-130,0)
    ui.click (clicks=2, interval=0.2)
    time.sleep(0.2)
    
    # 复制粘贴手机号
    ui.hotkey('ctrl','c')
    # print(cl.copy())
    res = cl.paste()
    print('移动光标选取手机号:' + res)
    print('-----------------')
    
    return res, eye

# 识别下一步图片
def recognize_next():
    print(ui.size())
    img = "./next.png"
    
    # recognize_height = 100
    # ori_x = 0; ori_y = 1080-recognize_height-1 - BOTTOM_HEIGHT;
    # width = SCREEN_WIDTH-100; height = recognize_height; 
    
    # 识别区域，参数为区域左上与右下坐标点
    # region = (ori_x, ori_y, ori_x + width, ori_y + height)
    region = (0, 940, 1920, 1040)
    
    print(region)
    nextpng = ui.locateCenterOnScreen(img, confidence=0.7, 
                                  grayscale=True,region=region)
    print(nextpng)
    ui.moveTo(nextpng)

    if nextpng == None:
        return None
        
    return nextpng 
    
def scroll_to_top():
    ui.scroll(1000000)
    time.sleep(0.2)

def scroll_to_bottom():
    ui.scroll(-1000000)
    time.sleep(0.2)

# 处理单个页面
def dispose_page(page_count):
    try:
        count = page_count # 每页订单数量
        last_order = "ORDER_START_MARK" # 上一次的订单，防止重复
        order_dic = {} # 订单记录 {"order":"phone"}
        
        too_much_error = 100
        while count:
            # 识别订单
            order, copy_point = recognize_order()

            # 安全保险，防止点到订单跳去别的页面
            # ui.moveTo(safe_x, safe_y)
            
            # 未识别到订单
            if copy_point == None:
                ui.scroll(-FineTuning)
                too_much_error -= 1
                if too_much_error:
                    continue
                else:
                    exit(0)
            
            ## 识别到的是上一个订单号（重复）
            if last_order == order:
                ui.scroll(-FineTuning)
                continue
            
            # 记录为上次订单，无效跳过
            last_order = order
            
            
            # 调整位置
            padding = SCREEN_HEIGHT-copy_point.y-BOTTOM_HEIGHT
            if padding < Step:
                print('查找手机号页面向上滚动调整')
                # ui.scroll(padding.item()-Step-ResizePhoneStep)
                ui.scroll(-280)
            else:
                print('查找手机号页面向下微调')
                ui.scroll(50)

            # 识别眼睛
            # new_y = SCREEN_HEIGHT-(Step-padding.item())
            # adjust_point = pyscreeze.Point(copy_point.x, new_y)
            # print(adjust_point) # 根据订单识别点去寻找眼睛
            
            time.sleep(0.2)
            phone, eye_point = recognize_eye()
            
            # 记录订单
            if order not in order_dic:
                order_dic[order] = phone
                           
            # 寻找下一个
            time.sleep(0.2)
            count -= 1
        
        # 返回结果
        return order_dic
        
    except KeyboardInterrupt:
        ui.alert(text='处理单个页面时出错',title='因故停止，点击停止',button='OK')
        print('\nExit.')
        return {}
        


ORIGINAL_EXCEL = './original.xlsx' # 原始Excel文件
ORDER_EXCEL = 'order.xlsx' # 预操作文件

import pandas as pd # 表格操作
from pandas import DataFrame
# import numpy as np
# 禁用科学计数
pd.set_option('display.float_format', lambda x: '%.f' % x) 

def write_to_excel(ex_path, dic, df):
    print('record start ---------')
    for order, phone in dic.items():
        # if isinstance(order, str):
        #     # order = 
        # if isinstance(phone, str):
        #     phone = int(phone)
            
        # 找到行索引
        indexs = df.loc[df['order'] == order].index.tolist()
        
        print(indexs)
        if len(indexs) > 0:
            print('find a order index: ')
            index = indexs[0]; print(index);
            # A value is trying to be set on a copy of a slice from a DataFrame
            ## df.loc[index]['phone'] = phone 
            df.loc[:, 'phone'][index] = phone
            print(df.loc[index]['phone'])
        else:
            print('insert a new item: ' + str(order))
            new_line = {'order': order, 'phone': phone}
            df = df.append(new_line, ignore_index=True)

    # 重新写入
    try:
        # index表示设置是否保存索引（就是行号）
        # header表示设置是否保存表头（就是列名）
        df.to_excel(ex_path, index=None)
        print('...................')
    except KeyboardInterrupt:
        ui.alert(text='保存处理结果时出错！！！',title='因故停止，点击停止',button='OK')
        log = 'write excel error ..\n'
        print(log)
        
    print('record end ---------')
    print("write done!")
    return df

def save_to_excel(save_dic, pd_excel, res_path):
    # read and write
    # excel = pd.read_excel("test.xlsx", header=0)
    df = DataFrame(pd_excel, dtype=object)
    res = write_to_excel(res_path, save_dic, df)
    
    print(res.head())
    print("order dispose...")
    
    # print(df.columns)
    # print(df.index)
    # print(df.describe())

if __name__ == "__main__":

    PAGES = 177
    while True:
        # 初始化位置
        ui.moveTo(safe_x, safe_y)
        ui.click()
        scroll_to_top()  
        ui.scroll(-Step)
        time.sleep(0.8) # 滑动到顶等待时间 
        
        # 处理一页
        print('订单处理已开始，请勿操作电脑；如需停止请请鼠标移至屏幕左上角 0, 0 处')
        orders = dispose_page(PAGE_PER_COUNT)
        print(' ---- orders ---- ')
        print(orders)
        print(' ----- end ----')
        
        # 保存并写入
        read_and_write_path = r'order.xlsx'
        HEADER = ['order', 'book', 'price', 'state', 'nickname', 'phone']
        EXCEL = pd.read_excel(read_and_write_path, dtype=object)
        print(EXCEL.head())
        # 处理制表符
        EXCEL['order'] = EXCEL['order'].apply(lambda x:str(x).replace('\t','').replace('\n',''))
        # orders = { # for test 
        #     "333": "135764591111",
        #     "4942384593302937418": 13987653421,
        #     "4942197736270552398": "9876111111",
        #     "4941718353495080904": "2134987654"
        #     }
        save_to_excel(orders, EXCEL, read_and_write_path)
        time.sleep(2) # 保存文件要等一下
        print('save end ...')
        
        # 寻找下一页并进入
        scroll_to_bottom()
        time.sleep(0.5) # 滑动到底等待时间
        nPoint = recognize_next()
        ui.click(nPoint)
        print("顺利进入 第（%d）页，本页数据保存！" % (PAGES+1))
        print("点击完成等待~~~")
        time.sleep(2) # 点击下一页刷新时间等待
        
        PAGES += 1
        if PAGES % 5 == 0:
            time.sleep(45)
        
        
    
    
    
    