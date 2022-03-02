from shopping_cart import ShoppingCart

class Customer:
    
    def __init__(self, name):
        self.name = name
        self.shopping_cart = ShoppingCart

    def add_product_to_cart(self):
        ShoppingCart.add_new_product

    def view_cart(self):
        for product in ShoppingCart.products:
            print(product)

    


