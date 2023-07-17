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
