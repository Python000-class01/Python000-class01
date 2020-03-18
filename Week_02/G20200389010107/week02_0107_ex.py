class CustomerPayment(object):
    def __init__(self, raw_total_price, item_count):
        self._raw_total_price = raw_total_price
        self._item_count = item_count

    @property
    def payment(self):
        return self._raw_total_price


class NormalCustomerPayment(CustomerPayment):
    def __init__(self, raw_total_price, item_count):
        super().__init__(raw_total_price, item_count)

    @property
    def payment(self, no_discount_limit=200, dicount_rate=0.9):
        if self._raw_total_price < no_discount_limit:
            return self._raw_total_price
        else:
            return self._raw_total_price * dicount_rate


class VIPCustomerPayment(CustomerPayment):
    def __init__(self, raw_total_price, item_count):
        super().__init__(raw_total_price, item_count)

    @property
    def payment(self, no_discount_limit=200, dicount_rate1=0.8, count_limit=10, discount_rate2=0.85):
        final_payment = self._raw_total_price
        if self._raw_total_price >= no_discount_limit:
            final_payment = self._raw_total_price * dicount_rate1
        if self._item_count >= count_limit:
            if self._raw_total_price * discount_rate2 < final_payment:
                final_payment = self._raw_total_price * discount_rate2

        return final_payment


class Settlement(object):
    def __init__(self, customer_type, total_price, item_count):
        if customer_type == "normal":
            self._payment = NormalCustomerPayment(total_price, item_count)
        elif customer_type == "VIP":
            self._payment = VIPCustomerPayment(total_price, item_count)

    def check_cout(self):
        return self._payment.payment


if __name__ == "__main__":
    # unit test
    a = Settlement("normal", 200, 5)
    assert a.check_cout() == 200 * 0.9

    b = Settlement("VIP", 200, 5)
    assert b.check_cout() == 200 * 0.8

    c = Settlement("VIP", 100, 10)
    assert c.check_cout() == 100 * 0.85
