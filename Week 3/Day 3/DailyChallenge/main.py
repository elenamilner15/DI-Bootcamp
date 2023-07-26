# Daily Challenge - Circle
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the attributes of the circle - use a dunder method
# Be able to add two circles together - use a dunder method
# Be able to compare two circles to see which is bigger - use a dunder method
# Be able to compare two circles and see if there are equal - use a dunder method
# Be able to put them in a list and sort them

import math

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            print("Radius or diameter should be > 0")      
        else:
            self.radius = radius
            self.diameter = radius * 2
            
    def __str__(self):
        return f"Radius = {self.radius}, Diameter = {self.diameter}"

    def __add__(self, other): 
        return Circle(self.radius + other.radius)
       
    def __lt__(self, other):        
            return self.radius < other.radius
     
    def __eq__(self, other):        
            return self.radius == other.radius
           
    def area(self):
        return math.pi * self.radius ** 2


circle1 = Circle(2)  
circle2 = Circle(4)
print(circle1)  

circle3 = circle1 + circle2
print(circle3)  
print(circle1 < circle2)
print(circle3 < circle2)
print(circle1 == circle3)  
print(circle1.area())  
print(circle2.area()) 


circles = [Circle(5), Circle(3), Circle(7), Circle(1)]
sorted_circles = sorted(circles, key=lambda x: x.radius)
for circle in sorted_circles:
    print(circle)            
    
# Daily Challenge: Translator   
# french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
# Look at this result :
# {"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
# You have to recreate the result using a translator module.

from googletrans import Translator

def translate(items):
    translator = Translator()

    result = {}
    for item in items:
        translation = translator.translate(item, src='fr', dest='en').text
        result[item] = translation

    return result

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
result = translate(french_words)
print(result)