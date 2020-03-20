# 容器序列的拷贝问题
import copy

old_list = [i for i in range(1, 11)]

new_list1 = old_list

new_list2 = list(old_list)  # list 函数方法会重新生成一个对象，对象的内容和之前的一样
# 切片操作
new_list3 = old_list[:]

print(id(new_list1))
print(id(new_list2))
print(id(new_list3))
print(id(old_list))
# 嵌套操作
old_list.append([11, 12])
print(old_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12]]
print(new_list1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12]]
print(new_list2)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(new_list3)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list4 = copy.copy(old_list)  # 浅拷贝,类似箱子贴标签
new_list5 = copy.deepcopy(old_list)  # 深拷贝， 会深层创建对象，类似复制一份放入新的箱子
print(new_list4)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12]]
print(new_list5)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12]]
print(id(new_list4))
print(id(new_list5))
old_list[10][0] = 13
print(old_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [13, 12]]
print(new_list4)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [13, 12]]
print(new_list5)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12]]
print(id(old_list))
print(id(new_list4))
