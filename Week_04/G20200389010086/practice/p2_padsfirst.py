import pandas as pd

# pandas 读取数据
# 自动添加索引
data_info = pd.read_csv('book_utf8.csv')
# print(data_info)

#  赛选列
# print(data_info['还行'])

# 显示前 3行 , 切片方式处理

# print(data_info[1:3])   # 类似于sql   select * from table limit 3


#  增加列名,相当于是excel 创建表头
data_info.columns = ['star', 'vote','shorts']
# print(data_info[0:1])

# data_info.groupby('star')

# 特定行的列
# print(data_info.loc[1:2, 'star'])   类似于： alter table t1 drop column name

# 过略数据
# print(data_info['star']=='力荐')
# 把 全部是力荐的 赛选出来类似于 sql 的select * from table where type = '力荐'
# print(data_info[data_info['star']=='力荐'])

# 数据缺失
# print(data_info.dropna())

# print(data_info.star.count())

# 数据求和
# print(data_info.groupby('star').sum())  # select count(id)  from tb group by id

#  创建列
star_to_number = {
    '力荐' : 5,
    '推荐' : 4,
    '还行' : 3,
    '较差' : 2,
    '很差' : 1
}
# print(data_info['star'])
# data_info['new_star'] = data_info['star'].map(star_to_number)
# data_info['xx_star'] = ''


print(data_info)
