# Exercise 1 : Convert Lists Into Dictionaries

# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

numbers = dict(zip(keys, values))
print(numbers)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Exercise 2 : Cinemax

# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# How much does each family member have to pay ?
# Print out the family’s total cost for the movies.

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost =0
for member, age in family.items():    
    if 3<=age<12:
        price = 10        
    elif 12<=age:
        price = 15        
    else:
        price = 0
    print(f"{member} has to pay {price}$\n")    
    total_cost+=price
print(f"Family has to pay {total_cost}$")

# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).    



family_list=[]

family={}
while True:
    inp = input("Enter name and age of your family members divided by space. \n To QUIT enter q\n")
    if inp.lower()=='q':
        break
    else:
        items = inp.split() 
        name = items[0]
        age = int(items[1])
        family[name] = age

total_cost =0
for member, age in family.items():    
    if 3<=age<12:
        price = 10        
    elif 12<=age:
        price = 15        
    else:
        price = 0
    print(f"{member} has to pay {price}$\n")    
    total_cost+=price
print(f"Family has to pay {total_cost}$")
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!        
# Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green
# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).

brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': ['blue'],
        'Spain': ['red'],
        'US': ['pink', 'green']
    }
}

# 3. Change the number of stores to 2.
brand['number_stores']=2

# 4. Print a sentence that explains who Zaras clients are.
clients=brand['type_of_clothes'].copy()
clients.remove("home")
x=', '.join(clients)
print (f"Zaras clients are {x}")

# 5. Add a key called country_creation with a value of Spain.
brand['country_creation']="Spain"

# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.

if 'international_competitors' in brand:
    brand['international_competitors'].append("Desigual")
else:
    pass
# 7. Delete the information about the date of creation.
del brand['creation_date']
print(brand)
# 8. Print the last international competitor.
print(f"The last international competitor:   {brand['international_competitors'][-1]}\n")
# 9. Print the major clothes colors in the US.
y=', '.join(brand['major_color']['US'])
print(f"The major clothes colors in the US are:  {y}\n")

# 10. Print the amount of key value pairs (ie. length of the dictionary).
print(f"The amount of key value pairs is:  {len(brand)}\n")
print(brand)

# 11. Print the keys of the dictionary.
for key in brand:
    print(key)
# 12. Create another dictionary called more_on_zara with the following details:
# creation_date: 1975 
# number_stores: 10 000

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_on_zara)
print(brand)
# 14. Print the value of the key number_stores. What just happened ?
# New value of "number_stores" from "more_on_zara" overwrites old one


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Exercise 4 : Disney Characters
# Instructions
# Use this list :

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :


# 1. {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
# 2. {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}


users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A={}
disney_users_B={}
disney_users_C={}
disney_users_D={}
disney_users_E={}
# disney_users_A = {user: index for index, user in enumerate(users)}
# disney_users_B = {index: user for index, user in enumerate(users)}
for index, user in enumerate(users):
    disney_users_A[user] = index

print(disney_users_A)

for user, index  in enumerate(users):
    disney_users_B[user] = index
    
print(disney_users_B)

sorted_users = sorted(users)
for index, user in enumerate(sorted_users):
    disney_users_C[user] = index

print(disney_users_C)

# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.

for index, user in enumerate(users):
     if 'i' in user.lower():
         disney_users_D[user] = index
print(disney_users_D)

# The characters, which names start with the letter “m” or “p”.
for index, user in enumerate(users):
     if 'm' in user.lower() or 'p' in user.lower():
         disney_users_E[user] = index
print(disney_users_E)



