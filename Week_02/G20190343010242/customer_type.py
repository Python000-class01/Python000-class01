from enum import Enum, unique


@unique
class CustomerType(Enum):
    GENERIC = 0
    VIP = 1