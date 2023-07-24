# Exercise 1 : Geometry
# Write a class called Circle that receives a radius as an argument (default is 1.0).
# Write two instance methods to compute perimeter and area.
# Write a method that prints the geometrical definition of a circle.
class Circle:
    def __init__(self, radius=1):
        self.radius=radius
    
    def perimeter(self):
        result = 2 * 3.14 * self.radius
        # return result
        print(result)
        
    def area(self):
        result = 3.14 * self.radius ** 2
        # return result
        print(result)
    

my_radius = 3
my_circle = Circle(my_radius)
my_circle.perimeter()
my_circle.area()

# Exercise 2 : Custom List Class
# Create a class called MyList, the class should receive a list of letters.
# Add a method that returns the reversed list.
# Add a method that returns the sorted list.
# Bonus : Create a method that generates a second list with the same length as mylist. The list should be constructed with random numbers. (use list comprehension).
import random
class MyList:
    def __init__(self, letters_list):
        self.letters_list =letters_list
        
    def reverse_list (self):
        self.letters_list.reverse()
        print(self.letters_list)
    
    def sort_list(self):
        self.letters_list.sort()
        print(self.letters_list)
        
    def gen_list(self):
        random_list = [random.randint(1, 100) for _ in range(len(self.letters_list))]
        print(random_list)
    
letters = ['a', 'b', 'c', 'd']
my_list = MyList(letters)
reversed_letters= my_list.reverse_list()
sorted_letters =my_list.sort_list()
random_list = my_list.gen_list()    
    

 




    
    