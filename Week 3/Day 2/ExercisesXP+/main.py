# Exercise 1 : Family
# Create a class called Family and implement the following attributes:

# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]


# 2. Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ first name.

class Family:
    def __init__(self, last_name, members_data):
        self.last_name = last_name
        self.members = members_data      
        
    def born(self, **kwargs):
            self.members.append(kwargs)
            child_name = kwargs.get('name', 'Unknown')
            print(f"Congratulations with {child_name}'s Bitrthday!")           
            
    def is_18(self, name):
         for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
            else:
                return False
    
    def family_presentation(self):
        print(f"Family {self.last_name} members:")
        for member in self.members:
            print(member['name'])

members_data = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]
last_name = "Cohen"
my_family = Family(last_name, members_data)


my_family.family_presentation()

my_family.born(name='Golda', age=0, gender='Female', is_child=True)
my_family.family_presentation()

print(my_family.is_18('Michael'))
print(my_family.is_18('Golda'))