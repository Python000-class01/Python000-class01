import pandas as pd
import numpy as np

# series 是一维 数据
# print(pd.Series(['a', 'b', 'c']))  # 默认创建索引

# 通过字典创建带索引的series
s1 = pd.Series({'a': 1, 'b': 2, 'c': 3})
# print(pd.Series({'a' : 1, 'b': 2, 'c': 3}))

# 通过关键字创建带索引的Series
s2 = pd.Series([11, 22, 33], index=['a', 'b', 'c'])

print(s2)

#  获取索引
# print(s2.index)

#  获取值
# print(s2.values)
#  类型
# print(type(s2.values))
# type(np.array(['a', 'b']))

#  转换为列表

# print(s1.values.tolist())
# 使用index会提升查询性能
#    如果index唯一，pandas会使用哈希表优化，查询性能为O(1)
#    如果index有序不唯一，pandas会使用二分查找算法，查询性能为O(logN)
#    如果index完全随机，每次查询都要扫全表，查询性能为O(N)


# 取出email
emails = pd.Series(['buying books at amazom.com', 'rameses@egypt.com', 'matt@t.co', 'narendra@modi.com'])
import re

pattern = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'
mask = emails.map(lambda x: bool(re.match(pattern, x)))
# print(mask)
emails = emails[mask]
print(emails)


