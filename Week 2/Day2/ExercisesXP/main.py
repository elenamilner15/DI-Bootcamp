# Exercise 1 : Set
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.

my_fav_numbers ={1,3,4,6,7}
my_fav_numbers.add(10)
my_fav_numbers.add(12)
# print(my_fav_numbers)

#Remove the last number.
fav_numbers_list = list(my_fav_numbers)
fav_numbers_list.pop()

my_fav_numbers = set(fav_numbers_list)
# print(my_fav_numbers)

# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

friend_fav_numbers={1, 100, 200, 500}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

y = my_fav_numbers.intersection(friend_fav_numbers)
print(f"Me and my friend both like {y}")


# Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?      - No, it's not possible. Tuples could not be modified

# Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
# print(basket)
basket.insert(0, "Apples")
# print(basket)
counter = basket.count("Apples")
# print(counter)
basket.clear()


# Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?       
#           - float is a numerical data type for decimal numbers
#           - int is a whole number not a fractional

# Can you think of another way to generate a sequence of floats?

#           - it could be done with a loop by dividing number/numbers
#           - by by multiplying on floating number or just adding floating number to an integer

# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

start = 1.5
end = 5
step = 0.5
float_sequence=[]  
n = 0
element=0
print(float_sequence)
while element<=end:
  element = start + step*n
  n+=1
  float_sequence.append(element)  

print(float_sequence)


# Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
my_list=[]
el_list=[]
for number in range (1,21):
    my_list.append(number)  
print(my_list)

for element in my_list:
    index = my_list.index(element)
    if index%2 ==0:
        el_list.append(element)
print(el_list)


# Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

# !!!!!!!!!!!!!!!!!!!!!!!!!

name = ""
while True:
    name = input("Enter your name\n")
    if name.lower() != "elena":
        print("My name is different. Try again")
    else:
        print("My name is the same, Elena")
        break
        
    


# Exercise 7: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.


# !!!!!!!!!!!!!!!!!!!!!!!!!

fav_fru = input("input fruits name separated by space\n").lower()
fav_fru_list=fav_fru.split()
fru = input("input name of any fruit\n").lower()
if fru in fav_fru_list:
    print(f"You chose {fru} - one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")
    
# !!!!!!!!!!!!!!!!!!!!!!!!!

# Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).


# !!!!!!!!!!!!!!!!!!!!!!
inp = ""
top_list=[]
price_pizza=10
price_top=2.5
while True:
    inp = input("Add pizza toppings or type 'QUIT' to quit\n")
    if inp.lower() != "quit":
        print(f"We will add {inp} to your pizza")
        top_list.append(inp)
        price_pizza += price_top
    else:
        print(f"We added extra to your pizza:")
        for item in top_list:
            print (item)
        print(f"The total price for you order is {price_pizza}NIS")
        break       
        
# !!!!!!!!!!!!!!!!!!!!!!
# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# !!!!!!!!!!!!!!!!!!!!!!

price = 0
inp = input("Please enter the age of each member of your group separated by space\n")
age_list = list(map(int,inp.split()))
for age in age_list:
    if age <3:
        price +=0
    elif age<12:
        price+=10
    else:
        price+=15
print(f"total price is {price}")
# !!!!!!!!!!!!!!!!!!!!!!       

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

# !!!!!!!!!!!!!!!!!!!!!!    
member_list=[]
teens = ['Lena', 'Tal', 'Kate', 'David', 'Kira']  
for teen in teens:
    age=int(input(f"{teen}, enter your age  "))
    if age>= 21:
        teen_info = f"{teen} is {age} years old"
        member_list.append(teen_info)
    
    elif 16<=age< 21:
        teen_info = f"{teen} is {age} years old. PARENTAL GUIDANCE SUGGESTED"
        member_list.append(teen_info)       
    
    else:
        continue
print(f"List of permitted visitors for movie:\n")
for member in member_list:    
    print(member)
    
# !!!!!!!!!!!!!!!!!!!!!!    


# Exercise 10 : Sandwich Orders
# Using the list below :

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# 1. The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# 2. We need to prepare the orders of the clients:
# Create an empty list called finished_sandwiches.
# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# 3. After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# Remove Pastrami sandwich
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

# Prepare the orders
finished_sandwiches = []

while sandwich_orders != []: #the same as "while sandwich_orders
    current_sandwich = sandwich_orders.pop(0)    
    finished_sandwiches.append(current_sandwich)
    print(f"I made your {current_sandwich.lower()}.")

print("Finished sandwiches:\n")
for sandwich in finished_sandwiches:
    print(sandwich)


