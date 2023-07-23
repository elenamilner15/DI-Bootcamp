# Exercise 1: Cats
# Using Cat class
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Bob", 10)
cat2 = Cat("Bat", 11)
cat3 = Cat("Bill", 9)

# def old_cat(cat_list: list[Cat]) -> Cat | None:
#     if len(cat_list) == 0:
#         return None

def old_cat(cat_list):
    if not cat_list:
        return None

    oldest_cat = cat_list[0]

    for cat in cat_list:
        if cat.age > oldest_cat.age:
            oldest_cat = cat

    return oldest_cat

oldest = old_cat([cat1, cat2, cat3])
print(oldest.name)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Exercise 2 : Dogs

# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
           
# def bigger_dog(dog_list: list[Dog]) -> Dog | None:

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height       
           
    def bark(self):
            print(f"{self.name} goes woof!")
            
    def jump(self): 
            jumping_height = self.height*2
            print(f"{self.name} jumps {jumping_height}cm high")
            
obj1 = Dog(name='Sharik', height=15)        
obj1.bark()
obj1.jump()

davids_dog = Dog(name='Rex', height=50)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog(name='Teacup', height=20)
sarahs_dog.bark()
sarahs_dog.jump()

def find_big_dog(dog_list):
    if not dog_list:
        return None
    
    biggest_dog = dog_list[0]

    for dog in dog_list:
        if dog.height > biggest_dog.height:       
            biggest_dog = dog

    return biggest_dog

dogs = [obj1, davids_dog, sarahs_dog]
biggest = find_big_dog(dogs)
print(biggest.name)

# Exercise 3 : Who’s The Song Producer?

# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# Then, call the sing_me_a_song method. The output should be:
# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        # print(self.lyrics)
        for row in self.lyrics:
            print(row)
         

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
Song.sing_me_a_song(stairway)   #The same stairway.sing_me_a_song()
 

# Exercise 4 : Afternoon At The Zoo
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.

class Zoo:
    def __init__(self,zoo_name,animals):
        self.zoo_name=zoo_name
        self.animals = animals
    
    def add_animal(self, new_animals):
        for new_animal in new_animals:
            if new_animal in self.animals:
                print(f"{new_animal} already in the zoo")
            else:
                self.animals.append(new_animal)
                print(f"{new_animal} was added to the zoo")
        # print(self.animals)
    def get_animals(self):
        print(f"The residents of our Zoo: {', '.join(self.animals)}")
        
    def sell_animal(self, sold_animals):
        for sold_animal in sold_animals:
            if sold_animal in self.animals:
                self.animals.remove(sold_animal)
                print(f"{sold_animal} was sold")
            else:                
                print(f"There is no {sold_animal} in our zoo")             
    def sort_animals(self):
        self.animals.sort()
        self.get_animals()    #call print   
              
        
new_animals = ['kangaroo', 'penguin', 'panda', 'rhino']
TA_animals = ['tiger', 'bear', 'monkey', 'flamingo', 'rhino', 'giraffe', 'penguin']  
zoo_TA = Zoo('Tel-Aviv Zoo',TA_animals) 
        
Zoo.add_animal(zoo_TA,new_animals)
Zoo.get_animals(zoo_TA)

sold_animals = ['bear', 'monkey']  
Zoo.sell_animal(zoo_TA,sold_animals)
Zoo.get_animals(zoo_TA)

Zoo.sort_animals(zoo_TA)