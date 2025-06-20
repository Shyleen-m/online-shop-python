from product import Product  
from user import User        

def display_menu():
    print("\nOnline Shopping System")
    print("1. Add Product to Cart")
    print("2. Remove Product from Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

def run():
    products = [
        Product("Lipstick", 15.00, 100),
        Product("Fenty Blush", 35.90, 50),
        Product("Concealer", 20.50, 80),
        Product("Sephora Eyeliner", 8.00, 100),
        Product("Fenty Foundation", 40.75, 50),
        Product("Setting Spray", 35.00, 50),
    ]

    username = input("Enter your name: ")
    user = User(username) 

    while True: 
        display_menu()
        choice = input("Select an option (1-5): ")

        if choice == '1':
            print("\nAvailable Products:")
            for index, product in enumerate(products):
                print(f"{index + 1}. {product}")  
            try:
                product_index = int(input("Select the product number to add: ")) - 1
                quantity = int(input("Enter the quantity: "))
                if 0 <= product_index < len(products):
                    user.cart.add_product(products[product_index], quantity)
                else:
                    print("Invalid product selection.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")

        elif choice == '2':
            if user.cart.is_empty():
                print("Your cart is empty.")
                continue
            print("\nYour Cart:")
            cart_products = list(user.cart.items.keys())
            for index, product in enumerate(cart_products):
                print(f"{index + 1}. {product}")
            try:
                product_index = int(input("Select the product number to remove: ")) - 1
                if 0 <= product_index < len(cart_products):
                    product = cart_products[product_index]
                    quantity = int(input(f"Enter the quantity of {product.name} to remove: "))
                    user.cart.remove_product(product, quantity)
                else:
                    print("Invalid product selection.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")

        elif choice == '3':
            user.view_cart()

        elif choice == '4':
            if user.cart.is_empty():
                print("Your cart is empty. Nothing to checkout.")
                continue
            print("\nChecking out...")
            user.view_cart()
            total = user.cart.calculate_total()
            print(f"\nTotal amount: ${total:.2f}")
            confirm = input("Do you want to confirm the checkout? (yes/no): ").strip().lower()
            if confirm == 'yes':
                print("Thank you for your purchase!")
                user.cart.items.clear()
            else:
                print("Returning to the main menu.")

        elif choice == '5':
            print("Exiting the application.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    run()
