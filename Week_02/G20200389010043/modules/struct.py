from dataclasses import dataclass


@dataclass
class User:
    userID: str = "default"
    VIPCardNum: str = None


@dataclass
class Item:
    itemID: str
    itemName: str
    itemPrice: float
    itemUnits: int
