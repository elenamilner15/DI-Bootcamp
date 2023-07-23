class Farm:
    def __init__ (self, name):
        self.name=name
        self.animals={}
        self.slogan="\nE-I-E-I-O!"
        
    def add_animal(self,animal, quantity=1): #quantity=1 by default
        if animal in self.animals:
            self.animals[animal] += quantity
        else:
            self.animals[animal] = quantity   
    
    def get_info(self):
        info=(f"{self.name}'s farm\n\n")
        for animal, quantity in self.animals.items():           
            info +=(f"{animal} : {quantity}\n")
        info +=self.slogan
        return info
        
        
macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

        
        
    
    
    