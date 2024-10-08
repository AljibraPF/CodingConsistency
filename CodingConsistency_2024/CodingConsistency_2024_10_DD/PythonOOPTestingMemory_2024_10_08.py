#OOP Review to test my memory on OOP, feels nice to be back in python temporarily
class Laptop:
    def __init__(self):
        self.prices = []

    def add_price(self, price):
        self.prices.append(price)

    def display_prices(self):
        if self.prices:
            print("List of Laptop Prices:")
            for price in self.prices:
                print(f"${price:.2f}")
        else:
            print("No prices available.")


laptop_store = Laptop()

laptop_store.add_price(999.99)
laptop_store.add_price(1299.99)
laptop_store.add_price(749.99)

laptop_store.display_prices()
