from product import Product  

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

    def remove_product(self, product_name, quantity):
        if product_name in self.items:
            if quantity >= self.items[product_name]['quantity']:
                product = self.items[product_name]['product']
                product.stock += self.items[product_name]['quantity']  
                del self.items[product_name]
                print(f"Removed {product_name} from the cart.")
            else:
                self.items[product_name]['quantity'] -= quantity
                product = self.items[product_name]['product']
                product.stock += quantity 
                print(f"Removed {quantity} of {product_name} from the cart.")
        else:
            print(f"{product_name} is not in the cart.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            total_price = product.price * quantity  # Calculate total price for the quantity
            print(f"{product.name} - Quantity: {quantity}, Total Price: ${total_price:.2f}")
