from customer import Customer
from product import Product

customer_one = Customer('Tessa')
product_one = Product('Banana', 2, 'Produce')
product_two = Product('Donut', 1, 'Bakery')
product_three = Product('Cheese', 3, 'Dairy')

#print the customer's name
print(customer_one.name)
print(customer_one.shopping_cart.name)

#call the customer's products to shopping cart method three times and add the three product objects you created
customer_one.add_product_to_cart(product_one)
customer_one.add_product_to_cart(product_two)
customer_one.add_product_to_cart(product_three)

#call the customer's view products method
customer_one.view_cart()

#call the customer's shopping cart's get total method - capture the total method returns in a variable and print to the terminal
shopping_cart_total = customer_one.shopping_cart.calculate_total()
print('Your total is: $' + str(shopping_cart_total))

#call the customer's shopping cart's empty cart method
customer_one.shopping_cart.empty_cart()

#check if all products have been removed from the shopping cart
customer_one.view_cart()