from client.shopping_cart_client import ShoppingCartClient

def main():
    client = ShoppingCartClient()

    client.add_product("Laptop", 999.99, "A powerful laptop.", "27/10/2024")
    client.add_product("Mouse", 25.99, "A wireless mouse.")
    client.add_product("Keyboard", 49.99)

    client.view_cart()

    client.create_order()

    client.clear_cart()
    client.view_cart()

if __name__ == "__main__":
    main()