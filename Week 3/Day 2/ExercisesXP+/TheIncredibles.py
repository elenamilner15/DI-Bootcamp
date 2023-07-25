# Exercise 2 : TheIncredibles Family
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.
# Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.
# Add a method called incredible_presentation which :

# Prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method)
# Prints all the members’ incredible name and power.


from main import Family

class TheIncredibles(Family):
    def __init__(self, last_name, members_data):
        super().__init__(last_name, members_data)
        
    def use_power(self):
        for member in self.members:        
            if member['age'] >= 18:
                print(f"{member['name']}'s power: {member['power']}")
            else:
                  raise Exception(f"{member['name']} is not over 18 years old")


            
    def incredible_presentation(self):
        super().family_presentation()       
        for member in self.members:
            print(f"{member['name']}, Incredible Name: {member['incredible_name']}, Power: {member['power']}")


initial_incredibles_data = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

last_name = "Incredible"
incredible_family = TheIncredibles(last_name, initial_incredibles_data)


incredible_family.family_presentation()

incredible_family.born(name='Jack', age=5, gender='Male', is_child=True, power='super strength', incredible_name='StrongJack')




try:
    incredible_family.use_power()
except Exception as e:
    print(e)

incredible_family.incredible_presentation()
