class Shop:
    def __init__(self, name: str, type: str, capacity: int):
        self.capacity = capacity
        self.type = type
        self.name = name
        self.items_count = 0
        self.items = {}

    @classmethod
    def small_shop(cls, name: str, type: str):
        return cls(name, type, 10)

    def is_free_space(self):
        if self.items_count + 1 <= self.capacity:
            return True
        return False

    def add_item(self, item_name: str):
        if not self.is_free_space():
            return "Not enough capacity in the shop"
        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        self.items_count += 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name: str, amount: int):
        if item_name not in self.items or self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"
        self.items[item_name] -= amount
        self.items_count -= amount
        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)
print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))
print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
