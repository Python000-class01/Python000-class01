# Author: SecretYZJ
# Date: 2020-03-17 19:51:00
# LastEditTime: 2020-03-17 19:51:00
# LastEditors: SecretYZJ
# Edit Record:
# Description: Win10, Pycharm, python3.7.1
# Requirement:
'''
为“996 便利店”设计一套销售系统的结算模块，结算模块要求对不同类型的用户（普通用户、VIP 用户）的单次消费进行区分并按照不同的购买金额、不同的用户身份进行结账：
普通用户消费不足 200 元，无折扣，原价付费；
普通用户消费满 200 元打九折；
VIP 会员满 200 元打八折；
VIP 会员满 10 件商品打八五折。
'''
# Design Requirements:
'''
请使用面向对象编程实现结算功能。
由于 VIP 会员存在两种折扣方式，需自动根据最优惠的价格进行结算。
'''

import abc
import copy


class Sale_System(metaclass=abc.ABCMeta):

	# 获得用户详细账单
	def get_bill(self, dict_shopping_list):
		pass

	# 用户优惠计算
	@abc.abstractmethod
	def get_discount(self, customer_type, total_price, total_num):
		pass

	# 用户支付
	@abc.abstractmethod
	def pay(self, cumstomer_name, fee, order_numer):
		pass

class Store996_Sale_System(Sale_System):

	def __init__(self):
		# 店铺内产品信息表
		self.products = {
			# 编号、产品名称、单价（元）、促销（1为原价，小数为折扣价）
			'001': ['薯片1', 5, 1],
			'002': ['薯片2', 6, 1],
			'003': ['薯片3', 2, 1],
			'004': ['矿泉水1', 3, 1],
			'005': ['矿泉水2', 2, 1],
			'006': ['矿泉水3', 3, 1],
			'007': ['方便面1', 5, 1],
			'008': ['方便面2', 6, 1],
			'009': ['方便面3', 4.5, 1],
			'010': ['可乐1', 3, 1],
			'011': ['可乐2', 3, 1],
			'012': ['豆奶1', 3.5, 1],
			'013': ['豆奶2', 3.5, 1]
		}

	# 获得用户详细账单
	def get_bill(self, dict_shopping_list):
		dict_list = {}
		t_price = 0
		t_num = 0
		print(f'----本次购物详细清单-----')
		print('产品编号 | 产品名称 | 单价（元） | 单品折扣 | 购买件数 | 单品总价')
		for key, num in dict_shopping_list.items():
			dict_list[key] = copy.deepcopy(self.products[key])
			dict_list[key].append(num)
			dict_list[key].append(dict_list[key][1] * dict_list[key][2] * num)
			t_price += dict_list[key][4]
			t_num += num
			print(f'{key:>5} {dict_list[key][0]:>10} {dict_list[key][1]:>10} {dict_list[key][2]:>10} {dict_list[key][3]:>10} {dict_list[key][4]:>10}')
		print(f'--------------------------')
		print(f'账单总价: {t_price}')
		print(f'购买总件数：{t_num}')
		return dict_list, t_price, t_num

	# 用户优惠计算
	def get_discount(self, customer_type, total_price, total_num):
		fee = None
		discount = None
		if customer_type == 'VIP':
			fee, dicount = self.vip_discount(total_price, total_num)
		else:
			fee, dicount = self.dicount(total_price)
		return fee, dicount

	# 计算VIP客户优惠价
	def vip_discount(self, total_price, total_num):
		# VIP 会员满 200 元打八折；
		# VIP 会员满 10 件商品打八五折。
		pad = None  # 折后价
		dicount = None  # 折扣
		if total_price < 200 and total_num < 10:
			dicount = 1
			pad = total_price
		elif total_price > 200 and total_num < 10:
			dicount = 0.8
			pad = total_price * 0.8
		elif total_price < 200 and total_num > 10:
			dicount = 0.85
			pad = total_price * 0.85
		else:
			dicount = 0.8
			pad = total_price * 0.8
		return pad, dicount

	# 计算普通客户优惠价
	def dicount(self, total_price):
		# 普通客户折扣
		pad = None  # 折后价
		dicount = None  # 折扣
		if total_price < 200:
			dicount = 1
			pad = total_price
		else:
			dicount = 0.9
			pad = total_price * 0.9
		return pad, dicount

	# 用户支付
	def pay(self, customer_num, cumstomer_name, total_price, dicount_price, dicount):
		# 显示账单实际总结信息
		print('---------------------------------------------')
		print(f'尊敬的{cumstomer_name}，您本次消费总额为：{dicount_price}元，折扣：{dicount}，账单总价：{total_price}，编号：{customer_num}')
		print('---------------------------------------------')
		# 进行支付
		self.pay_process(customer_num, cumstomer_name, dicount_price)

	# 支付过程
	def pay_process(self, customer_num, cumstomer_name, fee):
		print(f'正在进行支付')
		print(f'支付完成')


	# 执行过程
	def main(self, customer_num, customer_name, customer_type, dict_shopping_list):
		print(f'欢迎{customer_name}，正在为您结账')

		# 计算用户购物清单
		dict_shopping_list, total_price, total_num = self.get_bill(dict_shopping_list)

		# 获得折扣价和折扣
		dicount_price, dicount = self.get_discount(customer_type, total_price, total_num)

		# 支付，显示账单实际总结信息
		self.pay(customer_num, customer_name, total_price, dicount_price, dicount)

		print()
		print('=======================================================================================================')
		print()


