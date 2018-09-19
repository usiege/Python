#!/usr/bin/python3
# --encoding=utf8--

import component as ct

def transform_npy(rootpath=""):
    
    print rootpath
    
    
    trantool = ct.TransformData()
    trantool.rootPath = rootpath
    
    ptsfiles = trantool.load_file_names()
    
    
    for file in ptsfiles:
        print '正在转换 file ：%s  ......' % file
        
        if file[-4:] == '.csv':
            npyname = (file[:-4] + '.npy')
            
            
            npypath = trantool.savePath + npyname
            print '%s 文件已生成' % npyname
        
if __name__ == '__main__':
    
    path = "/home/mengweiliang/disk15/df314/training"
    transform_npy(path)
    
    