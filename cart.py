from product import Product  # Import the Product class

class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.stock >= quantity:
            if product.name in self.items:
                self.items[product.name]['quantity'] += quantity
            else:
                self.items[product.name] = {'product': product, 'quantity': quantity}
            product.update_stock(quantity)
            print(f"Added {quantity} of {product.name} to the cart.")
        else:
            print(f"Not enough stock for {product.name}.")

    def remove_product(self, product_name):
        if product_name in self.items:
            product = self.items[product_name]['product']
            quantity = self.items[product_name]['quantity']
            product.stock += quantity
            del self.items[product_name]
            print(f"Removed {product_name} from the cart.")
        else:
            print(f"{product_name} is not in the cart.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            print(f"{product} - Quantity: {quantity}")