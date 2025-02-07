from product import Product  
from user import User        

def display_menu():
    print("\nOnline Shopping System")
    print("1. Add Product to Cart")
    print("2. Remove Product from Cart")
    print("3. View Cart")
    print("4. Exit")

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
        choice = input("Select an option (1-4): ")

        if choice == '1':
            print("\nAvailable Products:")
            for product in products:
                print(product)
            product_name = input("Enter the product name to add: ")
            quantity = int(input("Enter the quantity: "))
            for product in products:
                if product.name.lower() == product_name.lower():
                    user.cart.add_product(product, quantity)
                    break
            else:
                print("Product not found.")

        elif choice == '2':
            product_name = input("Enter the product name to remove: ")
            user.cart.remove_product(product_name)

        elif choice == '3':
            user.view_cart()

        elif choice == '4':
            print("Exiting the application.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    run()