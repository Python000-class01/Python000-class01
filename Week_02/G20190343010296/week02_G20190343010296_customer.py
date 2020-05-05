class Customer(object):
    def __init__(self, raw_total_price, item_count):
        self._raw_total_price = raw_total_price
        self._item_count = item_count

    @property
    def payment(self):
        return self._raw_total_price * 1.0


class NormalCustomer(Customer):

    @property
    def payment(self, no_discount_limit=200, dicount_rate=0.9):
        if self._raw_total_price >= no_discount_limit:
            return self._raw_total_price * dicount_rate
        return super().payment


class VIPCustomer(Customer):

    @property
    def payment(self, no_discount_limit=200, dicount_rate1=0.8, count_limit=10, discount_rate2=0.85):
        final_payment = super().payment
        if self._raw_total_price >= no_discount_limit:
            final_payment = self._raw_total_price * dicount_rate1
        if self._item_count >= count_limit:
            if self._raw_total_price * discount_rate2 < final_payment:
                final_payment = self._raw_total_price * discount_rate2

        return final_payment


class Settlement(object):
    def __init__(self, customer_type, total_price, item_count):
        if customer_type == "normal":
            self._payment = NormalCustomer(total_price, item_count)
        elif customer_type == "VIP":
            self._payment = VIPCustomer(total_price, item_count)

    def check_out(self):
        return self._payment.payment


if __name__ == "__main__":
    
    print(Settlement("normal", 200, 5).check_out())
    print(Settlement("normal", 100, 10).check_out())
    print(Settlement("VIP", 200, 5).check_out())
    print(Settlement("VIP", 100, 10).check_out())
    print(Settlement("VIP", 1, 1).check_out())
