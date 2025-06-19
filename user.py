from cart import Cart

class User:
    def __init__(self, username):
        self.username = username
        self.cart = Cart()

    def __str__(self):
        return f":User  {self.username}"

    def view_cart(self):
        print(f"{self.username}'s Cart:")
        self.cart.view_cart()