from hero import Hero

class Villain(Hero):
    villain = []
    def __init__(self, name: str, health: float, damage=0, hidden_damage=0):
        
        # Call super mom and dad
        super().__init__(name, health, damage)
        
        assert hidden_damage >=0, f"hidden damage {hidden_damage} should be greater than 0"
        
        self.hidden_damage = hidden_damage
        
        Villain.villain.append(self)
        
    def calculate_real_total_power(self):
        return self.health * (self.damage + self.hidden_damage)
    
hero1 = Villain("Baba", 1000, 1000, 3000)
hero2 = Villain("Babu", 1001, 1001, 3000)