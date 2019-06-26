# 特征工程
# 天知道我怎么又来这里记录这本书的东西了；
# 我只是觉得这样很好看，让人有种满足感；

# 5.4.1 分类特征
# 独热编码
# 就是用0和1出现在对应的列分别表示每个分类值的有或无
# 如果一列不够的话， 那么多加几列试试够不够表示
from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer(sparse=False, dtype=int)
vec.fit_transform(data)

data = [{'neighborhood': 'Queen anne'},
        {'neighborhood': 'Fremont'},
        {'neighborhood': 'Wallingford'},
        {'neighborhood': 'Fremont'}]

{'Queen anne': 1, 'Fremont': 2, 'Wallingford': 3}

# 查看特征名称
vec.get_feature_names()
# 可通过稀疏矩阵表示
vec = DictVectorizer(sparse=True, dtype=int)
vec.fit_transform(data)

# 5.4.2 文本特征
# 单词向量化
sample = ['problem of evil',
         'evil queen',
         'horizon problem']

from sklearn.feature_extraction.text import CountVectorizer

vec = CountVectorizer()
x = vec.fit_transform(sample)

# 可视化下
import pandas as pd
pd.DataFrame(x.toarray(), columns=vec.get_feature_names())

# TF-IDF词频逆文档频率
from sklearn.feature_extraction.text import TfidfVectorizer
vec = TfidfVectorizer()
x = vec.fit_transform(sample)
pd.DataFrame(x.toarray(), columns=vec.get_feature_names())


# 5.4.3 图像特征
# 请参考 http://scikit-image.org

# 5.4.4 衍生特征
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([4, 2, 1, 3, 7])
plt.scatter(x, y)

from sklearn.linear_model import LinearRegression
X = x[:, np.newaxis]
model = LinearRegression().fit(X, y)
yfit = model.predict(X)
plt.sctter(x, y)
plt.plot(x, yfit)

## 在数据中增加多项式特征
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=3, include_bias=False)
X2 = poly.fit_transform(X)

model = LinearRegression().fit(X2, y)
yfit = model.predict(X2)
plt.scatter(x, y)
plt.plot(x, yfit)


# 5.4.5 缺失值填充
from numpy import nan
X = np.array([[nan, 0, 3],
              [3, 7, 9],
              [3, 5, 2],
              [4, nan, 6]])

y = np.array([14, 16, -1, 8, -5])

# 填充方法如均值，中位数，众数
from sklearn.preprocessing import Imputer
imp = Imputer(strategy='mean')
X2 = imp.fit_transform(X)


# 5.4.6 特征管道
# 天知道什么才是管道
# 起名字的时候能不这么神化吗？

from sklearn.pipeline import make_pipeline
model = make_pipeline(Imputer(strategy='mean'),
                      PolynomialFeatures(degree=2),
                      LinearRegression())

model.fit(X, y)
model.predict(X)

# 貌似这个管道像个组装器，一键组装，省去中间商赚码字时间，我的天；
# 但是我还是不能接受你叫管道的这个事实，what the fuck！
# 好了，我可以回家了；
