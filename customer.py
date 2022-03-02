from ShoppingCart import ShoppingCart

class Customer:
    
    def __init__(self, name):
        self.name = name
        self.shopping_cart = ShoppingCart()

    def add_product_to_cart(self, product):
        self.shopping_cart.add_new_product(product)

    def view_cart(self):
        if self.shopping_cart == []:
            print('nothin here :/')
        else:
            for product in self.shopping_cart.products:
                print(product.name)

    


