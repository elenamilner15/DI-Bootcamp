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
    
    def get_animal_types(self):
        animal_types = sorted(self.animals.keys())
        return animal_types
    
    def get_short_info(self):
        animal_types = self.get_animal_types()
        if len(animal_types) > 1:
            animal_str = ", ".join(animal_types[:-1])
            animal_str += f" and {animal_types[-1]}"
        else:
            animal_str = animal_types[0]
        short_info = f"{self.name}'s farm has {animal_str}."
        return short_info
    
        
macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

# Expand The Farm
# Add a method called get_animal_types to the Farm class. This method should return a sorted list of all the animal types (names) in the farm. With the example above, the list should be: ['cow', 'goat', 'sheep'].

# Add another method to the Farm class called get_short_info. This method should return the following string: “McDonald’s farm has cows, goats and sheep.”. The method should call the get_animal_types function to get a list of the animals.
animal_types = macdonald.get_animal_types()
print("Animal Types:", animal_types)

short_info = macdonald.get_short_info()
print(short_info)       
        
    
    
    