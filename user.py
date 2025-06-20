from cart import Cart

class User:
    def __init__(self, username):
        self.username = username
        self.cart = Cart()

    def view_cart(self):
        print(f"\n{self.username}'s Shopping Cart:")
        if self.cart.is_empty():
            print("Your cart is empty.")
        else:
            for product, quantity in self.cart.items.items():
                print(f"{product.name} - Quantity: {quantity}")
