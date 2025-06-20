class Cart:
    def __init__(self):
        self.items = {}  # {Product: quantity}

    def add_product(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity
        print(f"Added {quantity} of {product.name} to cart.")

    def remove_product(self, product, quantity):
        if product in self.items:
            if quantity >= self.items[product]:
                del self.items[product]
                print(f"Removed all of {product.name} from cart.")
            else:
                self.items[product] -= quantity
                print(f"Removed {quantity} of {product.name} from cart.")
        else:
            print(f"{product.name} not found in cart.")

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.items.items())

    def is_empty(self):
        return not self.items

