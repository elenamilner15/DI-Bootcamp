# Exercise 3 : Dogs Domesticated
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

import random

from main import Dogs
class PetDog(Dogs):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)        
        self.trained = False
        
    def train(self):
        bark_output = self.bark()
        print(bark_output)
        self.trained = True

    # def play(self, *dog_names):
    #     all_dogs = ', '.join(dog_names)
    #     print(f"{all_dogs} all play together")
        
    def play(self, *dog_names):
        all_dogs = ', '.join([self.name] + list(dog_names))
        print(f"{all_dogs} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            random_trick = random.choice(tricks)
            print(random_trick)
        else:
            print(f"{self.name} is not trained yet.")
        
        
dog1 = PetDog("Alf", 3, 20)
dog1.train()
dog1.play("Willy", "Billy", "Dilly")
dog1.do_a_trick()

