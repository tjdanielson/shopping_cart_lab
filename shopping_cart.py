from product import Product

class ShoppingCart:

    def __init__(self):
        self.products = []
        self.total_price = 0

    def calculate_total(self, prices):
        self.total_price = sum(prices)

    def add_new_product(self, product):
        self.products.append(product)

    def empty_cart(self):
        self.products = []

        