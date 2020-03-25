from collections import defaultdict


class Customer(object):
    def __init__(self,ctm_name):
        self._name=ctm_name
        self._status=0
        # 用户购物车清单
        self._shoppingcar_list = defaultdict(int)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,cmt_name):
        self._name=cmt_name

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self,cmt_status):
        self._status=cmt_status

    #观察者模式，用户进入商店，通知超市
    def accessStore(self,store):
        store.custom_access()
        self.shopping(store)
        self.calcaulate(store)

    def shopping(self,store):
        self._shoppingcar_list=store.ctm_shopping(self._shoppingcar_list)

    def calcaulate(self,store):
        store.cmt_calculatePrice(self._status,self._shoppingcar_list)


class OrdinaryCtm(Customer):
    def __init__(self, ord_ctm_name):
        super().__init__(ord_ctm_name)
        self._status=0


class VIPCtm(Customer):
    def __init__(self,VIP_ctm_name):
        super().__init__(VIP_ctm_name)
        self._status=1

