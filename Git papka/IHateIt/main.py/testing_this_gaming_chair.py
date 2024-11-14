"""class character():

    def __init__(self, name="GG"):
        self.name = name
CI = character()
introduse = f"character name is, {CI.name}"
print(introduse)

class player:
    def __init__(self, character: character):
        self.character = character

    def print_character(self):
        print(f"Players character name is {self.character.name}")
class inventory:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def show_inventory(self):
        print("Inventory items:", self.items)
inventory_instance = inventory()
inventory_instance.add_item("Sword")
inventory_instance.add_item("Shield")
inventory_instance.show_inventory()

























class Rectangle:
    def __init__(self, a=5, b=0, c=5, d=5):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def divide(self):
        try:
            result = self.a * self.b * self.c * self.d
            return result
        except ZeroDivisionError:
            return "Error, can't divide by 0"
rect = Rectangle()
print(rect.divide())

"""






def generator():
    for i in range(1, 7):
        yield i


gen = generator()


print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))






