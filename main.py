class Item:
    def calculate_total_price(self, price, quantity):
        return price * quantity
        pass

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

item2 = Item()
item2.name = "Laptop"
item2.price = 2000
item2.quantity = 11