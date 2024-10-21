import csv

class Hero:
    nerf_rate = 0.8
    all = []
    
    
    def __init__(self, name: str, health: float, damage=0):
        # Run validations to the received arguments
        assert health >= 0, f"health {health} should be greater than 0"
        assert damage >=0, f"damage {damage} should be greater than 0"
        
        # Assing to self object
        self.__name = name
        self.__health = health
        self.damage = damage
        
        # Actions to execute
        Hero.all.append(self)
        
    @property
    def health(self):
        return self.__health
    
    def apply_nerf(self):
        self.__health = self.__health * self.nerf_rate
        
    def apply_buff(self, multiplier):
        self.__health = self.__health + (self.__health * multiplier)
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            raise Exception("The name is too long!")
        self.__name = new_name
    
    def calculate_total_power(self):
        return self.__health * self.damage
    

        
    @classmethod
    def instantiate_from_csv(cls):
        with open('heroes.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
        for item in items:
            Hero(
                name = item.get('name'),
                health = float(item.get('health')),
                damage = float(item.get('damage'))
            )
            
    @staticmethod
    def is_integer(num):
        # Count out floats that are .0 (5.0, 10.0)
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.health}, {self.damage})"
