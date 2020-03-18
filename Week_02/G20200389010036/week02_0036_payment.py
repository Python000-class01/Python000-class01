class Accounts(object):

	def __init__(self, order):
		self.totalNumber = sum([o[0] for o in order])
		self.totalPrice = sum([o[1] for o in order])


class NormalUser(Accounts):

	@property
	def pay(self):
		if self.totalPrice < 200:
			return self.totalPrice
		else:
			return self.totalPrice * 0.9


class VipUser(Accounts):

	@property
	def pay(self):
		if self.totalPrice >= 200:
			return self.totalPrice * 0.8
		if self.totalNumber >= 10:
			return self.totalPrice * 0.85
		else:
			return self.totalPrice


def main():
	# 一类商品数量，总价
	order1 = [
		[2, 200],
		[1, 30],
	]
	order2 = [
		[20, 100],
		[1, 30],
	]
	nu = NormalUser(order1)
	vip = VipUser(order2)
	print(nu.pay)
	print(vip.pay)


if __name__ == '__main__':
	main()
