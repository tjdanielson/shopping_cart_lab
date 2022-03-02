
class ShoppingCart:

    def __init__(self):
        self.name = "shopping cart"
        self.products = []

    def calculate_total(self, prices):
        total_price = sum(prices)
        return total_price

    def add_new_product(self, product):
        self.products.append(product)

    def empty_cart(self):
        self.products = []

        