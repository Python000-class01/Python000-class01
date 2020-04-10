import pandas as pd

#  excel 导入

excel1 = pd.read_excel(r'0321.xlsx')
print(excel1.head(10))

# 指定导入哪个Sheet
# excel2 = pd.read_excel(r'0321.xlsx', sheet_name=0)

#  指定某一列为索引
# 指定第2行做列索引
# head参数值默认为0，即用第一行作为列索引
# pd.read_excel(r'0321.xlsx', head =1 )

