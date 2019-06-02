from sklearn import datasets

iris = datasets.load_iris()
X = iris.data # 特征向量
y = iris.target # 获得样本label

from sklearn.datasets.samples_generator import make_clsssification

X, y = make_clsssification(n_samples=6, n_features=5, n_informative=2,
n_redundant=2, n_classes=2, n_clusters_per_class=2, scale=1.0, random_state=20)

# n_samples：指定样本数
# n_features：指定特征数
# n_classes：指定几分类
# random_state：随机种子，使得随机状可重

for x_, y_ in zip(X, y):
    print(y_, end=': ')
    print(x_)


from sklearn import preprocessing

# 归一化
data = [[0, 0], [0, 0], [1, 1], [1, 1]]
# 1. 基于mean和std的标准化
scaler = preprocessing.StandardScaler().fit(data)
scaler.transform(data)

# 2. 将每个特征值归一化到一个固定范围
scaler = preprocessing.MinMaxScaler(feature_range=(0, 1)).fit(data)
scaler.transform(data)

# 正则化
X_normalized = preprocessing.normalize(X, norm='l2')

# one-hot 编码
# 用于给线性模型增加非线性能力
data = [[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]]
encoder = preprocessing.OneHotEncoder().fit(data)
enc.transform(data).toarray()

## 数据集拆分
# 作用：将数据集划分为 训练集和测试集
# 格式：train_test_split(*arrays, **options)
from sklearn.mode_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
"""
参数
---
arrays：样本数组，包含特征向量和标签

test_size：
　　float-获得多大比重的测试样本 （默认：0.25）
　　int - 获得多少个测试样本

train_size: 同test_size

random_state:
　　int - 随机种子（种子固定，实验可复现）
　　
shuffle - 是否在分割之前对数据进行洗牌（默认True）

返回
---
分割后的列表，长度=2*len(arrays),
　　(train-test split)
"""
