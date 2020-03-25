import unittest
from decimal import Decimal

from .week02_0100_ex_1 import NormalUser, VipUser, Apple, Orange


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.apple = Apple()
        self.orange = Orange()

    def test_normal_user(self):
        normal = NormalUser()
        normal.add(self.apple, 100)
        self.assertEqual(normal.pay(), self.apple.price * Decimal(100) * Decimal('0.9'))
        normal.clear()
        self.assertEqual(normal.pay(), Decimal(0))
        normal.add(self.apple, 10)
        self.assertEqual(normal.pay(), self.apple.price * 10)
        normal.clear()
        self.assertEqual(normal.pay(), Decimal(0))

    def test_vip_user(self):
        user = VipUser()
        user.add(self.apple, 100)
        self.assertEqual(user.pay(), self.apple.price * Decimal(100) * Decimal('0.8'))
        user.clear()
        self.assertEqual(user.pay(), Decimal(0))
        user.add(self.apple, 10)
        self.assertEqual(user.pay(), self.apple.price * 10 * Decimal('0.85'))
        user.clear()
        self.assertEqual(user.pay(), Decimal(0))
        user.add(self.apple, 5)
        self.assertEqual(user.pay(), self.apple.price * 5)