if __name__ == '__main__':
	dict_customer_profile = {
		'客户编号': '',  # 例：N20200314001，编号: 日期加三位编号
		'客户名称': '',
		'客户身份': '',  # N 或 VIP
		'客户VIP编号': '',  # VIP编号: V+注册日期+三位编号
		'VIP用户电话号码': '',  # XXX-XXXX-XXXX
		'客户购物清单': ''
	}

	S996 = Store996_Sale_System()

	# 普通客户1，200元以下
	customer1 = copy.deepcopy(dict_customer_profile)
	customer1['客户编号'] = '20200318001'
	customer1['客户名称'] = '普通客户1'
	customer1['客户身份'] = 'N'
	customer1['客户购物清单'] = {
		'001': 1,
		'002': 1,
		'003': 1,
		'004': 1,
		'005': 1,
		'006': 1,
		'007': 1,
		'008': 1,
		'009': 1,
		'010': 1,
		'011': 1,
		'012': 1
	}
	S996.main(customer1['客户编号'], customer1['客户名称'], customer1['客户身份'], customer1['客户购物清单'])

	# 普通客户2，200元以上
	customer2 = copy.deepcopy(dict_customer_profile)
	customer2['客户编号'] = '20200318002'
	customer2['客户名称'] = '普通客户2'
	customer2['客户身份'] = 'N'
	customer2['客户购物清单'] = {
		'001': 10,
		'002': 10,
		'003': 10,
		'004': 10,
		'005': 10,
		'006': 10,
		'007': 10,
		'008': 10,
		'009': 10,
		'010': 10,
		'011': 10,
		'012': 10
	}
	S996.main(customer2['客户编号'], customer2['客户名称'], customer2['客户身份'], customer2['客户购物清单'])

	# VIP客户3，200元以下，10件以下
	customer3 = copy.deepcopy(dict_customer_profile)
	customer3['客户编号'] = '20200318003'
	customer3['客户名称'] = 'VIP客户3'
	customer3['客户身份'] = 'VIP'
	customer3['客户购物清单'] = {
		'001': 5,
		'002': 5,
		'003': 5,
		'004': 5,
		'005': 5,
		'007': 5,
		'008': 5
	}
	S996.main(customer3['客户编号'], customer3['客户名称'], customer3['客户身份'], customer3['客户购物清单'])

	# VIP客户4，200元以上，10件以下
	customer4 = copy.deepcopy(dict_customer_profile)
	customer4['客户编号'] = '20200318004'
	customer4['客户名称'] = 'VIP客户4'
	customer4['客户身份'] = 'VIP'
	customer4['客户购物清单'] = {
		'001': 100,
		'002': 100,
		'003': 100,
		'004': 100,
	}
	S996.main(customer4['客户编号'], customer4['客户名称'], customer4['客户身份'], customer4['客户购物清单'])

	# VIP客户5，200元以下，10件以上
	customer5 = copy.deepcopy(dict_customer_profile)
	customer5['客户编号'] = '20200318005'
	customer5['客户名称'] = 'VIP客户5'
	customer5['客户身份'] = 'VIP'
	customer5['客户购物清单'] = {
		'001': 10,
		'002': 10,
	}
	S996.main(customer5['客户编号'], customer5['客户名称'], customer5['客户身份'], customer5['客户购物清单'])

	# VIP客户6，200元以上，10件以上
	customer6 = copy.deepcopy(dict_customer_profile)
	customer6['客户编号'] = '20200318006'
	customer6['客户名称'] = 'VIP客户6'
	customer6['客户身份'] = 'VIP'
	customer6['客户购物清单'] = {
		'001': 10,
		'002': 10,
		'003': 10,
		'004': 10,
		'005': 10,
		'006': 10,
		'007': 10,
		'008': 10,
		'009': 10,
		'010': 10
	}
	S996.main(customer6['客户编号'], customer6['客户名称'], customer6['客户身份'], customer6['客户购物清单'])
