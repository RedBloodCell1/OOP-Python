class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} should be greater than 0"
        assert quantity >=0, f"Quantity {quantity} should be greater than 0"
        
        # Assing to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)
        
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
item1 = Item("Friend", 100, 1)
item2 = Item("Friend2", 1000, 3)
item3 = Item("Friend3", 10, 5)
item4 = Item("Friend4", 50, 5)
item5 = Item("Friend5", 75, 5)

print(Item.all)