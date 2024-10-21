from hero import Hero

class Npc(Hero):
    def __init__(self, name: str, health: float, damage=0):
        
        # Call super mom and dad
        super().__init__(name, health, damage)
    