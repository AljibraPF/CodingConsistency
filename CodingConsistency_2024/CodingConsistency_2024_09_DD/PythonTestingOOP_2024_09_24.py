class ItemOOP:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (Quantity: {self.quantity})"


class ShelfOOP:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added: {item}")

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"Removed: {item}")
                return
        print(f"Item '{item_name}' not found on the shelf.")

    def display_items(self):
        if not self.items:
            print("The shelf is empty.")
        else:
            print("Items on the shelf:")
            for item in self.items:
                print(f"- {item}")

# Learning how to organize and add more readable code, maybe comments should be next.
my_shelf = ShelfOOP()
item1 = ItemOOP("Book", 3)
item2 = ItemOOP("Pen", 10)
item3 = ItemOOP("Notebook", 5)

my_shelf.add_item(item1)
my_shelf.add_item(item2)
my_shelf.add_item(item3)

my_shelf.display_items()

my_shelf.remove_item("Pen")
my_shelf.display_items()

my_shelf.remove_item("Pencil")
