# Exercise 1 : Pets
# Create another cat breed named Siamese which inherits from the Cat class.
# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# Take all the cats for a walk, use the walk method.

from typing import Any


class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'



bengal_cat = Bengal("Ben", 10)
chartreux_cat = Chartreux("Char", 11)
siamese_cat = Siamese("Siam", 12)

all_cats = [bengal_cat, chartreux_cat, siamese_cat]

sara_pets = Pets(all_cats)
sara_pets.walk()

# Exercise 2 : Dogs
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.

class Dogs:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return (f"{self.name} is barking")
    
    def run_speed(self):
        self.speed = round(self.weight/self.age*10, 2)
        return(self.speed)
    
    def fight(self, other_dog):
        self_power = self.speed * self.weight
        other_dog_power = other_dog.speed * other_dog.weight
        if self_power > other_dog_power:
            return f"{self.name} won the fight"
        elif self_power < other_dog_power:
            return f"{other_dog.name} won the fight"
        else:
            return "No dog won"

dog1 = Dogs("Sharik", 12, 20)
dog2 = Dogs("Rex", 7, 35)
dog3 = Dogs("Fighter", 5, 50)
        
all_dogs = [dog1, dog2, dog3]
for dog in all_dogs:
    print(dog.bark())
    print(dog.run_speed())

dog_winner = dog1.fight(dog2)
print(dog_winner)


