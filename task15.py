# Task 15 - Order Fulfillment
import json
import uuid
import unittest

class Product:
    def __init__(self, price, stock):
        self.price = price
        self.stock = stock

class Inventory:
    def __init__(self, file):                       # read catalog from JSON
        self.products = {}
        for p in json.load(open(file)):
            self.products[p["id"]] = Product(p["price"], p["stock"])

class Cart:
    def __init__(self, discount=0):
        self.items = {}                              # product id -> quantity
        self.discount = discount                     # percent

    def add(self, pid, qty):
        if type(qty) != int or qty <= 0:
            raise ValueError("Invalid quantity")
        self.items[pid] = self.items.get(pid, 0) + qty

    def total(self, inventory):
        money = sum(inventory.products[p].price * q for p, q in self.items.items())
        return money - money * self.discount / 100

class Order:
    def __init__(self, cart, inventory):
        self.id = str(uuid.uuid4())                  # unique id
        self.items = cart.items
        self.total = cart.total(inventory)

def place_order(cart, inventory, orders_file):
    for pid, qty in cart.items.items():              # 1. check everything first
        if pid not in inventory.products or qty > inventory.products[pid].stock:
            raise ValueError("Unknown product or out of stock")

    order = Order(cart, inventory)
    for pid, qty in cart.items.items():              # 2. reduce stock
        inventory.products[pid].stock -= qty
    try:                                             # 3. save order
        try:
            orders = json.load(open(orders_file))
        except FileNotFoundError:
            orders = []
        orders.append({"id": order.id, "items": order.items, "total": order.total})
        json.dump(orders, open(orders_file, "w"))
    except Exception:                                # saving failed -> undo stock
        for pid, qty in cart.items.items():
            inventory.products[pid].stock += qty
        raise
    return order

class TestOrder(unittest.TestCase):
    def setUp(self):
        json.dump([{"id": "P1", "price": 100, "stock": 5}], open("catalog.json", "w"))
        self.inv = Inventory("catalog.json")

    def test_total_and_stock(self):
        cart = Cart(10)
        cart.add("P1", 2)
        order = place_order(cart, self.inv, "orders.json")
        self.assertEqual(order.total, 180)
        self.assertEqual(self.inv.products["P1"].stock, 3)

    def test_out_of_stock(self):
        cart = Cart()
        cart.add("P1", 10)
        with self.assertRaises(ValueError):
            place_order(cart, self.inv, "orders.json")

    def test_bad_quantity(self):
        with self.assertRaises(ValueError):
            Cart().add("P1", 0)

unittest.main()
