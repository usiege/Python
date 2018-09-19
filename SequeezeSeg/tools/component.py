#!/usr/bin/python3
# --encoding=utf8--

import os
import numpy as np
import pandas as pd
import cmath, math

class TransformData(object):
    
    # 数据根目录
    @property
    def rootPath(self):
        return self._rootPath
    
    @rootPath.setter
    def rootPath(self, path):
        self._rootPath = path
        
    # 生成的npy数据保存目录
    @property
    def savePath(self):
        return self.rootPath + '/npy/'

    # 转换数据 并 生成npy文件
    def transformData(self, filepath=""):
        assert filepath != ""
        
        

    def __init__(self):
        pass

    # 加载所有的文件名
    def load_file_names(self):
        assert self.rootPath != "", "root path is empty"
        rootname = self.rootPath + '/pts'
        
        result = []
        ext = ['csv', 'npy']

        files = self._filenames(rootname)
        for file in files:
            if file.endswith(tuple(ext)):
                result.append(file)

        return self._filenames(rootname)
    


    # 将csv转成npy文件
    # training下的三个目录中的文件名相同,分别提取出来合并成一个cvs文件
    # 将csv文件转换成与Seg相似的NPY文件
    
    # seg中npy文件格式为[x, y, z, intensity, range, category], 共有 64 * 512 = 32768个
    # 而我们的每个csv有57888个点。
    
    def cover_csv_to_npy(self, filename, ptsdirname='pts', intensitydirname='intensity', categorydirname='category'):
        
        rootpath = self.rootPath
        ptsPath = self.rootPath + '/' + ptsdirname + '/' + filename
        intensityPath = self.rootPath + '/' + intensitydirname + '/' + filename
        categoryPath = self.rootPath + '/' + categorydirname + '/' + filename
        
        npypath = self.savePath + '/' + filename
        
        pts = pd.read_csv(ptsPath, header=0)
        # pts.columns = ['x', 'y', 'z', 'i', 'c']
        intensity = pd.read_csv(intensityPath)
        category = pd.read_csv(categoryPath)
        
        # print '---- pts ----'
        # print pts.ix[1]
        
        # 连接操作
        contact = pd.concat([pts, intensity, category], axis=1)
        #
        data = pd.DataFrame(contact)
        data.columns = ['x', 'y', 'z', 'i', 'c']
        data.insert(3, 'r', 0)
        
        # data.loc[:, 'r'] = 0
        # data.loc[:, ['i', 'r']] = data.loc[:, ['r', 'i']].values # 交换值
        
        # print data
        # def range(x, y, z):
        #     total = x ** 2 + y ** 2 + z ** 2
        #     # print np.sqrt(total)
        #     # np.sqrt(x ** 2 + y ** 2 + z ** 2)
        #     return cmath.sqrt(total)
        
        
        # print '----- contact -----'
        data['r'] = np.sqrt(data['x'] ** 2 + data['y'] ** 2 + data['z'] ** 2)
        
        # print data
        nzero = data.loc[(data.x != 0) & (data.y != 0) & (data.z != 0)]
        
        # print nzero
        nzero.to_csv('./contact.csv', index=False, header=False)
        
        return nzero
        
    

    # np
    def generate_np_format(self, source=pd.DataFrame()):
        npy = np.zeros((64, 512, 6), dtype=np.float32)
    
        n = 0
        max_phi = 0
        min_phi = float('inf')
        
        # print 'generate np format: '
        # print 180.0 / 512
        
        xyflag = [0] * (64*512)
        
        for indexs in source.index:
        
            values = source.loc[indexs].values[:]
            # compute
            x, y, z, i, r, c = values[0], values[1], values[2], values[3], values[4], values[5]
        
            # theta -16~16 phi 45~135
            sqrt_xy = np.sqrt(x ** 2 + y ** 2)
            theta = np.arctan(z / sqrt_xy) * 180 / math.pi
            phi = np.arcsin(y / sqrt_xy) * 180 / math.pi
        
            point_x, point_y = int((theta - (-16)) // 0.5), int((phi - (-90)) // (180.0 / 512))
        
            # if xflag[point_x] == 0:
            #     xflag[point_x] = 1
            
            #
            flag_index = point_x * 512 + point_y
            
            if xyflag[flag_index] == 0:
                # print flag_index
                
                xyflag[flag_index] = 1
                npy[point_x , point_y, :] = [x, y, z, i, r, c]
                
            
            # test
            # print point_x, point_y
            
            if phi > max_phi: max_phi = phi
            if phi < min_phi: min_phi = phi
            
            # if n == 0:
            #     print 'values test: '
            #     print type(values)
            #     print (values)
            #     print (x, y, z)
            #     print theta
            #     print phi
            #     print (point_x, point_y)
            #     n += 1
                
        # print 'x flag: %s' % xyflag
        print 'point count is: %d' % (self._array_flag_count(xyflag, 1))
        #
        # print 'phi max and min: '
        # print max_phi, min_phi
        
        return npy

    # 所有子文件
    def _filenames(self, filedir):
        result = []
        for root, dirs, files in os.walk(filedir):
            # print "root: {0}".format(root)
            # print "dirs: {0}".format(dirs)
            # print "files: {0}".format(files)
            result = files
        return result
    
    # 统计标记数量
    def _array_flag_count(self, array, flag):
        count = 0
        for num in array:
            if num == flag:
                count += 1
        return count
        
       
        
    
        
# '''
if __name__ == '__main__':
    
    testpath = '../../data/training'
    
    compontent = TransformData()
    compontent.rootPath = testpath
    # print(compontent.load_file_names(testpath))
    
    source = compontent.cover_csv_to_npy('ac3fc22d-f288-477f-a7aa-b73936b23f91_channelVELO_TOP.csv')
    #
    print '源数据：'
    print source
    
    print '正在转换......'
    result = compontent.generate_np_format(source)
    
    print '转换后数据：'
    # 生成一个csv文件
    pdata = pd.DataFrame(np.reshape(result, (-1, 6)), columns = ['x', 'y', 'z', 'intensity', 'range', 'category'])
    # pdata[['x', 'y', 'z', 'intensity', 'range', 'category']].astype('float64').to_csv('transnpy.csv', index=None, header=None)
    
    # 生成一个npy文件
    np.save("./data.npy", result)
    
    # 检查npy文件
    npy = np.load("./data.npy")
    
    print '文件转换已完成！'
    print np.shape(npy)
    
    # print result
# '''