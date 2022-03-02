
class ShoppingCart:

    def __init__(self):
        self.name = "shopping cart"
        self.products = []

    def calculate_total(self):
        total = 0
        for i in self.products:
            total += i.price
        return total

    def add_new_product(self, product):
        self.products.append(product)

    def empty_cart(self):
        self.products = []

        