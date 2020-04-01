from sklearn import datasets

#  鸢尾花

iris = datasets.load_iris()

iris_x, iris_y = iris.data, iris.target

#  查看特征
print(iris.feature_names)
# 查看标签
print(iris.target_names)

# 按照3比1的比例划分训练集和测试集
from sklearn.model_selection import train_test_split

train_x, test_x, train_y, test_y = train_test_split(iris_x, iris_y, test_size=0.25)
